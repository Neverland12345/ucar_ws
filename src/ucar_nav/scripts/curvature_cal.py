#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PointStamped
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
import time
import math
import numpy as np
import numpy.linalg as LA
from move_base_msgs.msg import MoveBaseActionGoal

#from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
class path_following:
    def __init__(self):
        self.front_flag = 0
        self.point_width = 35 #三个点之间的间隔距离
        self.mid_point = 75  #中间的点离小车的距离
        self.curvature_flag = 0
        self.flag = 0         #最后一段路程的判断标志，因为本次迅飞的最后一段路程要求不能撞墙，但障碍却少，适合冲刺，所以要求冲的又快又稳，所以需要判断标志
        self.pub_cmd = rospy.Publisher("/cmd_vel",Twist,queue_size=1)

        self.pub_point1 = rospy.Publisher("point1", PointStamped, queue_size = 1)
        self.pub_point2 = rospy.Publisher("point2", PointStamped, queue_size = 1)
        self.pub_point3 = rospy.Publisher("point3", PointStamped, queue_size = 1)

        self.point1 = PointStamped()
        self.point2 = PointStamped()
        self.point3 = PointStamped()

        self.speed_data=Float64()
        self.turn_data=Float64()
        self.min_curvature = Float64(1000.0)
        self.cmd_data = Twist()
        self.goal_point_x = Float64()
        self.goal_point_y = Float64()
        self.odom_point_x = Float64()
        self.odom_point_y = Float64()
        self.odom_yaw = Float64()
    def odom_callback(self,data):
        self.odom_point_x = data.pose.pose.position.x
        self.odom_point_y = data.pose.pose.position.y
        self.odom_yaw = data.twist.twist.angular.z
    def get_goal_callback(self,data):
        self.goal_point_x = data.goal.target_pose.pose.position.x
        self.goal_point_y = data.goal.target_pose.pose.position.y

    def lenth_cal(self,x1,x2,y1,y2):
        x = (x1 - x2)**2
        y = (y1 - y2)**2
        l = np.sqrt(x+y)
        return l

    def radius_cal(self,a,b,c):
        p = (a+b+c)/2.0
        s = np.sqrt(p*(p-a)*(p-b)*(p-c))
        r = (a*b*c)/4.0/s
        return r



    def cmd_vel_callback(self,data):
        # stop_flag = Float64(self.lenth_cal(float(self.odom_point_x) , float(self.goal_point_x) , float(self.odom_point_y) , float(self.goal_point_y)))
        # data.angular.z= (0 if abs(data.angular.z) < 0.0 else data.angular.z)    
        data.linear.x =data.linear.x *1.1
        data.linear.y =data.linear.y *1.1
        data.angular.z =data.angular.z *1.1  #1.6
        self.cmd_data.angular.z = data.angular.z
        self.cmd_data.linear.x = data.linear.x
        self.cmd_data.linear.y = data.linear.y
        # if  stop_flag.data <= 1.0:  #1.2  stop
        #     self.cmd_data.linear.x = 0
        #     self.cmd_data.angular.z = 0
        # else:
        # self.cmd_data.angular.z=data.angular.z
        # if self.flag == 8:  #接近二维码的弯道
        #     self.cmd_data.linear.x = 0
        #     self.cmd_data.linear.y = 0
        #     self.cmd_data.angular.z = 0 #1.35
        # elif self.flag == 9:  #二维码之前的
        #     self.cmd_data.linear.x = data.linear.x 
        #     self.cmd_data.linear.y = data.linear.y  
        #     self.cmd_data.angular.z = data.angular.z  
        # elif self.flag == 2:  #u型弯后的小直道，稍微加速！
        #     self.cmd_data.linear.x = data.linear.x*1.2 #1.3  
        #     self.cmd_data.linear.y = data.linear.y*1.2 #0.5  
        #     self.cmd_data.angular.z = data.angular.z*1.2 #1.0  
        # elif self.flag == 3:  #u型弯，减速！！！
        #     self.cmd_data.linear.x = data.linear.x*1.18 #0.8  
        #     self.cmd_data.linear.y = data.linear.y*1.18
        #     self.cmd_data.angular.z = data.angular.z*1.18 #1.6  
        # elif self.flag == 4:   #u型弯之前的小直道，加速！
        #     self.cmd_data.linear.x = data.linear.x*1.2 
        #     self.cmd_data.linear.y = data.linear.y*1.2
        #     self.cmd_data.angular.z = data.angular.z*1.2 #1.2
        # elif self.flag == 5:   #大弯
        #     self.cmd_data.linear.x = data.linear.x*1.25 #1.0  
        #     self.cmd_data.linear.y = data.linear.y*1.25 #1.3
        #     self.cmd_data.angular.z = data.angular.z*1.25
        # elif self.flag == 6:   #出发的直道
        #     self.cmd_data.linear.x = data.linear.x*1.2 
        #     self.cmd_data.linear.y = data.linear.y*1.2 #1.2
        #     self.cmd_data.angular.z = data.angular.z*1.2  
        # elif self.flag == 7:
        #     self.cmd_data.linear.x = data.linear.x*1.3
        #     self.cmd_data.linear.x = data.linear.x*1.3 #1.3
        #     self.cmd_data.angular.z = data.angular.z*1.3
        # elif self.flag == 8:
        #     self.cmd_data.linear.x = data.linear.x*1.0 #0.8
        #     self.cmd_data.linear.y = data.linear.y*1.0 #0.8
        #     self.cmd_data.angular.z = data.angular.z*1.0
        # elif self.flag == 10:
        #     self.cmd_data.linear.x = data.linear.x 
        #     self.cmd_data.linear.y = data.linear.y
        #     self.cmd_data.angular.z = data.angular.z
        # elif self.flag == 11:   #第一个挡板之前
        #     self.cmd_data.linear.x = data.linear.x *1.3 #1.4
        #     self.cmd_data.linear.y = data.linear.y *1.3
        #     self.cmd_data.angular.z = data.angular.z *1.3 #0.5
        # if self.curvature_flag == 4:
        #     self.cmd_data.linear.x = data.linear.x*1.0  #1.15
        #     self.cmd_data.linear.y = data.linear.y*1.0
        #     self.cmd_data.angular.z = data.angular.z*1.3
        # else:
        #     self.cmd_data.linear.x = data.linear.x*1.50
        #     self.cmd_data.linear.y = data.linear.y*1.50 #1.65/1.70比较好  >1.75第一个转弯停滞    
        self.pub_cmd.publish(self.cmd_data)




    def path_callback(self,data):
        x = len(data.poses) 
        if x < 5:
                self.flag = 10
                self.front_flag = 1
        if self.front_flag == 0:
            # print(x)  
            if len(data.poses) <= self.point_width*2:
                index1 = 0
                index2 = (len(data.poses)-1)//2
                index3 = len(data.poses)-1
            elif (len(data.poses) > (self.point_width*2)) and (len(data.poses) <= (self.mid_point+self.point_width)):
                index1 = (len(data.poses)-1)-(self.point_width*2)
                index2 = (len(data.poses)-1)-self.point_width
                index3 = len(data.poses)-1
            elif len(data.poses) > (self.mid_point+self.point_width):
                index1 = self.mid_point-self.point_width
                index2 = self.mid_point
                index3 = self.mid_point+self.point_width
            else:
                index1 = index2 = index3 = 0
            if len(data.poses)<=47:
                self.flag = 9
            elif len(data.poses)<=88: #90
                self.flag = 1
            elif len(data.poses)<=113: #115
                self.flag = 2
            elif len(data.poses)<=128:  
                self.flag = 3
            elif len(data.poses)<=166:
                self.flag = 4
            elif len(data.poses)<=240:
                self.flag = 5
            elif len(data.poses) >252 and len(data.poses)<=242:
                self.flag = 11
            else:
                self.flag = 6
        else: 
            print("start2")
            if len(data.poses) <= self.point_width*2:
                index1 = 0
                index2 = (len(data.poses)-1)//2
                index3 = len(data.poses)-1
            elif (len(data.poses) > (self.point_width*2)) and (len(data.poses) <= (self.mid_point+self.point_width)):
                index1 = (len(data.poses)-1)-(self.point_width*2)
                index2 = (len(data.poses)-1)-self.point_width
                index3 = len(data.poses)-1
            elif len(data.poses) > (self.mid_point+self.point_width):
                index1 = self.mid_point-self.point_width
                index2 = self.mid_point
                index3 = self.mid_point+self.point_width
            else:
                index1 = index2 = index3 = 0
            if len(data.poses) >=83:
                self.flag = 7
            elif len(data.poses)>20 and len(data.poses)<83:
                self.flag = 8

        self.point1.header.frame_id = 'map'
        self.point1.point.x = data.poses[index1].pose.position.x
        self.point1.point.y = data.poses[index1].pose.position.y
        self.pub_point1.publish(self.point1)

        self.point2.header.frame_id = 'map'
        self.point2.point.x = data.poses[index2].pose.position.x
        self.point2.point.y = data.poses[index2].pose.position.y
        self.pub_point2.publish(self.point2)

        self.point3.header.frame_id = 'map'
        self.point3.point.x = data.poses[index3].pose.position.x
        self.point3.point.y = data.poses[index3].pose.position.y
        self.pub_point3.publish(self.point3)

        if index1 >= 0:
            self.min_curvature = Float64(1000.0)
            for i in range(0,index1): 
                len1 = self.lenth_cal(data.poses[index1-i].pose.position.x , data.poses[index2-i].pose.position.x , data.poses[index1-i].pose.position.y , data.poses[index2-i].pose.position.y)
                len2 = self.lenth_cal(data.poses[index2-i].pose.position.x , data.poses[index3-i].pose.position.x , data.poses[index2-i].pose.position.y , data.poses[index3-i].pose.position.y)
                len3 = self.lenth_cal(data.poses[index1-i].pose.position.x , data.poses[index3-i].pose.position.x , data.poses[index1-i].pose.position.y , data.poses[index3-i].pose.position.y)
                curvature = Float64(self.radius_cal(len1 , len2 , len3))
                if curvature.data <= self.min_curvature.data:
                    self.min_curvature.data = curvature.data
                    if self.min_curvature.data<=3:
                        self.curvature_flag = 4
                        break
                    else:
                        self.curvature_flag = 0 
    
if __name__ == '__main__':
    try:
        rospy.init_node('curvature_cal', anonymous = True)
        Node = path_following()
        rospy.Subscriber("/vesc/cmd_vel", 
                         Twist, 
                         Node.cmd_vel_callback)
        rospy.Subscriber("/move_base/TebLocalPlannerROS/global_plan", 
                         Path, 
                         Node.path_callback)       
        rospy.Subscriber("/move_base/goal", 
                         MoveBaseActionGoal, 
                         Node.get_goal_callback)
        rospy.Subscriber("/odom", 
                         Odometry, 
                         Node.odom_callback) 
        
        
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
