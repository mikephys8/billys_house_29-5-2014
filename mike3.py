__author__ = 'Belonious'

a = 5
b = 'hello'
c = [['hello',5],['peinaw',2],['ksernaw',2],['peos',4],['kalhag',6]]

def check_list(lista):
    # if len(lista[0]) == lista[1]:
    #     return True
    # return len(lista[0]) == lista[1]
    return len(lista[0]) % lista[1] == 0

# print(check_list(['hello', 5]))
# print(check_list(['hello', 6]))

def final():
    for item in c:
        if check_list(item):
            print('To ' + item[0] + ' exei mhkos ' + str(item[1]))
final()


            # def check_list_all():
            #     for item in c:
            #         if len(item[0]) == item[1]:
            #            print('To ' + item[0] + ' exei mhkos ' + str(item[1]) )
            # check_list()


            # def sum_numbers():
            #     for item in c:
            #         for i in item:
            #             d.append(i)
            #         # mysum = mysum + item[1]
            #     # print(mysum)
            #     print (d)
            #
            # sum_numbers()