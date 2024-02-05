# mobile-robot-ros-cv
This project consist of creating xacro and Gazebo files within the URDF folder of a mobile robot. The objective is to define its mechanical characteristics and position of each component of this Robot, including the chassis, the 4 wheels, and the camera. Additionally, a Python script will be written to define a node for autonomously controlling the robot's movement from point A to point B (in this example I write a python pipeline named "main2.py" in src forlder to put the robot moving from point (0,0) to point (5,5) the return to (0,0).
# define the robot
## tester la camera  

      roslaunch usb_cam usb_cam-test.launch

then 
## Use this command to Open the project in gazebo
  
      roslaunch robot_model_pkg robot_xacro.launch  
      
## use this command to make the robot moving from A to B autonomously
      
      rosrun robot_model_pkg main2.py  

## Use this command to make the robot moving using keyboard

      rosrun teleop_twist_keyboard teleop_twist_keyboard.py

this is the end of the first section which is moving the robot autonomosly the second part consist of adding the Computer Vision part we will use the camera of the mobile robot to detect things. 

# adding the computer vision part

## The camera topic

      rostopic list 
      
as you see here the topic is .../image_raw
if you want to test it do ...
## Test the camera of the mobile robot

      rosrun image_view image_view image:=/robot/camera1/image_raw

## Now, edit in darknet the adress of the camera
Now install the "darknet_ros" package from this git "https://github.com/pushkalkatara/darknet_ros.git" and make it inside src of your project. and you should make some modification so enter to the package "darknet_ros" then enter to the folder "darknet_ros" you will find the file "ros.yaml" inside the folder "config" and change the topic of your camera.

##  Now, let's run the Computer Vision part by executing this command 

      roslaunch darknet_ros darknet_ros.launch

