import socket

# Configuração do servidor DNS:
DNS_SERVER_HOST = '127.0.0.1'
DNS_SERVER_PORT = 54321 

# Criação do socket do servidor:
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Criação do socket UDP do servidor DNS:
dns_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Request ao servidor dns para obter um numero ip e uma porta do dominio "servidortcp.com":
domain_name_request = "servidortcp.com"
dns_server_socket.sendto(domain_name_request.encode(), (DNS_SERVER_HOST, DNS_SERVER_PORT))

# Recebendo a resposta do servidor DNS e armazenando o host e ip disponibilizados por ele:
data, client_addr = dns_server_socket.recvfrom(1024)
address_requested = data.decode()
address_requested = address_requested.replace("(", "").replace(")", "").replace("'", "").replace(" ", "").split(",")

REQUESTED_HOST = address_requested[0]
REQUESTED_PORT = int(address_requested[1])

# bind deste servidor com o endereço que servidor dns disponibilizou:
server_socket.bind((REQUESTED_HOST, REQUESTED_PORT))
server_socket.listen(1)

print(f"Servidor escutando em {REQUESTED_HOST}:{REQUESTED_PORT}...")

while True:
    # Espera por uma conexão de cliente:
    client_socket, client_addr = server_socket.accept()
    print(f"Conexão estabelecida com {client_addr}")

    while True:
        # Recebe a solicitação do cliente:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        # Separa a solicitação em operação, num1 e num2:
        operacao, num1, num2 = data.split(',')
        num1 = float(num1)
        num2 = float(num2)

        # Executa a operação solicitada:
        resultado = None
        if operacao == "soma":
            resultado = num1 + num2
        elif operacao == "subtracao":
            resultado = num1 - num2
        elif operacao == "multiplicacao":
            resultado = num1 * num2
        elif operacao == "divisao":
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Divisão por zero não é permitida."

        # Envia o resultado de volta para o cliente:
        client_socket.send(str(resultado).encode())

    # Fecha a conexão com o cliente:
    print(f"Conexão encerrada com {client_addr}")
    client_socket.close()
