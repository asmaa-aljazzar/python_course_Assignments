class bcolor:    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# open, read, write, append, close

# region
#
#! Opening and closing files
#
#* r == mode == permition
#   - r = Read[default]: #* the file should be exist
#   - w = Write. Create or #* overwrites
#   - a = Append. #* Creates if not exixt
#   - b = Binary mode #* deal image and videos
#   - + = Read and Write,#* Set next to all above
#           r+ -> read and write but #* the file should be exist 
#           w+ -> like 'w' but allows reading too
#           a+ -> like 'a' but allows reading too
#
# region
#
#? utf-8 ===> uniencoding & encoding:
#*   converts characters into bytes Supports all global languages, symbols, emojis. Efficient for common characters, expands as needed
#*   python by default using utf-8
# print (bcolor.HEADER + "Try reading from 'sample.txt' file: " + bcolor.ENDC)
# file = open ('sample.txt', 'r', encoding='utf-8')
# content = file.read()
# if (file and content):
#     print (content)
#     print ('File content loaded, length:', len (content))
#     print (bcolor.OKGREEN + 'Reading done successfully' + bcolor.ENDC + '\n')

# file.close()
# #
# region
#? with: to close the file after using it, No need to close it manualy
# print (bcolor.HEADER + "Try reading from 'sample.txt' file using with open: " + bcolor.ENDC)
# with open ('sample.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     if (f and content):
#         print (content)
#         print (bcolor.WARNING +'File content loaded, length:' + bcolor.ENDC, len (content))
#         print (bcolor.OKGREEN + 'Reading done successfully' + bcolor.ENDC + '\n')

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
#
#
# region