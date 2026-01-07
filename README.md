# VR Behavior Data Pipeline

This repository presents a simplified data processing workflow designed for VR-based behavioral experiments, with a focus on behavioral feature engineering and reproducible data logic.

## Background
The project is inspired by my work on VR consumer behavior research, where participant sessions included multiple data sources such as eye-tracking logs, interaction events, and session metadata collected separately.  
A single session often required reconstructing timelines and deriving interpretable behavioral features from raw sensor data.

For the experimental procedure, please click the image below to download and watch the video.

[![Watch the video](https://github.com/Sandoich/VR-behavior-data-pipeline/releases/download/v1.0_demo_video/cover.png)](https://github.com/Sandoich/VR-behavior-data-pipeline/releases/download/v1.0_demo_video/demo_first_person.mp4)


## What I did
- Designed modular Python functions for VR behavioral feature extraction
- Implemented angular kinematics (velocity and acceleration) from rotation data
- Built logic to detect and merge stationary (pause) intervals based on motion thresholds
- Emphasized clear data assumptions, reproducibility, and readable data pipelines

## Skills & Technologies
- Python  
- Behavioral and eye-tracking data  
- Feature engineering  
- Data validation and preprocessing  
- Research-oriented data workflows  

## Notes
This repository focuses on data logic and workflow design.  
The original VR environments and raw study data are not included.  
Data schemas and metadata handling are illustrated directly in the code through documented input assumptions and synthetic examples.

## Quick Start
Run the example scripts to explore the feature extraction pipeline:

python scripts/demo_behavior_features.py  
python scripts/demo_stop_detection.py  

## Core Modules
src/vr_behavior/kinematics.py  
Compute angular velocity and angular acceleration from VR rotation data.

src/vr_behavior/stop_detection.py  
Detect and merge stationary (pause) intervals based on motion thresholds.

## Repository Structure
docs/  
- project_overview.md — overview of the original VR experiment and pipeline context  

src/vr_behavior/  
- kinematics.py — core kinematic feature extraction  
- stop_detection.py — stationary interval detection logic  

scripts/  
- demo_behavior_features.py — runnable example for kinematic features  
- demo_stop_detection.py — example pipeline for stop detection  
