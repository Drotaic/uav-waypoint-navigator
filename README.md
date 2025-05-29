# UAV Waypoint Navigator

This project demonstrates how to control a drone using DroneKit and ArduPilot, designed for deployment on Raspberry Pi + Pixhawk. It sends the UAV through a series of GPS waypoints in autonomous mode.

## 🛩️ Use Case
This tool is designed for autonomous navigation missions — e.g., patrolling post-disaster zones or inspecting infrastructure — with commands sent from onboard systems.

## 📡 Features
- Connects to ArduPilot using DroneKit
- Loads GPS coordinates from config
- Arms, takes off, and flies to waypoints
- Returns to launch if instructed

## 📁 Structure
- `scripts/`: Main Python script for waypoint navigation
- `configs/`: Text file with sample mission coordinates
- `notebooks/`: Visual flight planning or simulation
- `assets/`: Example path diagrams or screenshots

## 🔧 Requirements
- DroneKit
- ArduPilot (sim or real)
- Raspberry Pi + Pixhawk (target hardware)

## 🔮 Future Work
- Add obstacle checking
- Integrate with vision triggers
