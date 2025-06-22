# IRC Rover Control System

This project is a multi-component system for controlling and monitoring a rover with video streaming, joystick-based remote control, GPS mapping, and science payload management. It uses Python, Arduino (C++), Flask, OpenCV, Pygame, and HTML.

## Project Structure

```
arm_motor_control.ino         # Arduino code for rover and arm motor control
cam.py                       # Flask server for multi-camera video streaming
cam_multi.html               # Webpage for displaying multiple camera feeds
final_joystick_rx.py         # UDP receiver for joystick commands, sends to serial
final_joystick_tx.py         # UDP transmitter for joystick commands
joyrx.py                     # Alternate UDP joystick receiver
joytx_motor.py               # Alternate UDP joystick transmitter
map_base_station             # Flask server for GPS mapping and rover tracking
map_rover.py                 # Sends GPS data from rover to base station
rover.py                     # Main rover-side server: video, GPS, and command relay
science.py                   # Science payload control via joystick and serial
video_from_hub.py            # Flask server for video streaming from hub
video.html                   # Webpage for displaying video feeds
```

## Features

- **Rover Motor & Arm Control:**  
  [`arm_motor_control.ino`](arm_motor_control.ino) runs on Arduino, controlling rover movement and arm actuators via serial commands.

- **Joystick Remote Control:**  
  - [`final_joystick_tx.py`](final_joystick_tx.py): Reads joystick input, sends commands over UDP.
  - [`final_joystick_rx.py`](final_joystick_rx.py): Receives UDP commands, relays to Arduino via serial.

- **Video Streaming:**  
  - [`cam.py`](cam.py), [`video_from_hub.py`](video_from_hub.py), [`rover.py`](rover.py): Flask servers streaming multiple camera feeds using OpenCV.
  - [`video.html`](video.html), [`cam_multi.html`](cam_multi.html): Web interfaces to view video streams.

- **GPS Mapping:**  
  - [`map_base_station`](map_base_station): Flask server with Folium map, receives rover GPS, displays path and destination.
  - [`map_rover.py`](map_rover.py), [`rover.py`](rover.py): Send GPS data from rover to base station.

- **Science Payload Control:**  
  - [`science.py`](science.py): Reads joystick input, sends science payload commands via serial.

## Setup & Usage

### 1. Arduino

- Upload [`arm_motor_control.ino`](arm_motor_control.ino) to your Arduino Mega or compatible board.

### 2. Python Environment

- Install dependencies:
  ```sh
  pip install flask opencv-python pygame folium geopy pyserial requests
  ```

### 3. Running Components

- **Joystick Transmitter:**  
  On the control PC:
  ```sh
  python final_joystick_tx.py
  ```

- **Joystick Receiver:**  
  On the rover PC (connected to Arduino):
  ```sh
  python final_joystick_rx.py
  ```

- **Video Streaming:**  
  On the rover PC:
  ```sh
  python rover.py
  ```
  Or for hub streaming:
  ```sh
  python video_from_hub.py
  ```

- **GPS Mapping (Base Station):**  
  On the base station PC:
  ```sh
  python map_base_station
  ```

- **GPS Sender (Rover):**  
  On the rover PC:
  ```sh
  python map_rover.py
  ```

- **Science Payload Control:**  
  On the science control PC:
  ```sh
  python science.py
  ```

- **View Video Feeds:**  
  Open [`video.html`](video.html) or [`cam_multi.html`](cam_multi.html) in your browser.

### 4. Configuration

- Update serial port names (e.g., `COM3`, `/dev/ttyACM0`) and IP addresses in the Python scripts as per your hardware setup.

## Notes

- Ensure all required cameras and joysticks are connected before running the scripts.
- The system uses UDP for joystick commands and HTTP (Flask) for video and GPS data.
- Logging is enabled in some scripts for debugging.

## Authors

- Deepak Rishi G and Dhanush Kumar V

## License

- Specify your license here (e.g., MIT, GPL, etc.)
