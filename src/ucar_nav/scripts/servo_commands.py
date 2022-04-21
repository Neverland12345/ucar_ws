#!/usr/bin/env python
import rospy
import math
import time
import sys
import tty
import threading
import select
import signal
import termios
import numpy as np
from std_msgs.msg import Bool
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import pid
from sensor_msgs.msg import Imu

class pid_ctl:
    def __init__(self):
            self.x = 0
            self.last_x = 0
            self.y = 0
            self.last_y = 0
            self.linear_vel_x = 0
            self.angular_vel_z = 0
            self.linear_acc_x = 0
            self.int_start_flag = 1
            self.vel_update_start_time = 0
            self.vel_update_start_flag = 1

    flag_move = 0


    def limsteer(data,maxdata):
        if data>0 and data > maxdata:
            data = maxdata
        elif data<0 and math.fabs(data) > maxdata:
            data = maxdata
        return data

    def update_posture(self, imu_data):
            # Read the quaternion of the robot IMU
            x = imu_data.orientation.x
            y = imu_data.orientation.y
            z = imu_data.orientation.z
            w = imu_data.orientation.w

            # Read the angular velocity of the robot IMU
            self.angular_vel_z = imu_data.angular_velocity.z

            # Read the linear acceleration of the robot IMU
            self.linear_acc_x = imu_data.linear_acceleration.x

            # Convert Quaternions to Euler-Angles
            #[roll, pitch, yaw] = euler_from_quaternion([x, y, z, w])
            #self.yaw = yaw
            # print("linear_vel_x:%5.2f linear_acc_x:%5.2f angular_vel_z:%5.2f yaw:%5.2f" % (
            #     self.linear_vel_x, self.linear_acc_x, self.angular_vel_z, self.yaw))

    def update_position(self, odom_data):
            self.x = odom_data.pose.pose.position.x
            self.y = odom_data.pose.pose.position.y
            if self.vel_update_start_flag == 1:
                self.vel_update_start_flag = 0
                self.vel_update_start_time = rospy.get_time()
            if (rospy.get_time() - self.vel_update_start_time) > 0.01:
                self.int_start_flag = 1
                self.linear_vel_x = (self.x - self.last_x) / 0.01
                self.last_x = self.x
                self.linear_vel_y = (self.y - self.last_y) / 0.01
                self.last_y = self.y
                # print("linear_vel_x:%5.2f linear_acc_x:%5.2f angular_vel_z:%5.2f yaw:%5.2f" % (
                #     self.linear_vel_x, self.linear_acc_x, self.angular_vel_z, self.yaw))

    def set_speed(data):
        global flag_move
        
        pub_vel_left_rear_wheel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        vel = Twist()
        ex_x = data.linear.x
        ex_y = data.linear.y
        ex_z = data.angular.z
    # z= (0 if abs(z) < 0.05 else z)    
    # if z == 0:
        #    x=x*1.2
        #   y=y*1.2
        #elif math.fabs(z)<0.2:
        # x=x*1.0
        # y=y*1.0
        # z=z*1.1
    # else:
        # x=x*0.92
        # y=y*0.92
        # z=z*1.76


        vel_x_ctrl_value = vel_x_pid.get_output(self.linear_vel_x, self.ex_x)
        vel_y_ctrl_value = vel_y_pid.get_output(self.linear_vel_y, self.ex_y)
        vel_z_ctrl_value = vel_z_pid.get_output(self.angular_vel_z, self.ex_z)
            # print("ctrl_value:%5.2f now:%5.2f" %
            #       (vel_x_ctrl_value, self.linear_vel_x)

        #linear_x = x * 1.1
        #linear_y = y * 1.1
        #angular_z = z * 1.1
        #vel.linear.x = linear_x
        #vel.linear.y = linear_y
        #vel.angular.z = angular_z   
        vel.linear.x = vel_x_ctrl_value
        vel.linear.y = vel_y_ctrl_value
        vel.angular.z = vel_z_ctrl_value   
        pub_vel_left_rear_wheel.publish(vel)
    

if __name__ == '__main__':
    rospy.init_node('servo_commands',)
    pid_CTL = pid_ctl()
    rospy.Subscriber("/vesc/cmd_vel", Twist, pid_CTL.set_speed)
    rospy.Subscriber("/odom", Odometry, pid_CTL.update_position)
    rospy.Subscriber("/imu", Imu, pid_CTL.update_posture)

    vel_x_pid = pid.PID_t(5, 0.15, 0.05, int_max=10, output_max=6, sub_ctrl=False)  
    vel_y_pid = pid.PID_t(5, 0.15, 0.05, int_max=10, output_max=6, sub_ctrl=False)  
    vel_z_pid = pid.PID_t(5, 0.15, 0.05, int_max=10, output_max=6, sub_ctrl=False) 
    start_time = rospy.get_time()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.sleep(0.1)

    #try:
       # ()
  #  except rospy.ROSInterruptException:
    #    pass
