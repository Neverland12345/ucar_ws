#include <iostream>
#include <aruco/aruco.h>
#include <aruco/cvdrawingutils.h>

#include <ros/ros.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>
#include <sensor_msgs/image_encodings.h>
#include <aruco_ros/aruco_ros_utils.h>
#include <aruco_msgs/MarkerArray.h>
#include <tf/transform_listener.h>
#include <std_msgs/UInt32MultiArray.h>
#include <geometry_msgs/PoseStamped.h>
#include <std_msgs/String.h>
#include <move_base_msgs/MoveBaseAction.h>
#include <move_base_msgs/MoveBaseGoal.h>

int id_flag = 1;
int goal_flag = 0;
class ArucoMarkerPublisher
{
private:
  // ArUco stuff
  aruco::MarkerDetector mDetector_;
  aruco::CameraParameters camParam_;
  std::vector<aruco::Marker> markers_;

  // node params
  bool useRectifiedImages_;
  std::string marker_frame_;
  std::string camera_frame_;
  std::string reference_frame_;
  double marker_size_;

  // ROS pub-sub
  ros::NodeHandle nh_;
  image_transport::ImageTransport it_;
  image_transport::Subscriber image_sub_;

  image_transport::Publisher image_pub_;
  image_transport::Publisher debug_pub_;
  ros::Publisher marker_pub_;
  ros::Publisher marker_list_pub_;
  ros::Publisher send_goal_pub;
  ros::Publisher chatter_pub;
  tf::TransformListener tfListener_;

  ros::Subscriber cam_info_sub_;
  ros::Subscriber goal_sub;

  aruco_msgs::MarkerArray::Ptr marker_msg_;
  geometry_msgs::PoseStamped goal_msg;
  std_msgs::String food_msg;
  cv::Mat inImage_;
  bool useCamInfo_;
  std_msgs::UInt32MultiArray marker_list_msg_;

public:
  ArucoMarkerPublisher() :
      nh_("~"), it_(nh_), useCamInfo_(true)
  {
    image_sub_ = it_.subscribe("/image", 1, &ArucoMarkerPublisher::image_callback, this);
    // goal_sub = nh_.subscribe("move_base/result", 10, &ArucoMarkerPublisher::goal_callback, this);

    nh_.param<bool>("use_camera_info", useCamInfo_, true);
    if (useCamInfo_)
    {
      sensor_msgs::CameraInfoConstPtr msg = ros::topic::waitForMessage<sensor_msgs::CameraInfo>("/camera_info", nh_); //, 10.0);

      nh_.param<double>("marker_size", marker_size_, 0.05);
      nh_.param<bool>("image_is_rectified", useRectifiedImages_, true);
      nh_.param<std::string>("reference_frame", reference_frame_, "");
      nh_.param<std::string>("camera_frame", camera_frame_, "");
      camParam_ = aruco_ros::rosCameraInfo2ArucoCamParams(*msg, useRectifiedImages_);
      ROS_ASSERT(not (camera_frame_.empty() and not reference_frame_.empty()));
      if (reference_frame_.empty())
        reference_frame_ = camera_frame_;
    }
    else
    {
      camParam_ = aruco::CameraParameters();
    }

    image_pub_ = it_.advertise("result", 1);
    debug_pub_ = it_.advertise("debug", 1);
    marker_pub_ = nh_.advertise<aruco_msgs::MarkerArray>("markers", 100); //id
    marker_list_pub_ = nh_.advertise<std_msgs::UInt32MultiArray>("markers_list", 10);
    send_goal_pub = nh_.advertise<geometry_msgs::PoseStamped>("/move_base_simple/goal",1);
    chatter_pub = nh_.advertise<std_msgs::String>("/food", 10);
    marker_msg_ = aruco_msgs::MarkerArray::Ptr(new aruco_msgs::MarkerArray());
    marker_msg_->header.frame_id = reference_frame_;
    marker_msg_->header.seq = 0;

    goal_msg.header.frame_id = "map";
    goal_msg.pose.position.x =  0.258254051208;
    goal_msg.pose.position.y = 0.682775437832;
    goal_msg.pose.position.z = 0.0;
    goal_msg.pose.orientation.x = 0;
    goal_msg.pose.orientation.y = 0;
    goal_msg.pose.orientation.z = 0.707492250868;
    goal_msg.pose.orientation.w = 0.706721101257;

    // goal_msg.header.frame_id = "map";
    // goal_msg.pose.position.x = 0.998185098171;
    // goal_msg.pose.position.y = -1.13430953026;
    // goal_msg.pose.position.z = 0.0;
    // goal_msg.pose.orientation.x = 0;
    // goal_msg.pose.orientation.y = 0;
    // goal_msg.pose.orientation.z = 0.701436965022;
    // goal_msg.pose.orientation.w = 0.712731495095;

    // goal_msg.header.frame_id = "map";
    // goal_msg.pose.position.x = 0.442360460758;
    // goal_msg.pose.position.y = -1.1876398325;
    // goal_msg.pose.position.z = 0.0;
    // goal_msg.pose.orientation.x = 0;
    // goal_msg.pose.orientation.y = 0;
    // goal_msg.pose.orientation.z = 0.699699748914;
    // goal_msg.pose.orientation.w = 0.714437024076;

    // goal_msg.header.frame_id = "map";
    // goal_msg.pose.position.x = -0.0271990336478;
    // goal_msg.pose.position.y = -1.18817043304;
    // goal_msg.pose.position.z = 0.0;
    // goal_msg.pose.orientation.x = 0;
    // goal_msg.pose.orientation.y = 0;
    // goal_msg.pose.orientation.z = 0.701288729782;
    // goal_msg.pose.orientation.w = 0.712877350938;
  }

  bool getTransform(const std::string& refFrame, const std::string& childFrame, tf::StampedTransform& transform)
  {
    std::string errMsg;

    if (!tfListener_.waitForTransform(refFrame, childFrame, ros::Time(0), ros::Duration(0.5), ros::Duration(0.01),
                                      &errMsg))
    {
      ROS_ERROR_STREAM("Unable to get pose from TF: " << errMsg);
      return false;
    }
    else
    {
      try
      {
        tfListener_.lookupTransform(refFrame, childFrame, ros::Time(0), // get latest available
                                    transform);
      }
      catch (const tf::TransformException& e)
      {
        ROS_ERROR_STREAM("Error in lookupTransform of " << childFrame << " in " << refFrame);
        return false;
      }

    }
    return true;
  }

  // void goal_callback(const move_base_msgs::MoveBaseActionResult& msg)
  // {	
  //   ROS_INFO("goal_callback");
  //   if(msg.status.status == 3)//到达
  //   {
  //     goal_flag = goal_flag+1;
  //   }
  //   if(goal_flag == 2)
  //   {
  //     ROS_INFO("goal_flag=2");
  //     geometry_msgs::PoseStamped goal_msg;
  //     ros::Duration(2).sleep();
  //     goal_msg.header.frame_id = "map";
  //     goal_msg.pose.position.x = 0.998185098171;
  //     goal_msg.pose.position.y = -1.13430953026;
  //     goal_msg.pose.position.z = 0.0;
  //     goal_msg.pose.orientation.x = 0;
  //     goal_msg.pose.orientation.y = 0;
  //     goal_msg.pose.orientation.z = 0.701436965022;
  //     goal_msg.pose.orientation.w = 0.712731495095;
  //     send_goal_pub.publish(goal_msg);
  //   }
  // }

  void image_callback(const sensor_msgs::ImageConstPtr& msg)
  {
    bool publishMarkers = marker_pub_.getNumSubscribers() > 0;
    bool publishMarkersList = marker_list_pub_.getNumSubscribers() > 0;
    bool publishImage = image_pub_.getNumSubscribers() > 0;
    bool publishDebug = debug_pub_.getNumSubscribers() > 0;

    // if (1)
    //   return;

    ros::Time curr_stamp = msg->header.stamp;
    cv_bridge::CvImagePtr cv_ptr;
    try
    {
      cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::RGB8);
      //inImage_ = cv_ptr->image;
      cv::flip(cv_ptr->image,inImage_,1);

      // clear out previous detection results
      markers_.clear();

      // ok, let's detect
      mDetector_.detect(inImage_, markers_, camParam_, marker_size_, false);

      // marker array publish
      if (1)
      {
        marker_msg_->markers.clear();
        marker_msg_->markers.resize(markers_.size());
        marker_msg_->header.stamp = curr_stamp;
        marker_msg_->header.seq++;

        for (std::size_t i = 0; i < markers_.size(); ++i)
        {
          aruco_msgs::Marker & marker_i = marker_msg_->markers.at(i);
          marker_i.header.stamp = curr_stamp;
          marker_i.id = markers_.at(i).id;
          marker_i.confidence = 1.0;
        }

        // if there is camera info let's do 3D stuff
        if (useCamInfo_)
        {
          // get the current transform from the camera frame to output ref frame
          tf::StampedTransform cameraToReference;
          cameraToReference.setIdentity();

          if (reference_frame_ != camera_frame_)
          {
            getTransform(reference_frame_, camera_frame_, cameraToReference);
          }

          // now find the transform for each detected marker
          for (std::size_t i = 0; i < markers_.size(); ++i)
          {
            aruco_msgs::Marker & marker_i = marker_msg_->markers.at(i);
            tf::Transform transform = aruco_ros::arucoMarker2Tf(markers_[i]);
            transform = static_cast<tf::Transform>(cameraToReference) * transform;
            tf::poseTFToMsg(transform, marker_i.pose.pose);
            marker_i.header.frame_id = reference_frame_;
          }
        }

        // publish marker array
        if (marker_msg_->markers.size() > 0)
        {  
          
          marker_pub_.publish(marker_msg_);
          aruco_msgs::Marker & marker_i = marker_msg_->markers.at(0);
          if(id_flag == 1)
          {
            ROS_INFO("2");
          if(marker_i.id == 0)
          {
            food_msg.data = "veg";
            chatter_pub.publish(food_msg);
            ros::Duration(3).sleep();
            send_goal_pub.publish(goal_msg);      
            id_flag = 0;
          } 
          else if(marker_i.id == 1) 
          {
            food_msg.data = "fruit";
            chatter_pub.publish(food_msg);
            ros::Duration(3).sleep();
            send_goal_pub.publish(goal_msg);
            id_flag = 0;
          }
          else if(marker_i.id == 2)
          {
            food_msg.data = "meat";
            chatter_pub.publish(food_msg);
            ros::Duration(3).sleep();
            send_goal_pub.publish(goal_msg);
            id_flag = 0;
          }

          }
        }    
      }

      if (1)
      {
        marker_list_msg_.data.resize(markers_.size());
        for (std::size_t i = 0; i < markers_.size(); ++i)
          marker_list_msg_.data[i] = markers_[i].id;

        marker_list_pub_.publish(marker_list_msg_);
      }

      // draw detected markers on the image for visualization
      for (std::size_t i = 0; i < markers_.size(); ++i)
      {
        markers_[i].draw(inImage_, cv::Scalar(0, 0, 255), 2);
      }

      // // draw a 3D cube in each marker if there is 3D info
      // if (camParam_.isValid() && marker_size_ != -1)
      // {
      //   for (std::size_t i = 0; i < markers_.size(); ++i)
      //     aruco::CvDrawingUtils::draw3dAxis(inImage_, markers_[i], camParam_);
      // }

      // publish input image with markers drawn on it
      if (publishImage)
      {
        // show input with augmented information
        cv_bridge::CvImage out_msg;
        out_msg.header.stamp = curr_stamp;
        out_msg.encoding = sensor_msgs::image_encodings::RGB8;
        out_msg.image = inImage_;
        image_pub_.publish(out_msg.toImageMsg());
      }

      // publish image after internal image processing
      if (publishDebug)
      {
        // show also the internal image resulting from the threshold operation
        cv_bridge::CvImage debug_msg;
        debug_msg.header.stamp = curr_stamp;
        debug_msg.encoding = sensor_msgs::image_encodings::MONO8;
        debug_msg.image = mDetector_.getThresholdedImage();
        debug_pub_.publish(debug_msg.toImageMsg());
      }

    }
    catch (cv_bridge::Exception& e)
    {
      ROS_ERROR("cv_bridge exception: %s", e.what());
    }
  }
};

int main(int argc, char **argv)
{
  ros::init(argc, argv, "aruco_marker_publisher");
  ArucoMarkerPublisher node;

  ros::spin();
}
