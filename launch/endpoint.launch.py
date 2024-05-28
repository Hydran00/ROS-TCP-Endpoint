from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument("ip", default_value="0.0.0.0"),
            DeclareLaunchArgument("port", default_value="10000"),
            DeclareLaunchArgument("interface", default_value="enp38s0"),
            Node(
                package="ros_tcp_endpoint",
                executable="default_server_endpoint",
                emulate_tty=True,
                parameters=[{"ROS_IP": LaunchConfiguration("ip")}, 
                            {"ROS_TCP_PORT": LaunchConfiguration("port")},
                            {"interface": LaunchConfiguration("interface")}],
            )
        ]
    )
