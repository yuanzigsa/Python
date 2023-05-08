import paramiko

# 创建SSH客户端对象
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接远程服务器
ssh.connect('192.168.1.100', username='username', password='password')

# 执行命令并获取结果
stdin, stdout, stderr = ssh.exec_command('ifconfig')
output = stdout.read().decode()

# 输出结果
print(output)

# 关闭SSH连接
ssh.close()