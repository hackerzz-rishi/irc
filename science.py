import serial
import time

import pygame

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check for available joysticks
joystick_count = pygame.joystick.get_count()

if joystick_count > 0:
    # Find the Logitech Extreme 3D Pro joystick (you might need to adjust the index)
    joystick = pygame.joystick.Joystick(0)

# Replace 'COMx' with the appropriate port name on Windows, or '/dev/ttyUSB0' on Linux
ser = serial.Serial('COM8', 115200, timeout=1)

joystick.init()
counta = 0
countb = 0
countc = 0
countd = 0
try:
    while True:
        # Send data to the serial device
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        button_state_a = joystick.get_button(9)
        button_state_b = joystick.get_button(10)
        button_state_c = joystick.get_button(11)

        #print(button_state_a, button_state_b, button_state_c)

        res = 'a' * button_state_a + 'b' * button_state_b + 'c' * button_state_c
        if res == 'a':
            counta += 1
        elif res == 'b':
            countb += 1
        elif res == 'c':
            countc += 1
        elif res == 'd':
            countd += 1

        if counta == 1:
            ser.write('a'.encode())
        elif countb == 1:
            ser.write('b'.encode())
        elif countc == 1:
            ser.write('c'.encode())
        elif countd == 1:
            ser.write('d'.encode())

        print(res)

except KeyboardInterrupt:
    print("KeyboardInterrupt: Stopping the serial communication.")

finally:
    # Close the serial connection when done
    ser.close()
