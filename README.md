# mobile-robot-ros-cv
This project consist of creating xacro and Gazebo files within the URDF folder of a mobile robot. The objective is to define its mechanical characteristics and position of each component of this Robot, including the chassis, the 4 wheels, and the camera. Additionally, a Python script will be written to define a node for autonomously controlling the robot's movement from point A to point B (in this example I write a python pipeline named "main2.py" in src forlder to put the robot moving from point (0,0) to point (5,5) the return to (0,0).
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

## Test the camera of the mobile robot

      rosrun image_view image_view image:=/robot/camera1/image_raw

#tod5ol ll file ros.yaml tbedel el topic mta3 l camera
3/roslaunch darknet_ros darknet_ros.launch

#t7eb ettastih od5ol ll "ielson" wzid chais
