
def main():
    datalist = [0]
    instruction_list = []

    loopstart = []
    loopend = []

    data_pointer = 0
    instruction_pointer = 0

    operators = ["<", ">", "+", "-", "[", "]", ".", ","]

    file = open(input("File: "), "r")

    for line in file:
        for character in line:
            if character in operators:
                instruction_list.append(character)

    while instruction_pointer < len(instruction_list):

        if instruction_list[instruction_pointer] == "<":
            if data_pointer != 0:
                data_pointer -= 1

        elif instruction_list[instruction_pointer] == ">":
            if len(datalist) < (data_pointer + 2):
                datalist.append(0)
            data_pointer += 1

        elif instruction_list[instruction_pointer] == "+":
            if datalist[data_pointer] == 255:
                datalist[data_pointer] = 0
            else:
                datalist[data_pointer] += 1

        elif instruction_list[instruction_pointer] == "-":
            if datalist[data_pointer] == 0:
                datalist[data_pointer] = 255
            else:
                datalist[data_pointer] -= 1

        elif instruction_list[instruction_pointer] == "[":
            if datalist[data_pointer] == 0 and len(loopend) == 0:
                count = 1
                run = True
                while run:
                    instruction_pointer += 1
                    if instruction_list[instruction_pointer] == "[":
                        count += 1

                    elif instruction_list[instruction_pointer] == "]":
                        count -= 1
                        if count <= 0:
                            run = False

            elif datalist[data_pointer] == 0 and len(loopend) != 0:
                instruction_pointer = loopend[-1] + 1
                loopend.pop()

            elif datalist[data_pointer] != 0:
                loopstart.append(instruction_pointer)
                if len(loopend) != 0:
                    loopend.pop()

        elif instruction_list[instruction_pointer] == "]":
            loopend.append(instruction_pointer - 1)
            instruction_pointer = loopstart[-1] - 1
            loopstart.pop()

        elif instruction_list[instruction_pointer] == ".":
            print(chr(datalist[data_pointer]), end='')

        elif instruction_list[instruction_pointer] == ",":
            datalist[data_pointer] = ord(input("somehthih")[0])

        instruction_pointer += 1


if __name__ == '__main__':
    main()
