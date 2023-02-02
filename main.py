# import face_recognition
import cv2, time, recogFace, takePhoto
import json
import gui_modules
import sys
from PyQt5.QtWidgets import QApplication,QMessageBox




def get_init_data():
    frame_box=''
    cascade=cv2.CascadeClassifier('init_data/haarcascade_frontalface_default.xml')
    with open('init_data/frame_box.json','rb') as frame:
        frame_box=json.load(frame)
    
    return cascade,frame_box

    
def run_face_detect(cascade,frame_box):
    cap=cv2.VideoCapture(0)
    time_end=0
    time_set=0
    bound_name=''
    box_color=None
    cap_frame=None
    rem_time=0


    while True:
        ret,frame=cap.read()
        cap_frame=frame.copy()
        frame=cv2.resize(frame,(700,500))
        cap_frame=cv2.resize(cap_frame,(700,500))
        

        if not ret:
            print('Unable to access camera')     
            return ord('q')   

        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        

        limit_x=int(frame_box['frame_x'])        #Control the X coordinate of the capturing frame
        limit_y=int(frame_box['frame_y'])        #Control the Y coordinate of the capturing frame
        offset=int(frame_box['offset'])          #Control the size contraint of the capturing frame
        
        cv2.rectangle(frame,(limit_x,limit_y),(limit_x+offset,limit_y+offset),(0,255,0),2)  # Draw the capturing rectangle

        faces=cascade.detectMultiScale(grey,scaleFactor=1.05,minNeighbors=7)     
        
        if len(faces)!=0:
            faces=faces[0]
            x=faces[0]
            y=faces[1]
            w=faces[2]
            h=faces[3]
            
            
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
            

            if x>limit_x and y>limit_y and (x+w)<limit_x+offset and y+h<limit_y+offset:
                bound_name='OK'
                box_color=(0,255,0)

                if time_set==0:
                    time_set=int(time.time())
                    time_end=time_set+3
                
                

                if int(time.time())>=time_end:
                    cv2.destroyWindow("Frame")
                    cap.release()
                    res=recogFace.recog_image(cap_frame)
                    return res
                rem_time=int(time_end)-int(time.time())
                cv2.putText(frame,f'Please wait: {str(rem_time)}',(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.4,(0,0,0),1)    
                    
            else:
                time_set=0
                time_end=0
                box_color=(0,0,255)
                bound_name='Not in Frame'


            cv2.putText(frame, bound_name, (x-100+w,y+15+h), cv2.FONT_HERSHEY_SIMPLEX,.5, box_color, 2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            return ord('q')
        
        cv2.imshow('Frame',frame)



if __name__=="__main__":
    cascade,frame_box=get_init_data()
    app=QApplication(sys.argv)
    

    while True:
        window=gui_modules.GUI()
        res=run_face_detect(cascade,frame_box)

        if res== ord('q'):
            break
        
        if res=='Unknown':

            # print(window)

            window.name_edit()
            app.exec_()
            new_name=window.return_name()
            # new_name=input("Enter your name")
            try:

                if new_name=="":
                    raise Exception('Name cannot be empty')
                    
                for char in new_name:
                    if char.isdigit():
                        raise Exception("Name cannot contain number")

            except Exception as e:
                msg=QMessageBox()
                msg.setWindowTitle("Failed")
                msg.setText(str(e))
                x=msg.exec_()

            else:
                val=takePhoto.take_photo(new_name)
                if val:
                    window.reg_ok()

                else:
                    window.reg_failed()
                app.exec_()

        else:

            window.entr_ok()
            app.exec_()
    
