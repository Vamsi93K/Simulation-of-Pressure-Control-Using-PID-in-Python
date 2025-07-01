# Simulation-of-Pressure-Control-Using-PID-in-Python
##🚰 Water Pressure Control System using PID Controller (Python)
This project simulates a basic PID (Proportional–Integral–Derivative) controller to manage water pressure in a system using a virtual solenoid valve. It logs real-time pressure data and visualizes how the valve responds over time.
🎓 Created as part of my learning journey into Python control systems and real-time simulations.
##📌 Project Overview
- 🧠 Implements a PID controller in Python
- 🌡️ Simulates real-time water pressure readings
- 🔁 Controls a valve based on PID output
- 📊 Visualizes pressure and valve behavior using matplotlib

##⚙️ How It Works
- User inputs PID constants (Kp, Ki, Kd) and target pressure.
- The simulation runs for a defined number of seconds.
- At each time step:
- A pressure sensor reading is simulated.
- The PID controller calculates the error and produces a control signal.
- The valve opens/closes based on that signal.
- Finally, data is plotted to show how pressure evolves and how the valve behaves.

##🛠️ Requirements
- Python 3.x
- Required libraries:
pip install matplotlib numpy



##🚀 Running the Code
python file_name.py


##The script will prompt for:
- Kp, Ki, Kd (PID parameters)
- Desired pressure setpoint
- Simulation duration
Leave empty to use default values.

##📈 Output Sample
- Terminal prints each second's pressure, PID output, and valve state.
- At the end, you’ll see a graph like this:
[05s] Pressure: 4.63 psi | PID: 0.27 | Valve: OPEN
...


##Plot includes:
- Real-time pressure values (line with markers)
- Valve state (0 = CLOSED, 1 = OPEN)
- Setpoint reference line

##🎯 Learning Goals
- Understand basic PID logic
- Simulate sensor-controlled systems
- Practice data visualization in Python
- Build confidence with classes and loops

##📚 References
- Wikipedia – PID Controller
- Python matplotlib documentation
- Control systems examples from academic tutorials
If you liked this project or found it useful, feel free to ⭐️ this repo or give feedback!
