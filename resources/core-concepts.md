# ROS 2 Core Concepts - Beginner Guide

**Date**: 2026-07-15  
**ROS Version**: Jazzy Jalisco  
**Repository**: [ros2-learning-journey](https://github.com/Hayat373/ros2-learning-journey)

This document provides a clear and formal explanation of the fundamental ROS 2 concepts introduced during early tutorials using the **Turtlesim** simulator.

## 1. Nodes

A **Node** is the basic executable unit in ROS 2. It is a process that performs a specific computation or task.

- Nodes are the building blocks of any ROS 2 system.
- Each node can publish data, subscribe to data, provide services, and manage parameters.
- A complete robot system usually consists of many interacting nodes.

**Common CLI Commands**:
```bash
ros2 node list                    # List all active nodes
ros2 node info /turtlesim         # Detailed information about a node
```
Real-world analogy: A camera node publishes images, a navigation node subscribes to them and publishes motor commands.

## 2. Topics
Topics are named communication channels that enable asynchronous data exchange between nodes using the publish-subscribe model.

One or more publishers can send messages to a topic.
One or more subscribers can receive those messages.
This decouples producers and consumers of data.

Key Commands:

```
ros2 topic list                   # List all active topics
ros2 topic list -t                # List topics with message types
ros2 topic echo /turtle1/pose     # Display live messages on a topic
ros2 topic info /turtle1/cmd_vel  # Information about a specific topic
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}" --once
```

## 3. Messages
Messages are structured data types used for communication over topics and services.

ROS 2 includes many standard message types (e.g., geometry_msgs/msg/Twist for velocity, sensor_msgs/msg/Image for camera data).
You can also define custom messages.

## 4. Services
Services provide synchronous (request-response) communication.

A service server waits for requests and sends back a response.
Used for actions that need immediate feedback (e.g., "turn on camera", "set pen color").

Common Commands:
```bash
ros2 service list
ros2 service call /turtle1/set_pen turtlesim/srv/SetPen "{r: 255, g: 0, b: 0, width: 3}"
```
## 5. Parameters
Parameters allow runtime configuration of nodes without changing code.

Nodes can declare, get, and set parameters.
Useful for tuning values like speeds, thresholds, or modes.

Commands:
``` bash 
ros2 param list
ros2 param get /turtlesim background_r
ros2 param set /turtlesim background_r 100
```
## 6. ROS 2 Graph & Visualization Tools

The ROS 2 Graph shows the connectivity between nodes, topics, and services.
Tool:
```bash 
sudo apt install ros-jazzy-rqt-graph
rqt_graph
```
## 7. Launch Files
Launch Files are used to start multiple nodes (and configure parameters) with a single command.

They improve reproducibility and organization.
Written in Python (.launch.py files).
Can launch nodes, set parameters, remap topics, etc.

