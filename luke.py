import requests
import base64
import math

url = "http://ctf26.vanierhacks.net/cryptography/signalNoise"
team_id = "ouikf"
auth_key = "23b644a0-85d5-451a-8bae-4300cf5aa61c"
credentials = f"{team_id}:{auth_key}"
encoded_credentials = base64.b64encode(credentials.encode("ascii")).decode("ascii")
headers = {"Authorization": f"Basic {encoded_credentials}"}

response = requests.get(url, headers=headers)
message = response.json()["message"]

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n*0.5)+1, 2):
        if n % i == 0: return False
    return True

prime_chars = [(i, message[i]) for i in range(len(message)) if isprime(i)]
binary = ''.join('1' if c.isupper() else '0' for , c in prime_chars)
n = len(binary)
sq = int(math.isqrt(n))

size = 38
chunk = binary[:sizesize]

def render(data, size, b1, b0):
    for row in range(size):
        line = data[rowsize:(row+1)size]
        print(''.join(b1 if b == '1' else b0 for b in line))

print(f"Binary length: {n}, using size: {size}x{size}")
print(f"Density: {chunk.count('1')/(size*size):.2f}\n")

print("=== NORMAL double ██/  ===")
render(chunk, size, '██', '  ')

print("\n=== INVERTED double  /██ ===")
render(chunk, size, '  ', '██')

print("\n=== NORMAL single █/  ===")
render(chunk, size, '█', ' ')

print("\n=== INVERTED single  /█ ===")
render(chunk, size, ' ', '█')

print("\n=== NORMAL double █░/░█ (high contrast) ===")
render(chunk, size, '██', '░░')

print("\n=== INVERTED double ░█/█░ ===")