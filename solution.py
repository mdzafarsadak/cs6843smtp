from socket import *

#import time

msg = "\r\n I love Computer"
endmsg = "\r\n.\r\n"

mailserver = ("mail.smtp2go.com", 2525) #Fill in start #Fill in end

clientSocket = socket(AF_INET, SOCK_STREAM)
#clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024)
recv = recv.decode()
print("Message after connection request:" + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print("Message after EHLO command:" + recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


mailFrom = "MAIL FROM: <bappy1122@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)

rcptTo = "RCPT TO: <ms12871@nyu.edu> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: "+recv3)

data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)


#sub = input("Enter the subject : ")
subject = "Subject: SMTP Client Python Script \r\n\r\n"
clientSocket.send(subject.encode())
#date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
#date = date + "\r\n\r\n"
#clientSocket.send(date.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())

quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()