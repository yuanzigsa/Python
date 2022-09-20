print("计算一下今年过了多少天！")
year = int(input('请输入年份:\n'))
month = int(input('请输入月份:\n'))
day = int(input('请最后输入天数:\n'))
 
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print ('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print ('今天是'+ str(year) + '年的第%d天。' % sum )