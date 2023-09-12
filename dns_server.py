import socket
import random

# configurações deste servidor DNS
DNS_SERVER_HOST = '127.0.0.1'
DNS_SERVER_PORT = 54321 

known_addresses = {}
available_addresses = [
        ("127.0.0.10", 10345), 
        ("127.0.0.11", 11345), 
        ("127.0.0.12", 12345), 
        ("127.0.0.13", 13345), 
        ("127.0.0.14", 14345), 
        ("127.0.0.15", 15345)
    ]

# Criação do socket udp:
dns_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dns_server_socket.bind((DNS_SERVER_HOST, DNS_SERVER_PORT))
print(f"Servidor DNS ouvindo em {DNS_SERVER_HOST}:{DNS_SERVER_PORT}")

# Escolhe um endereço disponível para a aplicação, removendo-o da lista de endereços disponíveis e colocando no 
# dicionário de endereços conhecidos, junto com o domínio requisitado:
def choose_one_of_the_available_addresses():
    pick = random.choice(available_addresses)
    available_addresses.remove(pick)
    return pick

while True:
    # Recebe a primeira requisição e armazena o dominio desejado pelo cliente:
    data, client_addr = dns_server_socket.recvfrom(1024)
    requested_domain_name = data.decode()
    print("requested_domain_name: ", requested_domain_name)

    # Se o dominio solicitado não estiver cadastrado na lista de domínios conhecidos, 
    # é sorteado uma tupla (ip, port) e retornado para o cliente:
    if(requested_domain_name not in known_addresses):
        known_addresses[requested_domain_name] = choose_one_of_the_available_addresses()
        address_requested = known_addresses[requested_domain_name]
        dns_server_socket.sendto(str(address_requested).encode(), client_addr)
    # Se o domínio solicitado já estiver no dicionário de domínios conhecidos, é retornado o endereço deste domínio:
    else:
        address_requested = known_addresses[requested_domain_name]
        dns_server_socket.sendto(str(address_requested).encode(), client_addr)
    