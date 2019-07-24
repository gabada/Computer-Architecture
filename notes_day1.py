import sys

PRINT_BEEJ = 1
HALT	   = 2
PRINT_NUM  = 3
SAVE_REGISTER = 4
PRINT_REGISTER = 5
PUSH = 6
POP = 7

memory = [
		PRINT_BEEJ,
		SAVE_REGISTER,
		77, # store 77
		2, # in register 2
		PRINT_REGISTER,
		2, # Print value in register 2
		# PRINT_NUM, # opcode == instruction
		# 12,		   # operand = argument
		# PRINT_NUM, # opcode == instruction
		# 24,		   # operand = argument
		HALT
]

register = [0] * 8 # 8 registers
SP = 7

pc = 0 # Program Counter, points to currently-executing instruction

running = True
register[SP] = 127 # SP top of memory in this case

while running:
	command = memory[pc]

	if command == PRINT_BEEJ:
		print('Beej!')
		pc += 1

	elif command == HALT:
		running = False
		pc += 1

	elif command == PRINT_NUM:
		operand = memory[pc + 1]
		print(operand)
		pc += 2

	elif command == SAVE_REGISTER:
		value = memory[pc + 1]
		regnum = memory[pc + 2]
		register[regnum] = value
		pc += 3

	elif command == PRINT_REGISTER:
		regnum = memory[pc + 1]
		print(register[regnum])
		pc += 2

	elif command == PUSH:
		register[SP] -= 1 # decrement SP
		regnum = memory[pc + 1] # get the reg number operand
		value = register[regnum] # get the value from register
		memory[register[SP]] = value # store that value in memory at SP
		pc += 2

	elif command == POP:
		value = memory[register[SP]] # get value from memory at SP
		regnum = memory[pc + 1] # get the register num operand
		register[regnum] = value # store the value in 
		register[SP] += 1 # increment SP
		pc += 2

	else:
		print(f'unknown instruction {command}')
		sys.exit(1)
