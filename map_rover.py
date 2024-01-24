from flask import Flask, jsonify, Response
import cv2
import time
import socket
import threading
import requests
import json
import time
import serial


import serial
import time
import requests


def data_to_send():
    url = 'http://10.10.165.85:8000/receive_data'   #flask server ip

    max_retries = 3
    retry_delay = 1

    c = 1
    with serial.Serial('COM10', 9600, timeout=1) as serial_gps:
        time.sleep(2)
        while True:
            for attempt in range(1, max_retries + 1):
                try:
                    # Wait for the Arduino to initialize
                    con = 0
                    gps_data = serial_gps.readline().decode().strip().split(',')
                    print(gps_data)
                    if gps_data and len(gps_data) == 2:
                        lat = float(gps_data[0])
                        lon = float(gps_data[1])
                        data_to_send = {'lat': lat, 'lon': lon}
                    else:
                        data_to_send = {'lat': con, 'lon': con}
                        con += 1

                    # Send data as JSON to the Flask server
                    response = requests.post(url, json=data_to_send)

                    # Check the response from the server
                    if response.status_code == 200:
                        server_response = response.json()  # Get the JSON response from the server
                        print("Data sent successfully")
                        print("Server response:", server_response)
                        break  # Exit the loop on successful send
                    else:
                        print(f"Failed to send data. Server responded with status code: {response.status_code}")

                except requests.exceptions.ConnectionError as e:
                    print(
                        f"ConnectionError: Failed to connect to the server. Attempt {attempt}/{max_retries}. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                except ConnectionResetError as e:
                    print(
                        f"ConnectionResetError: The connection was reset by the server. Attempt {attempt}/{max_retries}. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

            c += 1  # Increment c outside the loop
            # time.sleep(5)  # Adjust the delay between consecutive data sends as needed




if __name__ == '__main__':
    data_to_send()
