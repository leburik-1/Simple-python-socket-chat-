import socket
import os
import argparse


# accepting IP and Port address from the command line using argparse 

parser = argparse.ArgumentParser(description="Chat Client ")
parser.add_argument('--ip',action='store',dest='IP',required=True)
parser.add_argument('--port',action='store',dest="PORT",required=True,type=int)

given_args = parser.parse_args()

# assigning variable accepted from the command line parser
IP = given_args.IP
PORT = given_args.PORT

USER_NAME = input("Please enter username for chat : ")


print("<1>ONLINE...")

name = USER_NAME + ">> "
encoded_name = name.encode()

# create socket instance (client) for accepting and sending message
def chat():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((IP,PORT))

    # sending and accepting a message in inifite loop unless the user recieves 'bye' message
	while True:
		In_msg = s.recv(8192)
		recv_data = In_msg.decode()
		print("\n"+recv_data)
		out_msg = input("SEND => ")
		data = encoded_name + out_msg.encode()
		s.send(data)
        
        # if the accepted message is 'bye' close the connection
		if recv_data == 'bye':
			print("<0>OFFLINE ...?")
			s.close()
			break

def main():
	chat()

main()