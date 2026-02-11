program:
        LOAD 0x08, 0x0  ; load 0x08 value to (RF) 0x0
        LOAD 0x09, 0x1  ; load 0x09 value to (RF) 0x1
        ADD 0x0, 0x1    ; ADD R1,R2 -> result (defaulted) to ACC
        STOR ACC, 0x0A  ; stor ACC in 0x0A (RAM)

DATA:
    RAM[0x08] = 0001
    RAM[0x09] = 0001

ASSEMBLED:                 ; In load instructions (xxyy xxxx), (yy) address of the RF.
        RAM[0x00] = 1000
        RAM[0x01] = 1000
        RAM[0x02] = 1001
        RAM[0x03] = 1001
        RAM[0x04] = 0000
        RAM[0x05] = 0001
        RAM[0x06] = 11xx    ; (xx) ignored bits
        RAM[0x07] = 1010

RESULT:                   ; After 15 falling edges (of the clock)
        RAM[0x0A] == 0010