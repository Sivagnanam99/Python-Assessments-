try:
    f = open('somefile.txt', 'r')
    print(f.read())
    f.close()
except IOError:
    print('IO Exception Occurs.....')
