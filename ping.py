import subprocess
import multiprocessing
import ipaddress


def ping(host):
    """Ping 指定主机，并返回结果"""
    result = subprocess.run(['ping', '-n', '1', '-w', '1000', str(host)], capture_output=True)
    if result.returncode == 0:
        return (host, True)
    else:
        return (host, False)


if __name__ == '__main__':
    ip = input('请输入 IP 地址：')
    mask = input('请输入子网掩码：')

    # 计算子网地址
    net = ipaddress.IPv4Network(f'{ip}/{mask}', strict=False)
    subnet = str(net.network_address)

    # 生成子网内所有地址
    hosts = [str(host) for host in net.hosts()]

    # 并行 ping 操作
    with multiprocessing.Pool(processes=len(hosts)) as pool:
        results = pool.map(ping, hosts)

    # 按是否可达分别存储地址
    reachable_hosts = [host for host, reachable in results if reachable]
    unreachable_hosts = [host for host, reachable in results if not reachable]

    # 显示可达地址和不可达地址
    print(f'可达地址：{", ".join(reachable_hosts)}')
    print(f'不可达地址：{", ".join(unreachable_hosts)}')
