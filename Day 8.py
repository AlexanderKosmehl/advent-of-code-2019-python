with open("Advent of Code/input_day_8.txt", "r") as input_file:
    input = input_file.readline()
    input.strip()
    input = [int(x) for x in input]

width_counter = 0
height_counter = 0

layers = []
next_line = []
next_layer = []

max_width = 25
max_height = 6

def count_number_on_layer(number, layer):
    counter = 0
    for line in layer:
        for digit in line:
            if digit == number:
                counter += 1
    return counter

for digit in input:
    # New Layer
    if height_counter == max_height:
        layers.append(next_layer)
        next_layer = []
        height_counter = 0

    # New Line
    if width_counter == max_width:
        next_layer.append(next_line)
        next_line = []
        width_counter = 0
        height_counter += 1

    # Add to Line
    next_line.append(digit)
    width_counter += 1

next_layer.append(next_line)
layers.append(next_layer)

fewest_zeroes = 9999999
layer_with_fewest_zeroes = -1

for index, layer in enumerate(layers):
    count = count_number_on_layer(0, layer)
    if count < fewest_zeroes:
        fewest_zeroes = count
        layer_with_fewest_zeroes = index

print("Layer with fewest zeroes: " + str(layer_with_fewest_zeroes))
print("Ones * Twos: " + str(count_number_on_layer(1, layers[layer_with_fewest_zeroes]) * count_number_on_layer(2, layers[layer_with_fewest_zeroes])) + "\n")

final_picture = [[2 for x in range(max_width)] for x in range(max_height)]

for height in range(max_height):
    for width in range(max_width):
        current_color = 2
        for depth in range(len(layers)):
            if layers[depth][height][width] < current_color:
                current_color = layers[depth][height][width]
                final_picture[height][width] = current_color
                break


for line in final_picture:
    print(line)

for line in final_picture:
    for digit in line:
        if digit == 0:
            print("# ", end="")
        elif digit == 1:
            print("  ", end="")
        else:
            print("  ", end="")
    print()
