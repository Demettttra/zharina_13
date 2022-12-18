#задача_1
def decor(my_func):
    def wrapper(arg):
        print(type(arg))
        my_func(788)
    return wrapper
@decor
def my_func(a):
    if type(a) is tuple:    #(1,2,3,'a','bc8?',7,8,9)
        simbols = 0
        for i in a:
            if type(i) is str:    simbols+=len(i)
        print('Длина всех строк равна: ', simbols)
    if type(a) is list:    #[1,2,3,'a','bc8?']
        nums=0
        letters=0
        for i in str(a):
            if i.isdigit():    nums+=1
            if i.isalpha():    letters+=len(i)
        print('чисел: ', nums, 'букв: ', letters)
    if type(a) is str:    #'788'
        alph=''
        for i in a:
            if i.isalpha():    alph+=i
        print(len(alph))
    if type(a) is int:    #788
        nechet=''
        for i in str(a):
            if int(i)%2!=0:    nechet+=i
        print(len(nechet))
my_func(788)













