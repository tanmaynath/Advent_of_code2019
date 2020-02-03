import math


def fuel_required(module_mass, total_fuel_per_module):

    """Calculate fuel for module mass"""
    fuel = math.floor((module_mass/3) - 2)
    """Calculate fuel for every unit of fuel added(since fuel also has its own mass)"""

    if fuel > 0:
        total_fuel_per_module += fuel
        return fuel_required(fuel, total_fuel_per_module)
    else:
        return total_fuel_per_module


"""
Read all input masses from file
"""
input_file = open("puzzle_input_file.txt", "r")

input_by_line = input_file.readlines()

list_of_module_mass = []

for line in input_by_line:
    list_of_module_mass.append(float(line.replace("\n", "")))

total_fuel = 0
for mass in list_of_module_mass:
    total_fuel += fuel_required(mass,0)

print(total_fuel)