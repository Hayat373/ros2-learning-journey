from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # URDF files
        ('share/' + package_name + '/urdf', glob('urdf/*.urdf')),
        
        # Launch files
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hayat',
    maintainer_email='hayahmam3@gmail.com',
    description='Simple robot description for ROS 2 learning journey',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)
