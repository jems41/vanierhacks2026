const res = await fetch("http://ctf26.vanierhacks.net/reverseEngineering/youKnowWhoToCall", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        Authorization: "Basic " + Buffer.from("ouikf:23b644a0-85d5-451a-8bae-4300cf5aa61c", "ascii").toString("base64")
    },
    body: JSON.stringify({
        verificationCode: "flag{7305e92a-c4bb-4455-9cf4-20b7f430721a}"
    })
});

console.log(await res.json());