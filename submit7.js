const res = await fetch("http://ctf26.vanierhacks.net/steganography/spaceNoises", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        Authorization: "Basic " + Buffer.from("HGZZC:ba0bf0fe-1197-48bd-943f-ce86dccd4435", "ascii").toString("base64")
    },
    body: JSON.stringify({
        verificationCode: "flag{b8aa24dd-048B-4433-10c-cbd54b986bae}"
    })
});

console.log(await res.json());