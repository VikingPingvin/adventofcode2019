
OPCODE_TERMINATE = 99
OPCODE_ADD = 1
OPCODE_MUL = 2


def readOpCodes(path):
    codes = list()
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            codes.extend(line.strip('\n').split(','))
        codes = [int(i) for i in codes]
        return codes


def handle_intcode(index, code_collection):
    iterations = 0
    nextIndex = index

    while code_collection[nextIndex] != OPCODE_TERMINATE:
        opCode = code_collection[nextIndex]
        leftCode = code_collection[nextIndex + 1]
        rightCode = code_collection[nextIndex + 2]
        outCode = code_collection[nextIndex + 3]
        if opCode == OPCODE_ADD:
            code_collection[outCode] = code_collection[leftCode] + code_collection[rightCode]
        elif opCode == OPCODE_MUL:
            code_collection[outCode] = code_collection[leftCode] * code_collection[rightCode]
        else:
            return 0
        iterations += 1
        nextIndex += 4
    return code_collection[0]


def findValues(target, codes):
    for noun in range(100):
        for verb in range(100):
            codesAttempt = list(codes)
            codesAttempt[1] = noun
            codesAttempt[2] = verb
            handle_intcode(0, codesAttempt)
            if codesAttempt[0] == target:
                return noun, verb
    return 0, 0


if __name__ == "__main__":
    codesOriginal = readOpCodes("source")
    codes = list(codesOriginal)
    # Reset program
    # Replace position 1 with the value 12 and replace position 2 with the value 2.
    codes[1] = 12
    codes[2] = 2
    print('Part 1 answer: ' + str(handle_intcode(0, codes)))

    noun, verb = findValues(19690720, codesOriginal)
    print('Part 2 andser: ' + str((100 * noun) + verb))


