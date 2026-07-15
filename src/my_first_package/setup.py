from setuptools import find_packages, setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hayat',
    maintainer_email='hayahmam3@gmail.com',
    description='My first ROS 2 package',
    license='Apache-2.0',
    tests_require=['pytest'],

      
          entry_points={
        'console_scripts': [
            'publisher_node = my_first_package.publisher_node:main',
            'subscriber_node = my_first_package.subscriber_node:main',
        ],
    },
)