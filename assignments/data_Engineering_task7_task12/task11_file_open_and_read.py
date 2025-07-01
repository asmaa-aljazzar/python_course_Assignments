class bcolor:    
    WARNING = '\033[93m'
    ENDC = '\033[0m'
   
with open ('sample.txt', 'r', encoding='utf-8') as f:
    count_line = 0
    count_word = 0
    content = f.read ()
    lines = content.split('\n')
    for i in lines:
        if i:
            count_line += 1
    print (bcolor.WARNING + 'Total Num of lines' + bcolor.ENDC, count_line + 1)
    for word in lines:
        if word:
            count_word += 1
    print (bcolor.WARNING + 'Total Num of words' + bcolor.ENDC, count_line + 1)