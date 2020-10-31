import socket                                                           
ip = '127.0.0.1'       #input('digite o ip de conexao: ')
port = 7000
addr = ((ip,port))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        
mensagem = input("\nDigite o numero: ")                                 
client_socket.sendto(mensagem.encode('utf-8'),(addr))                  
print ("\nmensagem enviada\n")                                          
Mensagem_enviar, serverAddress = client_socket.recvfrom(1024)           
print ("IP DO SERVIDOR: ", serverAddress,"\n")                          
print ("Retorno do servidor: ", Mensagem_enviar)                        

client_socket.close()                                                   
