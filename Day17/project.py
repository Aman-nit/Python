import cv2

# Initialize video capture
cap = cv2.VideoCapture(0)  # Use 0 for webcam, or provide video file path

# Create a CSRT tracker (use directly if version supports it)
tracker = cv2.TrackerCSRT_create()

# Initialize the first frame and manually select the object to track
ret, frame = cap.read()
if not ret:
    print("Failed to read video")
    exit()

# Select the region of interest (ROI) manually (bounding box around the object)
bbox = cv2.selectROI(frame, fromCenter=False, showCrosshair=True)

# Initialize the tracker with the first frame and the selected object
tracker.init(frame, bbox)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Update the tracker and get the new bounding box coordinates
    success, bbox = tracker.update(frame)

    # Draw the bounding box if the tracker was successful
    if success:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.putText(frame, "Tracking failure", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display the frame with the bounding box
    cv2.imshow("Tracking", frame)

    # Press 'q' to quit the tracking window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
