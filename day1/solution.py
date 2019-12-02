import functools

def calc_fuel(mass):
    return int(mass / 3) - 2

def calc_fuel_rec(mass):
    new_mass = int(mass / 3) - 2
    if new_mass <= 0:
        return 0
    else:
        return new_mass + calc_fuel_rec(new_mass)


input = open("input.txt").read().splitlines()

input = input[0:-1]
input = list(map(int,input))
#input = list(map(calc_fuel, input))
#input = functools.reduce(lambda a, b: a+b, input)
result = sum([calc_fuel_rec(x) for x in input])

print(result)
#print(calc_fuel_rec(100756))

