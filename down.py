import numpy as np
import pyautogui
import time
import datetime
import requests
from PIL import Image, ImageChops
info = """
这是一个根据当前屏幕动态信息自动发送钉钉告警信息的脚本
Author: Yuanzi
Date: 22 April 2023
Version：v1.0
"""
banner = """
 ██    ██ ██     ██     ██     ████     ██  ████████ ██
░░██  ██ ░██    ░██    ████   ░██░██   ░██ ░░░░░░██ ░██
 ░░████  ░██    ░██   ██░░██  ░██░░██  ░██      ██  ░██
  ░░██   ░██    ░██  ██  ░░██ ░██ ░░██ ░██     ██   ░██
   ░██   ░██    ░██ ██████████░██  ░░██░██    ██    ░██
   ░██   ░██    ░██░██░░░░░░██░██   ░░████   ██     ░██
   ░██   ░░███████ ░██     ░██░██    ░░███  ████████░██
   ░░     ░░░░░░░  ░░      ░░ ░░      ░░░  ░░░░░░░░ ░░ 
"""
print(banner,info, "\n程序已启动......")
def capture_screen(region=None):
    # 获取屏幕截图
    return np.array(pyautogui.screenshot(region=region))

def compare_images(img1, img2):
    # 将两张图片转换为灰度图像
    gray1 = img1.convert('L')
    gray2 = img2.convert('L')
    # 计算差分图
    diff = ImageChops.difference(gray1, gray2)
    # 对差分图进行阈值化
    thresh = 10
    diff = diff.point(lambda x: 255 if x > thresh else 0)
    # 统计不同之处的数量
    bbox = diff.getbbox()
    if bbox is not None:
        count = bbox[2] * bbox[3]
    else:
        count = 0
    return count

def is_icon_flashing():
    # 截取微信区域
    qq_region = (1540, 965, 1680, 995) #左上角和右下角的横纵坐标
    # 获取两张屏幕截图
    img1 = Image.fromarray(capture_screen(qq_region))
    time.sleep(0.5)  # 等待一段时间，确保图标有足够的时间来闪烁
    img2 = Image.fromarray(capture_screen(qq_region))
    # 比较两张图片的不同之处
    count = compare_images(img1, img2)
    # 如果不同之处的数量超过某个阈值，则认为图标正在闪烁
    return count > 1  # 这里的阈值是根据实际情况来调整的

# 发送钉钉告警
def send_alert():
    url = "https://oapi.dingtalk.com/robot/send?accs_token=eea77628444837429394d98417d1feb5583e9535fcc7e7fefff16303de3d70b3"
    headers = { "Content-Type": "application/json" }
    data = {
        "msgtype": "text",
        "text": {
            "content": "值班号有新消息，请及时处理！！！"
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"监测到状态栏信息图标闪烁，告警消息已发送。")
    else:
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"发送告警消息失败。")


# 持续监控
time_counter1 = 0
time_counter2 = 0
alert_sent = False  # 添加标志变量，看之前有没有发过告警信息
status_msg_sent = False  # 添加标志变量，看之前有没有在控制台输出过消息状态

while True:
    if is_icon_flashing():
        if not alert_sent:  # 如果是首次，则直接发送警报消息
            send_alert()
            alert_sent = True  # 将标志变量设置为True，表示已经发送过警报消息
        else:
            time_counter1 += 1
            if time_counter1 == 7:
                send_alert()
                time_counter1 = 0
                alert_sent = False  # 发送警报消息后，将标志变量重新设置为False
    else:
        if not status_msg_sent:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), "当前无消息")
            status_msg_sent = True
        else:
            time_counter2 += 1
            if time_counter2 == 360:
                status_msg_sent = False  # 控制台输出完，将标志变量重置为False
                time_counter2 = 0
        time.sleep(10)