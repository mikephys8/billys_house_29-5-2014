__author__ = 'Belonious'

a = 5
b = 'hello'
c = [['hello',5],['peinaw',2],['ksernaw',2],['peos',4],['kalhag',6]]
d = []
def sum_numbers():
    # mysum = 0
    for item in c:
        for i in item:
            d.append(i)
        # mysum = mysum + item[1]
    # print(mysum)
    print (d)

sum_numbers()



# def print_b(word, number):
#     for item in range(number):
#         c.append(word)
#     return c
#
#     # print(number * word)
#
# print(print_b(b, a))




