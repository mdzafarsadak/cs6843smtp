from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = 'smtp.nyu.edu'
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 25))
    recv = clientSocket.recv(1024)

    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    mailfromcommand = 'MAIL FROM\r\n'
    clientSocket.send(b"MAIL FROM: bappy1122@gmail.com\r\n")
    recv2 = clientSocket.recv1(1024).decode()
    print(recv2)
    if recv2[:3] != '250':
        print('250 reply not received from server.')


    # Send RCPT TO command and print server response.
    mailrcptto = 'RCPT TO\r\n'
    clientSocket.send(b"RCPT TO: ms12871@nyu.edu\r\n")
    recv2 = clientSocket.recv(1024).decode()
    print(recv2)
    if recv2[:3] != '250':
        print('250 reply not received from server.')

    # Send DATA command and print server response.
    clientSocket.send(b"DATA\r\n")
    recv2 = clientSocket.recv(1024)

    # Send message data.

    msg += '\r\n' + msg
    clientSocket.sendall(msg.encode())

    # Message ends with a single period.
    clientSocket.sendall(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if (recv[:3] != '250'):
        print('250 reply not received from server')

    # Send QUIT command and get server response.
    clientSocket.sendall('QUIT\r\n'.encode())


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
