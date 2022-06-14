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


f =0
img_flag = 0
# class_dict = {'gh_00':0,'gh_01':0,'gh_02':0,'gh_10':0,'gh_11':0,'gh_12':0,'gh_20':0,'gh_21':0,'gh_22':0}
Img_1 = Image()
Img_2 = Image()
Img_3 = Image()
Img_4 = Image()
g1 = 0
h1 = 0
g2 = 0
h2 = 0
g3 = 0
h3 = 0
g4 = 0
h4 = 0
goal_flag = 0
g = 0
h = 0
def goal_id_callback(msgs):
    if msgs.data == "goal_1":
        goal_pose = PoseStamped()
        goal_pose.header.frame_id = "map"
        goal_pose.pose.position.x = 1.75479720116
        goal_pose.pose.position.y = 3.29980039597
        goal_pose.pose.position.z = 0.0
        goal_pose.pose.orientation.x = 0
        goal_pose.pose.orientation.y = 0
        goal_pose.pose.orientation.z = -0.0101698932772
        goal_pose.pose.orientation.w = 0.999948285298
        goal_pub.publish(goal_pose)

def food_callback(data):
    if data.data == "veg":
        argv = '/home/ucar/ucar_ws/src/audio_common/mp3/veg.mp3'
    elif data.data =="fruit":
        argv = '/home/ucar/ucar_ws/src/audio_common/mp3/fruit.mp3'
    elif data.data == "meat":
        argv = '/home/ucar/ucar_ws/src/audio_common/mp3/meat.mp3'
    soundhandle = SoundClient()
    rospy.sleep(1)
    rospy.loginfo('Playing "%s".' % argv)
    volume = 1.0
    soundhandle.playWave(argv, volume)
def classes_callback(msg):
    global g1,h1,g2,h2,g3,h3,g4,h4,g,h
    global bridge,f,Img_1,Img_2,Img_3,Img_4,img_flag
    if f == 1:
        g1 = msg.glass_num
        h1 = msg.long_hair_num 
    elif f == 3:
        g2 = msg.glass_num
        h2 = msg.long_hair_num
    elif f ==5 :        
        g3 = msg.glass_cut_num
        h3 = msg.long_hair_cut_num
    elif f == 6:
        if img_flag >=5:
            g4 = msg.glass_num
            h4 = msg.long_hair_num
            print ("g1,g2,g3,g42 = ",g1,g2,g3,g4)
            print ("h1,h2,h3,h4 = ",h1,h2,h3,h4)
            print ("g=",g)
            print ("h=",h)

def goal_callback(msg):
    print("回调函数")
    global f,Img_4
    if msg.status.status == 3:       
        if f <=1 or f==3 or f ==4:
            rospy.sleep(0.3)
        f =f+1 
        if f==6:
            img_pub.publish(Img_4)
                   
        
def img_callback(data):
    # define picture to_down' coefficient of ratio
    global bridge,f,img_flag,Img_1,Img_2,Img_3,Img_4,goal_flag,g,h,g1,h1,g2,h2,g3,h3,g4,h4
    bridge = CvBridge()
    # print (img_flag)
    if f==1 :
        if img_flag == 0:
            img_flag = 1
            goal_flag =1
            Img_1 = data
            img_pub.publish(Img_1)
            cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
            image_name = str(img_flag)+ ".jpg" 
            cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)  
            print ('1.jpg')
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 1.77696251869
            goal_pose.pose.position.y = 2.23875494003
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z =  -0.69648739508
            goal_pose.pose.orientation.w = 0.717569026989
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
            goal_pose.pose.position.x = 2.60925364494
            goal_pose.pose.position.y = 1.15061187744
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.995692950469
            goal_pose.pose.orientation.w = 0.0927121803506
            goal_pub.publish(goal_pose)
    elif f==4 :
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
            goal_pose.pose.position.x = 0.286945343018
            goal_pose.pose.position.y = 1.17591929436
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.340140454291
            goal_pose.pose.orientation.w = 0.940374644147
            goal_pub.publish(goal_pose)
    elif f==5:
        if img_flag == 3:
            img_flag = 4
            goal_flag =3
            Img_4 = data

            print ('4.jpg')
            cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
            image_name = str(img_flag)+ ".jpg" 
            cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)
            goal_pose = PoseStamped()
            goal_pose.header.frame_id = "map"
            goal_pose.pose.position.x = 0.749822478294
            goal_pose.pose.position.y = 2.67
            goal_pose.pose.position.z = 0.0
            goal_pose.pose.orientation.x = 0
            goal_pose.pose.orientation.y = 0
            goal_pose.pose.orientation.z = 0.699846946135
            goal_pose.pose.orientation.w = 0.714292833498
            goal_pub.publish(goal_pose)
    elif f==6:
        if img_flag == 4:
            rospy.sleep(1.5)
            img_flag = 5
        elif img_flag ==5:
            rospy.sleep(1.5)
            img_flag =6
        elif img_flag == 6:
            img_flag = 7
            g = g1+g2+g3+g4
            h = h1+h2+h3+h4
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
    rospy.init_node('play', anonymous=True)
    rospy.Subscriber("food", String, food_callback)
    rospy.Subscriber("move_base/result",MoveBaseActionResult,goal_callback)
    rospy.Subscriber("/darknet_ros/classes_num",classes,classes_callback)
    rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
    rospy.Subscriber('/goal_id', String, goal_id_callback)
    goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
    img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
    # argv = rospy.myargv()
    rospy.spin()


# #!/usr/bin/env python
# import rospy
# from std_msgs.msg import String
# from sound_play.msg import SoundRequest
# from sound_play.libsoundplay import SoundClient
# from darknet_ros_msgs.msg import classes
# # from move_base_msgs.msg import MoveBaseAction
# # from move_base_msgs.msg import MoveBaseGoal
# from move_base_msgs.msg import MoveBaseActionResult
# from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
# import numpy as np
# from sensor_msgs.msg import Image
# from cv_bridge import CvBridge, CvBridgeError
# import cv2


# f =0
# img_flag = 0
# # class_dict = {'gh_00':0,'gh_01':0,'gh_02':0,'gh_10':0,'gh_11':0,'gh_12':0,'gh_20':0,'gh_21':0,'gh_22':0}
# Img_1 = Image()
# Img_2 = Image()
# Img_3 = Image()
# Img_4 = Image()
# g1 = 0
# h1 = 0
# g2 = 0
# h2 = 0
# g3 = 0
# h3 = 0
# g4 = 0
# h4 = 0
# goal_flag = 0
# g = 0
# h = 0
# def goal_id_callback(msgs):
#     if msgs.data == "goal_1":
#         goal_pose = PoseStamped()
#         goal_pose.header.frame_id = "map"
#         goal_pose.pose.position.x = 1.75479720116
#         goal_pose.pose.position.y = 3.29980039597
#         goal_pose.pose.position.z = 0.0
#         goal_pose.pose.orientation.x = 0
#         goal_pose.pose.orientation.y = 0
#         goal_pose.pose.orientation.z = -0.0101698932772
#         goal_pose.pose.orientation.w = 0.999948285298
#         goal_pub.publish(goal_pose)
# def food_callback(data):
#     if data.data == "veg":
#         argv = '/home/ucar/ucar_ws/src/audio_common/mp3/veg.mp3'
#     elif data.data =="fruit":
#         argv = '/home/ucar/ucar_ws/src/audio_common/mp3/fruit.mp3'
#     elif data.data == "meat":
#         argv = '/home/ucar/ucar_ws/src/audio_common/mp3/meat.mp3'
#     soundhandle = SoundClient()
#     rospy.sleep(1)
#     rospy.loginfo('Playing "%s".' % argv)
#     volume = 1.0
#     soundhandle.playWave(argv, volume)
# def classes_callback(msg):
#     global g1,h1,g2,h2,g3,h3,g4,h4,g,h
#     global bridge,f,Img_1,Img_2,Img_3,Img_4
#     if f == 1:
#         g1 = msg.glass_num
#         h1 = msg.long_hair_num 
#     elif f == 3:
#         g2 = msg.glass_num
#         h2 = msg.long_hair_num
#     elif f == 4:        
#         g3 = msg.glass_cut_num
#         h3 = msg.long_hair_cut_num
#     elif f == 6:
#         g4 = msg.glass_num
#         h4 = msg.long_hair_num
#         print ("g1,g2,g3,g4 = ",g1,g2,g3,g4)
#         print ("h1,h2,h3,h4 = ",h1,h2,h3,h4)
#         print ("g=",g)
#         print ("h=",h)

# def goal_callback(msg):
#     global f,Img_4
#     if msg.status.status == 3:       
#         if f <=1 or f==3 or f ==4:
#             rospy.sleep(0.5)
#         f =f+1 
#         if f==6:
#             img_pub.publish(Img_4)
                   
        
# def img_callback(data):
#     # define picture to_down' coefficient of ratio
#     global bridge,f,img_flag,Img_1,Img_2,Img_3,Img_4,goal_flag,g,h,g1,h1,g2,h2,g3,h3,g4,h4
#     bridge = CvBridge()
#     if f==1 :
#         if img_flag == 0:
#             img_flag = 1
#             goal_flag =1
#             Img_1 = data
#             img_pub.publish(Img_1)
#             cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
#             image_name = str(img_flag)+ ".jpg" 
#             cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)  
#             print ('1.jpg')
#             goal_pose = PoseStamped()
#             goal_pose.header.frame_id = "map"
#             goal_pose.pose.position.x = 1.77696251869
#             goal_pose.pose.position.y = 2.23875494003
#             goal_pose.pose.position.z = 0.0
#             goal_pose.pose.orientation.x = 0
#             goal_pose.pose.orientation.y = 0
#             goal_pose.pose.orientation.z =  -0.69648739508
#             goal_pose.pose.orientation.w = 0.717569026989
#             goal_pub.publish(goal_pose)
#     elif f==2 :
#         if img_flag == 1:
#             img_flag = 2
#             goal_flag =1
#             Img_2 = data
#             img_pub.publish(Img_2)
#             cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
#             image_name = str(img_flag)+ ".jpg" 
#             cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)  
#             print ('2.jpg')
#             goal_pose = PoseStamped()
#             goal_pose.header.frame_id = "map"
#             goal_pose.pose.position.x = 2.60925364494
#             goal_pose.pose.position.y = 1.15061187744
#             goal_pose.pose.position.z = 0.0
#             goal_pose.pose.orientation.x = 0
#             goal_pose.pose.orientation.y = 0
#             goal_pose.pose.orientation.z = 0.995692950469
#             goal_pose.pose.orientation.w = 0.0927121803506
#             goal_pub.publish(goal_pose)
#     elif f==4 :
#         if img_flag == 2:
#             img_flag = 3
#             goal_flag =1
#             Img_3 = data
#             img_pub.publish(Img_3)
#             cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
#             image_name = str(img_flag)+ ".jpg" 
#             cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)  
#             print ('3.jpg')
#             goal_pose = PoseStamped()
#             goal_pose.header.frame_id = "map"
#             goal_pose.pose.position.x = 0.286945343018
#             goal_pose.pose.position.y = 1.17591929436
#             goal_pose.pose.position.z = 0.0
#             goal_pose.pose.orientation.x = 0
#             goal_pose.pose.orientation.y = 0
#             goal_pose.pose.orientation.z = 0.340140454291
#             goal_pose.pose.orientation.w = 0.940374644147
#             goal_pub.publish(goal_pose)
#     elif f==5:
#         if img_flag == 3:
#             img_flag = 4
#             goal_flag =3
#             Img_4 = data

#             print ('4.jpg')
#             cv_img = bridge.imgmsg_to_cv2(data, "bgr8")
#             image_name = str(img_flag)+ ".jpg" 
#             cv2.imwrite('/home/ucar/ucar_ws/src/audio_common/sound_play/data/' + image_name, cv_img)
#             goal_pose = PoseStamped()
#             goal_pose.header.frame_id = "map"
#             goal_pose.pose.position.x = 0.749822478294
#             goal_pose.pose.position.y = 2.72
#             goal_pose.pose.position.z = 0.0
#             goal_pose.pose.orientation.x = 0
#             goal_pose.pose.orientation.y = 0
#             goal_pose.pose.orientation.z = 0.699846946135
#             goal_pose.pose.orientation.w = 0.714292833498
#             goal_pub.publish(goal_pose)
#     elif f==6:
#         if img_flag == 4:
#             rospy.sleep(2)
#             img_flag = 5
#         elif img_flag ==5:
#             img_flag =6
#             g = g1+g2+g3+g4
#             h = h1+h2+h3+h4
#             if g>2:
#                 g = 2
#             if h>2:
#                 h = 2
#             argv = '/home/ucar/ucar_ws/src/audio_common/mp3/gh_'+str(g)+str(h)+'.mp3'
#             soundhandle = SoundClient()
#             rospy.sleep(1)
#             rospy.loginfo('Playing "%s".' % argv)
#             volume = 1.0
#             soundhandle.playWave(argv, volume)    
#             print ('goal rrrrrrrrrrrrrrrrrrrrrrrrrrrr')
#     else:
#         pass
 

        


# if __name__ == '__main__':
#     rospy.init_node('play', anonymous=True)
#     rospy.Subscriber("food", String, food_callback)
#     rospy.Subscriber("move_base/result",MoveBaseActionResult,goal_callback)
#     rospy.Subscriber("/darknet_ros/classes_num",classes,classes_callback)
#     rospy.Subscriber('usb_cam/image_raw', Image, img_callback)
#     rospy.Subscriber('/goal_id', String, goal_id_callback)
#     goal_pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=1)
#     img_pub = rospy.Publisher('/final_image',Image,queue_size=1)
#     # argv = rospy.myargv()
#     rospy.spin()
