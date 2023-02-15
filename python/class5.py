# class Person:
#     a = 'Belal'
#     print(a)

# obj = Person()

# class Person:
#     def add(self, a, b):
#         return a+b

#     def sub(self, x ,y):
#         return x-y


# obj = Person()

# result = obj.add(5,7)

# print(obj.add(5,7))

# print(obj.sub(10,5))


# class Myclass:

#     def __init__(self, a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a + self.b

#     def sub(self):
#         return self.a - self.b

#     def multip(self):
#         return self.a * self.b

# num1 = int(input('Enter 1st number : ' ))
# num2 = int(input('Enter 2nd number : ' ))

# my_obj = Myclass(num1,num2)

# # result = my_obj.add()
# # print(result)

# print(my_obj.add())
# # print(my_obj.sub())
# print(my_obj.multip())


class Person:
    def info(self, name,address,phone):
        return name,address,phone

class StudentProfile(Person):
    def info2(self, sroll, scls):
        return sroll, scls

s_obj = StudentProfile()

print(s_obj.info('Belal','Madaripur','01704870490'))
print(s_obj.info2(45,'5th'))


class TeacherProfile(Person):
    def info3(self,designation,salary):
        return designation,salary

t_obj = TeacherProfile()

print(t_obj.info('Belal2','Madaripur2','01704870491'))

print(t_obj.info3('teacher',25000))


class Mentor(Person):
    def info(self, name,address, phone,designation,salary):
        return name,address,phone,designation,salary
    # pass
 
mentor_obj = Mentor()
print(mentor_obj.info('Belal','Madaripur','01704870490','python','25000'))









