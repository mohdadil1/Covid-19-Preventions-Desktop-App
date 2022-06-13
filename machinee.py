
from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import imutils
import time
import cv2
import os

# load our serialized face detector model from disk
prototxtPath = './models/deploy.prototxt'
weightsPath = './models/res10_300x300_ssd_iter_140000.caffemodel'
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

# load the face mask detector model from disk
maskNet = load_model('./mobilenet_v2.model/')

def detect_and_predict_image(frame):
    if frame is not None:
        frame=cv2.imread(frame[0])
        #frame=cv2.resize(frame,(471,459))
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),(104.0, 177.0, 123.0),swapRB=True)
    faceNet.setInput(blob)
    detections = faceNet.forward()
    faces = []
    locs = []
    preds = []
    for i in range(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > 0.5:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))
            face = frame[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)
            faces.append(face)
            locs.append((startX, startY, endX, endY))
    if len(faces) > 0:
        faces = np.array(faces, dtype="float32")
        preds = maskNet.predict(faces, batch_size=32)
        
    m,w=0,0
    for (box, pred) in zip(locs, preds):
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred
        label = "Mask" if mask > withoutMask else "No Mask"
        if label=="No Mask":
            w+=1
        if label=="Mask" :
            m+=1   
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        
        label = "{}: {:.2f}%".format(label,max(mask, withoutMask) * 100)
        
        
    
        
            
    
        cv2.putText(frame, label,(startX, startY - 10),cv2.FONT_HERSHEY_PLAIN, 2, color, 2)
        
        cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
    
    return frame,m,w
   

    
        






