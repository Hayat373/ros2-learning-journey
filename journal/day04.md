# Day 4 - Custom Messages, Parameters & Launch Files 
Date: 2026-07-15

## What I Learned
- How to create **custom messages** (.msg files)
- Using **Parameters** in nodes (dynamic configuration)
- Creating **Launch Files** to start multiple nodes easily
- Proper package structure and rebuilding workflow

## What I Did
- Created `NumString.msg` custom message
- Wrote `parameter_publisher.py` node with parameter support
- Created `demo.launch.py` to launch publisher + subscriber together
- Updated `setup.py` and `package.xml`
- Successfully built and ran everything

## Key Commands Used
```bash
# Build
colcon build --packages-select my_first_package --symlink-install
source install/setup.bash

# Run with parameter
ros2 run my_first_package parameter_publisher --ros-args -p greeting:="Hi from Hayat"

# Run with launch file (best way)
ros2 launch my_first_package demo.launch.py
```

## Resources Used

Official ROS 2 Launch Documentation
`resources/core-concepts.md`