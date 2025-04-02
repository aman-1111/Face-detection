from deepface import DeepFace
import cv2

cap = cv2.VideoCapture(0)  # Open the default webcam

while True:
    ret, frame = cap.read()
    
    # Check if the frame is captured properly
    if not ret or frame is None:
        print("Error: Could not capture frame. Check your webcam.")
        break  # Exit the loop if no frame is captured
    
    try:
        # Perform emotion detection
        result = DeepFace.analyze(frame, actions=['emotion'])
        print(result)
    except Exception as e:
        print("DeepFace Error:", e)
    
    cv2.imshow('Emotion Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
