from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument('drone_id', default_value='drone0'),
        DeclareLaunchArgument('log_level', default_value='info'),
        Node(
            package='trajectory_generator',
            executable='trajectory_generator_node',
            name='trajectory_generator',
            namespace=LaunchConfiguration('drone_id'),
            output='screen',
            arguments=['--ros-args', '--log-level',
                       LaunchConfiguration('log_level')],
            emulate_tty=True
        )
    ])