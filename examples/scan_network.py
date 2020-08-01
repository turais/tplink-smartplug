from pprint import pprint

import tplink_smartplug

ip_begin = "192.168.178."

for i in range(0, 254, 1):
    ip = ip_begin + str(i)
    result = tplink_smartplug.send_v(ip, 9999, 0.1, "info")
    if result:
        pprint(result)