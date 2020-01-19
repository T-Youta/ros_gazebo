#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

# Node name
rospy.init_node("sample")

# Topic   : /mobile_base/commands/velocity
# Type    : Twist
# Options : queue_size=10
pub = rospy.Publisher("/mobile_base/commands/velocity", Twist, queue_size=10)

fb=0.5
lr=1.0
print ("Method of operation  Enter the following command")

# Loop while not shutdown
while not rospy.is_shutdown():
    # construct Twist object
    vel  = Twist()

    # wait user input
    direction = raw_input("f: forward, b: backward, l: left, r: right q: quit > ")

    # commands
    if "f" in direction:
        vel.linear.x = +fb # forward

    if "b" in direction:
        vel.linear.x = -fb # backward

    if "l" in direction:
        vel.angular.z = +lr # rotate left

    if "r" in direction:
        vel.angular.z = -lr # rotate right

    if "q" in direction:
        break # quit program

    # print detail
    #print vel

    # publish
    pub.publish(vel)
