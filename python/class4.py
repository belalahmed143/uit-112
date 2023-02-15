
# my_dic = {
#     'name':'Belal',
#     'roll':45,
#     'department':'CSE',
#     'result':{
#         'bangla':85,
#         'computer':80
#     }
# }

# # print(type(my_dic))
# print(my_dic)
# print(my_dic['roll'])
# print(my_dic['department'])

# print(my_dic.get('name'))

# copy()
# count()

# def belal():
#     print('Hello')

# belal()
# belal()

# name = 'Belal'
# roll = 45
# dep = 'CSE'

# name1 = 'Belal2'
# roll1 = 452
# dep1 = 'CSE'

# print('Name -',name)
# print('Roll : ',roll)
# print('Roll : ',dep)

# print('Name -',name1)
# print('Roll : ',roll1)
# print('Roll : ',dep1)


# def student(name,roll,dep):
#     print(name,' ', roll, ' ',dep)
# #     return name,roll,dep


# student("Belal",45,'CSE')
# student("Belal2",445,'CSE')

# # print(r)
# print(student("Belal",45,'CSE'))
# print(student("Belal2",455,'CSE'))


# def result(roll):
#     bangla=5
#     english=10
#     math=15
#     total =bangla+english+math
#     print(total )
  
# result(10)
# result(20)


# def isc(section,version,roll):
#     print('Section :', section)
#     print('Version :', version)
#     print('Roll :', roll)

# isc(section='E',version='English',roll=7)


# def student(a,b,c):
#     # print(a+b+c)
#     return a+b+c

# # s1 = student(4,6,7)
# print('Belal : ',student(4,6,5))
# student(4,5,7)
# student(4,9,7)
# student(4,52,7)
# student(4,45,7)

# def students(name, number, number1,number2):
#   total =number +number1+number2
#   print(name, total)


# students("Tanvir", 10, 12,15)
# students("Belal", 10, 2,15)

# my=(45,23,45,56)

# def bazar(*args):
#     # print(type(args))
#     total = 0
#     for n in args:
#         total = total + n
#     return total

# print(bazar(23,45))
# print(bazar(23,45,45,21,45))


# def bazar(*args):
#     print(type(args))
#     total = 0
#     for n in args:
#         total=total+ n
#     return total
    
# print (bazar (10,9,12))


# def market (*args):
#     print (type (args))
#     total = 0
#     for n in args:
#         total=total+ n
#     return total
    
# print (market (10,6,12))


# def students(*c):
#   total = 0
#   for n in c:
#     total = total + n
#   return total 

# print(students(10, 12,15))
# print(students(10, 20, 4,15))


# def bazar(*args):
#     total = 0
#     for x in args:
#         total = total + x
#     return total

# print(bazar(25,85,65))
# print(bazar(24,50,20,30,45))
# print(bazar(20,54,52,60))


my_dic = {
    'name':'Belal',
    'roll':45,
    'department':'CSE',
}




# def mark(**kwargs):
#     total = 0
#     for key in kwargs:
#         total = total + kwargs[key]
#     return total

# print(mark(a=34,b=24))


# def mark(**kwargs):
#     total= 0
#     for key in kwargs:
#         total=total+kwargs[key]
#     return total 

# print (mark(a=3,b=5))

# def mark(**kwargs):
#     total= 0
#     for key in kwargs:
#         total=total+kwargs[key]
#     return total 

# print (mark(a=356,b=534))


# sum = lambda a,b : a + b

# print(sum(10,15))


# print((lambda a,b : a * b)(10,25))



def abc(func, a,b):
    return func(a,b)

abc(lambda x , y: x + y, 10,20)



