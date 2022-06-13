
import cv2
import numpy as np
import math
import os

distance=70

weightsPath = './models/yolov4.weights'
cfgPath = './models/yolov4.cfg'
coco_namePath = './models/coco.names'
net = cv2.dnn.readNet(weightsPath, cfgPath)
classes = []
with open(coco_namePath, "r") as f:
    classes = [line.strip() for line in f.readlines()]

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i- 1] for i in net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)



def get_distance(x1,x2,y1,y2):

    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
    return distance





def calculateCentroid(xmin,ymin,xmax,ymax):

    xmid = ((xmax+xmin)/2)
    ymid = ((ymax+ymin)/2)
    centroid = (xmid,ymid)

    return xmid,ymid,centroid





def draw_detection_box(frame,x1,y1,x2,y2,color):

    cv2.rectangle(frame,(x1,y1),(x2,y2), color, 2)






def web(frame,ret):
   
   
        stat_H, stat_L = 0, 0

        if ret:
            # Detecting objects
            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)
            class_ids = []
            confidences = []
            boxes = []
            centroids = []
            box_colors = []
            detectedBox = []
        #frame_rgb = cv2.cvtColor(frame, cv2.IMREAD_COLOR)
        height, width, channels = frame.shape
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                #if prediction is 50% and class id is 0 which is 'person'
                if confidence > 0.5 and class_id == 0:
                    
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # apply non-max suppression
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]

                xmin = x
                ymin = y
                xmax = (x + w)
                ymax = (y + h)

                '''use when to select person based on class label's name instead of object's class id'''
                #label = str(classes[class_ids[i]])
                #if label == 'person':

                #calculate centroid point for bounding boxes
                xmid, ymid, centroid = calculateCentroid(xmin,ymin,xmax,ymax)
                detectedBox.append([xmin,ymin,xmax,ymax,centroid])

                my_color = 0
                for k in range (len(centroids)):
                    c = centroids[k]
                    
                    if get_distance(c[0],centroid[0],c[1],centroid[1]) <= distance:
                        box_colors[k] = 1
                        my_color = 1
                        cv2.line(frame, (int(c[0]),int(c[1])), (int(centroid[0]),int(centroid[1])), (0,255,255), 1,cv2.LINE_AA)
                        cv2.circle(frame, (int(c[0]),int(c[1])), 3, (0,165,255), -1,cv2.LINE_AA)
                        cv2.circle(frame, (int(centroid[0]),int(centroid[1])), 3, (0,165,255), -1,cv2.LINE_AA)
                        break
                centroids.append(centroid)
                box_colors.append(my_color)        

        for i in range (len(detectedBox)):
            x1 = detectedBox[i][0]
            y1 = detectedBox[i][1]
            x2 = detectedBox[i][2]
            y2 = detectedBox[i][3]
            
            #for ellipse output
            xc = ((x2+x1)/2)
            yc = y2-5
            centroide = (int(xc),int(yc))
            
            if box_colors[i] == 0:
                color = (0,255,0)
                draw_detection_box(frame,x1,y1,x2,y2,color)
                label = "safe"
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)

                y1label = max(y1, labelSize[1])
                cv2.rectangle(frame, (x1, y1label - labelSize[1]),(x1 + labelSize[0], y1 + baseLine), (255,255,255), cv2.FILLED)
                cv2.putText(frame, label, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0), 1,cv2.LINE_AA)
                stat_L += 1

            else:
                color = (0,0,255)
                draw_detection_box(frame,x1,y1,x2,y2,color)
                # cv2.ellipse(frame, centroide, (35, 19), 0.0, 0.0, 360.0, RED, 2)
                label = "unsafe"
                labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)

                y1label = max(y1, labelSize[1])
                cv2.rectangle(frame, (x1, y1label - labelSize[1]),(x1 + labelSize[0], y1 + baseLine),(255,255,255), cv2.FILLED)
                cv2.putText(frame, label, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255), 1,cv2.LINE_AA)
                stat_H += 1

        cv2.rectangle(frame, (13, 10),(250, 60), (192,192,192), cv2.FILLED)
        LINE = "--"
        INDICATION_H = f'HIGH RISK: {str(stat_H)} people'
        cv2.putText(frame, LINE, (30,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255), 1,cv2.LINE_AA)
        cv2.putText(frame, INDICATION_H, (60,30), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,0,255), 1,cv2.LINE_AA)

        INDICATION_L = f'SAFE : {str(stat_L)} people'
        cv2.putText(frame, LINE, (30,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(0,255,0), 1,cv2.LINE_AA)
        cv2.putText(frame, INDICATION_L, (60,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,0,0), 1,cv2.LINE_AA)
        return frame,stat_H, stat_L







