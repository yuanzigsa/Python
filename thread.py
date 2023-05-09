import threading


def worker(num):
    """每个线程要执行的任务"""
    print(f"Worker {num} 开始工作")
    # 在这里编写需要在多个线程中并发执行的代码
    print(f"Worker {num} 结束工作")


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

print("所有线程执行完毕")
