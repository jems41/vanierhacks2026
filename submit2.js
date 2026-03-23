const res = await fetch("http://ctf26.vanierhacks.net/reverseengineering/youknowwhotocall", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        Authorization: "Basic " + Buffer.from("ouikf:23b644a0-85d5-451a-8bae-4300cf5aa61c", "ascii").toString("base64")
    },
    body: JSON.stringify({
        verificationCode: "flag{4fa3a939452d1b2992b5b806366ebeea3362e762926325f72a9d873538915952}"
    })
});

console.log(await res.json());