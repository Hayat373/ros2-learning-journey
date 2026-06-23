# ROS 2 Core Concepts - Beginner Guide

**Date**: 2026-06-23 (Day 2)  
**ROS Version**: Jazzy Jalisco  
**Part of**: [ros2-learning-journey](https://github.com/Hayat373/ros2-learning-journey)

This file explains the fundamental concepts you encountered on Day 2 with **Turtlesim**.

## 1. Nodes
- A **Node** is an executable process that performs a specific task.
- In ROS 2, everything runs as nodes (sensors, controllers, planners, etc.).
- Nodes communicate with each other.
- **CLI Commands**:
  ```bash
  ros2 node list
  ros2 node info /turtlesim
  ```

  Real-world example: One node reads camera data, another controls motors.
## 2. Topics

- Topics are named channels (like message buses) where nodes publish or subscribe to data.
- Communication is publish/subscribe (many-to-many).
Messages are sent over topics (e.g., /turtle1/cmd_vel, /turtle1/pose).

### Key Commands:
``` bash
ros2 topic list
ros2 topic list -t          # Show message types
ros2 topic echo /turtle1/pose
ros2 topic info /turtle1/cmd_vel
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.0}, angular: {z: 0.5}}" --once
```
## 3. Messages

- Messages are the data structures sent over topics (e.g., geometry_msgs/msg/Twist for velocity).


## 4. Services (Request/Response)

- Used for one-time actions (like "set pen color" in turtlesim).
Synchronous (wait for reply).

``` bash
ros2 service list
ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 255, g: 0, b: 0, width: 3}"
```
## 5. Parameters

- Configuration values for nodes (speed, thresholds, etc.).

```bash
ros2 param list
ros2 param get /turtlesim background_r
```
## 6. ROS 2 Graph

- Visualization of all nodes and how they are connected.

``` bash
rqt_graph   # (install with: sudo apt install ros-jazzy-rqt-graph)
```