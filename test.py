a = 5
b = "hello/mixalis"
c = {
    "name": "Vasilis",
    "last_name": "Amar",
    "number": 2105016799
}
d = {
    "name": "Nikos",
    "last_name": "val",
    "number": 2105867333
}
g = False
ppl = [c, d]
my_numbers = [1,2,3,4,5,6,7,8,9,0]

def iterate_dict(my_dict):
    for key, value in my_dict.items():
        print key, value

def iterate_list(my_list):
    for item in my_list:
        iterate_dict(item)
        print '\n'

def is_odd(number):
    '''
    peinaw agria
    '''
    return number % 2 == 0

def find_by_type(numbers, what_type):
    if what_type is 'odd':
        for number in numbers:
            print is_odd(number)
            if is_odd(number):
                print number
    elif what_type is 'even':
        for number in numbers:
            if is_odd(number) == False:
                print number
    else:
        print what_type + "is a fail type my friend"

# find_by_type(my_numbers, 'odd')
# print'\n'
# find_by_type(my_numbers, 'even')
# print'\n'
# find_by_type(my_numbers, 'poutsa')
# print(b.split('/')[0])

print str(a) + b