#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from darknet_ros_msgs.msg import classes
from move_base_msgs.msg import MoveBaseAction
from move_base_msgs.msg import MoveBaseGoal
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

print("第一行")
f =0 
img_flag = 0
# class_dict = {'gh_00':0,'gh_01':0,'gh_02':0,'gh_10':0,'gh_11':0,'gh_12':0,'gh_20':0,'gh_21':0,'gh_22':0}
Img_1 = Image()
Img_2 = Image()
Img_3 = Image()
g1 = 0
h1 = 0
g2 = 0
h2 = 0
g3 = 0
h3 = 0
goal_flag = 0
g = 0
h = 0



#def goal_id_callback(msgs):
#    if msgs.data == "goal_1":                      
#        goal_pose = PoseStamped()
#        goal_pose.header.frame_id = "map"
#        goal_pose.pose.position.x = 1.75479720116
#        goal_pose.pose.position.y = 3.29980039597
#        goal_pose.pose.position.z = 0.0
#        goal_pose.pose.orientation.x = 0
#        goal_pose.pose.orientation.y = 0
#        goal_pose.pose.orientation.z = -0.0101698932772
#        goal_pose.pose.orientation.w = 0.999948285298
#        goal_pub.publish(goal_pose)


def classes_callback(msg):
    global g1,h1,g2,h2,g3,h3,g4,h4,g,h
    global bridge,f,Img_1,Img_2,Img_3,Img_4,img_flag
    if f == 1:
        g1 = msg.glass_num
        h1 = msg.long_hair_num 
    elif f == 2:
        g2 = msg.glass_num
        h2 = msg.long_hair_num
    elif f == 3 :        
        g3 = msg.glass_cut_num
        h3 = msg.long_hair_cut_num
    elif f == 4:
        if img_flag>=3:
            g4 = msg.glass_num
            h4 = msg.long_hair_num
            print ("g1,g2,g3,g4 = ",g1,g2,g3,g4)
            print ("h1,h2,h3,h4 = ",h1,h2,h3,h4)
            print ("g=",g)
            print ("h=",h)

def goal_callback(msg):
    global f,Img_3
    print("goal_callback回调函数")
    if msg.data == 3:       #判断是否到达
        if f <4:
            rospy.sleep(0.3)
        f =f+1 
        if f==4:
            img_pub.publish(Img_3)
    print("11111111111111")
                   
        
def img_callback(data):
    # define picture to_down' coefficient of ratio
    global bridge,f,img_flag,Img_1,Img_2,Img_3,Img_4,goal_flag,g,h,g1,h1,g2,h2,g3,h3,g4,h4
    bridge = CvBridge()
    if f==1 :
        if img_flag == 0:
            print("图像保存程序")
            img_flag = 1
            goal_flag =1
            Img_1 = data
            img_pub.publish(Img_1)
            cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
            image_name = str(img_flag)+ ".jpg" 
            cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)  
            print ('1.jpg')
            goal_pose = PoseStamped()                          #拍照之后发布下一个目标点
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 2.27096251869
            goal_pose.pose.position.y = -3.05275494003
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z =  -0.55848739508
            goal_pose.pose.orientation.w = 0.830569026989
            goal_pub.publish(goal_pose)
    elif f==2 :
        if img_flag == 1:
            img_flag = 2
            goal_flag =1
            Img_2 = data
            img_pub.publish(Img_2)
            cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
            image_name = str(img_flag)+ ".jpg" 
            cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)  
            print ('2.jpg')
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 0.79925364494
            goal_pose.pose.position.y = 2.41861187744
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.710692950469
            goal_pose.pose.orientation.w = 0.7047121803506
            goal_pub.publish(goal_pose)
    elif f==3 :
        if img_flag == 2:
            img_flag = 3
            goal_flag =1
            Img_3 = data
            img_pub.publish(Img_3)
            cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
            image_name = str(img_flag)+ ".jpg" 
            cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)  
            print ('3.jpg')
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 0.056945343018
            goal_pose.pose.position.y = -0.51291929436
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.993140454291
            goal_pose.pose.orientation.w = 0.119374644147
            goal_pub.publish(goal_pose)
    elif f==4:
        if img_flag == 3:
            rospy.sleep(1.5)
            img_flag = 4
        elif img_flag ==4:
            rospy.sleep(1.5)
            img_flag =5
        elif img_flag == 5:
            img_flag = 6
            g = g1+g2+g3
            h = h1+h2+h3
            if g>2:
                g = 2
            if h>2:
                h = 2
            argv = '/home/ucar/ucar_ws/src/audio_common/mp3/gh_'+str(g)+str(h)+'.mp3'
            soundhandle = SoundClient()
            rospy.sleep(1)
            rospy.loginfo('Playing "%s".' % argv)
            volume = 1.0
            soundhandle.playWave(argv, volume)    
            print ('goal rrrrrrrrrrrrrrrrrrrrrrrrrrrr')
    else:
        pass
 

        


if __name__ == '__main__':
    print("执行1")
    rospy.init_node('play', anonymous=True)
    print("执行")
    rospy.Subscriber("/move_base/result/status",Int32,goal_callback)  #判断是否到达既定目标点
    rospy.Subscriber("/darknet_ros/classes_num",classes,classes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    #rospy.Subscriber('/goal_id', String, goal_id_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    # argv = rospy.myargv()
    rospy.spin()