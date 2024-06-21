import cv2
import os

def capture_faces(user_name):
    if not os.path.exists('dataset'):
        os.makedirs('dataset')

    user_dir = os.path.join('dataset', user_name)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Frame', frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            img_path = os.path.join(user_dir, f"{user_name}_{count}.jpg")
            cv2.imwrite(img_path, frame)
            print(f"Captured {img_path}")
            count += 1

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    user_name = input("Enter the user name: ")
    capture_faces(user_name)
