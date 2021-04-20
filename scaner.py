import socket

def scan(ip, port):
	print('1')
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('2')
	if client.connect_ex((ip, port)):
		print(f"закрыт{port}")
	else:
		print(f'открыт {port}') 

# ip = socket.gethostbyname('https://tvoirecepty.ru/recepts/vypechka-na-lyuboi-vkus')
ip = '46.46.41.240'
for i in range(100):
	print('Порт')
	scan(ip, i)