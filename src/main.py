#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist 
from nav_msgs.msg import Odometry
import math

def go_to_goal(x_goal,y_goal):
    global x 
    global y
    global yaw

    velocity_msg = Twist()
    cmd_vel_topic = '/cmd_vel'


    while True :
        k_linear = 0.5
        distance = abs(math.sqrt((x_goal-x)**2)+(y_goal-y)**2)
        linear_speed = distance * k_linear

        #k_angular = 0.4
        #desired_angle_goal = math.atan2(y_goal-y,x_goal - x)
        #angular_speed = (desired_angle_goal)*k_angular

        velocity_msg.linear.x = linear_speed
        #velocity_msg.angular.z = angular_speed

        pub.publish(velocity_msg)

        if (distance < 0.0000001):
            break

        


def odom (msg):
    global x 
    global y
    global yaw
    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    yaw = msg.pose.pose.orientation.z
    print ("pose x = " + str(x), x)
    print ("pose y = " + str(y))
    print ("*********************")
    #print ("orientation x = " + str(msg.pose.pose.orientation.x))
    #print ("orientation y = " + str(msg.pose.pose.orientation.y))
    rate.sleep()
    

def twist(msg):
    #print("velocity linear x = " + str(msg.linear.x))
    #print("velocity linear y = " + str(msg.linear.y))
    rate.sleep()

#definition du node "robot_four_monitor" sub(gazebo) pub
rospy.init_node('robot_four_monitor')
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)
sub = rospy.Subscriber('/odom' ,Odometry , odom)
sub2 = rospy.Subscriber('cmd_vel',Twist,twist)
rate = rospy.Rate(0.5)

while not rospy.is_shutdown():
    move = Twist()
    move.linear.x = 0.5 #m/s 
    move.angular.z = 0.5 #rad/s
    pub.publish(move)
    #rospy.spin()
    go = Odometry()
    x_goal= 5
    y_goal= 2
    #go_to_goal(x_goal,y_goal,x,y,yaw)
    rate.sleep()