import torch
import torchvision
from motor import Robot
import torch.nn.functional as F
import torchvision.models 
import cv2
import numpy as np
from camera import gstreamer_pipeline

model = torchvision.models.alexnet(pretrained=False)
model.classifier[6] = torch.nn.Linear(model.classifier[6].in_features, 2)

# model.load_state_dict(torch.load('best_model.pth'))


device = torch.device('cuda')

model.classifier[6] = torch.nn.Linear(model.classifier[6].in_features, 2)
model.load_state_dict(torch.load('test2.pth')) 
model = model.to(device)


mean = 255.0 * np.array([0.485, 0.456, 0.406])
stdev = 255.0 * np.array([0.229, 0.224, 0.225])

normalize = torchvision.transforms.Normalize(mean, stdev)

def preprocess(camera_value):
    global device, normalize
    x = camera_value
    x = cv2.cvtColor(x, cv2.COLOR_BGR2RGB)
    x = x.transpose((2, 0, 1))
    x = torch.from_numpy(x).float()
    x = normalize(x)
    x = x.to(device)
    x = x[None, ...]
    return x





robot = Robot()

def update(change):
    global blocked_slider, robot
    x = change['new'] 
    x = preprocess(x)
    y = model(x)
    
    # we apply the `softmax` function to normalize the output vector so it sums to 1 (which makes it a probability distribution)
    y = F.softmax(y, dim=1)
    
    prob_blocked = float(y.flatten()[0])
        
    if prob_blocked < 0.7:
        robot.forward(0.8)
    else:
        robot.left(0.8)

cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)
while True:
    ret,image = cap.read()
    if not ret : break
    cv2.imshow('img',image)
    update(image)
    keyco = cv2.waitKey(1) & 0xFF
    if keyco == 27:
        break

cap.release()
cv2.destroyAllWindows()
robot.init()