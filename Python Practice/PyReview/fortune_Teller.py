# This is a Fortune Teller Game
print('Please insert first name in all lower case:')
user_inputName=raw_input()
array1=['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j','k','l', 'm','n','o']
firstLetter = user_inputName[0]
array2=['p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

def Fortune():
    if len(user_inputName) < 6 and array1.count(firstLetter) == 1 :
        print "A"

    elif len(user_inputName) < 6 and array1.count(firstLetter) == 0:
        print "B"

    elif array2.count(firstLetter) == 1:
        print "C"

    elif array2.count(firstLetter) == 0:
        print "D"
    else:
        print "You're not special enough for a fortune"

Fortune()
