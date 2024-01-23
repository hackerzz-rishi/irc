from flask import Flask, jsonify, Response
import cv2
import time
import socket
import threading
import requests
import json
import time
import serial
import random
app = Flask(__name__)
import serial
import time
import requests
global new_rover_lat, new_rover_lon
new_rover_lat, new_rover_lon = 12.959563, 80.058549
def data_to_send():
    url = 'http://192.168.1.109:8000/receive_data'
    max_retries = 3  
    retry_delay = 1 
    c = 1 
    time.sleep(2)
    while True:
        for attempt in range(1, max_retries + 1):
            try:
            # Wait for the Arduino to initialize
                with serial.Serial('COM9', 9600, timeout=1) as serial_gps:
                    con = 0
                    gps_data = serial_gps.readline().decode().strip().split(',')
                    print(gps_data)
                    if gps_data and len(gps_data) == 2:
                        lat = float(gps_data[0])
                        lon = float(gps_data[1])
                        data_to_send = {'lat': lat, 'lon': lon}
                        print('1')
                    else:
                        global new_rover_lat, new_rover_lon
                        new_rover_lat = new_rover_lat + int(random.random() * 10) * 0.00001
                        new_rover_lon = new_rover_lon + int(random.random() * 10) * 0.00001
                        data_to_send = {'lat': new_rover_lat, 'lon': new_rover_lon}
                        con += 1
                        print('2')

                    # Send data as JSON to the Flask server
                    response = requests.post(url, json=data_to_send)
                    serial_gps.close()
                    # Check the response from the server
                    if response.status_code == 200:
                        server_response = response.json()  # Get the JSON response from the server
                        print("Data sent successfully")
                        print("Server response:", server_response)
                        break  # Exit the loop on successful send
                    else:
                        print(f"Failed to send data. Server responded with status code: {response.status_code}")
    
            except requests.exceptions.ConnectionError as e:
                print(f"ConnectionError: Failed to connect to the server. Attempt {attempt}/{max_retries}. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            except ConnectionResetError as e:
                print(f"ConnectionResetError: The connection was reset by the server. Attempt {attempt}/{max_retries}. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
    
            c += 1  # Increment c outside the loop
            # time.sleep(5)  # Adjust the delay between consecutive data sends as needed

def flask_app():
    try:
        camera1 = cv2.VideoCapture(0)
        camera2 = cv2.VideoCapture(1)
        camera3 = cv2.VideoCapture(2)
        camera4 = cv2.VideoCapture(3)
        camera5 = cv2.VideoCapture(4)
        camera6 = cv2.VideoCapture(5)
        camera7 = cv2.VideoCapture(6)
        camera8 = cv2.VideoCapture(7)
        camera9 = cv2.VideoCapture(8)
        
        def generate_frames(camera, camera_name):
            frame_count = 0
            start_time = time.time()
            while True:
                success, frame = camera.read()
                if not success:
                    break
                else:
                    ret, buffer = cv2.imencode('.jpg', frame)
                    if not ret:
                        break
                    frame_bytes = buffer.tobytes()
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
                    frame_count += 1
                    if frame_count % 30 == 0:  # Calculate FPS every 30 frames
                        end_time = time.time()
                        elapsed_time = end_time - start_time
                        fps = frame_count / elapsed_time
                        # print(f"{camera_name} FPS: {fps:.2f}")
        
        @app.route('/video_feed_camera1')
        def video_feed_camera1():
            return Response(generate_frames(camera1, "Camera 1"), mimetype='multipart/x-mixed-replace; boundary=frame')
        
        
        @app.route('/video_feed_camera2')
        def video_feed_camera2():
            return Response(generate_frames(camera2, "Camera 2"), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        @app.route('/video_feed_camera3')
        def video_feed_camera3():
            return Response(generate_frames(camera3, "Camera 3"), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        @app.route('/video_feed_camera4')
        def video_feed_camera4():
            return Response(generate_frames(camera4, "Camera 4"), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        @app.route('/video_feed_camera5')
        def video_feed_camera5():
            return Response(generate_frames(camera5, "Camera 5"), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        @app.route('/video_feed_camera6')
        def video_feed_camera6():
            return Response(generate_frames(camera6, "Camera 6"), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        @app.route('/video_feed_camera7')
        def video_feed_camera7():
            return Response(generate_frames(camera7, "Camera 7"), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        @app.route('/video_feed_camera8')
        def video_feed_camera8():
            return Response(generate_frames(camera8, "Camera 8"), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        @app.route('/video_feed_camera9')
        def video_feed_camera9():
            return Response(generate_frames(camera9, "Camera 9"), mimetype='multipart/x-mixed-replace; boundary=frame')
            
        app.run(host='0.0.0.0', port=8080)
    except Exception as e:
        print(f"An error occurred: {e}")

def receive_data():
    try:
            with serial.Serial('COM12', 115200, timeout=1) as serial_command:

        # print(f"Connection from {addr} has been established.")
            # Receive data from the client
                server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Get the local machine name and a port number
                host = socket.gethostname()
                port = 12345
                # Bind the socket to the port
                server_socket.bind((host, port))
                # Listen for incoming connections (max queue of 5)
                server_socket.listen(5)        
                # Accept incoming connections
                client_socket, addr = server_socket.accept()
                while True:

                        data = client_socket.recv(1024).decode('utf-8')
                    # if not data:
                    #     break
                        print(f"Received from client: {data}")
                        serial_command.write((data + '\n').encode())
    except Exception as e:
        print(f"An error occurred during data reception: {e}")
        serial_command.close()


    finally:
        # Close the connection
        client_socket.close()
        print(f"Connection with {addr} closed.")
if __name__ == '__main__':
    # Start Flask in one thread
    flask_thread = threading.Thread(target=flask_app)
    flask_thread.start()

    # Start socket server in another thread
    #socket_thread = threading.Thread(target=receive_data)
    #socket_thread.start()

    data_send = threading.Thread(target=data_to_send)
    data_send.start()
    # Wait for both threads to finish
    flask_thread.join()
    #socket_thread.join()
    data_send.join()
