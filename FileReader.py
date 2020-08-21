def clean_line_of_text(line):
    temp_line = ''
    temp_line = line.strip('\n')
    line = temp_line.strip(' ')
    return line.__add__(' ')

sentence = ''
with open("resources/data.txt") as f:
    for line in f:   
        sentence += clean_line_of_text(line)
    print(sentence.strip(' ').__add__('.'))