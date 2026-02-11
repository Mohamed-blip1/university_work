# Digital Electronics – Logisim

Projects:
- ALU:
    - 4-bit ALU
    ```
    supporting: ADD, SUB, AND, OR, XOR 
    Opcode width: 3 bits 
    Outputs: Result, ZF, CF, OF, SF
    ```
- CPU:
    - RAM + MAR
    - Register file
    - ALU
    - ACC
    - Instruction register
    - Control unit with step counter
    - Single DATA_BUS
    - Address bus
    - Instruction flow: ```RAM → RF → ALU → ACC → RAM```
    
- RAM:
    - basic_rams : 1-bit memory with enable. 2 words, 1 bit RAM. 4 words, 1 bits RAM. 4 words, 2 bits RAM. 4 words, 4 bits RAM 
    -  16x4 bit ram
    ```
    RAM built from registers
    ```
- register
    - 4-bit register using D flip-flops
    - Register file with 2 read ports and 1 write port

Goal: practice how CPU memory structures are built from logic gates.