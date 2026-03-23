import base64

s = "REZAUBdmQQROEVEWPV1VR0ZCQksHUFEdCwhaBFEGCwlUUwBZ"
decoded = base64.b64decode(s)

print(decoded)
print(decoded.hex())
print(len(decoded))