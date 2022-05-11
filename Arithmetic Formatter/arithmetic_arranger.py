def arithmetic_arranger(problems, result=False):

    # lists that are required to store values or for checking.
    top_level_operands = []
    middle_level_operands = []
    middle_level_operators = []
    acceptable_operators = ['+', '-']
    digit_length = []
    results = []

    # check if there's too many problems. limit is 5.
    if len(problems) > 5:
        return "Error: Too many problems."

    # goes through each element in the list, splits them up and append to appropriate lists.
    for item in problems:
        split_items = item.split()
        (top_num, oper, mid_num) = split_items
        top_level_operands.append(top_num)
        middle_level_operators.append(oper)
        middle_level_operands.append(mid_num)

        # also check the largest size by comparing the top and middle operand. sets the len to digit_length list + 2.
        # +2 is added to account for the spaces required between the longest digit and operator. will be changes further down.
        if len(top_num) > len(mid_num):
            digit_length.append(len(top_num) + 2)
        else:
            digit_length.append(len(mid_num) + 2)

        # check if both operand contains only number. If yes, check if the digits are 4 or less.
        if top_num.isnumeric() and mid_num.isnumeric():
            if len(top_num) and len(mid_num) <= 4:
                pass
            else:
                return "Error: Numbers cannot be more than four digits."
        else:
            return "Error: Numbers must only contain digits."

        # check if operators are + or -
        if oper not in acceptable_operators:
            return "Error: Operator must be '+' or '-'."

    # creates empty strings to store the digits, operators and the dividing lines.
    top_arrangement = ''
    middle_arrangement = ''
    dividing_lines = ''
    final_result = ''

    # calculates result of each operation if needed and stores in a list
    for index in range(len(digit_length)):
        if middle_level_operators[index] == '+':
            results.append(int(top_level_operands[index]) + int(middle_level_operands[index]))
        elif middle_level_operators[index] == '-':
            results.append(int(top_level_operands[index]) - int(middle_level_operands[index]))

    # puts the top operands and the spaces into top_arrangement; the middle operands and operator and spaces into middle_arrangement;
    # appropriate dividing lines into dividing_lines
    for index in range(len(digit_length)):
        if index == len(top_level_operands) - 1:
            top_arrangement += top_level_operands[index].rjust(digit_length[index])
            middle_arrangement += middle_level_operators[index] + middle_level_operands[index].rjust(digit_length[index] - 1)
            dividing_lines += '-' * digit_length[index]
            final_result += str(results[index]).rjust(digit_length[index])
        else:
            top_arrangement += top_level_operands[index].rjust(digit_length[index]) + '    '
            middle_arrangement += middle_level_operators[index] + middle_level_operands[index].rjust(digit_length[index] - 1) + '    '
            dividing_lines += '-' * digit_length[index] + '    '
            final_result += str(results[index]).rjust(digit_length[index]) + '    '

    # check if result is set to True. if True, add in the final result, else exclude it.
    if result:
        arranged_problems = f"{top_arrangement}\n{middle_arrangement}\n{dividing_lines}\n{final_result}"
        return arranged_problems
    else:
        arranged_problems = f"{top_arrangement}\n{middle_arrangement}\n{dividing_lines}"
        return arranged_problems
