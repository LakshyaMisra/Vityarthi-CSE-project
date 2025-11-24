import math

G = 9.81  

# 1. FUNCTIONAL MODULE: INPUT & VALIDATION 
def get_launch_parameters():
   
    print("\n--- Projectile Trajectory Simulator (Setup) ---")
    
    while True:
        try:
           
            v0 = float(input("Enter initial velocity (m/s): "))
            if v0 <= 0:
                print("Error: Velocity must be a positive value.")
                continue

            angle_deg = float(input("Enter launch angle (degrees, 0-90): "))
            if not (0 <= angle_deg <= 90):
                print("Error: Angle must be between 0 and 90 degrees.")
                continue

            return v0, angle_deg
            
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

# 2. FUNCTIONAL MODULE: CORE CALCULATION
def calculate_flight_metrics(v0, angle_deg):
   
    angle_rad = math.radians(angle_deg)
    
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)

    time_of_flight = (2 * v0y) / G
    
    range_value = v0x * time_of_flight
    
    return time_of_flight, range_value, v0x, v0y

# 3. FUNCTIONAL MODULE: SIMULATION & REPORTING 
def generate_trajectory_data(v0x, v0y, time_of_flight, dt=0.5):
   
    print("\n--- Calculated Trajectory (t, x, y, Angle) ---")
    print("Time (s) | Horizontal (x, m) | Vertical (y, m) | Angle (degrees)")
    print("-----------------------------------------------------------------")
    
    t = 0.0
    
    while t <= time_of_flight:

        x = v0x * t
        y = v0y * t - 0.5 * G * (t**2)
        
        vx = v0x
        vy = v0y - G * t
        
        if vx != 0:
            gamma_rad = math.atan2(vy, vx)
            gamma_deg = math.degrees(gamma_rad)
        else: 
            gamma_deg = 90.0

        if y < 0 and t > 0:
            y = 0.0
            gamma_deg = -math.degrees(math.acos(v0x / math.sqrt(v0x**2 + (-v0y)**2))) 
            
        print(f"{t:8.2f} | {x:17.2f} | {y:13.2f} | {gamma_deg:14.2f}")
        
        t += dt

    if round(t - dt, 2) != round(time_of_flight, 2):
        x_final = v0x * time_of_flight
        y_final = 0.0
        
        final_angle_rad = math.atan2(-v0y, v0x)
        final_angle_deg = math.degrees(final_angle_rad)
        
        print(f"{time_of_flight:8.2f} | {x_final:17.2f} | {y_final:13.2f} | {final_angle_deg:14.2f} (End)")


# MAIN EXECUTION LOGIC 
def main():
    
    while True:
        try:
            v0, angle_deg = get_launch_parameters()
        except TypeError:
            continue
            
        time_of_flight, range_value, v0x, v0y = calculate_flight_metrics(v0, angle_deg)
        
        print("\n--- Summary Results ---")
        print(f"Initial Velocity: {v0:.2f} m/s")
        print(f"Launch Angle:     {angle_deg:.2f} degrees")
        print(f"Total Time of Flight (T): {time_of_flight:.2f} seconds")
        print(f"Total Range (R):          {range_value:.2f} meters")

        generate_trajectory_data(v0x, v0y, time_of_flight)

        while True:
            choice = input("\nRun another simulation? (y/n): ").lower().strip()
            if choice == 'n':
                print("Exiting simulator. Goodbye!")
                return  
            elif choice == 'y':
                print("\n--- Starting New Simulation ---")
                break 
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")


if __name__ == "__main__":

    main()
