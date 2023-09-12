import socket
import time

# Configuração do servidor DNS:
DNS_SERVER_HOST = '127.0.0.1'
DNS_SERVER_PORT = 54321 

# Configuração do endereço deste client:
CLIENT_HOST = '127.0.0.20'
CLIENT_PORT = 12321 

# Criação do socket deste cliente:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

print(f"Servidor {REQUESTED_HOST}:{REQUESTED_PORT} CONECTADO.")

client_socket.bind((CLIENT_HOST, CLIENT_PORT))
client_socket.connect((REQUESTED_HOST, REQUESTED_PORT))

# Abre o arquivo apenas para apagar os registros da execução anterior(zerar o arquivo):
with open("tcp_client_time_data.txt", "w") as arquivo_aberto:
    pass

# Lista de operações para automatização dos testes de requisição:
operacoes = [
    {"operacao": "soma", "num1": 10, "num2": 5},
    {"operacao": "subtracao", "num1": 20, "num2": 8},
    {"operacao": "multiplicacao", "num1": 7, "num2": 3},
    {"operacao": "soma", "num1": 10, "num2": 5},
    {"operacao": "subtracao", "num1": 20, "num2": 8},
    {"operacao": "multiplicacao", "num1": 7, "num2": 3},
]

for op in operacoes:
    # precisei utilizar um intervalo entre as requisições, pois aparentemente o curto intervalo entre as requisições estava afetando o resultado do teste:
    time.sleep(1)
    print("_________")
    operacao = op["operacao"]
    num1 = op["num1"]
    num2 = op["num2"]

    # Envia os dados para o servidor e registra o momento do envio da requisição:
    data = f"{operacao},{num1},{num2}"
    envio = time.time()
    client_socket.send(data.encode())

    # Recebe o resultado do servidor e registra o momento do recebimento da resposta:
    resultado = client_socket.recv(1024).decode()
    recebimento = time.time()

    print(f"Resultado da operação '{operacao}': {resultado}")
    tempo = recebimento - envio

    print(f"TEMPO: {tempo}")
    print("_________")

    # Salva no arquivo o tempo total registrado entre o tempo de envio e da resposta do calculo:
    with open("tcp_client_time_data.txt", "a") as arquivo:
        arquivo.write(str(tempo)+"\n")

# Fecha a conexão com o servidor:
client_socket.close()
