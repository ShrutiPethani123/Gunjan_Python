# import datetime

# n = datetime.datetime.now()
# print(n)

# current_date = datetime.date.today()
# print(current_date)

# print(dir(datetime))

# from datetime import date

# current_date = date.today()
# print(current_date)

# d = date(2023,12,15)
# print(d)

# today=date.today()
# print(today)
# print("Current year: ",today.year)
# print("Current month: ",today.month)
# print("Current day: ",today.day)


# from datetime import time

# t = time()
# print(t)

# t=time(11,31,35) #hour:min:sec
# print(t)

# t=time(hour=11,minute=45,second=56)
# print(t)

# t=time(hour=11,minute=45,second=56 ,microsecond=532532)
# print(t)

# a=time(2,45,20,7567)
# print("Hour: ",a.hour)
# print("minute: ",a.minute)
# print("sec: ",a.second)
# print("Microsecond ", a.microsecond)

from datetime import datetime

# a=datetime(2023 , 12, 3, 4 ,5,56,765)
# print("Current year: ",a.year)
# print("Current month: ",a.month)
# print("Current day: ",a.day)
# print("Hour: ",a.hour)
# print("minute: ",a.minute)
# print("sec: ",a.second)
# print("Microsecond ", a.microsecond)

# print(type(a))

# strftime()

# n = datetime.now()
# print(n)

# t=n.strftime("%H:%M:%S")
# print(t)

# t=n.strftime("%m-%d-%Y")
# print(t)
'''
year - %Y , %y
month - %m
day - %d
hour - %H
min- %M
sec - %S


'''

# strptime()

# d1 = "20 December,2022"
# print(d1)

# date1 = datetime.strptime(d1,"%d %B,%Y")
# print(date1)

# a = "March 15 2023"
# print(a)

# b = datetime.strptime(a,"%B %d %Y")
# print(b)

