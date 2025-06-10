import ctypes
from ctypes import c_char_p, c_int32, POINTER, Structure, c_size_t

# 定义结构体 KeyValuePair
class KeyValuePair(Structure):
    _fields_ = [
        ('key', c_char_p),
        ('value', c_char_p),
    ]

def find_library():
    import os
    import sys
    lib_dir = os.path.join(os.path.dirname(__file__), 'lib')
    if sys.platform == 'win32':
        lib_path = os.path.join(lib_dir, 'easytier_ffi.dll')
    elif sys.platform == 'darwin':
        lib_path = os.path.join(lib_dir, 'libeasytier_ffi.dylib')
    else:
        lib_path = os.path.join(lib_dir, 'libeasytier_ffi.so')
    if not os.path.exists(lib_path):
        raise FileNotFoundError(f"Library not found.")
    return lib_path

lib = ctypes.CDLL(find_library())

# void get_error_msg(const char **out);
lib.get_error_msg.argtypes = [POINTER(c_char_p)]
lib.get_error_msg.restype = None

# void free_string(char* s);
lib.free_string.argtypes = [c_char_p]
lib.free_string.restype = None

# int32_t parse_config(const char* cfg_str);
lib.parse_config.argtypes = [c_char_p]
lib.parse_config.restype = c_int32

# int32_t run_network_instance(const char* cfg_str);
lib.run_network_instance.argtypes = [c_char_p]
lib.run_network_instance.restype = c_int32

# int32_t retain_network_instance(const char** inst_names, uintptr_t length);
lib.retain_network_instance.argtypes = [POINTER(c_char_p), c_size_t]
lib.retain_network_instance.restype = c_int32

# int32_t collect_network_infos(KeyValuePair* infos, uintptr_t max_length);
lib.collect_network_infos.argtypes = [POINTER(KeyValuePair), c_size_t]
lib.collect_network_infos.restype = c_int32


__version__ = "0.1.0"

__doc__ = """
ctypes_easytier_ffi - A Python FFI for EasyTier
"""