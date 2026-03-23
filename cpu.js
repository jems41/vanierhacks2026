const http = require("http");
const fs = require("fs");

const TEAM_ID = "HGZZC";
const AUTH_KEY = "ba0bf0fe-1197-48bd-943f-ce86dccd4435";

function authHeader() {
  return "Basic " + Buffer.from(`${TEAM_ID}:${AUTH_KEY}`, "utf8").toString("base64");
}

function httpRequest(method, path, bodyObj = null) {
  return new Promise((resolve, reject) => {
    const body = bodyObj ? Buffer.from(JSON.stringify(bodyObj), "utf8") : null;

    const req = http.request(
      {
        hostname: "ctf26.vanierhacks.net",
        port: 80,
        path,
        method,
        headers: {
          Authorization: authHeader(),
          Accept: "application/json",
          ...(body
            ? {
                "Content-Type": "application/json; charset=utf-8",
                "Content-Length": body.length,
              }
            : {}),
          Connection: "close",
        },
      },
      (res) => {
        let data = "";
        res.setEncoding("utf8");

        res.on("data", (chunk) => {
          data += chunk;
        });

        res.on("end", () => {
          resolve({
            status: res.statusCode,
            headers: res.headers,
            body: data,
          });
        });
      }
    );

    req.on("error", reject);

    if (body) req.write(body);
    req.end();
  });
}

function simulateCPU1(challenge) {
  const regs = new Array(8).fill(0);
  const input = [...challenge.input];
  const output = [];

  for (const instr of challenge.instructions) {
    const opcode = (instr >> 8) & 0b11;
    const src = (instr >> 4) & 0xF;
    const dst = instr & 0xF;

    if (opcode !== 0b01) {
      throw new Error(`Unexpected opcode ${opcode} for instruction ${instr}`);
    }

    let value;

    if (src >= 0 && src <= 7) {
      value = regs[src];
    } else if (src === 8) {
      if (input.length === 0) {
        throw new Error("Tried to read from empty input queue");
      }
      value = input.shift();
    } else {
      throw new Error(`Unsupported source address ${src}`);
    }

    value &= 0xff;

    if (dst >= 0 && dst <= 7) {
      regs[dst] = value;
    } else if (dst === 8) {
      output.push(value);
    } else {
      throw new Error(`Unsupported destination address ${dst}`);
    }
  }

  return output;
}

async function main() {
  try {
    console.log("Fetching fresh challenge...");
    const getRes = await httpRequest("GET", "/ALSS/cpu1");

    console.log("GET status:", getRes.status);
    console.log("GET body:", getRes.body.slice(0, 500) + (getRes.body.length > 500 ? "..." : ""));

    if (getRes.status < 200 || getRes.status >= 300) {
      throw new Error(`GET failed with status ${getRes.status}`);
    }

    const payload = JSON.parse(getRes.body);

    const answer = {
      submissionId: String(payload.submissionId),
      output: payload.challenges.map((challenge) =>
        simulateCPU1(challenge).map((n) => Number(n))
      ),
    };

    fs.writeFileSync("answer.json", JSON.stringify(answer, null, 2));
    console.log("Wrote answer.json");
    console.log("submissionId:", answer.submissionId);
    console.log("challenge count:", answer.output.length);
    console.log("first output length:", answer.output[0]?.length ?? 0);

    console.log("\nSubmitting answer...");
    const postRes = await httpRequest("POST", "/ALSS/cpu1", answer);

    console.log("POST status:", postRes.status);
    console.log("POST body:", postRes.body);
  } catch (err) {
    console.error("Error:", err.message);
  }
}

main();