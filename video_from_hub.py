from flask import Flask, render_template, Response
import cv2
import time
app = Flask(__name__)

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
