import socket

class Client:
    def _init_(self, host, port):
        self.host = str(host)
        self.port = int(port)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        # Connect to the remote server (ngrok public TCP tunnel)
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")

            # Receive data from the server
            
            while True:
                data = self.client_socket.recv(1024)
                if data == b'q':
                    break
                print(data)

        except Exception as e:
            print(f"Error connecting to server: {e}")
        finally:
            self.client_socket.close()
            print("Connection closed.")

# ngrok's public host
ngrok_host = "0.tcp.in.ngrok.io" 

# ngrok's public port 
ngrok_port = 10681  

# Create and run the client
client = Client(ngrok_host, ngrok_port)
client.connect()
