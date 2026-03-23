const submission = {
    submissionId: "test123",
    challenges: [
        {
            instructions: [
                0b01100001, // example instruction
                0b01011000
            ],
            input: [65, 66, 67]
        }
    ]
};

const result = simulateCPU(submission);

console.log(JSON.stringify(result, null, 2));