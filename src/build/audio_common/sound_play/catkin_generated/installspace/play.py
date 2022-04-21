#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from darknet_ros_msgs.msg import classes
# from move_base_msgs.msg import MoveBaseAction
# from move_base_msgs.msg import MoveBaseGoal
from move_base_msgs.msg import MoveBaseActionResult


f =0
class_dict = {'gh_00':0,'gh_01':0,'gh_02':0,'gh_10':0,'gh_11':0,'gh_12':0,'gh_20':0,'gh_21':0,'gh_22':0}
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
    if msg.glass_num == 0:
        if msg.long_hair_num == 0:
            class_dict['gh_00'] += 1
        elif msg.long_hair_num == 1:
            class_dict['gh_01'] += 1
        elif msg.long_hair_num == 2:
            class_dict['gh_02'] += 1
    elif msg.glass_num == 1:
        if msg.long_hair_num == 0:
            class_dict['gh_10'] += 1
        elif msg.long_hair_num == 1:
            class_dict['gh_11'] += 1
        elif msg.long_hair_num == 2:
            class_dict['gh_12'] += 1
    elif msg.glass_num == 2:
        if msg.long_hair_num == 0:
            class_dict['gh_20'] += 1
        elif msg.long_hair_num == 1:
            class_dict['gh_21'] += 1
        elif msg.long_hair_num == 2:
            class_dict['gh_22'] += 1


def goal_callback(msg):
    global f
    if msg.status.status == 3:
        f =f+1        
    if f == 3:
        d_order=sorted(class_dict.items(),key=lambda x:x[1],reverse=True)
        gh = 'gh_00' if d_order[0][1] == 0 else d_order[0][0]
        argv = '/home/ucar/ucar_ws/src/audio_common/mp3/'+gh+'.mp3'
        soundhandle = SoundClient()
        rospy.sleep(1)
        rospy.loginfo('Playing "%s".' % argv)
        volume = 1.0
        soundhandle.playWave(argv, volume)

        


if __name__ == '__main__':
    rospy.init_node('play', anonymous=True)
    rospy.Subscriber("food", String, food_callback)
    rospy.Subscriber("move_base/result",MoveBaseActionResult,goal_callback)
    rospy.Subscriber("/darknet_ros/classes_num",classes,classes_callback)
    # argv = rospy.myargv()
    rospy.spin()
