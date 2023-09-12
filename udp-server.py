import socket

# Configuração do servidor DNS:
DNS_SERVER_HOST = '127.0.0.1'
DNS_SERVER_PORT = 54321 

# Criação do socket UDP deste servidor:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Criação do socket UDP do servidor DNS:
dns_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Request ao servidor dns para obter um numero ip e uma porta do dominio "servidorudp.com":
domain_name_request = "servidorudp.com"
dns_server_socket.sendto(domain_name_request.encode(), (DNS_SERVER_HOST, DNS_SERVER_PORT))

# Recebendo a resposta do servidor DNS e armazenando o host e ip disponibilizados por ele:
data, client_addr = dns_server_socket.recvfrom(1024)
address_requested = data.decode()
address_requested = address_requested.replace("(", "").replace(")", "").replace("'", "").replace(" ", "").split(",")

REQUESTED_HOST = address_requested[0]
REQUESTED_PORT = int(address_requested[1])

# bind deste servidor com o endereço que servidor dns disponibilizou:
server_socket.bind((REQUESTED_HOST, REQUESTED_PORT))

print(f"Servidor ouvindo em {REQUESTED_HOST}:{REQUESTED_PORT}")

# Função para realizar cálculos:
def calcular(operacao, num1, num2):
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 != 0:
            return num1 / num2
        else:
            return "Divisão por zero não é permitida."
    else:
        return "Operação não suportada."

while True:
    # Recebe os dados do cliente:
    data, client_addr = server_socket.recvfrom(1024)
    data = data.decode()
    operacao, num1, num2 = data.split(',')
    num1 = float(num1)
    num2 = float(num2)

    # Realiza o cálculo:
    resultado = calcular(operacao, num1, num2)

    # Envia o resultado de volta para o cliente:
    server_socket.sendto(str(resultado).encode(), client_addr)
