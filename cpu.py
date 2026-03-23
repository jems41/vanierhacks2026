import json
import base64
from collections import deque
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

TEAM_ID = "HGZZC"
AUTH_KEY = "ba0bf0fe-1197-48bd-943f-ce86dccd4435"
URL = "https://ctf26.vanierhacks.net/ALSS/cpu1"

def make_headers():
    token = base64.b64encode(f"{TEAM_ID}:{AUTH_KEY}".encode()).decode()
    return {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

def fetch_payload():
    req = Request(URL, headers=make_headers(), method="GET")
    with urlopen(req) as resp:
        return json.load(resp)

def simulate_cpu1(challenge):
    regs = [0] * 8
    input_q = deque(challenge["input"])
    output_q = []

    for instr in challenge["instructions"]:
        opcode = (instr >> 8) & 0b11
        src = (instr >> 4) & 0xF
        dst = instr & 0xF

        if opcode != 0b01:
            raise ValueError(f"Unexpected opcode in cpu1: {opcode:02b} (instruction {instr})")

        # Read source
        if src <= 7:
            value = regs[src]
        elif src == 8:
            if not input_q:
                raise ValueError("Tried to read from input, but input queue is empty")
            value = input_q.popleft()
        else:
            raise ValueError(f"Unsupported source address for cpu1: {src}")

        value &= 0xFF

        # Write destination
        if dst <= 7:
            regs[dst] = value
        elif dst == 8:
            output_q.append(value)
        else:
            raise ValueError(f"Unsupported destination address for cpu1: {dst}")

    return output_q

def build_answer(payload):
    return {
        "submissionId": payload["submissionId"],
        "output": [simulate_cpu1(ch) for ch in payload["challenges"]]
    }

def post_answer(answer):
    data = json.dumps(answer).encode()
    req = Request(URL, data=data, headers=make_headers(), method="POST")
    with urlopen(req) as resp:
        return resp.read().decode()

def main():
    try:
        payload = fetch_payload()
        answer = build_answer(payload)

        print("Computed answer JSON:")
        print(json.dumps(answer, indent=2))

        print("\nPosting answer...\n")
        result = post_answer(answer)
        print("Server response:")
        print(result)

    except HTTPError as e:
        body = e.read().decode(errors="replace")
        print(f"HTTPError {e.code}")
        print(body)
    except URLError as e:
        print("URLError:", e)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()