# ALSS 1

Endpoint: `/ALSS/cpu1`

Provided input:

```jsonw
{
    "submissionId": string,
    "challenges": {
        instructions": number[],
        "input": number[]
    }[]
}
```

Expected response:

```json
{
    "submissionId": string, // Same as the one you were provided with
    "output": number[][]
}
```

The MJSS is in drydock on the Teganessine Station orbiting Mars. It is due for some upgrades on its main computer, named the Automated Life Support System. In order to program it, we will first need to simulate it.

This state of the art 8 bit computer will have 10 bit wide instructions to control it, and 8 bits of data to handle numbers.

The computer can execute only one instruction at a time, and they have the following format:

```
00 0000 0000
^  ^    ^
|  |    Second nibble of data
|  First nibble of data
Instruction operation code (opcode for short)
```

The computer has 4 opcode types:

```
00: Load Immediate
01: Move
10: ALU
11: Jump
```

We will first concentrate on simulating moving data around (opcode `01`)

The computer must be able to move data from "registers" of data, which are 8 bits of memory each.

A move instruction looks like this:

```
01 0110 0101
^  ^    ^
|  |    Moving to register 5
|  Moving from register 6
Move opcode
```

The first 8 registers (Register 0 to Register 7) are simple registers, they only hold data. The following addresses have special meaning:

- Address 8:
    - Input if in the first nibble
        - Pulling from the output removes the first element from the input queue and puts it in the destination register, at the address specified in the second nibble
    - Output if in the second nibble
        - Moving to the output adds it to a queue which you will then return as the result of the computer to ensure you implemented it correctly.
- Address 9:
    - Memory, we will implement this later
- Address 10:
    - Stack, we will implement this later

There will be multiple challenges to solve, each one has a dedicated set of instructions, inputs and outputs. You must compute the correct outputs to simulate the CPU.

Note that:

- The Read Only Memory (instructions) will never be larger than 256, as the program counter (ROM pointer incremented every instruction) can only be 8 bits.
