import paramiko

# 设置远程服务器信息
host = 'your_server_ip'
username = 'your_username'
password = 'your_password'

# 创建ssh客户端对象
ssh = paramiko.SSHclient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 连接到远程服务器
    ssh.connect(host,username=username,password=password)

    # 执行远程命令
    command = 'ls -l /'
    stdin, stdout, stderr = ssh.exec_command(command)

    # 打印命令输出结果
    print(stdout.read().decode('utf-8'))

except Exception as e:
    print('Error:',str(e))

finally:
    # 关闭SSH连接
    ssh.close()