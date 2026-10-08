timeout 6 ros2 topic pub -r  10  /cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.5}}' >> /dev/null
ros2 topic pub --once  /cmd_vel geometry_msgs/msg/Twist '{}' >> /dev/null
ros2 topic echo /odom --field pose.pose.position.x --once
