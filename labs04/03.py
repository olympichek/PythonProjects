input_file_name = input('Введіть назву вхідного файлу: ')

try:
    input_file = open(input_file_name, 'r')
    lines = []
    for line in input_file:
        lines.append(line)
    input_file.close()
except IOError as e:
    print('Неможливо зчитати файл!')
    print(str(e))
    exit()

def hasComments(line):
    for c in line:
        if c == '#':
            return True
    return False

def cutComments(line):
    line_builder = []
    for c in line:
        if c == '#': break
        line_builder.append(c)
    return ''.join(line_builder)

for i in range(len(lines)):
    if hasComments(lines[i]):
        lines[i] = cutComments(lines[i])

output_file_name = input('Введіть назву вихідного файлу: ')
try:
    output_file = open(output_file_name, "w")
    for line in lines:
        output_file.write(line)
    output_file.close()
except IOError as e:
    print('Неможливо записати файл!')
    print(str(e))
