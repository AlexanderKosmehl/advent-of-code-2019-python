import time
import numpy

class Moon:
    def __init__(self, x, y, z):
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0


moons = [Moon(-4, -9, -3), Moon(-13, -11, 0), Moon(-17, -7, 15), Moon(-16, 4, 2)]

start_time = time.time()
for step in range(1000):

    # Calculate Gravity
    for moon in moons:
        for another_moon in moons:
            if moon is not another_moon:
                # x-Velocity
                if moon.x_pos < another_moon.x_pos:
                    moon.x_vel += 1
                elif moon.x_pos > another_moon.x_pos:
                    moon.x_vel -= 1

                # y-Velocity
                if moon.y_pos < another_moon.y_pos:
                    moon.y_vel += 1
                elif moon.y_pos > another_moon.y_pos:
                    moon.y_vel -= 1

                # z-Velocity
                if moon.z_pos < another_moon.z_pos:
                    moon.z_vel += 1
                elif moon.z_pos > another_moon.z_pos:
                    moon.z_vel -= 1

    # Apply Gravity
    for moon in moons:
        moon.x_pos += moon.x_vel
        moon.y_pos += moon.y_vel
        moon.z_pos += moon.z_vel

total_energy = 0

for moon in moons:
    total_potential_energy = abs(moon.x_pos) + abs(moon.y_pos) + abs(moon.z_pos)
    total_kinetic_energy = abs(moon.x_vel) + abs(moon.y_vel) + abs(moon.z_vel)
    total_energy += total_potential_energy * total_kinetic_energy

print(time.time() - start_time)
print("Sum of total energy: " + str(total_energy))




