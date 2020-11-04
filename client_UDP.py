import socket                                                           # Biblioteca de sockets Python
ip = '127.0.0.1'       #input('digite o ip de conexao: ')
port = 7000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        # Cria o socket UDP
mensagem = input("\nDigite o numero: ")                                 # Digitar a mensagem para ser enviada
client_socket.sendto(mensagem.encode('utf-8'),(addr))                   # Envia a mensagem
print ("\nmensagem enviada\n")                                          # Confirmacao que enviou
Mensagem_enviar, serverAddress = client_socket.recvfrom(1024)           # Le o socket do SERVIDOR e pega IP do mesmo
print ("IP DO SERVIDOR: ", serverAddress,"\n")                          # Mostra o IP e a Porta do Servidor
print ("Retorno do servidor: ", Mensagem_enviar)                        # Mostra a mensagem que o Servidor Retornou
stop = input("")
client_socket.close()                                                   # Fecha o socket
