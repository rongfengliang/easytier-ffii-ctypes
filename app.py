
import time
from ctypes_easytier_ffi import lib, KeyValuePair

config = ""
with open("app.yaml","r") as f:
    config = f.read()

result = lib.run_network_instance(config.encode())

if result == 0:
    print("Network instance started successfully.")
    while True:
        try:
            print("Collecting network infos...")
            time.sleep(3)
            MAX_LEN = 10
            infos = (KeyValuePair * MAX_LEN)()
            result = lib.collect_network_infos(infos, MAX_LEN)
            for i in range(result):
                print(f"{infos[i].key.decode()} => {infos[i].value.decode()}")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

