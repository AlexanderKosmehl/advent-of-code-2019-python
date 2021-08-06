import itertools


def calculate_amplification_output(phase_setting, phase_is_set, old_program, instruction_pointer, amp_input):
    if old_program is None:
        with open("Advent of Code/input_day_7.txt", "r") as input_file:
            program = input_file.readline().split(",")
            program = [int(x) for x in program]
    else:
        program = old_program

    # Input Automization
    if phase_is_set == False:
        has_used_phase_setting = False
    else:
        has_used_phase_setting = True

    if instruction_pointer is None:
        i = 0
    else:
        i = instruction_pointer

    while (True):

        # Parse Input Code
        instruction = str(program[i]).zfill(5)
        opcode = instruction[3:]
        first_param_mode = instruction[2]
        second_param_mode = instruction[1]
        third_param_mode = instruction[0]

        if opcode not in ["03", "04", "99"]:
            # Preprocess Parameters
            if first_param_mode == "0":
                first_value = program[program[i + 1]]
            else:
                first_value = program[i + 1]

            if second_param_mode == "0":
                second_value = program[program[i + 2]]
            else:
                second_value = program[i + 2]

            # if third_param_mode == "0":
            #     third_value = program[program[i + 3]]
            # else:
            #     third_value = program[i + 3]

        # Addition
        if opcode == "01":
            program[program[i + 3]] = first_value + second_value

            # Increment Counter
            i += 4

        # Multiplication
        elif opcode == "02":
            program[program[i + 3]] = first_value * second_value

            # Increment Counter
            i += 4


        # Automated Input Mode
        elif opcode == "03":
            if has_used_phase_setting == False:
                input = phase_setting
                has_used_phase_setting = True
            else:
                input = amp_input
            program[program[i + 1]] = int(input)

            # Increment Counter
            i += 2

        # Output Mode for Functions
        elif opcode == "04":
            if first_param_mode == "0":
                return (program[program[i + 1]], program, i)
            else:
                return program[i + 1]

            # Increment Counter
            i += 2

        # jump-if-true
        elif opcode == "05":
            if first_value > 0:
                i = second_value
            else:
                i += 3

        # jump-if-false
        elif opcode == "06":
            if first_value == 0:
                i = second_value
            else:
                i += 3

        # less-than
        elif opcode == "07":
            # check
            if first_value < second_value:
                program[program[i + 3]] = 1
            else:
                program[program[i + 3]] = 0

            # Increment Counter
            i += 4

        # equals
        elif opcode == "08":
            if first_value == second_value:
                program[program[i + 3]] = 1
            else:
                program[program[i + 3]] = 0

            # Increment Counter
            i += 4

        # Exit
        elif opcode == "99":
            break


possible_phase_settings = list(itertools.permutations(range(5, 10, 1)))
setting_scores = {}

for setting in possible_phase_settings:
    output = 0



    setting_scores[output] = setting

print(sorted(setting_scores, reverse=True))
