; Auto-generated. Do not edit!


(cl:in-package darknet_ros_msgs-msg)


;//! \htmlinclude classes.msg.html

(cl:defclass <classes> (roslisp-msg-protocol:ros-message)
  ((glass_num
    :reader glass_num
    :initarg :glass_num
    :type cl:fixnum
    :initform 0)
   (long_hair_num
    :reader long_hair_num
    :initarg :long_hair_num
    :type cl:fixnum
    :initform 0)
   (glass_cut_num
    :reader glass_cut_num
    :initarg :glass_cut_num
    :type cl:fixnum
    :initform 0)
   (long_hair_cut_num
    :reader long_hair_cut_num
    :initarg :long_hair_cut_num
    :type cl:fixnum
    :initform 0)
   (short_hair_num
    :reader short_hair_num
    :initarg :short_hair_num
    :type cl:fixnum
    :initform 0)
   (short_hair_cut_num
    :reader short_hair_cut_num
    :initarg :short_hair_cut_num
    :type cl:fixnum
    :initform 0))
)

(cl:defclass classes (<classes>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <classes>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'classes)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name darknet_ros_msgs-msg:<classes> is deprecated: use darknet_ros_msgs-msg:classes instead.")))

(cl:ensure-generic-function 'glass_num-val :lambda-list '(m))
(cl:defmethod glass_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:glass_num-val is deprecated.  Use darknet_ros_msgs-msg:glass_num instead.")
  (glass_num m))

(cl:ensure-generic-function 'long_hair_num-val :lambda-list '(m))
(cl:defmethod long_hair_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:long_hair_num-val is deprecated.  Use darknet_ros_msgs-msg:long_hair_num instead.")
  (long_hair_num m))

(cl:ensure-generic-function 'glass_cut_num-val :lambda-list '(m))
(cl:defmethod glass_cut_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:glass_cut_num-val is deprecated.  Use darknet_ros_msgs-msg:glass_cut_num instead.")
  (glass_cut_num m))

(cl:ensure-generic-function 'long_hair_cut_num-val :lambda-list '(m))
(cl:defmethod long_hair_cut_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:long_hair_cut_num-val is deprecated.  Use darknet_ros_msgs-msg:long_hair_cut_num instead.")
  (long_hair_cut_num m))

(cl:ensure-generic-function 'short_hair_num-val :lambda-list '(m))
(cl:defmethod short_hair_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:short_hair_num-val is deprecated.  Use darknet_ros_msgs-msg:short_hair_num instead.")
  (short_hair_num m))

(cl:ensure-generic-function 'short_hair_cut_num-val :lambda-list '(m))
(cl:defmethod short_hair_cut_num-val ((m <classes>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader darknet_ros_msgs-msg:short_hair_cut_num-val is deprecated.  Use darknet_ros_msgs-msg:short_hair_cut_num instead.")
  (short_hair_cut_num m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <classes>) ostream)
  "Serializes a message object of type '<classes>"
  (cl:let* ((signed (cl:slot-value msg 'glass_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'long_hair_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'glass_cut_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'long_hair_cut_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'short_hair_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'short_hair_cut_num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <classes>) istream)
  "Deserializes a message object of type '<classes>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'glass_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'long_hair_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'glass_cut_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'long_hair_cut_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'short_hair_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'short_hair_cut_num) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<classes>)))
  "Returns string type for a message object of type '<classes>"
  "darknet_ros_msgs/classes")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'classes)))
  "Returns string type for a message object of type 'classes"
  "darknet_ros_msgs/classes")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<classes>)))
  "Returns md5sum for a message object of type '<classes>"
  "807f252bc3466dd12378a82941c798f7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'classes)))
  "Returns md5sum for a message object of type 'classes"
  "807f252bc3466dd12378a82941c798f7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<classes>)))
  "Returns full string definition for message of type '<classes>"
  (cl:format cl:nil "int16 glass_num  ~%int16 long_hair_num~%int16 glass_cut_num~%int16 long_hair_cut_num~%int16 short_hair_num~%int16 short_hair_cut_num~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'classes)))
  "Returns full string definition for message of type 'classes"
  (cl:format cl:nil "int16 glass_num  ~%int16 long_hair_num~%int16 glass_cut_num~%int16 long_hair_cut_num~%int16 short_hair_num~%int16 short_hair_cut_num~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <classes>))
  (cl:+ 0
     2
     2
     2
     2
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <classes>))
  "Converts a ROS message object to a list"
  (cl:list 'classes
    (cl:cons ':glass_num (glass_num msg))
    (cl:cons ':long_hair_num (long_hair_num msg))
    (cl:cons ':glass_cut_num (glass_cut_num msg))
    (cl:cons ':long_hair_cut_num (long_hair_cut_num msg))
    (cl:cons ':short_hair_num (short_hair_num msg))
    (cl:cons ':short_hair_cut_num (short_hair_cut_num msg))
))
