def calculate_output(noun, verb):
    with open("input_day_2.txt", "r") as input_file:
        program = input_file.readline().split(",")
        program = [int(x) for x in program]
        program[1] = noun
        program[2] = verb
        for i in range(0, len(program), 4):
            if program[i] == 1:
                program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
            elif program[i] == 2:
                program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
            elif program[i] == 99:
                return program[0]
        return -1


print(calculate_output(12, 2))

for i in range(0, 100, 1):
    for j in range(0, 100, 1):
        if calculate_output(i, j) == 19690720:
            print(str(i) + str(j))
