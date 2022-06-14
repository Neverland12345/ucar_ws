#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from darknet_ros_msgs.msg import classes
# from move_base_msgs.msg import MoveBaseAction
# from move_base_msgs.msg import MoveBaseGoal
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from actionlib_msgs.msg import GoalStatusArray
from playsound import playsound

a=0
f =0
fang="0"
img_flag = 0
# class_dict = {'gh_00':0,'gh_01':0,'gh_02':0,'gh_10':0,'gh_11':0,'gh_12':0,'gh_20':0,'gh_21':0,'gh_22':0}
Img_1 = Image()
Img_2 = Image()
Img_3 = Image()
lh=[0,0,0]
sh=[0,0,0]
lh_f=0
sh_f=0
hear_flag="0"
g1 = 0
h1 = 0
sh1 = 0
g2 = 0
h2 = 0
sh2 = 0
g3 = 0
h3 = 0
sh3 = 0
goal_flag = 0
g = 0
h = 0
shibie=1

flag=0
flag2=0
flag_sleep=0

h_flag = 0
sh_flag = 0

def fang_jian():
    global h1,h2,h3
    global sh1,sh2,sh3
    global fang
    if h1 >= 1 and sh2 >=1:#b长c短
        fang="b1c0"#B房间为长头发，C房间为短头发
    elif h1>=1 and sh3>=1 and h2==h3==sh1==sh2==0:#b长d短
        fang="b1d0"
    elif sh1>=1 and h2>=1 and sh2==sh3==h1==h3==0:#b短c长
        fang="b0c1"
    elif sh1>=1 and h3>=1 and sh2==sh3==h1==h2==0:#b短d长
        fang="b0d1"
    elif h2>=1 and sh3>=1 and h1==h3==sh1==sh2==0:#c长d短
        fang="c1d0"
    elif sh2>=1 and h3>=1 and sh1==sh3==h1==h2==0:#c短d长
        fang="c0d1"
    elif h1>=1 and h2>=1 and h3==0 and sh1==sh2==sh3==0:#b长c长
        print("错误2")
        fang="b1c1"
    elif h1>=1 and h3>=1  and h2==sh1==sh2==sh3==0:#b长d长
        fang="b1d1"
    elif h2>=1 and h3>=1 and h1==sh1==sh2==sh3==0:#c长d长
        fang="c1d1"
    elif sh1>=1 and sh2>=1 and h3==sh3==h1==h2==0:#b短c短
        fang="b0c0"
    elif sh1>=1 and sh3>=1 and sh2==h1==h2==h3==0:#b短d短
        fang="b0d0"
    elif sh2>=1 and sh3>=1 and sh1==h1==h2==h3==0:#c短d短
        fang="c0d0"
    elif sh1>=1 and sh2==0 and sh3==0 and h1==0 and h2==0 and h3==0:
        fang="b0c0"
    elif h1>=1 and h2==0 and h3==0 and sh1==0 and sh2==0 and sh3==0:
        print("错误1")
        fang="b1c1"
    else:
        fang="00"
        


def classes_callback(msg):

    global lh,sh,hear_flag,lh_f,sh_f
    global g1,h1,g2,h2,g3,h3,g,h
    global sh1,sh2,sh3     
    global bridge,f,Img_1,Img_2,Img_3,Img_4,img_flag
    print(msg)
    # if hear_flag!=str(msg):
    #     lh[lh_f]=msg.long_hair_num
    #     sh[sh_f]=msg.short_hair_num
    #     lh_f+=1
    #     sh_f+=1
    #     hear_flag=str(msg)
    if f == 1 and hear_flag!= str(msg):
        h1 = msg.long_hair_num 
        sh1 = msg.short_hair_num
        hear_flag=str(msg)
    elif f == 2 and hear_flag!= str(msg):
        h2 = msg.long_hair_num
        sh2 = msg.short_hair_num
        hear_flag=str(msg)
    elif f == 3 and hear_flag!= str(msg):          #cut?
        h3 = msg.long_hair_cut_num
        sh3 = msg.short_hair_cut_num
        hear_flag=str(msg)
    elif f == 4:
        if img_flag==3:
            h3 = msg.long_hair_num
            sh3 = msg.short_hair_num
            print ("h1,h2,h3 = ",h1,h2,h3)
            print("sh1,sh2,sh3 = ",sh1,sh2,sh3)
            img_flag+=1


def goal_callback(msg):
    global flag ,flag2, f,a,flag_sleep
    print(f,a)
    sta1=str(msg.status_list)
    status=int(sta1[sta1.find('status')+8])
    if status==1 or img_flag==3:
        a=1
    if status== 3 and a==1:       #判断是否到达
        if f <4:
            rospy.sleep(1.0)
            f =f+1 
            a=0 
        if f==4:
            img_pub.publish(Img_3)
    if f==2 and flag_sleep==0:
        rospy.sleep(0.5)
        flag_sleep=1   

                   
        
def img_callback(data):
    # define picture to_down' coefficient of ratio
    global bridge,f,img_flag,Img_1,Img_2,Img_3,Img_4,goal_flag,g,h,g1,h1,g2,h2,g3,h3,g4,h4,fang
    if f==1 :
        if img_flag == 0:
            img_flag = 1
            goal_flag =1
            Img_1 = data
            img_pub.publish(Img_1)
            print ('1.jpg'+"h1="+str(h1)+"sh1="+str(sh2))
            goal_pose = PoseStamped()                    #拍照之后发布下一个目标点
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 2.55296251869
            goal_pose.pose.position.y = -3.32375494003
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z =  -0.724
            goal_pose.pose.orientation.w = 0.690
            goal_pub.publish(goal_pose)
    elif f==2 :
        if img_flag == 1:
            img_flag = 2
            goal_flag =1
            Img_2 = data
            img_pub.publish(Img_2)
            print ('2.jpg')
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.3395364494
            goal_pose.pose.position.y = -2.6411861187744
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = -0.717692950469
            goal_pose.pose.orientation.w = 0.6977121803506
            goal_pub.publish(goal_pose)
    elif f==3 :
        if img_flag == 2:
            img_flag = 3
            goal_flag =1
            Img_3 = data
            img_pub.publish(Img_3)
            print ('3.jpg')
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 0.146945343018#0.088
            goal_pose.pose.position.y = -1.02891929436#-0.989
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.00540454291#0.004
            goal_pose.pose.orientation.w = 1.000374644147#1.000
            goal_pub.publish(goal_pose)
    elif f==4:
        print(img_flag)
        if img_flag == 3:
        #     rospy.sleep(0.5)
        #     img_flag = 4
        # elif img_flag ==4:
        #     rospy.sleep(0.5).
            
            print ("h1,h2,h3 = ",h1,h2,h3)
            print("sh1,sh2,sh3 = ",sh1,sh2,sh3)
            fang_jian()
            argv = '/home/ucar/ucar_ws/src/audio_common/mp3/'+fang+'.mp3'
            playsound(argv)  
            print ('goal rrrrrrrrrrrrrrrrrrrrrrrrrrrr')
            f=f+1
    else:
        pass
 

        


if __name__ == '__main__':
    print("执行play5")
    rospy.init_node('play', anonymous=True)
    rospy.Subscriber("/darknet_ros/classes_num",classes,classes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    rospy.Subscriber("move_base/status",GoalStatusArray,goal_callback)
    #rospy.Subscriber('/goal_id', String, goal_id_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    # rospy.Subscriber("/move_base/result",MoveBaseActionResult,goal1_callback)  #判断是否到达既定目标点
    # argv = rospy.myargv()
    rospy.spin()    
