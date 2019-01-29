# import os
#
#
# def is_devices():
#     dev = []
#     devices_name = os.popen("adb devices")
#     devices_names = (devices_name.read())
#     list = str(devices_names).splitlines()
#     del list[0]  # 删除List of devices attached
#     for i in list:
#         if i:
#             devices = (i.split()[0])
#             dev.append(devices)
#     if dev is None:
#         print(dev)
#     else:
#         x = os.popen("adb connect 127.0.0.1:7555")
#         print(x.read())


# if __name__ == '__main__':
#     is_devices()

# x = ('device agent responds with an error code 502', '')
# print(x[0])

def test(*args):
    print(args)
    print(args[0])
    print(args[1])


test("x", "t")