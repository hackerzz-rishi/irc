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
        # data_to_send = "Hello, UDP!"  # Replace with your actual data
        # print(data_to_send)
        # Send data using the UDP socket
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Read the joystick input
            joystick_data = []

            hat_state = joystick.get_hat(0)
            dir2 = "s"
            if (hat_state == (0, 1)):
                dir2 = "f"
            elif (hat_state == (0, -1)):
                dir2 = "b"
            elif (hat_state == (-1, 0)):
                dir2 = "l"
            elif (hat_state == (1, 0)):
                dir2 = "r"
            else:
                dir2 = "s"

            joystick_data.append(dir2)

            speed = joystick.get_axis(3) * -1024
            speed = map_range(speed, -1024, 1024, 0, 255)
            joystick_data.append(str(speed))

            dir = "s"

            if (joystick.get_axis(1) * -1024) >= 500:
                dir = 'u'
            elif (joystick.get_axis(1) * -1024) <= -500:
                dir = 'd'
            elif (joystick.get_axis(2) * -1024) <= -500:
                dir = 'r'
            elif (joystick.get_axis(2) * -1024) >= 500:
                dir = 'l'
            elif joystick.get_button(2):
                dir = 'x'
            elif joystick.get_button(3):
                dir = 'v'
            elif joystick.get_button(4):
                dir = 'z'
            elif joystick.get_button(5):
                dir = 'c'
            else:
                dir = 's'

            joystick_data.append(dir)

            joystick_str = ','.join(joystick_data)

            print(joystick_str)
            udp_socket.sendto(joystick_str.encode(), receiver_address)
            time.sleep(0.1)

            # time.sleep(1)  # Adjust the delay as needed
        # Optional: Add a delay to control the sending rate

except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully close the socket when the script is interrupted
    print("Transmitter script interrupted. Closing socket.")
    udp_socket.close()
