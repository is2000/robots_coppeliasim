# Road Following in CoppeliaSim: An Introduction to Robotic Navigation

This repository contains the code and documentation for the Embedded Control Lab 3 project on robotic navigation. The project, titled "Road Following in Coppelia Sim: An Introduction to Robotic Navigation," was created by Group 8: Davin Edison, Hatim Sadliwala, Ishita Singh, and Oussema Kassebi. The goal of this lab was to develop an algorithm that enables a simulated robot to follow a designated path in the CoppeliaSim environment.

## Project Overview

The project focuses on **robotic navigation**, a critical component in robotics that involves a robot determining its position and planning movement within an environment. The core of this lab is a **road-following algorithm** that uses computer vision and a proportional controller to guide a simulated robot. The project uses the CoppeliaSim software as a virtual platform to simulate real-world conditions for experimentation and development.

The main components of the project are:
* **Sensor Integration**: The algorithm utilizes simulated vision sensors in CoppeliaSim to detect the path.
* **Computer Vision**: Image processing techniques like color detection, edge detection, or even neural networks are used to process the images from the robot's camera.
* **Control Logic**: A proportional controller adjusts the robot's steering based on its deviation from the path. This is achieved by calculating the center of the image to determine the robot's orientation and then manipulating the motor speeds to keep the robot in the middle of the road.

---

## Repository Structure

The project code is organized into several Python files to improve readability and maintain a robust structure.

.
├── README.md
├── constant.py
├── main_controller.py
├── robot.py
└── utils.py

* `README.md`: The file you are currently reading.
* `constant.py`: This file consists of constant variables for the entire program, including PID control logic parameters like `kp`, `ki`, and `kd`.
* `utils.py`: This file consists of functions for image processing. It is needed to read, process, and make decisions from the images taken from the robot's camera.
* `robot.py`: This file consists of a class for creating instances of robot objects. It includes the initialization of the robot, steering angle calculation, velocity calculation, and an update function.
* `main_controller.py`: This file consists of the main sequence of the code for this project: creating robot objects, starting the simulation, and updating each robot's steering angle and velocity throughout the simulation.

## Requirements

The project requires the following software and libraries:

* **CoppeliaSim (edu version)**: A versatile and powerful 3D robot simulation software. It is a virtual robotic experimentation platform that allows users to create, customize, and control a wide range of robotic models and scenarios.
* **Python 3.x**: The recommended programming language for this project.
* **coppeliasim-zmqremoteapi-client**: The CoppeliaSim Python API is crucial for interfacing with CoppeliaSim from Python scripts. It can be installed using `pip`.
* **NumPy**: This library is needed for numerical operations.
* **OpenCV**: This library is required for image processing.

You can install the necessary Python libraries using `pip`:

```bash
pip install coppeliasim-zmqremoteapi-client numpy opencv-python


## Usage

1.  **Set up the CoppeliaSim environment**: Download and install the educational version of CoppeliaSim from their official website. Load the provided custom scene file, which contains predefined paths and robot models setup for the road following task.
2.  **Ensure Python dependencies are installed**: Use the command above to install the required libraries.
3.  **Run the main controller**: Execute the `main_controller.py` file to start the simulation and control the robots.

The simulation will run for a set time (less than 30 seconds), and the robots will attempt to follow the road using the implemented algorithm.
