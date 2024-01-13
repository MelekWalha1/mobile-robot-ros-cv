#!/usr/bin/env python3

import rospy
from nav_msgs.msg  import Odometry
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point
from math import atan2 , sqrt 

x= 0.0
y = 0.0
theta = 0.0

def newOdom(msg):
    global x
    global y
    global theta
    x= msg.pose.pose.position.x 
    y= msg.pose.pose.position.y 
    
    rot_q = msg.pose.pose.orientation
    (roll , pitch , theta) = euler_from_quaternion([rot_q.x,rot_q.y,rot_q.z,rot_q.w])


rospy.init_node("speed_controller")
sub = rospy.Subscriber("/odom",Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel",Twist, queue_size = 1)

r = rospy.Rate(4)

speed = Twist()

goal = Point()
goal.x = 5.0
goal.y = 5.0

while(not rospy.is_shutdown()):
    inc_x = goal.x - x
    inc_y = goal.y - y

    distance = sqrt(inc_x**2 + inc_y**2)

    ang_to_goal = atan2(inc_y,inc_x)

    if abs(ang_to_goal - theta)> 0.2:
        speed.linear.x = 0.0
        speed.angular.z = 0.3
        print("-------------------")
        print ("ang_to_goal = " , ang_to_goal)
        print ("theta = " , theta )
        print("la difference est ) ",abs(ang_to_goal - theta))
    else:
        if (distance > 0.1):
            linear_speed = distance * 0.5
            speed.linear.x = linear_speed
            speed.angular.z = 0.0
        else :
            speed.angular.z = 0.0
            speed.linear.x = 0.0
            print("x = " , x)
            print("y = ",y)
            print("theta = ",theta)
            print("------finish-------------")
            goal.x = 0
            goal.y = 0
        
    pub.publish(speed)
    r.sleep()
speed.angular.z = 0.0
speed.linear.x = 0.0
pub.publish(speed)
r.sleep()