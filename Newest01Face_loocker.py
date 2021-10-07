import PIL
from PIL import Image,ImageTk
import cv2
from tkinter import *
import tkinter.messagebox
from tkinter import font as tkFont
import time
import threading
import os
import RPi.GPIO as GPIO


import face_recognition
import cv2
import numpy as np

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

MODEL = 'cnn'
TOLERANCE = 0.10

unlock1=True
unlock2=True
unlock3=True
unlock4=True
unlock5=True

LockerStatus="No State"

global TreadStatus
TreadStatus=True
global Stop_thread
Stop_thread=False
global Stop_thread2
Stop_thread2=False
global TreadState
TreadState=True
global CheckLocker
CheckLocker=True
Deposit_Mode=True
Claim_Mode=True



video_capture = cv2.VideoCapture(0)
width, height = 500, 500

video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.geometry("1280x720")

root.configure(background='#FFFAFA')

root.bind('<Escape>', lambda e: root.quit()) 





def Stop_showFrame():
     global Stop_thread
     Stop_thread=True
     hide_Show_frame()
     MainFrame()
     


def Camera_Tread():
     global t1
     global Stop_thread
     t1=threading.Thread(target=show_frame)
     t1.start()
     print("t1-started Main")
     

def Start_showFrame():
    global Stop_thread
    Stop_thread=False
    global TreadStatus
    Spacer2.grid(row=0,column=1)
    Frame_imageCapture.grid(row=0,column=0)   
    lmain.grid(row=0,column=0) 
    imageCaptureFrame.grid(row=0,column=0,padx=30,pady=50)

    if TreadStatus:
        Camera_Tread()
        TreadStatus=False
    else:
         if (t1.is_alive):
             print("T1 is alive")
         else:
            print("T1 start")
            Stop_thread=True
    print(LockerStatus)

def Capture_Image(index):
        a=tkinter.messagebox.askyesno("Face Capture ","Camera will take a photo of your face to Lock locker 2, Do you want to Proceed ? ")
        global unlock1,unlock2,unlock3,unlock4,unlock5
        time.sleep(1.5)
        if a==True:
            print("capture picture")
            ret, frame = video_capture.read()
 
            if ret:
                 cv2.imwrite(index+".jpg",frame)

                 image=face_recognition.load_image_file(index+".jpg")
                 face_locations = face_recognition.face_locations(image)
                 print("I found {} face(s) in this photograph.".format(len(face_locations)))

                 faces=len(face_locations)
                 if faces==1:
                     if index=="locker1":
                          unlock1=True
                          print("locker 1 lock")
                          tkinter.messagebox.showinfo("face Capture","Face Capture Complete Locker 1 will be Locked ")
                          GPIO.setmode(GPIO.BCM)
                          GPIO.setup(17, GPIO.OUT)
                          GPIO.output(17,True)
                          print("Locker on 1")
                          time.sleep(4)
                          GPIO.output(17,False)
                          GPIO.cleanup()

                     elif index=="locker2":
                          unlock2=True
                          print("locker 2 unlock")
                          tkinter.messagebox.showinfo("face Capture","Face Capture Complete Locker 2 will be Locked ")
                          GPIO.setmode(GPIO.BCM)
                          GPIO.setup(27, GPIO.OUT)
                          GPIO.output(27,True)
                          print("Locker on 1")
                          time.sleep(4)
                          GPIO.output(27,False)
                          GPIO.cleanup()
                     elif index=="locker3":
                          unlock3=True
                          print("locker 3 unlock")
                          tkinter.messagebox.showinfo("face Capture","Face Capture Complete Locker 3 will be Locked ")
                          GPIO.setmode(GPIO.BCM)
                          GPIO.setup(22, GPIO.OUT)
                          GPIO.output(22,True)
                          print("Locker on 1")
                          time.sleep(4)
                          GPIO.output(22,False)
                          GPIO.cleanup()
                     elif index=="locker4":
                          unlock4=True
                          print("locker 4 unlock")
                          tkinter.messagebox.showinfo("face Capture","Face Capture Complete Locker 4 will be Locked ")
                          GPIO.setmode(GPIO.BCM)
                          GPIO.setup(23, GPIO.OUT)
                          GPIO.output(23,True)
                          print("Locker on 1")
                          time.sleep(4)
                          GPIO.output(23,False)
                          GPIO.cleanup()
                     elif index=="locker5":
                          unlock5=True
                          print("locker 5 unlock")
                          tkinter.messagebox.showinfo("face Capture","Face Capture Complete Locker 5  will be Locked ")
                          GPIO.setmode(GPIO.BCM)
                          GPIO.setup(24, GPIO.OUT)
                          GPIO.output(24,True)
                          print("Locker on 1")
                          time.sleep(4)
                          GPIO.output(24,False)
                          GPIO.cleanup()
                
                     Stop_showFrame()
                 else:
                      tkinter.messagebox.showinfo("face Capture","No face Identified")




imageCaptureFrame=Frame(root)
Frame_imageCapture=Frame(imageCaptureFrame, bg="#FFA500",width=1400,height=1900)
lmain = Label(Frame_imageCapture)
button_Cature=Button(Frame_imageCapture,text="Face lock Capture",font=('Helvetica', '20'),command=lambda :Capture_Image(LockerStatus),width=39,height=3,padx=2,pady=2,bg="#F5FFFA").grid(row=1,column=0)
Spacer2=Frame(imageCaptureFrame,width=630,height=630)        

MessageLabel=Label(Spacer2,text="Face Locker will Capture your Face for face Recognition key",font="30",bg="#F0F8FF").grid(row=0,column=0)
MessageLabel=Label(Spacer2,text="Look at the camera and Press Capture",font="30",bg="#F0F8FF").grid(row=1,column=0)
button_Back=Button(Spacer2,text="back to Locker 11",font=('Helvetica', '20'),command=Stop_showFrame,width=39,height=3,padx=2,pady=2,bg="#F5FFFA").grid(row=2,column=0)                     

    
   
        
def show_frame():
   while True:
    while (not Stop_thread):
     ret, frame = video_capture.read()
     if ret:
        print(Stop_thread)
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        time.sleep(0.1)
    

def hide_Show_frame():
    imageCaptureFrame.grid_forget()
    MainFrame_()
    

def show_frame_Claim():
    imageCaptureFrame.grid(row=0,column=0,padx=30,pady=50)
    
    ret, frame = video_capture.read()
    if ret:
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = PIL.Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame_Claim)
    
    Hide_LockerFrame_Claim()

   



def Validate_image(index):

    ret, frame=video_capture.read()
    pic=frame

    cv2.imwrite(index+"_verify.jpg",frame)
    import face_recognition




    known_image = face_recognition.load_image_file(index+".jpg")
    unknown_image = face_recognition.load_image_file(index+"_verify.jpg")

    try:
        biden_encoding = face_recognition.face_encodings(known_image)[0]
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError:
        print("Invalid Image")

    known_encodings = [
    unknown_encoding,
    biden_encoding
    ]

    image_to_test = face_recognition.load_image_file(index+"_verify.jpg")
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

    # See how far apart the test image is from the known faces
    face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)
 
    print("Face distance "+str(face_distances[1]))
    for i, face_distance in enumerate(face_distances):
        print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
        print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
        print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
        print()

    
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

    print("Validating.....")







    print(results[0])
    global unlock1,unlock2,unlock3,unlock4,unlock5

    if face_distances[1]<0.40:
        print("valid image")
        tkinter.messagebox.showinfo("Valid Image ",index+" Unlocked!")
        if index=="locker1":
            unlock1=True
            print("locker 1 unlock")
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(17, GPIO.OUT)
            GPIO.output(17,True)
            print("led on 1")
            time.sleep(4)
            GPIO.output(17,False)
            GPIO.cleanup()
            os.remove("locker1.jpg")
        elif index=="locker2":
             unlock2=True
             GPIO.setmode(GPIO.BCM)
             GPIO.setup(27, GPIO.OUT)
             GPIO.output(27,True)
             print("led on 2")
             time.sleep(4)
             GPIO.output(27,False)
             GPIO.cleanup()
             print("locker 2 unlock")
             os.remove("locker2.jpg")
        elif index=="locker3":
             unlock3=True
             print("locker 3 unlock")
             GPIO.setmode(GPIO.BCM)
             GPIO.setup(22, GPIO.OUT)
             GPIO.output(22,True)
             print("led on 3")
             time.sleep(4)
             GPIO.output(22,False)
             GPIO.cleanup()
             os.remove("locker3.jpg")
        elif index=="locker4":
             unlock4=True
             GPIO.setmode(GPIO.BCM)
             GPIO.setup(23, GPIO.OUT)
             GPIO.output(23,True)
             print("led on 4")
             time.sleep(4)
             GPIO.output(23,False)
             GPIO.cleanup()
             print("locker 4 unlock")
             os.remove("locker4.jpg")
        elif index=="locker5":
             unlock5=True
             GPIO.setmode(GPIO.BCM)
             GPIO.setup(24, GPIO.OUT)
             GPIO.output(24,True)
             print("led on 5")
             time.sleep(4)
             GPIO.output(24,False)
             GPIO.cleanup()
             print("locker 5 unlock")
             os.remove("locker5.jpg")
        MainFrame_()
    else:
        print("Invalid image")
        tkinter.messagebox.showinfo("Invalid Image","Invalid face unlock, Locker locked!")

def Locker1():
     global unlock1
     global LockerStatus
     if  unlock1==True:
        print(str(unlock1)+" unlock mode 1")
        if Claim_Mode==True:
           Validate_image("locker1")
            
        else:
          print("Locker 1 capture..")
          LockerStatus="locker1"
          if(os.path.isfile('locker1.jpg')):
             tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
          else:
               Start_showFrame()
        
     else:
        print("Validate image start")
        if Deposit_Mode==True:
           tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
           #Validate_image("locker5")
        
def Locker2():
    global unlock2
    global LockerStatus
    if  unlock2==True:
        if Claim_Mode==True:
           Validate_image("locker2")
            
        else:
          print("Locker 2 capture..")
          LockerStatus="locker2"
          if(os.path.isfile('locker2.jpg')):
             tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
          else:
               Start_showFrame()
        
    else:
        print("Validate image start")
        if Deposit_Mode==True:
           tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
           #Validate_image("locker5")

def Locker3():
     global unlock4
     global LockerStatus
     if  unlock4==True:
        if Claim_Mode==True:
           Validate_image("locker3")
            
        else:
          print("Locker 3 capture..")
          LockerStatus="locker3"
          if(os.path.isfile('locker3.jpg')):
             tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
          else:
               Start_showFrame()
        
     else:
        print("Validate image start")
        if Deposit_Mode==True:
           tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
           #Validate_image("locker5")

def Locker4():
     global unlock4
     global LockerStatus
     if  unlock4==True:
        if Claim_Mode==True:
           Validate_image("locker4")
            
        else:
          print("Locker 4 capture..")
          LockerStatus="locker4"
          if(os.path.isfile('locker4.jpg')):
             tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
          else:
               Start_showFrame()
        
     else:
        print("Validate image start")
        if Deposit_Mode==True:
           tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
           #Validate_image("locker5")

def Locker5():
    global unlock5
    global LockerStatus


    if  unlock5==True:
        if Claim_Mode==True:
                Validate_image("locker5")
            
        else:
            print("Locker 5 capture..") 
            LockerStatus="locker5"
            if(os.path.isfile('locker5.jpg')):
                tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
            else:
                Start_showFrame()
        
    else:
        print("Validate image start")
        if Deposit_Mode==True:
            tkinter.messagebox.showinfo("Locker Ouccupied","Locker ouccupied, Please Select anothere locker!")
            #Validate_image("locker5")

    


def MainFrame_():
    print(threading.active_count)
    global CheckLocker
    global unlock1,unlock2,unlock3,unlock4,unlock5
    i=1
    while(CheckLocker):
        
        if(os.path.isfile('locker1.jpg')):
            unlock1=True
            print("Locker 1 locked")

        if(os.path.isfile('locker2.jpg')):
            unlock2=True
            print("Locker 2 locked")

        if(os.path.isfile('locker3.jpg')):
            unlock3=True
            print("Locker 3 locked")

        if(os.path.isfile('locker4.jpg')):
            unlock4=True
            print("Locker 4 locked")

        if(os.path.isfile('locker5.jpg')):
            unlock3=True
            print("Locker 5 locked")
        

      
        CheckLocker=False
        

    

    global AddFrame1
    AddFrame1=Frame(root, bg="#FFFAFA", padx=15, pady=15,width=140,height=700)
    AddFrame1.grid(row=0,column=0)
    global MainFrame
    MainFrame=Frame(root, bg="#FFFAFA", padx=15, pady=15,)
    MainFrame.grid(row=0,column=1)
    global AddFrame2
    AddFrame2=Frame(root, bg="#FFFAFA", padx=15, pady=15,width=140,height=500)
    AddFrame2.grid(row=0,column=2)
    button_Claim=Button(MainFrame,text="Claim",font=('Helvetica', '20'),command=Hide_MainFrame_claim,width=60,height=10,bg="#F5FFFA").grid(row=2,column=0,sticky=NSEW)
    button_Deposit=Button(MainFrame,text="Deposit",font=('Helvetica', '20'),command=Hide_MainFrame,width=60,height=10,bg="#F5FFFA").grid(row=3,column=0)

def Hide_MainFrame():
    AddFrame1.grid_forget()
    MainFrame.grid_forget()
    AddFrame2.grid_forget()
    LockerFrame()

def Hide_MainFrame_claim():
    AddFrame1.grid_forget()
    MainFrame.grid_forget()
    AddFrame2.grid_forget()
    LockerFrame_Claim()

def LockerFrame():
    global FrameDeposit,Claim_Mode,Deposit_Mode
    Claim_Mode=False
    Deposit_Mode=True
    FrameDeposit=Frame(root,bg="#FFFAFA")
    FrameDeposit.grid(row=0,column=1,padx=5,pady=16)
    global Spacer1
    Spacer1=Frame(root,width=275,height=691,bg="#F0F8FF")
    Spacer1.grid(row=0,column=0)

    button_Deposit1=Button(FrameDeposit,text="Locker 1",font=('Helvetica', '20'),command=Locker1,width=20,height=10,padx=2,pady=2,bg="#F0F8FF")
    button_Deposit1.grid(row=0,column=0,)
    button_Deposit2=Button(FrameDeposit,text="Locker 2",font=('Helvetica', '20'),command=Locker2,width=20,height=10,padx=2,pady=2,bg="#F0F8FF")
    button_Deposit2.grid(row=0,column=1,)
    button_Deposit3=Button(FrameDeposit,text="Locker 3",font=('Helvetica', '20'),command=Locker3,width=20,height=10,padx=2,pady=2,bg="#F0F8FF")
    button_Deposit3.grid(row=0,column=2)
    button_Deposit4=Button(FrameDeposit,text="Locker 4",font=('Helvetica', '20'),command=Locker4,width=20,height=10,padx=2,pady=2,bg="#F0F8FF")
    button_Deposit4.grid(row=1,column=0,)
    button_Deposit5=Button(FrameDeposit,text="Locker 5",font=('Helvetica', '20'),command=Coin_Tread,width=20,height=10,padx=2,pady=2,bg="#F0F8FF")
    button_Deposit5.grid(row=1,column=1,)
    button_DepositBack=Button(FrameDeposit,text="Back",font=('Helvetica', '20'),command=Hide_LockerFrame_back,width=20,height=10,padx=2,pady=2,bg="#F0F8FF").grid(row=1,column=2,)

    if(os.path.isfile('locker1.jpg')):
        button_Deposit1.config(bg='#FA8072')
    if(os.path.isfile('locker2.jpg')):
        button_Deposit2.config(bg='#FA8072')
    if(os.path.isfile('locker3.jpg')):
        button_Deposit3.config(bg='#FA8072')
    if(os.path.isfile('locker4.jpg')):
        button_Deposit4.config(bg='#FA8072')
    if(os.path.isfile('locker5.jpg')):
        button_Deposit5.config(bg='#FA8072')
            

            
def InsertCoin():
    Hide_LockerFrame()
    global insertCoin
    global Stop_thread2
    InsertCoin=Frame(root,bg="#F5FFFA")
    Spacer_claim=Frame(root,width=275,height=691,bg="#F5FFFA")
    Spacer_claim.grid(row=0,column=0)
    ClaimMessage=Label(Spacer_claim,text="Insert Coin to Proceed",font="120")
    ClaimMessage.grid(row=1,column=1)
    n=0
    while True:
        while (not Stop_thread2):
            print("waiting for coin to insert")
            time.sleep(1)
            n=n+1
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(18, GPIO.IN) #elisi ang channel na variable sa port na gusto nimo
            #GPIO.output(channel_is_on,LOW)
            channel_is_on = GPIO.input(18)  # Returns 0 if OFF or 1 if ON elisi ang channel na variable sa port na gusto nimo
            

            if n==22:
                Stop_thread2=True
                Spacer_claim.grid_forget()
                MainFrame_()
            elif channel_is_on==1:
                print("Channel")
                print(channel_is_on)
                Stop_thread2=True
                Locker5()
            
                
                 

            
                


def Coin_Tread():
     global t2
     global Stop_thread2
     t2=threading.Thread(target=InsertCoin)
     if t2.is_alive==True:
        print("Insert coin called")
        InsertCoin()
        
     else:
        t2.start()
        print("t2-started Main")





  
def LockerFrame_Claim():
    global FrameClaim,Claim_Mode,Deposit_Mode,unlock1,unlock3
    
    Claim_Mode=True
    Deposit_Mode=False
    print(str(Claim_Mode)+ " claim mode")
    print(str(unlock1)+ " unlock 1 mode")
    print(str(unlock3)+ " unlock 3 mode")
    
    FrameClaim=Frame(root,bg="#F5FFFA")
    FrameClaim.grid(row=0,column=1,padx=5,pady=16)
    global Spacer_claim
    Spacer_claim=Frame(root,width=275,height=691,bg="#F5FFFA")
    Spacer_claim.grid(row=0,column=0)
    ClaimMessage=Label(Spacer_claim,text="Select your Locker",font="50")
    ClaimMessage.grid(row=0,column=0)
   
    button_Deposit1=Button(FrameClaim,text="Locker 1",font=('Helvetica', '20'),command=Locker1,width=20,height=10,padx=2,pady=2,bg="#F0F8FF").grid(row=0,column=0,)
    button_Deposit2=Button(FrameClaim,text="Locker 2",font=('Helvetica', '20'),command=Locker2,width=20,height=10,padx=2,pady=2,bg="#F0F8FF").grid(row=0,column=1,)
    button_Deposit3=Button(FrameClaim,text="Locker 3",font=('Helvetica', '20'),command=Locker3,width=20,height=10,padx=2,pady=2,bg="#F0F8FF").grid(row=0,column=2)
    button_Deposit4=Button(FrameClaim,text="Locker 4",font=('Helvetica', '20'),command=Locker4,width=20,height=10,padx=2,pady=2,bg="#F0F8FF").grid(row=1,column=0,)
    button_Deposit5=Button(FrameClaim,text="Locker 5",font=('Helvetica', '20'),command=Locker5,width=20,height=10,padx=2,pady=2,bg="#F0F8FF").grid(row=1,column=1,)
    button_DepositBack=Button(FrameClaim,text="Back",font=('Helvetica', '20'),command=Hide_LockerFrame_Claim_back,width=20,height=10,padx=2,pady=2,bg="#F0F8FF").grid(row=1,column=2,)



def Hide_LockerFrame():
    FrameDeposit.grid_forget()
    Spacer1.grid_forget()


def Hide_LockerFrame_Claim():
    FrameClaim.grid_forget()
    Spacer_claim.grid_forget()

def Hide_LockerFrame_Claim_back():
    FrameClaim.grid_forget()
    Spacer_claim.grid_forget()
    MainFrame_()

def Hide_LockerFrame_back():
    FrameDeposit.grid_forget()
    Spacer1.grid_forget()
    MainFrame_()



helv36 = tkFont.Font(family='Helvetica', size=15, weight=tkFont.BOLD)






MainFrame_()


#show_frame()
root.mainloop()