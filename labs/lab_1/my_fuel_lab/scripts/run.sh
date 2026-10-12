source /opt/ros/jazzy/setup.bash
source ./labs/lab_1/install/setup.sh
ros2 run ros_gz_bridge parameter_bridge --ros-args -p config_file:=labs/lab_1/my_fuel_lab/config/bridge.yaml &
ros2 bag record /odom &
(gz sim -r ./labs/lab_1/my_fuel_lab/worlds/myworld.sdf) &
ros2 run rviz2 rviz2 &
sleep 1
timeout 6 ros2 topic pub -r  10  /cmd_vel geometry_msgs/msg/Twist '{linear: {x: 0.5}}'
ros2 topic pub --once  /cmd_vel geometry_msgs/msg/Twist '{}' >> /dev/null
ros2 topic echo /odom --field pose.pose.position.x --once
ros2 run teleop_twist_keyboard teleop_twist_keyboard