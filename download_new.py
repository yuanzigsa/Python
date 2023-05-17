#!/usr/bin/python
# coding=utf-8
import os, re, time, random
import threading
import queue
import asyncio
import aiohttp

# 定义一个全局变量，用于存储URL列表
urls = []

# 定义一个函数，用于读取URL列表
def read_urls():
    global urls
    with open('./soft.txt') as f:
        urls = f.readlines()
    urls = ['http' + url.strip().split('http')[-1] for url in urls if 'http' in url]

# 定义一个函数，用于下载URL对应的内容
async def download(url, source_ip):
    connector = aiohttp.TCPConnector(local_addr=(source_ip, 0))
    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(url) as response:
            await response.read()

# 定义一个函数，用于定时杀死所有正在运行的wget进程
async def kill_wget():
    while True:
        os.popen('pkill wget')
        print('pkill wget')
        sec = random.randint(10, 20)
        await asyncio.sleep(sec)

# 定义一个函数，用于分配URL列表和源IP地址
def assign_urls(urls, source_ips):
    url_groups = [[] for i in range(len(source_ips))]
    for i, url in enumerate(urls):
        url_groups[i % len(source_ips)].append(url)
    return [(url_groups[i], source_ips[i]) for i in range(len(source_ips))]

# 定义一个函数，用于启动下载任务
def start_tasks(tasks):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.wait(tasks))

# 主程序
if __name__ == '__main__':
    read_urls()
    source_ips = ['192.168.1.100', '192.168.1.101', '192.168.1.102', '192.168.1.103', '192.168.1.104', '192.168.1.105', '192.168.1.106', '192.168.1.107', '192.168.1.108', '192.168.1.109']
    url_groups = assign_urls(urls, source_ips)
    tasks = []
    for url_group, source_ip in url_groups:
        for url in url_group:
            tasks.append(asyncio.ensure_future(download(url, source_ip)))
    tasks.append(asyncio.ensure_future(kill_wget()))
    start_tasks(tasks)