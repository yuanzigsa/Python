money=1000 #余额
s=int(input('请输入取款金额'))
if money>=s:
    money=money-s
    print('取款成功，余额剩余:',money)