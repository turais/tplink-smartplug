import tplink_smartplug

result = tplink_smartplug.send("192.168.178.24", 9999, "info")

if result:
    relay_state = result['system']['get_sysinfo']['relay_state']

    out_string = ""
    if (relay_state):
        out_string = " an."
    else:
        out_string = " aus."

    print("Steckdose ist" + out_string)
