#!/usr/bin/env python
import rospy
import numpy as np

from jsk_recognition_msgs.msg import BoundingBox, BoundingBoxArray

class DaishaBox:

    def __init__(self):
        self.pub_box = rospy.Publisher("/daisha_box", BoundingBox, queue_size=10)
        rospy.init_node("daisha_box_publisher", anonymous=True)
        rospy.Subscriber("/HSI_color_filter_blue/boxes", BoundingBoxArray, self.publish_box)
        rospy.spin()

    def publish_box(self, msg):
        filtered_boxes = []
        filtered_dimension_x = []
        for box in msg.boxes:
            filtered_dimension_x.append(box.pose.position.x)
        if filtered_dimension_x:
            msg_box = BoundingBox(header=msg.header)
            self.pub_box.publish(msg.boxes[np.argmin(filtered_dimension_x)])

if __name__ == '__main__':
    ins = DaishaBox()

