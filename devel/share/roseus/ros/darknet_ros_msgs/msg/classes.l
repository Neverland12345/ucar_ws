;; Auto-generated. Do not edit!


(when (boundp 'darknet_ros_msgs::classes)
  (if (not (find-package "DARKNET_ROS_MSGS"))
    (make-package "DARKNET_ROS_MSGS"))
  (shadow 'classes (find-package "DARKNET_ROS_MSGS")))
(unless (find-package "DARKNET_ROS_MSGS::CLASSES")
  (make-package "DARKNET_ROS_MSGS::CLASSES"))

(in-package "ROS")
;;//! \htmlinclude classes.msg.html


(defclass darknet_ros_msgs::classes
  :super ros::object
  :slots (_glass_num _long_hair_num _glass_cut_num _long_hair_cut_num ))

(defmethod darknet_ros_msgs::classes
  (:init
   (&key
    ((:glass_num __glass_num) 0)
    ((:long_hair_num __long_hair_num) 0)
    ((:glass_cut_num __glass_cut_num) 0)
    ((:long_hair_cut_num __long_hair_cut_num) 0)
    )
   (send-super :init)
   (setq _glass_num (round __glass_num))
   (setq _long_hair_num (round __long_hair_num))
   (setq _glass_cut_num (round __glass_cut_num))
   (setq _long_hair_cut_num (round __long_hair_cut_num))
   self)
  (:glass_num
   (&optional __glass_num)
   (if __glass_num (setq _glass_num __glass_num)) _glass_num)
  (:long_hair_num
   (&optional __long_hair_num)
   (if __long_hair_num (setq _long_hair_num __long_hair_num)) _long_hair_num)
  (:glass_cut_num
   (&optional __glass_cut_num)
   (if __glass_cut_num (setq _glass_cut_num __glass_cut_num)) _glass_cut_num)
  (:long_hair_cut_num
   (&optional __long_hair_cut_num)
   (if __long_hair_cut_num (setq _long_hair_cut_num __long_hair_cut_num)) _long_hair_cut_num)
  (:serialization-length
   ()
   (+
    ;; int16 _glass_num
    2
    ;; int16 _long_hair_num
    2
    ;; int16 _glass_cut_num
    2
    ;; int16 _long_hair_cut_num
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int16 _glass_num
       (write-word _glass_num s)
     ;; int16 _long_hair_num
       (write-word _long_hair_num s)
     ;; int16 _glass_cut_num
       (write-word _glass_cut_num s)
     ;; int16 _long_hair_cut_num
       (write-word _long_hair_cut_num s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int16 _glass_num
     (setq _glass_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _long_hair_num
     (setq _long_hair_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _glass_cut_num
     (setq _glass_cut_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _long_hair_cut_num
     (setq _long_hair_cut_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get darknet_ros_msgs::classes :md5sum-) "e6802d1037088d3136af614c2e78487e")
(setf (get darknet_ros_msgs::classes :datatype-) "darknet_ros_msgs/classes")
(setf (get darknet_ros_msgs::classes :definition-)
      "int16 glass_num  
int16 long_hair_num
int16 glass_cut_num
int16 long_hair_cut_num
")



(provide :darknet_ros_msgs/classes "e6802d1037088d3136af614c2e78487e")


