# Install script for directory: /home/ucar/ucar_ws/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/ucar/ucar_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ucar/ucar_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/ucar/ucar_ws/install" TYPE PROGRAM FILES "/home/ucar/ucar_ws/build/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ucar/ucar_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/ucar/ucar_ws/install" TYPE PROGRAM FILES "/home/ucar/ucar_ws/build/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ucar/ucar_ws/install/setup.bash;/home/ucar/ucar_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/ucar/ucar_ws/install" TYPE FILE FILES
    "/home/ucar/ucar_ws/build/catkin_generated/installspace/setup.bash"
    "/home/ucar/ucar_ws/build/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ucar/ucar_ws/install/setup.sh;/home/ucar/ucar_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/ucar/ucar_ws/install" TYPE FILE FILES
    "/home/ucar/ucar_ws/build/catkin_generated/installspace/setup.sh"
    "/home/ucar/ucar_ws/build/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ucar/ucar_ws/install/setup.zsh;/home/ucar/ucar_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/ucar/ucar_ws/install" TYPE FILE FILES
    "/home/ucar/ucar_ws/build/catkin_generated/installspace/setup.zsh"
    "/home/ucar/ucar_ws/build/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/ucar/ucar_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/ucar/ucar_ws/install" TYPE FILE FILES "/home/ucar/ucar_ws/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/ucar/ucar_ws/build/gtest/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/audio_common/audio_common/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry/geometry/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/geometry2/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/audio_common/audio_common_msgs/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/navigation/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/aruco_ros/aruco_msgs/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry/eigen_conversions/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry/kdl_conversions/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_msgs/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_bullet/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_eigen/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/audio_common/audio_capture/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/audio_common/audio_play/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/map_server/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_py/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/aruco_ros/aruco/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/darknet_ros/darknet_ros_msgs/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/darknet_ros/darknet_ros/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/robot_voice/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/audio_common/sound_play/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_ros/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry/tf/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/aruco_ros/aruco_ros/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/fdilink_ahrs/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_geometry_msgs/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/amcl/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/fake_localization/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_kdl/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/test_tf2/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_sensor_msgs/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry2/tf2_tools/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/geometry/tf_conversions/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/ucar_cam/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/ucar_controller/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/ucar_map/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/ucar_nav/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/voxel_grid/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/costmap_2d/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/nav_core/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/base_local_planner/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/carrot_planner/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/clear_costmap_recovery/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/dwa_local_planner/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/move_slow_and_clear/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/navfn/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/global_planner/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/rotate_recovery/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/move_base/move_base/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/xf_mic_asr_offline/cmake_install.cmake")
  include("/home/ucar/ucar_ws/build/ydlidar/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/ucar/ucar_ws/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
