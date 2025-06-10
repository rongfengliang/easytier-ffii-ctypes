# libeasytier-ffi ctypes

## running 

* app.yaml

```code
instance_name = "xxxx"
instance_id = "xxxxxx"
dhcp = true
listeners = [
    "tcp://0.0.0.0:11010",
    "udp://0.0.0.0:11010",
    "wg://0.0.0.0:11011",
]
rpc_portal = "0.0.0.0:0"

[network_identity]
network_name = "xxxxx"
network_secret = "xxxxx"

[[peer]]
uri = "tcp://xxxxx:11010"

[flags]
```

* running

```code
sudo python app.py
```
