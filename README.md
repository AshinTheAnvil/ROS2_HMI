# HMI Interface ROS 2 Node

## Overview

This ROS 2 node provides an HMI interface that displays the state of the robotic cell system in real-time. It collects information on the door state, emergency button status, and stack light status via ROS 2 topics and displays it on a simple web interface built with Flask.

## Features

- **Displays**:
  - The state of the emergency button (pressed or not).
  - The state of the door (open or closed).
  - The state of the stack light (Operational, Paused, Emergency).
  - Pickup and response information (if available).(This has problems in displaying in the HMI, but in terminal I am able to extract the latest id)
  
- **Real-time updates** using Flask with ROS 2 subscription.

## Requirements

- **ROS 2** (Humble)
- **Flask** for web interface


### Install dependencies:
1. **Install Flask**:
    ```bash
    pip install flask
    ```


## Setup

1. **Clone the repository** and navigate into the package directory.

    ```bash
    cd ~/ros2_ws/src
    git clone <repository_url>
    cd <package_name>
    ```

2. **Build the workspace** (if needed):
    ```bash
    cd ~/ros2_ws
    colcon build
    ```

3. **Source the workspace**:
    ```bash
    source ~/ros2_ws/install/setup.bash
    ```

4. **Run the HMI node**:
    ```bash
    ros2 run hmi_interface hmi_interface_node
    ```
5. **Run the other relevant nodes**:
    ```bash
    i.e. the door state, emergency stop and stack light and barcode nodes and check using ros2 topi list.
Video is attached
    ```

---

## Running the Web Interface

Once the node is running, access the HMI interface through a browser
---

## ROS 2 Topics/Subscribers

This node subscribes to the following topics:

- **`/door_state`**: Bool - Represents the state of the door (True for closed, False for open).
- **`/emergency_button_state`**: Bool - Represents whether the emergency button is pressed (True for pressed, False for released).
- **`/stack_light_state`**: Int8 - Represents the state of the stack light (0 for operational, 1 for paused, -1 for emergency).

---



