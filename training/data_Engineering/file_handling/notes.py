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
#todo: CODE
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
#
#? with: to close the file after using it, No need to close it manualy
#todo: CODE
# print (bcolor.HEADER + "Try reading from 'sample.txt' file using with open: " + bcolor.ENDC)
# with open ('sample.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
#     if (f and content):
#         print (content)
#         print (bcolor.WARNING +'File content loaded, length:' + bcolor.ENDC, len (content))
#         print (bcolor.OKGREEN + 'Reading done successfully' + bcolor.ENDC + '\n')
#
#todo: CODE
# with open ('sample.txt', 'r', encoding='utf-8') as f:
#     count_line = 0
#     count_word = 0
#     content = f.read ()
#     lines = content.split('\n')
#     for i in lines:
#         if i:
#             count_line += 1
#     print (bcolor.WARNING + 'Total Num of lines' + bcolor.ENDC, count_line + 1)
#     for word in lines:
#         if word:
#             count_word += 1
#     print (bcolor.WARNING + 'Total Num of words' + bcolor.ENDC, count_line + 1)
#
#
# region
#? Reading line by line
# strip(): Dont set an empty line between output, #! Not actual empty line in the file
#todo: CODE
# with open ('sample.txt', 'r', encoding='utf-8') as file:
#     sample_txt = file.readlines ()
#     i = 0
#     print ( bcolor.WARNING + 'num of lines: ' + bcolor.ENDC, len (sample_txt))
#     print (bcolor.FAIL +"With strip" + bcolor.ENDC)
#     for line in sample_txt:
#         #with strip
#         print (bcolor.WARNING + 'line [',(i + 1),']:' + bcolor.ENDC, line.strip ())
#         i += 1
#     print (bcolor.FAIL +"Without strip" + bcolor.ENDC)
#     for line in sample_txt:
#         #with strip
#         print (bcolor.WARNING + 'line [',(i + 1),']:' + bcolor.ENDC)
#         i += 1
# 
# region
#todo: CODE
# lines_to_write = [
#     'First Line\n',
#     'Second Line\n',
#     'Third Line\n',
# ]
# # 
# with open ('output.txt', 'w', encoding='utf-8') as file:
#     for line in lines_to_write:
#         file.write (line)
# print (bcolor.OKGREEN + 'Finishing writhing to [output.txt]' + bcolor.ENDC)
#
# region
#? Append will use function write but mode 'a'
#todo: CODE
# lines_to_write = [
#     'First Line\n',
#     'Second Line\n',
#     'Third Line\n',
# ]
#
# with open ('sample.txt', 'a+', encoding='utf-8') as file:
#     for line in lines_to_write:
#         file.write (line)
# print (bcolor.OKGREEN + 'Finishing writhing to [sample.txt]' + bcolor.ENDC)
# with open ('second.txt', 'a+', encoding='utf-8') as file:
#     for line in lines_to_write:
        # file.write (line)  
# print (bcolor.OKGREEN + 'Finishing writhing to [second.txt]' + bcolor.ENDC)
#
# region
# 
#? try, except, print
#* try: 
#  try a block of code that may cause and error. Python will try to execute this. #! Should have AT LEAST one except
#* except:
#  if Pythin could not find the file, this block runs instead. to print what is the exeption and where happpened.
#* print:
#  Shows a helpful message instead of crashing the program.
# #
# #* read from existing file
#todo: CODE
# try:
#     with open ('sample.txt', 'r', encoding='utf-8') as f:
#         content = f.read ()
#         print (content)
# except:
#     print ("Can't open [sample.txt] for reading Or the file doesn't exist")
# #
# #* read from not existing file
# try:
#     with open ('not_exist_file.txt', 'r', encoding='utf-8') as f:
#         content = f.read ()
#         print (content)
# except:
#     print ("Can't open [not_exist_file.txt] for reading Or the file doesn't exist")
#? without try, except
# with open ('not_exist_file.txt', 'r', encoding='utf-8') as f:
#     content = f.read ()
#     print (content)
#
#? Common Exceptions
#! FileNotFoundError
#todo: CODE
# filename = input ('Enter the file name: ')
# try:
#     with open (filename, 'r', encoding='utf-8') as f:
#         content = f.read ()
#         print (content)
# except FileNotFoundError:
#     print (bcolor.FAIL + "Can't open [" + bcolor.WARNING, filename, bcolor.FAIL + "] for reading Or the file doesn't exist"+ bcolor.ENDC)
#
# region