#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################
# Copyright 2024 Dong Zhaorui. All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2024-09-05
################################################################

from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    # python_template
    python_template_param_path = FindPackageShare('hex_python_template').find(
        'hex_python_template') + '/config/ros2/params.yaml'
    python_template_node = Node(package='hex_python_template',
                                executable='python_template',
                                name='python_template',
                                output="screen",
                                emulate_tty=True,
                                parameters=[python_template_param_path],
                                remappings=[
                                    ('in_str', 'in_str'),
                                    ('in_int', 'in_int'),
                                    ('out_str', 'out_str'),
                                    ('out_int', 'out_int'),
                                ])

    return LaunchDescription([
        python_template_node,
    ])
