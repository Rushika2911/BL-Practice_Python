              #functions# (runs only when called)
#Calculating wages according to hours
# def calculate_wages(hours: float, rate: float):
#     if hours<=40:
#         return rate*hours
#     else:
#         remain= hours-40
#         return ((rate*40)+ remain*1.5*rate)

# hours= float(input())
# rate=float(input())
# print('Total wages:',calculate_wages(hours,rate))


#assigning grades 
# marks= int(input())
# def get_grades(marks):
#     if marks>=80:
#         print('A')
#     elif marks>=70:
#         print('B')
#     elif marks>=60:
#         print('C')
#     elif marks>=50:
#         print('D')
#     else:
#         print('F')

# get_grades(marks)


#interest calculator
# principal =float(input())
# rate= float(input())
# time= int (input())

# def calculate_interest(principal, rate, time):
#     simple_interest= (principal*rate*time)/100
#     print('simple interest is:', simple_interest)

# calculate_interest(principal, rate , time)


         #eception handling
class InvalidAgeError(Exception):
    pass
def valid_age(age):
    if not isinstance(age,int):
        raise InvalidAgeError('age should be integer')
    if age<0:
        raise InvalidAgeError('age cannot be negative')
    
    if age<18:
        print("not eligible")
    else:
        print('eligible to vote')

try:
    age= int(input('enter yout age'))
    valid_age(age)
except ValueError:
    print('age should be integer')
except InvalidAgeError as e:
    print (e)