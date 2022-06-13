
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import sys
from social import web
import numpy as np
import cv2
from machinee import detect_and_predict_image
from Machinelearnin import detect_and_predict_mask

class mainwindow(qtw.QWidget):
    def __init__(self):
     
        super().__init__()
        self.setWindowTitle('Covid 19 preventions')
        self.setFixedSize(1024, 870)
        self.setWindowIcon(qtg.QIcon('./images/i3.ico'))
       
 
        
        label_img=qtw.QLabel(self)
        label_img.move(0,0)
        label_img.resize(321,171)
        label_img.setAlignment(qtc.Qt.AlignLeft)
        label_img.setStyleSheet('border:1px solid black')
        label_img.setStyleSheet("border-image: url('./images/COVID-19-Control-and-Prevention.jpg');\n"
"border-color: rgb(255, 255, 127);\n"
"border-bottom-color: rgb(255, 85, 0);")
        
        label_h=qtw.QLabel( "<html><head/><body><p align=\"center\"><span style=\" font: bold 28pt; vertical-align:sub;\"><a align=\"center\" style=\" color:black;\"><span>Covid-19 Preventions</span></a><br>Face Mask Detection And Social Distance Detection<br></span></p></body></html>",self)
        label_h.move(320,0)
        label_h.resize(720,171)
        label_h.setAlignment(qtc.Qt.AlignCenter)
        font=qtg.QFont()
        font.setFamily('Times New Roman')
        font.setBold(True)
        font.setPointSize(22)
        font.setItalic(True)
        font.setWeight(70)
        label_h.setFont(font)
        label_h.setScaledContents(True)
        label_h.setStyleSheet('border:1px solid black')
        label_h.setStyleSheet("color:rgb(0,0,0);\n"
"background-color: rgb(255,255,255);")
        bg=qtw.QLabel(self)
        bg.setGeometry(qtc.QRect(0, 170, 1024, 700))
        bg.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border-image: url('./images/p1.png');\n"
"\n"
"background-repeat: no-repeat; \n"
"") 
        label_t1=qtw.QLabel("Face Mask Dectection",self)
        label_t1.setGeometry(qtc.QRect(300, 200, 351, 71))
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setItalic(True)
        label_t1.setFont(font)
        line = qtw.QFrame(self)
        line.setGeometry(qtc.QRect(260, 250, 411, 20))
        line.setFrameShape(qtw.QFrame.HLine)
        line.setFrameShadow(qtw.QFrame.Sunken)
        webcam1=qtw.QPushButton("Webcam",self)
        webcam1.clicked.connect(self.web)
        webcam1.setGeometry(qtc.QRect(380, 280, 151, 71))
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        webcam1.setFont(font)
        image1=qtw.QPushButton("Image",self)
        image1.clicked.connect(self.img)
        image1.setGeometry(qtc.QRect(380, 380, 151, 71))
        image1.setFont(font)
        label_t2=qtw.QLabel("Social Distance Detection",self)
        label_t2.setGeometry(qtc.QRect(260, 510, 401, 71))
        font = qtg.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setItalic(True)
        font.setBold(True)
        label_t2.setFont(font)
        line_2=qtw.QFrame(self)
        line_2.setGeometry(qtc.QRect(245, 580, 411, 20))
        line_2.setFrameShape(qtw.QFrame.HLine)
        line_2.setFrameShadow(qtw.QFrame.Sunken)
        video= qtw.QPushButton("Webcam /Video",self)
        video.clicked.connect(self.vid)
        video.setGeometry(qtc.QRect(380, 610, 151, 71))
        video.setStyleSheet("font: 75 bold 12pt \"Times New Roman\";\n"
                              )
        about=qtw.QLabel("<h4>Made by\n Mohd Adil",self)
        about.setGeometry(qtc.QRect(380,750,180,80))
        about.setStyleSheet("font: 75 bold 12pt \"Times New Roman\";\n"
                              "background-color:black;color:white;")
        exit=qtw.QPushButton("Exit",self)
        exit.clicked.connect(self.quit)
        exit.setGeometry(qtc.QRect(860, 770, 151, 71))
        exit.setFont(font)
    def quit(self):
        print('hello')
        sys.exit()
    def web(self):
        self.w=webcame()
        self.w.show()
        self.hide()
    def img(self):
        self.img=image()
        self.img.show()
        self.hide()
    def vid(self):
        self.s=social()
        self.s.show()
        self.hide()
class predict(qtc.QThread):
    change_pixmap_signal=qtc.pyqtSignal(np.ndarray)
    display_status=qtc.pyqtSignal(int,int)
    
    def __init__(self):
        super().__init__()
        self.run_flag=True
    def run(self):
       
        
        (fname1,m,w)=detect_and_predict_image(fname)
        
            
        self.change_pixmap_signal.emit(fname1)
            
        self.display_status.emit(m,w)
           
           
            
        
                   
           
class image(qtw.QWidget):
    
    def __init__(self):
        super().__init__()
        self.resize(975, 728)
        self.setFixedSize(975,728)
        self.setWindowTitle('Face Mask with Image')
        self.setWindowIcon(qtg.QIcon('./images/i.ico'))
        self.setStyleSheet("background-color:rgb(55, 131, 230)")
        self.label = qtw.QLabel(self)
        self.label.setAlignment(qtc.Qt.AlignCenter)
        self.label.setFixedHeight(81)
        self.label.setFixedWidth(401)
        self.label.move(190,10)
        font = qtg.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(17)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        
        self.label.setText('Face Mask Dectection With Image')
      
        self.label.setStyleSheet("background-color:rgb(255, 255, 127)")
        self.horizontalLayoutWidget = qtw.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(qtc.QRect(10, 110, 951, 80))
        self.horizontalLayout = qtw.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
       
        self.Readimage = qtw.QPushButton(self.horizontalLayoutWidget)
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(False)
        self.Readimage.setFont(font)
        self.Readimage.setStyleSheet("background-color:rgb(255, 170, 0)")
       
        self.horizontalLayout.addWidget(self.Readimage)
        self.Readimage.setText('Read Image')
        self.Readimage.clicked.connect(self.display_image)
        self.Predict = qtw.QPushButton(self.horizontalLayoutWidget)
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Predict.setFont(font)
        self.Predict.setStyleSheet("background-color:rgb(85, 170, 127)")
        self.Predict.setText('Predict')
        self.Predict.clicked.connect(self.predict)
        self.horizontalLayout.addWidget(self.Predict)
        self.Back = qtw.QPushButton(self)
        self.Back.setGeometry(qtc.QRect(870, 670, 93, 31))
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Back.setFont(font)
        self.Back.setText('Back')
        self.Back.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.Back.clicked.connect(self.back) 
        self.label_img = qtw.QLabel(self)
        self.label_img.setGeometry(qtc.QRect(0, 10, 195, 110))
        
        self.label_img.setPixmap(qtg.QPixmap('./images/m.png'))
        self.label_img.setScaledContents(True)
        self.label_m= qtw.QLabel(self)
        self.label_m.setGeometry(qtc.QRect(630, 8, 61, 31))
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_m.setText("Mask")
        self.label_m.setFont(font)
        self.label_m.setStyleSheet("background-color: rgb(170, 255, 0)")
        self.lcdNumber = qtw.QLCDNumber(self)
        self.lcdNumber.setGeometry(qtc.QRect(610, 40, 111, 81))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcdNumber.setDigitCount(4)
        self.horizontalLayoutWidget_2 = qtw.QWidget(self )
        self.horizontalLayoutWidget_2.setGeometry(qtc.QRect(10, 200, 951, 461))
        self.horizontalLayout_2 = qtw.QHBoxLayout(self.horizontalLayoutWidget_2)
        #self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_R = qtw.QLabel(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.label_R)
        #self.label_R.setText("adil")
        self.label_p = qtw.QLabel(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.addWidget(self.label_p)
        #self.label_p.setText("sss") 
        self.lcdNumber_2 = qtw.QLCDNumber(self)
        self.lcdNumber_2.setGeometry(qtc.QRect(770, 40, 111, 81))
        self.lcdNumber_2.setDigitCount(4)
        self.lcdNumber_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_w = qtw.QLabel(self)
        self.label_w.setGeometry(qtc.QRect(780, 8, 91, 31))
        font = qtg.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_w.setFont(font)
        self.label_w.setText("No Mask")
        self.label_w.setStyleSheet("background-color: rgb(255, 0, 0)")
        global i
        i=1
        
    def display_image(self):
        global fname
        global i
        global j
        j=1
        fname = qtw.QFileDialog.getOpenFileName(self, 'Open file', 
           'e:\\',"Image Files (*.jpg *.gif *.bmp *.png)")
        pixmap = qtg.QPixmap(fname[0])
        self.label_R.setPixmap(pixmap)
        self.label_R.setScaledContents(True)
        i+=1
        j+=1
        
       
    def predict(self):
        global i
        
        print(i)
        if i==1:
            msgBox = qtw.QMessageBox()
            msgBox.setIcon(qtw.QMessageBox.Critical)
            msgBox.setText("Read the Image First")
            msgBox.setWindowTitle("Error")
            msgBox.setStandardButtons(qtw.QMessageBox.Ok)
            returnValue = msgBox.exec()
            if returnValue == qtw.QMessageBox.Ok:
                print('OK clicked')
                self.display_image()
               
        if j==j:
            self.cap=predict()
            self.cap.change_pixmap_signal.connect(self.detect_image)
            self.cap.display_status.connect(self.status)
            self.cap.start()
        
        
    @qtc.pyqtSlot(np.ndarray)    
    def detect_image(self,fname1):
        
        rgb_img=cv2.cvtColor(fname1,cv2.COLOR_BGR2RGB)
        h,w,ch=rgb_img.shape
        bytes_per_line=ch*w

        img =qtg.QImage(rgb_img.data,w,h,bytes_per_line,qtg.QImage.Format_RGB888)
        scaledImage=img.scaled(951, 461,qtc.Qt.KeepAspectRatio)
        
        pixmap = qtg.QPixmap.fromImage(scaledImage)
        self.label_p.setPixmap(pixmap)
        self.label_p.setScaledContents(True)
    @qtc.pyqtSlot(int,int)
    def status(self,str1,int1):
        print("hello")
        self.lcdNumber.display(str1)
        self.lcdNumber_2.display(int1)
        
    def back(self):
        self.mn=mainwindow()
        self.mn.show()
        self.hide()
        print('clicked')

#face mask web

class VideoCapture1(qtc.QThread):
    change_pixmap_signal=qtc.pyqtSignal(np.ndarray)
    dsply_status=qtc.pyqtSignal(int,int)
    def __init__(self):
        super().__init__()
        self.run_flag=True
    def run(self):
        cap=cv2.VideoCapture(0)
        while self.run_flag:
            ret,frame=cap.read()
            frame=cv2.resize(frame,(851,631))
            (image,m,n)=detect_and_predict_mask(frame)
            

            if ret == True:
                self.change_pixmap_signal.emit(image)
                self.dsply_status.emit(m,n)
        cap.release()
    def stop(self):
        self.run_flag=False
        self.wait()
class webcame(qtw.QWidget,qtg.QFont):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(qtg.QIcon('./images/i'))
        self.setWindowTitle('Face Mask recognition software')
        self.setFixedSize(867, 823)
        self.setStyleSheet("background-color:rgb(55, 131, 230)")
        #Adding widgets
        self.wid1=qtw.QWidget(self)
        self.wid1.setGeometry(qtc.QRect(9, 9, 535, 141))
        self.img=qtw.QLabel(self.wid1)
        self.img.setGeometry(qtc.QRect(0, 0, 161, 131))
        self.img.setPixmap(qtg.QPixmap("./images/m1.png"))
        self.img.setScaledContents(True)
        self.h1=qtw.QLabel("<h2>Face Mask Recognition Web Cam",self.wid1)
        self.h1.setGeometry(qtc.QRect(170, 0, 366, 71))
        font = qtg.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.h1.setFont(font)
        self.h1.setStyleSheet("background-color: rgb(255, 255, 127); border: 1px solid black;")
        self.cameraButton=qtw.QPushButton('open camera',self.wid1,clicked=self.cameraButton,checkable=True)
        
        self.cameraButton.setGeometry(qtc.QRect(190, 80, 121, 61))
        self.cameraButton.setStyleSheet("font: 75 bold 12pt \"Times New Roman\";\n"
                              "background-color:lightgreen;")
        self.bbk=qtw.QPushButton("Back",self.wid1,clicked=self.bbk,checkable=True)
        #self.bbk.clicked.connect(self.bbk)
        self.bbk.setGeometry(qtc.QRect(370, 80, 111, 61))
        font = qtg.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.bbk.setFont(font)
        self.bbk.setStyleSheet("font: 75 bold 12pt \"Times New Roman\";\n"
                              "background-color:rgb(255, 170, 0)")
        
        self.wid2=qtw.QWidget(self)

        self.wid2.setGeometry(qtc.QRect(570, 0, 291, 61))
        self.nm=qtw.QLabel("<h3>No Mask",self.wid2)
        self.nm.setGeometry(qtc.QRect(170, 10, 100, 41))
        self.nm.setStyleSheet("font: 75 bold 12pt \"Times New Roman\";\n"
                              "background-color: rgb(255, 0, 0);border: 1px solid black;")
        self.ms=qtw.QLabel("<h3>Mask",self.wid2)
        self.ms.setGeometry(qtc.QRect(30, 10, 81, 41))
        self.ms.setStyleSheet("font: 75 bold 12pt \"Times New Roman\";\n"
                              "background-color: rgb(0, 255, 0);border: 1px solid black;")
        self.hlw1 = qtw.QWidget(self)
        self.hlw1.setGeometry(qtc.QRect(550, 50, 301, 91))
        self.hlw2=qtw.QWidget(self)
        self.hlw2.setGeometry(qtc.QRect(10, 159, 851, 631))
        self.lcd=qtw.QLCDNumber(self.hlw1)
        self.lcd.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lcd2=qtw.QLCDNumber(self.hlw1)
        self.lcd2.setStyleSheet("background-color: rgb(255, 255, 255);")
         #Screen
        self.screen=qtw.QLabel()
        self.img=qtg.QPixmap(851,631)
        self.img.fill(qtg.QColor('darkgray'))
        self.screen.setPixmap(self.img)

        layout=qtw.QHBoxLayout(self.hlw1)
        layout1=qtw.QHBoxLayout(self.hlw2)
        layout.addWidget(self.lcd)
        layout.addWidget(self.lcd2)
        layout1.addWidget(self.screen)
    def bbk(self):
        self.mn=mainwindow()
        self.mn.show()
        self.hide()
        print('clicked')
       
    def cameraButton(self):
        status=self.cameraButton.isChecked()
        print(status)
        if status==True:
            font=qtg.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.cameraButton.setText('Close camera')
            self.cameraButton.setFont(font)
            self.cameraButton.setStyleSheet("background-color: Red;")
             #open camera 
            self.capture=VideoCapture1()
            self.capture.change_pixmap_signal.connect(self.updateImage)
            self.capture.dsply_status.connect(self.shows)
            self.capture.start()
        elif status == False:
            self.cameraButton.setText('Open camera')
            self.cameraButton.setStyleSheet("background-color:Green")
            self.capture.stop()  
    @qtc.pyqtSlot(np.ndarray)        
    def updateImage(self,image_array):
        rgb_img=cv2.cvtColor(image_array,cv2.COLOR_BGR2RGB)
        h,w,ch=rgb_img.shape
        bytes_per_line=ch*w
        convertdImage=qtg.QImage(rgb_img.data,w,h,bytes_per_line,qtg.QImage.Format_RGB888)
        scaledImage=convertdImage.scaled(851,631,qtc.Qt.KeepAspectRatio)
        qt_img=qtg.QPixmap.fromImage(scaledImage)
        #update to screen
        self.screen.setPixmap(qt_img)
    @qtc.pyqtSlot(int,int)
    def shows(self,ms,nm):
        self.lcd.display(ms)
        self.lcd2.display(nm)
# social distance
class VideoCapture(qtc.QThread):
    change_pixmap_signal=qtc.pyqtSignal(np.ndarray)
    
    display_lcd=qtc.pyqtSignal(int,int)
    def __init__(self):
        super().__init__()
        self.run_flag=True
    def run(self):
        global a,b
        print(a)
        if a==10:
            b=fname[0]
            a-=1
            
        else:
            b=0
        cap=cv2.VideoCapture(b)
        writer= None
        while self.run_flag:
            ret,frame=cap.read()
            frame=cv2.resize(frame,(861,631))
            (viedo,v,b)=web(frame,ret)
           
            if writer is None:
                fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                writer = cv2.VideoWriter("Output_file1.avi", fourcc, 25, (frame.shape[1], frame.shape[0]), True)
            
            if writer is not None:
               writer.write(viedo)
            if ret == True:
                self.change_pixmap_signal.emit(viedo)
                self.display_lcd.emit(v,b)
            
        cap.release()
    
    def stop(self):
        
        self.run_flag=False
       
       
        self.wait()
class social(qtw.QWidget,qtg.QFont):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1040,858)
        self.setWindowTitle('Social Distance Detection')
        self.setWindowIcon(qtg.QIcon('./images/i3'))
        self.setStyleSheet('background-color:rgb(56, 126, 255)')
        self.img=qtw.QLabel(self)
        self.img.setGeometry(qtc.QRect(14, 10, 180, 131))
        self.img.setPixmap(qtg.QPixmap("./images/p1.png"))
        self.img.setScaledContents(True)
        self.label=qtw.QLabel("<h2>Social Distance Detection</h3>",self)
        self.label.setGeometry(240,60,420,91)
        self.label.setStyleSheet("background-color: rgb(255, 255, 127); border: 1px solid black;")
        font = qtg.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.lcdNumber = qtw.QLCDNumber(self)
        self.lcdNumber.setGeometry(qtc.QRect(870, 60, 161, 101))
        self.lcdNumber.setStyleSheet("background-color:rgb(255, 255, 255);border: 1px solid black;")
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setSegmentStyle(qtw.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcd2 = qtw.QLCDNumber(self)
        self.lcd2.setGeometry(qtc.QRect(690, 60, 161, 101))
        self.lcd2.setStyleSheet("background-color:rgb(255, 255, 255);border: 1px solid black;")
        self.lcd2.setSmallDecimalPoint(False)
        self.lcd2.setSegmentStyle(qtw.QLCDNumber.Filled)
        self.lcd2.setProperty("value", 0.0)
        self.person=qtw.QLabel('At Risk',self)
        self.person.setGeometry(890, 20, 121, 35)
        self.person.setStyleSheet("font: 75 bold 14pt \"Times New Roman\";\n""background-color:red; border: 1px solid black;")
        self.person1=qtw.QLabel('At Safe',self)
        self.person1.setGeometry(710, 20, 121, 35)
        self.person1.setStyleSheet("font: 75 bold 14pt \"Times New Roman\";\n""color:white;background-color:skyblue; border: 1px solid black;")
        
        #screen
        
        self.screen=qtw.QLabel(self)
        #self.screen.setGeometry(qtc.QRect(20, 190, 861, 631))
        self.img=qtg.QPixmap(861,631)
        self.screen.move(20,190)
        self.img.fill(qtg.QColor('darkgray'))
        self.screen.setPixmap(self.img)
            #button 3
        self.Read=qtw.QPushButton('Video',self,clicked=self.video,checkable=True)
        
        self.Read.setEnabled(True)
        font=qtg.QFont()
        self.Read.setGeometry(920,190, 111, 51)
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Read.setFont(font)
        self.Read.setStyleSheet("font: 75 bold 14pt \"Times New Roman\";\n""background-color:gray;")

        #buttons1
        self.start=qtw.QPushButton('Start',self,clicked=self.startbutton,checkable=True)
        #self.start.setEnabled(True)
        self.start.setCheckable(True)
        self.start.setGeometry(920, 270, 111, 51)
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color:lightgreen")
        #button 2
        self.back=qtw.QPushButton('back',self)
        self.back.setEnabled(True)
        self.back.setGeometry(920, 340, 111, 51)
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color:orange")
        self.back.clicked.connect(self.bk)
    global a,run_flag
    a=0
    
    b=0
    run_flag=True
    def bk(self):
        self.mn=mainwindow()
        self.mn.show()
        self.hide()
    def video(self):
        
        print('clicked')
        global a,fname,run_flag
        
        if run_flag:
            fname = qtw.QFileDialog.getOpenFileName(self, 'Open file', 
           'e:\\',"Image Files (*.mp4 *.avi *.mkv *.mpeg)")
        status=self.Read.isChecked()
        print(status)
        if status==True:
            a=10
            font=qtg.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.Read.setText('Pause')
            self.Read.setFont(font)
            self.Read.setStyleSheet("background-color: Red; border: 1px solid black;")
            self.capture=VideoCapture()
            self.capture.change_pixmap_signal.connect(self.updateImage)
            self.capture.start()
            self.capture.display_lcd.connect(self.lcd)
            run_flag=False
           
        elif status==False:
            font=qtg.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.Read.setText('Play')
            self.Read.setFont(font)
            self.Read.setStyleSheet("background-color:lightgreen ;")
            self.capture.stop()
    def startbutton(self):
       
        print("clicked")
        status=self.start.isChecked()
        print(status)
        
        if status==True:
            font=qtg.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.start.setText('Stop')
            self.start.setFont(font)
            self.start.setStyleSheet("background-color: Red; ")
            self.capture=VideoCapture()
            self.capture.change_pixmap_signal.connect(self.updateImage)
            self.capture.start()
            self.capture.display_lcd.connect(self.lcd)
            
        elif status==False:
            font=qtg.QFont()
            font.setPointSize(9)
            font.setBold(True)
            font.setWeight(75)
            self.start.setText('Start')
            self.start.setFont(font)
            self.start.setStyleSheet("background-color:lightgreen")
            self.capture.stop()
    @qtc.pyqtSlot(np.ndarray)        
    def updateImage(self,image_array):
        rgb_img=cv2.cvtColor(image_array,cv2.COLOR_BGR2RGB)
        h,w,ch=rgb_img.shape
        bytes_per_line=ch*w
        convertdImage=qtg.QImage(rgb_img.data,w,h,bytes_per_line,qtg.QImage.Format_RGB888)
        scaledImage=convertdImage.scaled(861,631,qtc.Qt.KeepAspectRatio)
        qt_img=qtg.QPixmap.fromImage(scaledImage)
        
       
        #update to screen
        self.screen.setPixmap(qt_img)
    @qtc.pyqtSlot(int,int)
    def lcd(self,num,num1):
        self.lcdNumber.display(num)
        self.lcd2.display(num1)





if __name__ =='__main__':
    app=qtw.QApplication(sys.argv)

    
    mn=mainwindow()
    mn.show()
    sys.exit(app.exec())
