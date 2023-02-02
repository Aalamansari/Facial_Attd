import shutil
import os
from imutils import paths
import face_recognition
import pickle

#New faces model training algorithm

def train_new_algo():
    try:
        root_path='new_register_images'
        data=pickle.loads(open('init_data'+os.path.sep+'encodings.pickle','rb').read())
        

        image_path= list(paths.list_images(root_path))

        for images in image_path:
            per_name=images.split(os.path.sep)[-2]

            face_image = face_recognition.load_image_file(images)
            face_encoding = face_recognition.face_encodings(face_image)[0]
            
            data['names'].append(per_name)
            data['encodings'].append(face_encoding)

        f = open('init_data'+os.path.sep+'encodings.pickle','wb')
        f.write(pickle.dumps(data))
        f.close()

        shutil.rmtree(root_path+os.path.sep+per_name)     
                    #Remove the pictures and folder after model has been re-trained
        return True

    except Exception as e:
        return False
    
    