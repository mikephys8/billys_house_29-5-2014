__author__ = 'Belonious'

a = 100

def fizz_buzz():
    for i in range(1, a):
        if i % 3 == 0 and i % 5 == 0:
            print('we are checking if ' + str(i) + ' is divided  by 3 and 5')
            print('fizzbuzz')
        elif i % 3 == 0:
            print('we are checking if ' + str(i) + ' is divided  by 3')
            print('fizz')
        elif i % 5 == 0:
            print('we are checking if ' + str(i) + ' is divided  by 5')
            print('buzz')

        else:
            print(i)


fizz_buzz()