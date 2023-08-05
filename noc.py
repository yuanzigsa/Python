import requests
import json
import datetime

# 在一切开始之前，添加本月周末和对应的值班人员，初始化字典
noc_schedule = {}
# 添加值班信息
noc_schedule['5'] = ['魏志强', '李进元']
noc_schedule['6'] = ['桂如宾', '周忠正']
noc_schedule['12'] = ['李进元', '彭延庆']
noc_schedule['13'] = ['王犇', '魏志强']
noc_schedule['19'] = ['李进元', '周忠正']
noc_schedule['20'] = ['王犇', '彭延庆']
noc_schedule['26'] = ['王犇', '李进元']
noc_schedule['27'] = ['彭延庆', '桂如宾']


# 定义电话号码字典
phonebook = {
    '李进元': '17354394275',
    '魏志强': '15871434437',
    '桂如宾': '16602756472',
    '周忠正': '18771078584',
    '王犇': '13278020239',
    '彭延庆': '15272770071',
    '严义兵': '13027180603',
}

# 定义webhook地址和请求头
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=2988f5486ec4bf803d5a1420de389690c4ee6a0b001d29581792860bb232423d'  # 钉钉机器人的Webhook地址

headers = {'Content-Type': 'application/json;charset=utf-8'}

# 获取明天的日期
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
tomorrow_day = str(tomorrow.day)

# 检查明天是否有值班人员的安排
if tomorrow_day in noc_schedule:
    for index, person in enumerate(noc_schedule[tomorrow_day]):
        # 如果只有一个人值班，不添加班次
        if len(noc_schedule[tomorrow_day]) == 1:
            shift = ""
        else:
            shift = "白天" if index == 0 else "晚上"
        # 获取电话号码
        phone_number = phonebook.get(person)
        if not phone_number:
            print(f"找不到{person}的电话号码")
            continue
        # 构建消息内容
        data = {
            "msgtype": "text",
            "text": {
                "content": f"你好，{person}，你明天{shift}有值班安排，请注意！（如果存在换班的情况，请提醒接替人） @{phone_number}"
            },
            "at": {
                "atMobiles": [
                    phone_number  # 需要@的成员手机号
                ],
                "isAtAll": False
            }
        }

        # 发送POST请求
        response = requests.post(webhook, headers=headers, data=json.dumps(data))

        # 打印响应
        print(response.content)
