import socket
import time

import pygame
import sys

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
        data_to_send = "Hello, UDP!"  # Replace with your actual data
        print(data_to_send)
        # Send data using the UDP socket
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Read the joystick input
            joystick_data = []
            for i in range(joystick.get_numaxes()):
                if i == 1:
                    axis_value = joystick.get_axis(i)
                    axis_value = -1 * axis_value * 1024
                    if axis_value >= 500 :
                        joystick_data.append(f"Axis_{i}:f" )
                    elif axis_value <= -500:
                        joystick_data.append(f"Axis_{i}:b" )
                elif i == 2:
                     axis_value = joystick.get_axis(i)
                     axis_value = -1 * axis_value * 1024
                     if axis_value <= -500:
                          joystick_data.append(f"Axis_{i}:l" )
                     elif axis_value >= 500:
                          joystick_data.append(f"Axis_{i}:r" )
                elif i == 3:
                    axis_value = joystick.get_axis(i)
                    axis_value = -1 * axis_value * 1024
                    axis_value = map_range(axis_value, -1024, 1024, 0, 255)
                    joystick_data.append(f"Axis_{i}:{axis_value} " )
                
                

                
            hat_x, hat_y = joystick.get_hat(0)
            #joystick_data.append(f"Hat_Switch_X:{hat_x} Hat_Switch_Y:{hat_y} ")



            # Combine all joystick data into a single string
            joystick_str = ''.join(joystick_data)
            print(joystick_str)
            #udp_socket.sendto(joystick_str.encode(), receiver_address)
            time.sleep(0.01)

            # time.sleep(1)  # Adjust the delay as needed
        # Optional: Add a delay to control the sending rate

except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully close the socket when the script is interrupted
    print("Transmitter script interrupted. Closing socket.")
    #udp_socket.close()
