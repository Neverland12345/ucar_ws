execute_process(COMMAND "/home/ucar/ucar_ws/src/build/move_base/base_local_planner/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/ucar/ucar_ws/src/build/move_base/base_local_planner/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
