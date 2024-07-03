import cv2
from cv2 import aruco
def main():
    
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)
    param_markers = aruco.DetectorParameters()

    cap = cv2.VideoCapture(0)

    while True:
        
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame")
            break
 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        marker_corners, marker_IDs, reject = aruco.detectMarkers(gray, aruco_dict, parameters=param_markers)
        
        if marker_IDs is not None:
            frame = aruco.drawDetectedMarkers(frame, marker_corners, marker_IDs)

        cv2.imshow('Aruco Marker Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()