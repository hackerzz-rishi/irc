import socket
import time
import serial 
ser = serial.Serial("/dev/ttyACM0" , 115200);
s = time.time()
# Create a UDP socket
di = { 'Direction' : s , 'Speed' : 0  }


while True:

 print("Start")
 udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 #Bind the socket to a specific IP address and port number 
 receiver_address = ('192.168.1.110', 12345)  # Replace with the actual IP and port to listen on
 udp_socket.bind(receiver_address)

 print("Socket Binded ")

 try:
   while True:
    #print("Data Receiving ")
    # Receive data and the address of the sender
    data, sender_address = udp_socket.recvfrom(1024)  # Adjust buffer size as needed
   
    if not data:
     print("Data not received ")
     break

    # Decode the received data
    received_data = data.decode()

    # Process or display the received data
    #print(received_data)
    #ser.write(result.encode())
	
    #ser.reset_input_buffer()
    e = time.time()
    temp = received_data[2: len(received_data) - 2].split(',')
    for i in temp:
      a,v = i.split(':')
      if a in di:
        di[a] = v
    
    res = []
    for i in di:
     res.append(di[i])
    
    out = ",".join(res)
    
    print(out,e-s)
    ser.write(out.encode())
    ser.reset_input_buffer()
        		
 except Exception:
    		# Handle Ctrl+C to gracefully close the socket when the script is interrupted
  print("Receiver script interrupted. Closing socket.")
  udp_socket.close()
