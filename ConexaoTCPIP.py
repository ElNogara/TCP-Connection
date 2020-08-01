import socket   #Biblioteca responsável por habilitar os sockets de redes do computador/S.O

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # Make the conection UDP/IP.

ip_dominio = "192.168.0.18"      #IP/DOMINIO.
serverPort = 3000                #Server port.

entrada = 'teste'  # Input that will be passed to the server. GET / HTTP/1.1\nhost: google.com\n\n
client.connect((ip_dominio, serverPort))
try:
    while (input("Digite 0 para fechar a conexão: ") != '0'):
        client.send((input("Você: ") + "\n").encode('utf-8'))  #Send message for the other side and Starting the connection.
        # .encode('utf-8') -> Is used for convert the str to bytes
        resposta = client.recv(1024)                         #Where will receive the message(Quantidade de bytes que podem ser recebidos).
        print(resposta)                    #To print the message.


    client.sendto("\nMESSAGE ENDED...\n".encode('utf-8'), (ip_dominio, serverPort))
    client.close()   #Close the connection
    print("MESSAGE ENDED")
except Exception as erro:
    print(erro) #If the connection not be correct, will show the error.
    client.close()