cmake_minimum_required(VERSION 2.8.3)
project(iros)

set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_CXX_FLAGS "-std=c++11")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -Wall -g -m64")
set(CMAKE_CXX_LINKER_PREFERENCE "-Wl")

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  nav_msgs
  sensor_msgs
  roscpp
  rospy
  rosbag
  std_msgs
  image_transport
  cv_bridge
  tf
)

find_package(Eigen3 REQUIRED)
find_package(OpenCV REQUIRED)
find_package(Ceres REQUIRED)
find_package(Sophus REQUIRED)

find_package(PCL REQUIRED)
message(STATUS "***** PCL version: ${PCL_VERSION} *****")

include_directories(
  ${catkin_INCLUDE_DIRS} 
  ${PCL_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
  ${CERES_INCLUDE_DIRS}
  ${Sophus_INCLUDE_DIRS}
  )

catkin_package(
  CATKIN_DEPENDS geometry_msgs nav_msgs roscpp rospy std_msgs
  DEPENDS EIGEN3 PCL OpenCV
)

add_executable(kdtree src/kdtree.cpp ${catkin_INCLUDE_DIRS})
target_link_libraries(kdtree ${catkin_LIBRARIES} ${PCL_LIBRARIES})
