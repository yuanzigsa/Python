import subprocess
from multiprocessing import Pool

hosts = ["58.52.173.2", "192.168.1.2", "192.168.1.3", "192.168.1.4", "192.168.1.5"]

def ping(host):
    """
    Ping the given host and return the result
    """
    result = subprocess.run(['ping', '-c', '1', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return (host, True)
    else:
        return (host, False)

if __name__ == '__main__':
    # Create a process pool with 5 workers
    with Pool(processes=5) as pool:
        # Ping all hosts in parallel
        results = pool.map(ping, hosts)

    # Print the results
    for host, success in results:
        if success:
            print(f"{host} is up")
        else:
            print(f"{host} is down")
