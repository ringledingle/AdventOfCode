with open(r'C:\AOC\Day1_Input.txt', encoding='utf-8') as input_file:
    position = 0
    shitvar = 0
    input_file.read()
    amount_of_brackets = input_file.tell()
    for loop in range(0,amount_of_brackets + 1):
        input_file.seek(loop)
        reading_symbol = input_file.read(1)
        if (reading_symbol) == "(":
            position += 1
        elif (reading_symbol) == ")":
            position -= 1
        else:
            break
        if ((position < 0) & (shitvar == 0)):
            basement = loop + 1
            shitvar += 1
        else:
            continue
    result = (position,basement)
with open(r'C:\AOC\Day1_Output.log', mode='w', encoding='utf-8') as output_file:
        output_file.write(str(result))
