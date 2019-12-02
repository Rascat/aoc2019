# Def functions
def read_intcode(ints):
    i = 0
    code = ints[i]

    while code != 99:
        ia = ints[i+1]
        ib = ints[i+2]
        out = ints[i+3]
        a = ints[ia]
        b = ints[ib]

        if code == 1:
            ints[out] = a + b
            print('code: {}, a: {}, b: {}, out: {}'.format(code, a, b, out))

        elif code == 2:
            ints[out] = a * b
            print('code: {}, a: {}, b: {}, out: {}'.format(code, a, b, out))

        else:
            raise Exception('Unknown Opcode: {}'.format(code))
        
        i += 4
        code = ints[i]

    return ints

# Test
# print(read_intcode([1,9,10,3,2,3,11,0,99,30,40,50]))

# Read & sanitize input
input = open('input.txt').read().split(',')
input = [s.strip() for s in input]
input = [int(s) for s in input]

for i in range(100):
    for j in range(100):
        copy = input.copy()
        print(copy)
        copy[1] = i
        copy[2] = j
        result = read_intcode(copy)
        if result[0] == 19690720:
            print('noun: {}, verb: {}'.format(i, j))
            exit(0)

# Modify input
#input[1] = 12
#input[2] = 2

# Compute
#print(read_intcode(input))
