
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
        if code_collection[nextIndex] == OPCODE_ADD:
            code_collection[code_collection[nextIndex + 3]] = code_collection[code_collection[nextIndex + 1]] + code_collection[code_collection[nextIndex + 2]]
        elif code_collection[nextIndex] == OPCODE_MUL:
            code_collection[code_collection[nextIndex + 3]] = code_collection[code_collection[nextIndex + 1]] * code_collection[code_collection[nextIndex + 2]]
        else:
            return 0
        iterations += 1
        nextIndex += 4
    return code_collection[0]


if __name__ == "__main__":
    codes = readOpCodes("source")
    # Reset program
    # Replace position 1 with the value 12 and replace position 2 with the value 2.
    codes[1] = 12
    codes[2] = 2
    print(handle_intcode(0, codes))

