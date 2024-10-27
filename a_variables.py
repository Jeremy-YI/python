""" Variable
string, integer, float, boolean
variable = a container for a value, a variable behaves as if it was value it contains
"""
# string
name = 'bro'
print(name)
print(type(name))
# integer
number1 = 1
print(number1)
print(type(number1))
# float
float1 = 0.01
print(float1)
print(type(float1))
# boolean
bool1 = False
print(bool1)
print(type(bool1))

""" type casting 类型转换
str(), int(), float(), bool()
typecasting = the process of converting a variable from one data type to another 
"""
name = 'bro'
age = 18
score = 99.9
is_student = True
print(float(age))  # 18.0
print(int(score))  # 99
print(str(age))    # '18'
print(type(str(age)))
print(type(str(is_student)))
