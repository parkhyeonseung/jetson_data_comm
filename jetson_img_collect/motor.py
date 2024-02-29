import time
import busio

from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor

# motor4 = motor.DCMotor(pca.channels[12], pca.channels[13])
class Robot():
    def __init__(self):
        
        self.i2c = busio.I2C(SCL, SDA)

        self.pca = PCA9685(self.i2c, address=0x40)
        self.pca.frequency = 100
        self.motor1 =  motor.DCMotor(self.pca.channels[8], self.pca.channels[9]) # right
        self.motor2 = motor.DCMotor(self.pca.channels[11], self.pca.channels[10]) # left

    def forward(self,val):
        self.motor1.throttle = val
        self.motor2.throttle = val+.04

    def backward(self,val):
        self.motor1.throttle = -val
        self.motor2.throttle = -val-.04

    def left(self,val):
        self.motor1.throttle = val
        self.motor2.throttle = -val-.04

    def right(self,val):
        self.motor1.throttle = -val
        self.motor2.throttle = val+.04

    def stop(self):
        self.motor1.throttle = 0
        self.motor2.throttle = 0

    def init(self):
        self.pca.deinit()
    
if __name__=='__main__':
    robot = Robot()
    # robot.forward(0.7)
    robot.stop()
