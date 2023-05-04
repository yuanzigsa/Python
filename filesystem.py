# 打开输入文件和输出文件
with open('input.txt','r') as input_file, open('output.txt','w') as output_file:
    # 逐好行读取输入文件，并处理每一行数据
    for line in input_file:
        # 去掉每行末尾的换行符
        line = line.rstrip('\n')
        # 将字符串转换为大写字母，并将结果写入输出文件
        output_file.write(line.upper() + '\n')