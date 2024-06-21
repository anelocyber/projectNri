import face_recognition
import pickle
import os

def encode_faces():
    known_faces = []
    known_names = []

    for user_name in os.listdir('dataset'):
        user_dir = os.path.join('dataset', user_name)
        for image_name in os.listdir(user_dir):
            image_path = os.path.join(user_dir, image_name)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            if encodings:
                known_faces.append(encodings[0])
                known_names.append(user_name)

    with open('encodings.pkl', 'wb') as f:
        pickle.dump((known_faces, known_names), f)
    print("Encoding complete and saved to encodings.pkl")

if __name__ == "__main__":
    encode_faces()
