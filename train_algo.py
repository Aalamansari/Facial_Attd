import os
from imutils import paths
import face_recognition
import pickle

# First time dataset algo

root_path='dataset'


def train_algo():
    known_face_encodings = []
    known_face_names = []
    
    try:
        image_path= list(paths.list_images(root_path))
        for images in image_path:
            per_name=images.split(os.path.sep)[-2]

            face_image = face_recognition.load_image_file(images)
            face_encoding = face_recognition.face_encodings(face_image)[0]
            
            known_face_encodings.append(face_encoding)
            known_face_names.append(per_name)
            print(per_name)

        data = {"encodings": known_face_encodings, "names": known_face_names}
        f = open('init_data'+os.path.sep+'encodings.pickle', "wb")
        f.write(pickle.dumps(data))
        f.close()

    except Exception as e:
        print("Failed to register:- "+str(e))

train_algo()