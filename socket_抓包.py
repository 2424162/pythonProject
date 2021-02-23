import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('47.95.35.14', 80))
# while True:
#     re_data = input("SHU")
#     print(re_data.encode("utf8"))
while True:
    re_data = input("SHU")
    print(re_data.encode("utf8"))
    client.send(re_data.encode("utf8"))
    data = client.recv(1024)
    print(data.decode("utf8"))