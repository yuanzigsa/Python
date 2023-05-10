import pandas as pd

# 读取CSV文件
df = pd.read_csv('students.csv')

# 打印数据集前5行
print(df.head())

# 计算数学成绩平均值
mean_math_score = df['Math Score'].mean()
print("平均数学成绩：", mean_math_score)

# 计算数学成绩中位数
median_math_score = df['Math Score'].median()
print("数学成绩中位数：", median_math_score)

# 计算每个年龄段的学生数量
df['Birthyear'] = pd.to_datetime(df['Birthdate']).dt.year
df['Age'] = 2023 - df['Birthyear']
bins = [0, 18, 21, 25]
labels = ['Under 18', '18-21', '22-25']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
age_counts = df['Age Group'].value_counts()
print("年龄段计数：")
print(age_counts)