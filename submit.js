const res = await fetch("http://ctf26.vanierhacks.net/networking/wiresharkChallenge", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        Authorization: "Basic " + Buffer.from("ouikf:23b644a0-85d5-451a-8bae-4300cf5aa61c", "ascii").toString("base64")
    },
    body: JSON.stringify({
        verificationCode: "flag{4426ecee-6edd-483a-9331-f3e7ab87321e}"
    })
});

console.log(await res.json());