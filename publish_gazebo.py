#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("sample")

pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=10)

# distance of forward,rotate
fb=0.5
lr=1.0
print ("Method of operation  Enter the following command")

# Loop while not shutdown
while not rospy.is_shutdown():
    
    vel  = Twist()

    #input
    direction = raw_input("f: forward, b: backward, l: left, r: right q: quit > ")
    
    if "f" in direction:
        vel.linear.x = +fb # forward

    if "b" in direction:
        vel.linear.x = -fb # backward

    if "l" in direction:
        vel.angular.z = +lr # rotate left

    if "r" in direction:
        vel.angular.z = -lr # rotate right

    if "q" in direction:
        break # quit 

    # publish
    pub.publish(vel)
