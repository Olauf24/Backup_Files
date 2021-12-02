from time import sleep
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math
from turtlesim.srv import SetPen
from dual_mc33926_rpi import motors
from gpiozero import PhaseEnableRobot

def forward():
    motors.motor1.setSpeed(250)
    motors.motor2.setSpeed(250)
    
def turn_left_90():
    motors.motor1.setSpeed(250)
    motors.motor2.setSpeed(-250)
    
def main(args=None):
    rclpy.init(args=args)
    
    node = rclpy.create_node('Turtle_painter')
    cli = node.create_client(SetPen, 'turtle1/set_pen')
    
    req = SetPen.Request()
    req.g = 255
    req.width = 5
    req.off = 1
    
    future = cli.call_async(req)
    
    publisher = node.create_publisher(Twist, 'turtle1/cmd_vel', 10)
    
    msg = Twist()
    
    i = 0
    msg.angular.z = (math.pi / 2.0)
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 2.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = (math.pi / 2.0)
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 4.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = (math.pi / 2.0)
    publisher.publish(msg)
    sleep(1)
    
    req.off = 0
    future = cli.call_async(req)
    
    msg.angular.z = 0.0
    msg.linear.x = 5.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = (math.pi / 2.0)
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 2.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = (math.pi / 2.0)
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 5.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = ((3 * math.pi) / 2.0)
    publisher.publish(msg)
    sleep(1)
    
    req.off = 1
    future = cli.call_async(req)
    
    msg.angular.z = 0.0
    msg.linear.x = 3.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = math.pi
    publisher.publish(msg)
    sleep(1)
    
    req.off = 0
    future = cli.call_async(req)
    
    msg.angular.z = 0.0
    msg.linear.x = 2.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = (math.pi / 2.0)
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 5.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = (math.pi / 2.0)
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 2.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = 0.0
    publisher.publish(msg)
    sleep(1)
    
    req.off = 1
    future = cli.call_async(req)
    
    msg.linear.x = 1.0
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = math.pi / 2.25
    publisher.publish(msg)
    sleep(1)
    
    req.off = 0
    future = cli.call_async(req)
    
    msg.angular.z = 0.0
    msg.linear.x = 5.1
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = ((10.0 * math.pi) / 9.0)
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 5.1
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = math.pi
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 2.55
    publisher.publish(msg)
    sleep(1)
    msg.linear.x = 0.0
    msg.angular.z = math.pi / 2.25
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 1.0
    publisher.publish(msg)
    sleep(1)
    
    req.off = 1
    future = cli.call_async(req)
    
    msg.linear.x = 0.0
    msg.angular.z = ((11.0 * math.pi) / 6.0)
    publisher.publish(msg)
    sleep(1)
    msg.angular.z = 0.0
    msg.linear.x = 8.0
    publisher.publish(msg)
    sleep(1)
    
if __name__ == '__main__':
        main()