import sys

# Def functions
def parse_opcode(integer):
    chars = str(integer)
    code = int(chars[-2:])
    pm1 = int(chars[-3:-2]) if chars[-3:-2] != "" else 0
    pm2 = int(chars[-4:-3]) if chars[-4:-3] != "" else 0
    pm3 = int(chars[-5:-4]) if chars[-5:-4] != "" else 0

    return (code, pm1, pm2, pm3)


def read_intcode(ints, input_val = None):
    i = 0
    code = parse_opcode(ints[i])
    instruction = code[0]
    pm1 = code[1]
    pm2 = code[2]
    pm3 = code[3]
    input_val = input_val

    while instruction != 99:

        if instruction == 1:
            a = ints[ints[i+1]] if pm1 == 0 else ints[i+1]
            b = ints[ints[i+2]] if pm2 == 0 else ints[i+2]
            out = ints[i+3]
            ints[out] = a + b
            i += 4
            print('code: {}, a: {}, b: {}, out: {}'.format(code, a, b, out))

        elif instruction == 2:
            a = ints[ints[i+1]] if pm1 == 0 else ints[i+1]
            b = ints[ints[i+2]] if pm2 == 0 else ints[i+2]
            out = ints[i+3]
            ints[out] = a * b
            i += 4
            print('code: {}, a: {}, b: {}, out: {}'.format(code, a, b, out))

        elif instruction == 3:
            if input_val is None:
                raise Exception("No input")

            out = ints[i+1]
            ints[out] = input_val
            i += 2
            print('code: {}, out: {}'.format(code, out))
        
        elif instruction == 4:
            out = ints[i+1]
            print(ints[out])
            i += 2
            print('code: {}, out: {}'.format(code, out))

        elif instruction == 5:
            a = ints[ints[i+1]] if pm1 == 0 else ints[i+1]
            b = ints[ints[i+2]] if pm2 == 0 else ints[i+2]
            if a != 0:
                i = b
                print('Jump if true: set i to {}'.format(b))

                code = parse_opcode(ints[i])
                instruction = code[0]
                pm1 = code[1]
                pm2 = code[2]
                pm3 = code[3]
                continue
            else:
                i += 3

        elif instruction == 6:
            a = ints[ints[i+1]] if pm1 == 0 else ints[i+1]
            b = ints[ints[i+2]] if pm2 == 0 else ints[i+2]
            if a == 0:
                i = b
                print('Jump if false: set i to {}'.format(b))

                code = parse_opcode(ints[i])
                instruction = code[0]
                pm1 = code[1]
                pm2 = code[2]
                pm3 = code[3]
                continue
            else:
                i += 3

        elif instruction == 7:
            a = ints[ints[i+1]] if pm1 == 0 else ints[i+1]
            b = ints[ints[i+2]] if pm2 == 0 else ints[i+2]
            out = ints[i+3]
            
            ints[out] = 1 if a < b else 0
            i += 4

        elif instruction == 8:
            a = ints[ints[i+1]] if pm1 == 0 else ints[i+1]
            b = ints[ints[i+2]] if pm2 == 0 else ints[i+2]
            out = ints[i+3]

            ints[out] = 1 if a == b else 0
            i += 4

        else:
            raise Exception('Unknown Opcode: {}'.format(code))
        
        code = parse_opcode(ints[i])
        instruction = code[0]
        pm1 = code[1]
        pm2 = code[2]
        pm3 = code[3]

    return ints

def main():
    select = int(sys.argv[1])
    if select == 0:
        test()
    elif select == 1:
        part_one()
    elif select == 2:
        part_two()
    elif select == 3:
        part_three()
    elif select == 4:
        part_four()


def test():
    print(read_intcode([1002,4,3,4,33]))

def part_two():
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


def part_one():
    # Modify input
    input[1] = 12
    input[2] = 2
    # Compute
    print(read_intcode(input))


def part_three():
    # Read & sanitize input
    input = open('input.txt').read().split(',')
    input = [s.strip() for s in input]
    input = [int(s) for s in input]
    
    print(read_intcode(input, 1))


def part_four():
    # Read & sanitize input
    input = open('input.txt').read().split(',')
    input = [s.strip() for s in input]
    input = [int(s) for s in input]
    
    read_intcode(input, 5)


if __name__ == "__main__":
    main()
