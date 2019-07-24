"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [00000000] * 256 # 256 max memory
        self.reg = [0] * 8 # 8 gen purpose registers
        self.pc = 0
        self.branchtable = {}
        self.branchtable[0b00000001] = self.op_hlt
        self.branchtable[0b10000010] = self.op_ldi
        self.branchtable[0b01000111] = self.op_prn
        self.branchtable[0b10100010] = self.op_mul
        self.branchtable[0b01000101] = self.op_push
        self.branchtable[0b01000110] = self.op_pop
        self.running = True
        self.IR = 0
        self.reg[7] = 0xF4
        self.sp = self.reg[7]

    def ram_read(self, mar):
        print(self.ram[mar])

    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def load(self):
        """Load a program into memory."""

        address = 0
        file = sys.argv[1]

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            # 0b10000010, # LDI R0,8
            # 0b00000000,
            # 0b00001000,
            # 0b01000111, # PRN R0
            # 0b00000000,
            # 0b00000001, # HLT
        ]

        with open(file, 'r') as data:
            for x in data:
                line = x.split('#', 1)[0]
                if line.strip() == '':
                    continue
                program.append(int(line, 2))

            for instruction in program:
                self.ram[address] = instruction
                address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.ram[reg_a] += self.ram[reg_b]
        elif op == "SUB":
            self.ram[reg_a] -= self.ram[reg_b]
        elif op == "MUL":
            self.ram[reg_a] = self.ram[reg_a] * self.ram[reg_b]
        elif op == "DIV":
            self.ram[reg_a] /= self.ram[reg_b]
        elif op == "MOD":
            self.ram[reg_a] %= self.ram[reg_b]

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def op_hlt(self):
        self.running = False
        sys.exit(1)

    def op_ldi(self):
        reg_add = self.ram[self.pc + 1]
        reg_val = self.ram[self.pc + 2]
        self.ram_write(reg_add, reg_val)
        self.pc += 3

    def op_prn(self):
        reg_add = self.ram[self.pc + 1]
        self.ram_read(reg_add)
        self.pc += 2

    def op_mul(self):
        reg_add_a = self.ram[self.pc + 1]
        reg_add_b = self.ram[self.pc + 2]
        self.alu("MUL", reg_add_a, reg_add_b)
        self.pc += 3

    def op_push(self):
        self.sp -= 1
        reg_num = self.ram[self.pc + 1]
        value = self.ram[reg_num]
        self.ram[self.sp] = value
        self.pc += 2

    def op_pop(self):
        reg_num = self.ram[self.pc + 1]
        self.ram_write(reg_num, self.ram[self.sp])
        self.sp += 1
        self.pc += 2

    def run(self):
        """Run the CPU."""
        # self.trace()
        while self.running:
            command = self.ram[self.pc]
            if command in self.branchtable:
                self.branchtable[command]()
            else:
                print(f'unknown instruction {command}\n')
                sys.exit(1)