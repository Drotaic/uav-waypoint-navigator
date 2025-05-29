from dronekit import connect, VehicleMode, LocationGlobalRelative, Command
import time

print("Connecting to vehicle...")
vehicle = connect('127.0.0.1:14550', wait_ready=True)

waypoints = [
    (37.4289, -122.1760, 20),
    (37.4295, -122.1750, 20),
    (37.4290, -122.1740, 20)
]

def arm_and_takeoff(aTargetAltitude):
    print("Arming motors")
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

def fly_waypoints(points):
    for lat, lon, alt in points:
        location = LocationGlobalRelative(lat, lon, alt)
        print(f"Flying to {lat}, {lon} at {alt}m")
        vehicle.simple_goto(location)
        time.sleep(20)

def return_to_launch():
    print("Returning to Launch")
    vehicle.mode = VehicleMode("RTL")

if __name__ == "__main__":
    arm_and_takeoff(20)
    fly_waypoints(waypoints)
    return_to_launch()
    print("Mission complete")
    vehicle.close()
