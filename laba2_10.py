import os
import re
import threading

received_packages = re.compile(r"(\d) received")
status = ("no response", "alive but losses", "alive")

def ping_ip(ip):
    ping_out = os.popen("ping -q -c2 " + ip, "r")  # получение вердикта
    print("... pinging ", ip)
    while True:
        line = ping_out.readline()
        if not line:
            break
        n_received = received_packages.findall(line)
        if n_received:
            print(ip + ": " + status[int(n_received[0])])

# Список IP-адресов для проверки подлинности
ips_to_ping = ["192.168.178." + str(suffix) for suffix in range(20, 30)]

# Создаваем и запускаем потоки
threads = [threading.Thread(target=ping_ip, args=(ip,)) for ip in ips_to_ping]
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()