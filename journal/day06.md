# Day 6 - Gazebo Simulation & Teleoperation (Date: 2026-07-17)

## What I Learned
- How to spawn a URDF robot into **Gazebo Harmonic** simulator
- Using `ros_gz_sim` for simulation
- Keyboard teleoperation with `teleop_twist_keyboard`
- Adding Gazebo plugins for physics (DiffDrive)
- Debugging common Gazebo plugin loading issues

## What I Did
- Created `gazebo.launch.py` to launch empty world + robot
- Updated URDF with proper inertial properties and Gazebo plugin
- Successfully spawned the robot in Gazebo
- Attempted to control the robot with arrow keys

## Challenges Faced
- Gazebo plugin (`libgz-sim-diff-drive-system.so`) loading errors
- Robot appears but does not move due to plugin issues
- Fixed basic URDF problems (inertial, joints)

## Key Commands Used
```bash
ros2 launch my_robot_description gazebo.launch.py
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
## Status

- Robot successfully appears in Gazebo
- Teleop node running
- Movement not working yet (plugin issue — will fix in Day 7 with ros2_control)