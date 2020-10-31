import socket
import math                                                             # Biblioteca de sockets Python
host = '127.0.0.1'                                                      # input('digite o ip do servidor: ')
port = 7000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)          # Cria o socket UDP
serv_socket.bind((addr))                                                # Adiciona o endereco ao socket (IP E PORTA)

print ("\nAguardando mensagem\n")
mensagem, ClientAddress = serv_socket.recvfrom(1024)                    # Le o socket do cliente e pega o IP do mesmo
print("IP DO CLIENTE: ", ClientAddress,"\n")                            # Mostra o Endereco do cliente
print ("mensagem recebida: ", mensagem)                                 # Mostra a mensagem enviada do cliente para o servidor
Mensagem_Modificada =  math.exp(float(mensagem))                        # Aplicando a funcao de euler usando a variavel da mensagem do cliente, porem convertida em float
print ("mensagem recebida modificada: ", Mensagem_Modificada)           # Printando a mensagem modificada pelo SERVIDOR
Mensagem_enviar = str(Mensagem_Modificada).encode('utf-8')              # Convertendo Float para string
serv_socket.sendto(bytes(Mensagem_enviar), ClientAddress)               # Convertendo a string para bytes e enviando a mensagem de volta para o cliente

serv_socket.close()                                                     # Fecha o socket
