import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    urdf_path = '/home/suhail/diff_drive_robot_ws/src/diff_robot_description/urdf/test.urdf'
    try:
        import xacro
        robot_description_config = xacro.process_file(urdf_path)
        robot_desc = robot_description_config.toxml()
    except Exception as e:
        with open(urdf_path, 'r') as infp:
            robot_desc = infp.read()
    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        )
    ])





