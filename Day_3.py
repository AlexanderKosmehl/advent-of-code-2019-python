class Line:
    def __init__(self, x1, y1, x2, y2, length):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.length = length


class Position:
    def __init__(self, x, y, length, line1, line2):
        self.x = x
        self.y = y
        self.length = length
        self.line1 = line1
        self.line2 = line2


def get_distance_from_origin(elem):
    return abs(elem.x) + abs(elem.y)

def get_closest_crossing(elem):
    return elem.length


def create_lines(direction_codes):
    line = []
    line.append(Line(0, 0, 0, 0, 0))

    for direction_code in direction_codes:
        direction = str(direction_code[0])
        direction_length = int(direction_code[1:])

        if direction == "U":
            line.append(Line(line[-1].x2, line[-1].y2, line[-1].x2, line[-1].y2 + direction_length,
                             line[-1].length + direction_length))

        elif direction == "D":
            line.append(Line(line[-1].x2, line[-1].y2, line[-1].x2, line[-1].y2 - direction_length,
                             line[-1].length + direction_length))

        elif direction == "R":
            line.append(Line(line[-1].x2, line[-1].y2, line[-1].x2 + direction_length, line[-1].y2,
                             line[-1].length + direction_length))

        elif direction == "L":
            line.append(Line(line[-1].x2, line[-1].y2, line[-1].x2 - direction_length, line[-1].y2,
                             line[-1].length + direction_length))

    return line


with open("input_day_3.txt", "r") as input_file:
    input_file = input_file.readlines()
    first_line_directions = input_file[0].split(",")
    second_line_directions = input_file[1].split(",")

    # Create Lines
    first_cable = create_lines(first_line_directions)
    print("First line created!")

    second_cable = create_lines(second_line_directions)
    print("Second line created!")

    # Find Crossings
    crossings = []

    for i in first_cable:
        for j in second_cable:
            if (i.x1 < j.x1 < i.x2 and j.y1 < i.y1 < j.y2) or \
                    (i.x1 < j.x1 < i.x2 and j.y2 < i.y1 < j.y1) or \
                    (i.x2 < j.x1 < i.x1 and j.y2 < i.y1 < j.y1) or \
                    (i.x2 < j.x1 < i.x1 and j.y1 < i.y1 < j.y2):
                length = i.length + j.length - (abs(i.x2 - j.x2) + abs(i.y2 - j.y2))
                crossings.append(Position(j.x1, i.y1, length, i, j))
            if (j.x1 < i.x1 < j.x2 and i.y1 < j.y1 < i.y2) or \
                    (j.x1 < i.x1 < j.x2 and i.y2 < j.y1 < i.y1) or \
                    (j.x2 < i.x1 < j.x1 and i.y2 < j.y1 < i.y1) or \
                    (j.x2 < i.x1 < j.x1 and i.y1 < j.y1 < i.y2):
                length = i.length + j.length - (abs(i.x2 - j.x2) + abs(i.y2 - j.y2))
                crossings.append(Position(i.x1, j.y1, length, i, j))

    # Find Shortest Distance
    crossings.sort(key=get_distance_from_origin)

    print("The closest Crossing is at (" + str(crossings[0].x) + ", " + str(crossings[0].y) + ") and " + str(
        abs(crossings[0].x) + abs(crossings[0].y)) + " units away")

    crossings.sort(key=get_closest_crossing)

    print(str(crossings[0].length))

