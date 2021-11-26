import socket
import os
import argparse


# accepting IP and Port address from the command line using argparse 

parser = argparse.ArgumentParser(description="Chat Server")
parser.add_argument('--ip',action='store',dest='IP',required=True)
parser.add_argument('--port',action='store',dest='PORT',required=True,type=int)
given_args = parser.parse_args()

# assigning variable accepted from the command line parser
PORT = given_args.PORT
IP = given_args.IP

USER_NAME = input("Please Choose a username for the chat : ")

print("<**>ONLINE ...")
name = USER_NAME + ">>"
encoded_name = name.encode()


# create socket instance (server) for sending and accepting message
def chat():
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((IP,PORT))
	s.listen(1)

	conn, addr = s.accept()
	print(f"Connected to : {addr}")

    # sending and accepting a message in inifite loop unless the user 
    # types 'bye' which ends the connection
	while True:
		msg = input("\nSEND => ")
		# end connection if the user types 'bye'
		if msg == 'bye':
			conn.send("bye".encode())
			print('<0>OFFLINE =< ')
			# close the connection and exit 
			conn.close()
			sys.exit()
			break
		else:
			data = encoded_name + msg.encode()
			conn.send(data)
			In_messg = conn.recv(8192)
			recv_data = In_messg.decode()
			print("\n"+recv_data)

def main():
	chat()

main()


