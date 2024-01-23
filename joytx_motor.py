import socket
import time

import pygame
import sys

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the IP address and port number of the receiver
receiver_address = ('192.168.1.110', 12345)  # Replace with the actual IP and port of the receiversend


sys.setrecursionlimit(10 ** 6)
pygame.init()

pygame.joystick.init()

    # Get the number of connected joysticks
num_joysticks = pygame.joystick.get_count()

joystick = None  # Initialize the variable outside the if block

if num_joysticks > 0:
        # Get the first joystick
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print(f"Joystick Name: {joystick.get_name()}")
else:
        print("No joysticks found.")


def map_range(value, from_min, from_max, to_min, to_max):
    # Ensure the value is within the original range
    value = max(min(value, from_max), from_min)
    
    # Map the value to the new range
    from_range = from_max - from_min
    to_range = to_max - to_min
    
    scaled_value = float(value - from_min) / float(from_range)
    mapped_value = to_min + (scaled_value * to_range)
    
    return int(mapped_value)

try:
    while True:
        # Your continuous data generation or acquisition logic here
        # For example, generate some data to be sent
        #data_to_send = "Hello, UDP!"  # Replace with your actual data
        #print(data_to_send)
        # Send data using the UDP socket
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Read the joystick input
            joystick_data = []
            dir = " "
            axis_value = joystick.get_axis(1)
            axis_value1 = joystick.get_axis(2)
            axis_value = -1 * axis_value * 1024
            axis_value1 = -1 * axis_value1 * 1024
            if axis_value >= 500 :
                dir = 'f'
            elif axis_value <= -500:
                dir = 'b'
            elif axis_value1 <= -500:
                dir = 'r'
            elif axis_value1 >= 500:
                dir = 'l'
            else:
                dir = 's'
            axis_value2 = joystick.get_axis(3)
            joystick_data.append('Direction:'+dir)
            axis_value2 = -1 * axis_value2 * 1024
            axis_value2 = map_range(axis_value2, -1024, 1024, 0, 255)
            joystick_data.append(f"Speed:{axis_value2}" )

                
                



            # Combine all joystick data into a single string
            joystick_str = ','.join(joystick_data)
            joystick_str = "**" + joystick_str + "**"
            print(joystick_str)
            udp_socket.sendto(joystick_str.encode(), receiver_address)
            time.sleep(0.01)

            # time.sleep(1)  # Adjust the delay as needed
        # Optional: Add a delay to control the sending rate

except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully close the socket when the script is interrupted
    print("Transmitter script interrupted. Closing socket.")
    udp_socket.close()
