import socket
import time
import serial 
ser = serial.Serial("COM3" , 115200);
s = time.time()
# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port number
receiver_address = ('192.168.0.237', 12345)  # Replace with the actual IP and port to listen on
udp_socket.bind(receiver_address)

try:
    while True:
        # Receive data and the address of the sender
        data, sender_address = udp_socket.recvfrom(1024)  # Adjust buffer size as needed

        # Decode the received data
        received_data = data.decode()

        # Process or display the received data
        #print(received_data)
        temp = received_data.split()
        a1 , b1 = temp[0].split(":")
        c1 = abs(int(float(b1)))

        a2 , b2 = temp[1].split(":")
        c2 = abs(int(float(b2)))

        a3 , b3 = temp[3].split(":")
        c3 = abs(int(float(b3)))

        result = "A0:"+str(c1) + "," + "A1:"+str(c2) + ","  + "A2:"+str(c3) ;
        ser.write(result.encode())

        ser.reset_input_buffer()
        e = time.time()
        print(result, e-s)
except Exception:
    # Handle Ctrl+C to gracefully close the socket when the script is interrupted
    print("Receiver script interrupted. Closing socket.")
    udp_socket.close()
