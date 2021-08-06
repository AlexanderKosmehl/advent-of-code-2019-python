class CelestialBody:
    def __init__(self, name, center):
        self.name = name
        self.center = center

    def count_centers(self):
        if self.center is None:
            return 0
        else:
            return 1 + self.center.count_centers()


with open("Advent of Code/input_day_6.txt", "r") as input_file:
    orbit_strings = input_file.readlines()
    orbit_strings = [x.strip() for x in orbit_strings]

    celestial_bodies = []

    for line in orbit_strings:
        split_line = line.split(")")

        center_body = next((x for x in celestial_bodies if x.name == split_line[0]), None)
        if center_body is None:
            center_body = CelestialBody(split_line[0], None)
            celestial_bodies.append(center_body)

        orbiting_body = next((x for x in celestial_bodies if x.name == split_line[1]), None)
        if orbiting_body is None:
            orbiting_body = CelestialBody(split_line[1], center_body)
            celestial_bodies.append(orbiting_body)
        else:
            orbiting_body.center = center_body

    number_of_orbits = 0
    for body in celestial_bodies:
        number_of_orbits += body.count_centers()

    print("There is a total of " + str(number_of_orbits) + " orbits!")

    you = next((x for x in celestial_bodies if x.name == "YOU"), None)
    san = next((x for x in celestial_bodies if x.name == "SAN"), None)

    you_orbits = []
    san_orbits = []

    while True:
        you_orbits.append(you)
        if you.center is not None:
            you = you.center
        else:
            break

    while True:
        san_orbits.append(san)
        if san.center is not None:
            san = san.center
        else:
            break

    for body in you_orbits:
        common_body = next((x for x in san_orbits if x.name == body.name), None)
        if common_body is not None:
            break

    if common_body is not None:
        you_orbits = you_orbits[0:you_orbits.index(common_body)]
        san_orbits = san_orbits[0:san_orbits.index(common_body)]

    print("You need " + str(len(you_orbits + san_orbits) - 2) + " orbit transfers to reach Santa!")
