import time
import random
import numpy as np
import matplotlib.pyplot as plt


# PID Controller Class

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, setpoint, measured_value):
        error = setpoint - measured_value
        self.integral += error
        derivative = error - self.prev_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.prev_error = error
        return output

#Input

def get_float(prompt, default):
    try:
        return float(input(prompt) or default)
    except ValueError:
        print("Invalid input. Using default:", default)
        return default

Kp = get_float("Enter Kp (default 0.85): ", 0.85)
Ki = get_float("Enter Ki (default 0.12): ", 0.12)
Kd = get_float("Enter Kd (default 0.08): ", 0.08)
setpoint = get_float("Enter desired pressure setpoint in psi (default 5.0): ", 5.0)
SIM_DURATION = int(get_float("Enter simulation duration in seconds (default 60): ", 60))

valve_open = False


# Simulate Pressure Sensor

def simulate_pressure():
    return round(4.5 + random.uniform(-0.3, 0.3), 2)


# Solenoid Valve Logic

def control_valve(pid_output):
    global valve_open
    if pid_output > 0.5:
        valve_open = True
    elif pid_output < -0.5:
        valve_open = False
    return valve_open


# Initialize PID Controller

pid = PIDController(Kp, Ki, Kd)
pressure_log = []
valve_log = []

print("\nStarting simulation...\n")


# Main Loop

for t in range(SIM_DURATION):
    pressure = simulate_pressure()
    control_signal = pid.compute(setpoint, pressure)
    valve_state = control_valve(control_signal)

    print(f"[{t+1:02d}s] Pressure: {pressure} psi | PID: {control_signal:.2f} | Valve: {'OPEN' if valve_state else 'CLOSED'}")

    pressure_log.append(pressure)
    valve_log.append(1 if valve_state else 0)

    time.sleep(1)


# Visualization

plt.figure(figsize=(10, 5))
plt.plot(pressure_log, label="Pressure (psi)", marker='o')
plt.plot(valve_log, label="Valve State (1=Open)", linestyle='--', alpha=0.6)
plt.axhline(y=setpoint, color='r', linestyle=':', label="Setpoint")
plt.title("Water Pressure & Valve Control Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Pressure / Valve")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
