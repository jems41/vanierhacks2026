const res = await fetch("http://ctf26.vanierhacks.net/ALSS/cpu1", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        Authorization: "Basic " + Buffer.from("HGZZC:ba0bf0fe-1197-48bd-943f-ce86dccd4435", "ascii").toString("base64")
    },
    body: JSON.stringify({
        verificationCode: "flag{df969169-d9f5-4763-83f3-4c8687a7af18}"
    })
});

console.log(await res.json());