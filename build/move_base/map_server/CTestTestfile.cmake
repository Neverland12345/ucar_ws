# CMake generated Testfile for 
# Source directory: /home/ucar/ucar_ws/src/move_base/map_server
# Build directory: /home/ucar/ucar_ws/build/move_base/map_server
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_map_server_gtest_map_server_utest "/home/ucar/ucar_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_ws/build/test_results/map_server/gtest-map_server_utest.xml" "--return-code" "/home/ucar/ucar_ws/devel/lib/map_server/map_server_utest --gtest_output=xml:/home/ucar/ucar_ws/build/test_results/map_server/gtest-map_server_utest.xml")
add_test(_ctest_map_server_rostest_test_rtest.xml "/home/ucar/ucar_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python3" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/ucar/ucar_ws/build/test_results/map_server/rostest-test_rtest.xml" "--return-code" "/opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/ucar/ucar_ws/src/move_base/map_server --package=map_server --results-filename test_rtest.xml --results-base-dir \"/home/ucar/ucar_ws/build/test_results\" /home/ucar/ucar_ws/src/move_base/map_server/test/rtest.xml ")
