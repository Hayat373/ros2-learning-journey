# Gazebo Harmonic Guide - Quick Reference (ROS 2 Jazzy)

**Date**: 2026-07-17

## Common Issues & Solutions

### 1. Robot appears but doesn't move
- Plugin loading error → Use `ros2_control` + `gz_ros2_control` (recommended)
- Check joint names match exactly in URDF

### 2. Plugin Errors
```xml
<!-- Correct plugin syntax -->
<gazebo>
  <plugin name="diff_drive" filename="libgz-sim-diff-drive-system.so">
    <interface>gz::sim::systems::DiffDrive</interface>
    ...
  </plugin>
</gazebo>
```

### 3. Useful Commands
``` Bash 
ros2 launch my_robot_description gazebo.launch.py
ros2 run teleop_twist_keyboard teleop_twist_keyboard

# Check topics
ros2 topic list
ros2 topic echo /cmd_vel
```
### 4. Best Practices

- Always add <inertial> to every link
- Use Xacro for cleaner code (Day 7+)
- Prefer ros2_control over direct Gazebo plugins for complex robots

### Learning Resources

- Official: https://gazebosim.org/docs/harmonic
- ROS 2 + Gazebo: https://docs.ros.org/en/jazzy/Tutorials/Advanced/Simulation/Gazebo.html
- ros2_control documentation