import requests
import base64
import math

url = "http://ctf26.vanierhacks.net/cryptography/signalNoise"
team_id = "ouikf"
auth_key = "23b644a0-85d5-451a-8bae-4300cf5aa61c"
credentials = f"{team_id}:{auth_key}"
encoded_credentials = base64.b64encode(credentials.encode("ascii")).decode("ascii")
headers = {"Authorization": f"Basic {encoded_credentials}"}  # no Content-Type on GET

response = requests.get(url, headers=headers)
message = response.json()["message"]

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

prime_chars = [(i, message[i]) for i in range(len(message)) if is_prime(i)]
binary = ''.join('1' if c.isupper() else '0' for _, c in prime_chars)
n = len(binary)
sq = int(math.isqrt(n))
print(f"Binary length: {n}, sqrt: {sq}")

# Only try perfect-ish square sizes
for size in range(20,25):
    ones = binary[:size*size].count('1')
    density = ones / (size*size)
    print(f"\n{'='*size*2}")
    print(f"SIZE {size}x{size} | density={density:.2f}")
    print(f"{'='*size*2}")
    for row in range(size):
        line = binary[row*size:(row+1)*size]
        print(''.join('███' if b == '1' else '   ' for b in line))
    print(f"\n--- INVERTED ---")
    for row in range(size):
        line = binary[row*size:(row+1)*size]
        print(''.join('   ' if b == '1' else '███' for b in line))