#!/usr/bin/env python
#coding:utf-8

import rospy, math
from gazebo_msgs.msg import LinkStates
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped


class cqu_race_utils:

    def __init__(self):
        rospy.init_node("cqu_race_utils")
        self.started = False
        self.reached = False
        self.dist = 99999
        self.car_pos = None
        self.car_speed = None
        self.start_time = None
        self.time_taken = None

        self.goal_pose = PoseStamped()
        self.goal_pose.header.frame_id = "map"
        self.goal_pose.pose.position.x = -1.15406775475
        self.goal_pose.pose.position.y = 0.7056453228
        self.goal_pose.pose.position.z = 0.0
        self.goal_pose.pose.orientation.x = 0
        self.goal_pose.pose.orientation.y = 0
        self.goal_pose.pose.orientation.z = 0.999999669254
        self.goal_pose.pose.orientation.w = -0.000813321181547

        self.sub_link_states = rospy.Subscriber("/gazebo/link_states", LinkStates, self.pose_cb)
        self.sub_init_pose = rospy.Subscriber("/initialpose", PoseWithCovarianceStamped, self.init_cb)
        self.pub_goal = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)
        rospy.Timer(rospy.Duration(0.25), self.timer_cb) # 20hz

    def init_cb(self, pose):
        self.started = True
        self.start_time = rospy.Time.now()
        rospy.loginfo("=== RACE STARTED ===")
        self.goal_pose.header.stamp = rospy.Time.now()
        self.pub_goal.publish(self.goal_pose)

    def pose_cb(self, msg):
        try:
            arrayIndex = msg.name.index('racecar::base_footprint')
        except ValueError:
            # Wait for Gazebo to startup
            pass
        else:
            # Extract our current position information
            self.car_pos = msg.pose[arrayIndex]
            self.car_speed = msg.twist[arrayIndex].linear.x
            self.dist = math.sqrt(math.pow(self.car_pos.position.x - self.goal_pose.pose.position.x, 2) + math.pow(self.car_pos.position.y - self.goal_pose.pose.position.y, 2))
            if self.dist < 0.5:
                self.time_taken = rospy.Time.now() - self.start_time
                self.reached = True
        #self.last_recieved_stamp = rospy.Time.now()


    def timer_cb(self, event):
        if self.started and not self.reached:
            rospy.loginfo("dist {:2f} speed {:2f}".format(self.dist, self.car_speed))
        elif self.started and self.reached:
            rospy.loginfo_once("=== GUESS WHAT? ===")
            rospy.loginfo_once("")
            rospy.loginfo_once("# Goal reached: ({:.3f}, {:.3f})".format(self.goal_pose.pose.position.x, self.goal_pose.pose.position.y))
            rospy.loginfo_once("# Time taking: {:.3f}".format(self.time_taken.to_sec()))
            rospy.loginfo_once("# Average speed: {:.3f}".format( 45 / self.time_taken.to_sec()))
            rospy.loginfo_once("")
            rospy.loginfo_once("=== RACE FINISHED!! ===")


if __name__ == "__main__":
    cqu_race_utils()
    rospy.spin()