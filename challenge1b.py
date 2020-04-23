def calculate_fuel(mass):
    fuel = mass//3 - 2
    return fuel

f = open("module_masses.txt", "r")

total_fuel = 0
for mass in f:
    fuel = calculate_fuel(int(mass))
    total_fuel += fuel

    while fuel > 0:
        fuel = calculate_fuel(fuel)
        if fuel > 0:
            total_fuel += fuel

f.close()
print("total fuel:", total_fuel)
