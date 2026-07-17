# Day 5 - Robot Modeling with URDF & Visualization in RViz (Date: 2026-07-17)

## What I Learned
- How to create a basic robot model using **URDF** (Unified Robot Description Format)
- Structure of URDF: Links, Joints, Visual, Collision
- Using `robot_state_publisher` to publish the robot description
- Visualizing the robot in **RViz**
- Common debugging techniques (Fixed Frame, TF display, RobotModel)

## What I Did
- Created new package `my_robot_description`
- Built a simple differential-drive robot with base + 2 wheels
- Created `display.launch.py` to launch `robot_state_publisher` + RViz
- Successfully launched and visualized the robot in RViz (after fixing TF/Fixed Frame issues)

## Challenges Faced
- Robot not appearing in RViz initially
- "No TF data" error
- Fixed by adding **RobotModel** + **TF** displays and setting Fixed Frame to `base_link`

## Key Commands
```bash
colcon build --packages-select my_robot_description --symlink-install
ros2 launch my_robot_description display.launch.py
```
