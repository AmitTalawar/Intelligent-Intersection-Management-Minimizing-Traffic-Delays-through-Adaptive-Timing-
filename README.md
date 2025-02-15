# Intelligent Intersection Management: Minimizing Traffic Delays through Adaptive Timing

## Project Overview

This project focuses on developing an **adaptive traffic signal control system** to **reduce congestion and minimize waiting times** at intersections. Traditional traffic lights operate on fixed timing, which often leads to inefficiencies in handling real-time traffic fluctuations. Our approach employs **dynamic signal adjustments** based on real-time vehicle counts and congestion levels.

Using **simulation techniques** and **machine learning models** for vehicle detection and counting, this project aims to enhance **urban traffic management** by optimizing signal timing dynamically.

## Features

- **Adaptive Traffic Signal Algorithm**: Dynamically allocates green light time based on real-time congestion data.
- **Intersection Simulation**: A **pygame-based** simulation environment to model traffic scenarios.
- **Vehicle Detection & Counting**: Utilizes **YOLOv8** for real-time vehicle detection, classification, and counting.
- **Performance Analysis**: Compares adaptive signal control with static signal timings using lane-wise average waiting times.

## Methodology

### 1. **Traffic Junction Simulation**
- A four-way intersection is simulated using **pygame**.
- Each road has an **incoming** and **outgoing** lane.
- Vehicles include **cars, buses, trucks, and bikes**, with different movement speeds.
- **Traffic signals operate dynamically**, adjusting to real-time congestion.

### 2. **Adaptive Traffic Signal Algorithm**
- **Green Light Selection**: The lane with maximum congestion is chosen for a green signal.
- **Dynamic Timing Calculation**:
  - Green time = `α * vehicle_count`
  - Vehicles are dynamically **added** (incoming traffic) and **removed** (outflow).
- **Control Variables**:
  - `Traffic Density` (Inflow Rate)
  - `Outflow Constant (β)`
  - `Queue Time Constant (α)`
- **Mathematical Model**: Traffic updates occur at each iteration, ensuring smooth flow and **optimized signal control**.

### 3. **Vehicle Detection & Counting**
- YOLOv8-based **object detection model** trained on traffic datasets.
- **Bounding box detection** enables vehicle counting for real-world integration.
- Trained on **5,000+ images**, achieving **mAP50 scores of 0.6 to 0.7** after 20 epochs.

## Results

- **Significant reduction** in lane-wise waiting times using adaptive control vs. static signals.
- **YOLOv8 model** effectively detects vehicles despite image quality limitations.
- **Dynamic adjustments** successfully respond to fluctuating traffic conditions.

## Technologies Used

- **Python**
- **Pygame** (for simulation)
- **OpenCV & YOLOv8** (for vehicle detection)
- **NumPy, Matplotlib** (for data analysis)
- **Machine Learning** (model training & optimization)

## Future Work

- **Real-world deployment** using live traffic camera feeds.
- **Integration with IoT sensors** for enhanced real-time decision-making.
- **Further optimization** of control variables to reduce congestion even further.

## Contributors

- **Amit Appanna Talawar**
- **Anant Terkar**
- **Udit Jain**
- **Rahul Pentamsetty**

## Acknowledgments

This project was developed under the guidance of:
- **Dr. Prabhu Prasad B M** (Asst. Prof., Dept. of Computer Science and Engineering)
- **Dr. Manjunath K V** (Asst. Prof., Dept. of Data Science and Intelligent Systems)
- **Indian Institute of Information Technology Dharwad**

For access to dataset please use the following link:
https://drive.google.com/drive/folders/1r_Mutb5PlElaaDyPDtaZipHgl5FdDsLq?usp=sharing
