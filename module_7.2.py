def custom_write(file_name_1, strings):

    strings_positions = {}

    file = open(file_name_1, 'w', encoding='utf-8')
    try:
        for line_number, line in enumerate(strings, start=1):
            byte_position = file.tell()
            file.write(line + '\n')
            strings_positions[(line_number, byte_position)] = line
    finally:
        file.close()
    return strings_positions

info = [ 'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
