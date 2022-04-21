#include <ros/ros.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include "std_msgs/String.h"
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>
#include <aruco_ros/aruco_ros_utils.h>
#include <aruco_msgs/MarkerArray.h>
#include <geometry_msgs/PoseStamped.h>

#include <move_base_msgs/MoveBaseAction.h>
#include <move_base_msgs/MoveBaseGoal.h>

ros::Publisher tts_pub;
// aruco_msgs::MarkerArray::Ptr marker_msg_;
std::vector<aruco::Marker> markers_;
int flag=0;

void ttsCallback_food(const aruco_msgs::MarkerArray::Ptr &markers)
{
    aruco_msgs::Marker & marker_i = markers->markers.at(0);
    switch(marker_i.id)
    {
        case 0:
        {
            std_msgs::String voice_msg;
            voice_msg.data = "蔬菜";
            tts_pub.publish(voice_msg);
            ros::Duration(2).sleep();
            break;
        }
        case 1:
        {
            std_msgs::String voice_msg;
            voice_msg.data = "水果";
            tts_pub.publish(voice_msg);
            ros::Duration(2).sleep();
            break;
        }
        case 2:
        {
            std_msgs::String voice_msg;
            voice_msg.data = "肉类";
            tts_pub.publish(voice_msg);
            ros::Duration(2).sleep();
            break;
        }
    }
}

//获取到达目标的状态
void ttsCallback_end(const move_base_msgs::MoveBaseActionResult& msg)
{	
	if(msg.status.status == 3)//到达
	{
        flag = flag+1;
        if(flag == 2)
        {
            std::cout<<"the goal was achieved successfully!"<<std::endl;
            std_msgs::String voice_msg;
            voice_msg.data = "识别到长头发几人,戴眼镜几人,您的菜品已送达,请您取餐";
            tts_pub.publish(voice_msg);
            ros::Duration(2).sleep();
        }
	}
}

int main(int argc, char* argv[])
{
    ros::init(argc,argv,"tts_publisher");
    ros::NodeHandle n;
    ros::Subscriber marker_sub = n.subscribe("/aruco_marker_publisher/markers",100,ttsCallback_food);
    ros::Subscriber goal_sub =n.subscribe("move_base/result", 10, ttsCallback_end);

    tts_pub = n.advertise<std_msgs::String>("/voiceWords",1000);

    ros::spin();

    return 0;
}
