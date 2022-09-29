


break_line_chars = ['.', ':']

with open('current.txt', "r", encoding='utf8') as current_file:
    lines = current_file.readlines()

    with open('result.txt', 'w', encoding='utf8') as result_file:

        for line in lines:
            line_size = len(line)

            if line_size <= 4:
                continue

            last_char = line[line_size - 2]
            
            if last_char in break_line_chars:
                result_file.write(line)
            else:
                if line[len(line) - 2] == " ":
                    result_file.write(line[:len(line)-1])
                else:
                    result_file.write(line[:len(line)-1] + " ")