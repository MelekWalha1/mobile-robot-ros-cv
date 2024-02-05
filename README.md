# mobile-robot-ros-cv
this project consist of creating a xacro and gazebo fils in URDF folder of a mobile robot with identifing it's mecanical caracteristics and positioning every component of the robot the chassi, the 4 wheels and the camera. In addition, writing a script in python to define a node for controling autonomosly the robot from point A to point B.
## tester la camera  

      roslaunch usb_cam usb_cam-test.launch

then 
  
      roslaunch robot_model_pkg robot_xacro.launch  
      
      rosrun robot_model_pkg main2.py  
and run  

      rosrun teleop_twist_keyboard teleop_twist_keyboard.py

2/rosrun image_view image_view image:=/robot/camera1/image_raw

#tod5ol ll file ros.yaml tbedel el topic mta3 l camera
3/roslaunch darknet_ros darknet_ros.launch

#t7eb ettastih od5ol ll "ielson" wzid chais
