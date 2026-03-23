import requests

candidates = [
    "http://ctf26.vanierhacks.net/cryptography/signalNoise",
    "http://ctf26.vanierhacks.net/cryptography/signalnoise",
    "http://ctf26.vanierhacks.net/cryptography/signal-noise",
    "http://ctf26.vanierhacks.net/cryptography/signal_noise",
    "http://ctf26.vanierhacks.net/cryptography/signalNoise/",
    "http://ctf26.vanierhacks.net/challenges/cryptography/signalNoise",
    "http://ctf26.vanierhacks.net/challenge/cryptography/signalNoise",
    "http://ctf26.vanierhacks.net/api/cryptography/signalNoise",
    "http://ctf26.vanierhacks.net/api/challenges/cryptography/signalNoise",
]

for url in candidates:
    try:
        r = requests.get(url, timeout=10)
        print("=" * 80)
        print("URL:", url)
        print("Status:", r.status_code)
        print(r.text[:300])
    except Exception as e:
        print("=" * 80)
        print("URL:", url)
        print("Error:", e)