with open("input_day_1.txt", "r") as input_file:
    input_lines = input_file.readlines()

fuel_total = 0
for line in input_lines:
    module_fuel = 0
    mass = int(line)
    while(True):
        module_fuel = int(mass/3) - 2
        if module_fuel > 0:
            mass = module_fuel
            fuel_total += module_fuel
        else:
            break

print(fuel_total)