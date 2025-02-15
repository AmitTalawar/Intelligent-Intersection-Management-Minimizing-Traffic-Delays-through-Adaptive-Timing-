# 🚦 Intelligent Intersection Management: Minimizing Traffic Delays through Adaptive Timing

## 📌 Project Overview
Traffic congestion at intersections is a critical issue in urban areas, leading to increased delays, fuel wastage, and pollution. Traditional traffic light systems use **fixed-timing mechanisms**, which fail to dynamically adapt to real-time traffic conditions.

This project proposes an **adaptive traffic management system** that dynamically adjusts traffic light durations based on real-time congestion levels. By employing **simulation models** and **machine learning-based vehicle detection**, this system can effectively **reduce waiting times** at intersections.

## 🎯 Objectives
✔️ Develop an **adaptive traffic control algorithm** that dynamically changes green light durations.  
✔️ Simulate **real-world traffic scenarios** using Python (Pygame).  
✔️ Implement **YOLO-based vehicle detection** for real-time traffic monitoring.  
✔️ Compare **adaptive vs. static traffic control** based on performance metrics such as **average waiting time**.  

---

## 🏗️ Project Architecture
This project consists of **three main components**:

1. **Traffic Simulation Model**  
   - Built using **Pygame** to represent a **four-lane intersection**.  
   - Simulates **dynamic traffic flow** by generating vehicles with varying speeds and densities.  
   - Implements **fixed and adaptive traffic light control** mechanisms for comparison.

2. **Adaptive Traffic Algorithm**  
   - Uses real-time **vehicle count** and **lane-wise congestion** to allocate green light dynamically.  
   - Computes **optimal green signal time** based on traffic inflow and outflow rates.  
   - Prevents excessive waiting time in one lane by **balancing** signal durations.

3. **Vehicle Detection & Counting (YOLOv8)**  
   - Uses **YOLOv8** (You Only Look Once) for **real-time vehicle classification and counting**.  
   - Trained on **5,000+ images** for detecting different vehicle types (cars, buses, trucks, bikes).  
   - Provides **accurate vehicle density estimation** for adaptive control.  

---

## 🚀 Features
✅ **Dynamic Traffic Light Control**: Adapts to real-time congestion instead of following pre-defined signal timings.  
✅ **Lane-wise Traffic Optimization**: Allocates green signal to the most congested lane dynamically.  
✅ **YOLO-based Vehicle Detection**: Uses deep learning to detect and count vehicles.  
✅ **Performance Benchmarking**: Compares adaptive control with static signals using **average lane-wise waiting times**.  
✅ **Scalable & Realistic**: Can be extended to **multi-intersection networks** for smart city applications.  

---

## 📊 Methodology

### 1️⃣ Traffic Simulation Model
The simulation replicates a **four-lane intersection** where:
- Vehicles (cars, buses, trucks, bikes) arrive at different **random rates**.
- The **Pygame engine** visualizes traffic flow and signal transitions.
- The **static model** follows **predefined signal times**, while the **adaptive model** dynamically changes signal durations.

### 2️⃣ Adaptive Traffic Control Algorithm
- **Traffic Density Calculation**: Measures vehicle congestion **Vᵢ** in each lane.
- **Lane Selection**: Chooses the most congested lane for **green signal**.
- **Dynamic Green Time Allocation**: Computes optimal green signal duration based on:
  - **Traffic inflow rate (Dᵢ)**  
  - **Outflow rate (β)**  
  - **Queue time constant (α)**  

> **Mathematical Model:**  
> - Next Lane Selection: `Next = argmax(Vᵢ)`  
> - Green Time: `GreenTime = α * Vᵢ`  
> - Traffic Update: `Vᵢ(new) = Vᵢ(old) * (1 + α * Dᵢ - α * β)`

### 3️⃣ Vehicle Detection & Counting (YOLOv8)
- Trained **YOLOv8** on **5,000+ labeled images**.
- Evaluated **precision, recall, and mAP scores** to validate model accuracy.
- Used **Bounding Box Detection** for real-time vehicle counting.

### 4️⃣ Performance Analysis
- Compared **static vs. adaptive traffic control** by measuring:
  - **Lane-wise Average Waiting Time**  
  - **Traffic Flow Efficiency**  
  - **Vehicle Throughput Improvement**  

> **Key Findings:**  
> ✅ Adaptive control **reduced waiting times** significantly.  
> ✅ More **efficient traffic flow** during high congestion periods.  
> ✅ Vehicle detection provided **accurate real-time traffic density estimation**.

For access to dataset please use the following link:
https://drive.google.com/drive/folders/1r_Mutb5PlElaaDyPDtaZipHgl5FdDsLq?usp=sharing
