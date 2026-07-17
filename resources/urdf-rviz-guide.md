
# URDF & RViz Guide - Quick Reference

**Date**: 2026-07-17  
**For**: Future reference

## Common Issues & Solutions

### 1. Robot not visible in RViz
- Set **Fixed Frame** = `base_link`
- Add **RobotModel** display
- Add **TF** display
- Make sure `robot_state_publisher` is running

### 2. "No TF data" Error
- Check that `robot_state_publisher` node is active
- Run `ros2 topic echo /tf --once`

### 3. Good URDF Practices
- Always include `<visual>`, `<collision>`, and `<inertial>` for each link
- Use proper `<origin>` and `<axis>` in joints
- Start simple (box base + cylinders for wheels)

## Useful Commands
```bash
ros2 launch my_robot_description display.launch.py
ros2 node list
ros2 topic list
ros2 topic echo /tf --once
```

