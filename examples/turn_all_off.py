from pprint import pprint
from tqdm import tqdm

import tplink_smartplug

ip_begin = "192.168.178."

for i in tqdm(range(0, 254, 1)):
    ip = ip_begin + str(i)
    result = tplink_smartplug.send_v(ip, 9999, 0.1, "off")
    if result:
        pprint(result)