#script for making a class Robots with an algorithm and generalised functions which can be used to control multiple robots
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import constant
import utils
import numpy as np
import cv2 as cv
from constant import res, center, kp, ki, kd, scale_factor

#using the remote API client from zmq and naming it sim
client = RemoteAPIClient()
sim = client.require('sim')


#creating a class called robotics in which all of the functions can be made and accessed for multiple robots
class Robots:
    motor_r = "null"
    motor_l = "null"
    vision = "null"
    targetVelocity_r = 5.0
    targetVelocity_l = 5.0
    speed = 5.0
    integral = 0
    error_prev = 0

#constructor to set the values of some  class variables. also object selection from the robot
    def __init__(self, num):
        self.motor_r = sim.getObject(f"/PioneerP3DX[{num}]/rightMotor")
        self.motor_l = sim.getObject(f"/PioneerP3DX[{num}]/leftMotor")
        self.vision = sim.getObject(f"/PioneerP3DX[{num}]/Vision_sensor")
        self.speed = 5.0
        self.integral = 0
        self.error_prev = 0

#function for calculation of steering angle using pid logic
    def steeringcalc(self, cy):
        error = constant.center - cy
        self.integral = self.integral + error
        derivative = error - self.error_prev
        # Calculate PID output
        if error:
            pid_output = constant.kp * error + constant.ki * self.integral + constant.kd * derivative
        else:
            pid_output = 0.0
        # Save current error for the next iteration
        self.error_prev = error

        # steering angle
        steering_angle = constant.scale_factor * pid_output
        return steering_angle

#function for calculating final velocity
    def velocityangle(self, angle):
        self.targetVelocity_l = self.speed - (angle / 180) * self.speed
        self.targetVelocity_r = self.speed + (angle / 180) * self.speed

#function which follows through the whole algorithm
    def update(self):
        image, constant.res = sim.getVisionSensorImg(self.vision)
        cy = utils.processimage(image)
        ang = self.steeringcalc(cy)
        self.velocityangle(ang)
        sim.setJointTargetVelocity(self.motor_r, self.targetVelocity_r)
        sim.setJointTargetVelocity(self.motor_l, self.targetVelocity_l)