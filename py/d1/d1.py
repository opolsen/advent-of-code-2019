import math

def calc_fuel(mass):
    return math.floor(mass / 3) - 2

def calc_fuel_with_fuel(mass):
    fuel = calc_fuel(mass)
    total_fuel = 0 + fuel

    while fuel > 0:
        fuel = calc_fuel(fuel)
        total_fuel += max(fuel, 0)

    return total_fuel

def solve_1(masses):
    return sum(map(calc_fuel, masses))


def solve_2(masses):
    return sum(map(calc_fuel_with_fuel, masses))

if __name__ == '__main__':
    with open('input.txt') as f:
        masses = [int(line) for line in f]
        print(f'solve_1: {solve_1(masses)}')
        print(f'solve_2: {solve_2(masses)}')
