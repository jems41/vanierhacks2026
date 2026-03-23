const res = await fetch("http://ctf26.vanierhacks.net/reverseEngineering/peekInsideTheSatelite", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Basic " + Buffer.from("ouikf:23b644a0-85d5-451a-8bae-4300cf5aa61c", "ascii").toString("base64")
  },
  body: JSON.stringify({
    verificationCode: "7351"
  })
});

console.log("status:", res.status);
console.log("content-type:", res.headers.get("content-type"));

const text = await res.text();
console.log(text);