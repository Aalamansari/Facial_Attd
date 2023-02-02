import cv2, os, retrainModel, time,shutil
import tts

def take_photo(name=''):

    frame_timeout=None
    try:
        cap=cv2.VideoCapture(0)
        cascade=cv2.CascadeClassifier('init_data'+os.path.sep+'haarcascade_frontalface_default.xml')
        os.chdir('new_register_images')
        os.mkdir(name)
        os.chdir(name)
        count=0

        while True:
            ret,img=cap.read()
            cap_img=img.copy()
            grey=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            
            limit_x=200        #Control the X coordinate of the capturing frame
            limit_y=100        #Control the Y coordinate of the capturing frame
            offset=225      #Control the size contraint of the capturing frame
        
            cv2.rectangle(img,(limit_x,limit_y),(limit_x+offset,limit_y+offset),(0,255,0),2)  # Draw the capturing rectangle

            faces=cascade.detectMultiScale(grey,scaleFactor=1.05,minNeighbors=7)

            cv2.putText(img,str(f'Images left: {count}/5'),(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)


            if len(faces)!=0:
                faces=faces[0]
                x=faces[0]
                y=faces[1]
                w=faces[2]
                h=faces[3]
                
                
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)
                
                if x>limit_x and y>limit_y and (x+w)<limit_x+offset and y+h<limit_y+offset:
                    if count>=1:
                        frame_timeout=int(time.time()+10)

                    bound_name='OK'
                    box_color=(0,255,0)
                    
                    if time_set==0:
                        time_set=int(time.time())
                        time_end=time_set+3                  #Set timeout for each frame capture


                    time_left=int((time_end-time.time())+1)


                    
                    if time_left==0:
                        cv2.putText(img, 'Captured' ,(x-50,y+15), cv2.FONT_HERSHEY_SIMPLEX,.7, (0,255,0), 2)

                    else:
                        cv2.putText(img, str(time_left) ,(x-50,y+15), cv2.FONT_HERSHEY_SIMPLEX,.7, (0,0,0), 2)

                    if int(time.time())>=time_end:
                        # print("Frame Captured")
                        cv2.imwrite(name+str(count)+'.jpg',cap_img)
                        count=count+1
                                 #Set frame timeout after taking atleast one pic
                        if count!=5:
                            time_set=0
                        else:

                            # shutil.rmtree('new_register_images'+os.path.sep+name)
                            cv2.destroyAllWindows()
                            break
                        
                        
                else:

                    time_set=0
                    if frame_timeout:
                        cv2.putText(img,str(f'Time Left: {frame_timeout-int(time.time())}/10'),(50,80),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                        
                        if int(time.time())>frame_timeout:
                            cv2.destroyAllWindows()
                            os.chdir('..'+os.path.sep+'..'+os.path.sep)
                            shutil.rmtree('new_register_images'+os.path.sep+name)
                            return False


                    box_color=(0,0,255)
                    bound_name='Not in Frame'

                
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),2)

                cv2.putText(img, bound_name, (x-100+w,y+15+h), cv2.FONT_HERSHEY_SIMPLEX,.5, box_color, 2)




            key=cv2.waitKey(1)

            if key%256==27:
                cv2.destroyAllWindows()
                os.chdir('..'+os.path.sep+'..'+os.path.sep)
                shutil.rmtree('new_register_images'+os.path.sep+name)
                return False

            cv2.imshow('Cam',img)

        os.chdir('..'+os.path.sep+'..'+os.path.sep)
        res=retrainModel.train_new_algo()
        if res:
            tts.talk("Successfully Registered")
        return res

    except Exception as e:
        print("Detecting Failed:- ",str(e))
