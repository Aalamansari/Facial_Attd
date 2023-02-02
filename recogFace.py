import pickle, cv2, face_recognition, math, os, tts
import mysql.connector as connector
from datetime import datetime
import numpy as np

def init_vals():
    conn=connector.connect(host='localhost',username='root',password='8879309285@Adu',database='facial_recog')
    curs=conn.cursor()

    return curs,conn



def face_confidence(face_distance, face_match_threshold=0.6):
    range = (1.0 - face_match_threshold)
    linear_val = (1.0 - face_distance) / (range * 2.0)

    if face_distance > face_match_threshold:
        return str(round(linear_val * 100, 2)) + '%'
    else:
        value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))) * 100
        return round(value, 2)

def store_data(image,recog_name):
    curs,conn=init_vals()

    os.chdir('recognized_images')
    rec_time=str(datetime.now())
    store_time=(rec_time + '.')[:-1]

    rec_time=rec_time.replace(":","_")
    rec_time=rec_time.replace(" ","_")

    # print(recog_name)
    img_path=recog_name+'_'+rec_time+".jpg"
    cv2.imwrite(img_path,image)
    path='recognized'+os.path.sep+os.path.sep+img_path

    curs.execute(f'insert into user_log(captured_date,name,photo_path) values("{store_time}","{recog_name}","{path}")')
    conn.commit()
    os.chdir('..'+os.path.sep)


def recog_image(img):
    data = pickle.loads(open('init_data'+os.path.sep+'encodings.pickle','rb',).read())

    face_location=[]
    face_encoding=[]
    known_face_encoding=data['encodings']
    known_face_names=data['names']



    small_img=cv2.resize(img,(0,0), fx=0.25,fy=0.25)
    small_img=cv2.cvtColor(small_img,cv2.COLOR_RGB2BGR)

    face_location=face_recognition.face_locations(small_img)
    face_encoding=face_recognition.face_encodings(small_img,face_location)

    for face_encode in face_encoding:
        match=face_recognition.compare_faces(known_face_encoding,face_encode)

        name="Unknown"
        conf="?"

        face_dist=face_recognition.face_distance(known_face_encoding,face_encode)
        best_match_index=np.argmin(face_dist)

        if match[best_match_index]:
            name=known_face_names[best_match_index]
            conf=face_confidence(face_dist[best_match_index])
            
            
            if conf<96:
                name="Unknown"
                conf="?"
        
        if name=='Unknown':
            tts.talk('Please register at the desk')
            store_data(img,name)
            return name

        else:
            tts.talk(f'Welcome,{name}')
            tts.talk('Entry marked')
            store_data(img,name)
            return name

            

   

