from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_share = get_package_share_directory('my_robot_description')
    urdf_file = os.path.join(pkg_share, 'urdf', 'simple_robot.urdf')
    controllers_file = os.path.join(pkg_share, 'config', 'diff_controller.yaml')

    return LaunchDescription([
        # Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                get_package_share_directory('ros_gz_sim'),
                '/launch/gz_sim.launch.py'
            ]),
            launch_arguments={'gz_args': '-r empty.sdf'}.items()
        ),

        # Robot State Publisher
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),

        # Spawn robot
        Node(
            package='ros_gz_sim',
            executable='create',
            arguments=['-topic', '/robot_description', '-name', 'simple_robot'],
            output='screen'
        ),

        # ros2_control node
        Node(
            package='controller_manager',
            executable='ros2_control_node',
            parameters=[{'robot_description': open(urdf_file).read()}, controllers_file],
            output='screen'
        ),

        # Load controller
        Node(
            package='controller_manager',
            executable='spawner',
            arguments=['diff_drive_controller', '--controller-ros-args', '--activate'],
            output='screen'
        ),
    ])