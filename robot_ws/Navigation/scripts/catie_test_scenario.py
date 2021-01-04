#! /usr/bin/python
import numpy as np
import rospy
import actionlib
import math
from math import radians, degrees

import tf
import traceback
import time
import sys
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from simple_navigation_goals import simple_navigation_goals
from catie_particle_handler import particle_filter_handler

human = 0
pub = rospy.Publisher("/tb3/cmd_vel", Twist, queue_size=10)

#func to for initial emplacment form treatment
def laser_to_image():

	laser_scan = rospy.wait_for_message("/tb3/scan", LaserScan, timeout=None) #request a laser scan
	angle_increment = laser_scan.angle_increment
	angle_min = laser_scan.angle_min
	range_max = 3
	pixel_per_meter = 300
	image_size = range_max*pixel_per_meter
	height = image_size
	width = image_size
	image = np.zeros((height,width,3), np.uint8)
	index = -1 # the 0, 0 point of the laserscan will be drawn on the point x = width/2 and y = 0 (so the top of the image)

	for r in laser_scan.ranges :
		index +=1
		d = 0
		try :
			d = float(r)
			if (np.isnan(d)) :
				continue
		except :
			continue # inf?

		if (d < 0.01 or d >= range_max) :
			continue

		angle = angle_min + index*angle_increment

		x = int(round(width/2 + d*pixel_per_meter*math.sin(angle)))
		y = int(round(d*pixel_per_meter*math.cos(angle)))

		if x >=0 and x < width and y >=0 and y < height :
			image[y, x] = (255, 255, 255) 
			#y, x as always
	        #print(("Adding point {}".format(round(d*math.cos(angle)), round(width/2 + d*math.sin(angle)))))

        return image,pixel_per_meter

#func to for laser filter
def laser_filter():
	
	laser_scan = rospy.wait_for_message("/tb3/scan", LaserScan, timeout=None)
	angle_increment = laser_scan.angle_increment
	angle_min = laser_scan.angle_min
	index =0
	index -=1
	zoi = []
	global human

	#filtering for human ?
	for r in laser_scan.ranges :
		index +=1
		d = 0
		try :
			#print("r = {} \n".format(r))
			d = float(r)
			#print("d = {} \n".format(d))
			if (np.isnan(d)) :
				continue
		except :
			# inf?
			continue
		angle = angle_min + index*angle_increment
		#print("angle = {} \n".format(angle))
		#print("d = {} \n".format(d))
		if (d < 0.8 and d >= 0.3 and angle > -0.5 and angle < 0.5) :
			zoi.append([d, angle])
	print("zoi = {} \n".format(zoi))
	#print("laser_ranges = {} \n".format(laser_scan.ranges))

	d_moy = 0
	angle_moy = 0

    #getting the position of human
	if (len (zoi) == 0):
            print("zoi = 0")
        else:
            for p in zoi :
		    d_moy = d_moy + p[0]
		    angle_moy = angle_moy + p[1]
	    d_moy = float(d_moy) / len(zoi)
	    angle_moy = float(angle_moy) / len(zoi)

	#control loop
	#a modifier
	p_lin = 0.1 
	p_rot = 0.1 

	err_lin = (0.8 - 0.3 )/2 - d_moy
	err_rot = 0 - angle_moy 

	v_lin = p_lin * err_lin
	v_rot = p_rot * err_rot
	print ("vlin=", v_lin," vrot = ",v_rot)

    #TODO : Send command to TB3 like in Teleop
	twist = Twist()

        if (v_lin >= 0.026 or v_lin <=-0.026 and len(zoi)!=0):
             print("human is detected")
             twist.linear.x = v_lin; twist.linear.y = 0.0; twist.linear.z = 0.0
             twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z = v_rot
             human = 1
                
        if ((human == 1) and (len(zoi)==0)) :
             twist.linear.x = 1; twist.linear.y = 0.0; twist.linear.z = 0.0
             if (v_rot < -0.01):
                 v_rot= v_rot+(-0.04)

             elif (v_rot > 0.01):
                v_rot= v_rot + 0.04

             twist.angular.x = 0.0; twist.angular.y = 0.0; twist.angular.z =v_rot

        pub.publish(twist)
	return zoi

#launch node and treat exception
if __name__ == "__main__":

    try:
        rospy.init_node("catie_test_scenario", anonymous =False)

        while True:
	        laser_filter()

        rospy.loginfo("ParticleFilterHandler Initialization")
        particle_handler = particle_filter_handler.ParticleFilterHandler()
        rospy.loginfo("SimpleNavigationGoals Initialization")
        nav_goals = simple_navigation_goals.SimpleNavigationGoals()
        rospy.loginfo("Initializations done")

        # What to do if shut down (e.g. ctrl + C or failure)
        rospy.on_shutdown(nav_goals._shutdown)

        # Setting the assumed initial position of the robot
        particle_handler.reset_particle_cloud_simple(0, 0, 0 * math.pi / 4, x_var=0.5, y_var=0.5, theta_var=math.pi / 6)

        rospy.loginfo("Particles resetted")

        while True:
            if not (nav_goals.go_to(1.5, -2.98, 0)):
                break
            if not (nav_goals.go_to(1.5, -2.98, math.pi / 2)):
                break
            if not (nav_goals.go_to(-2.33, -9.86, 0)):
                break

        rospy.spin()

    except rospy.ROSInterruptException:
        rospy.logerr(traceback.format_exc())

    rospy.loginfo("test terminated.")