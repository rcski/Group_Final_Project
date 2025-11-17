def malfunction_detection(thrust_values):
    """
    Checks input thrust values and angles for each thruster against set limits.
    If a thruster is outside of these limits, it prints a message.
    """
# Create limits for thruster values to be compared against, these are in ALL_CAPS to indicate they are constants and will not change
    THRUST_LIMIT = 100  # Thrust limit in Newtons
    FLOW_RATE = 0.05  # Flow rate limit in kg/s
    EXHAUST_VELOCITY = 2000 # Exhaust velocity limit in m/s

# Initialize the thruster being compared and eventually be increased after each iteration of the for loop
    thruster_Number = 1

# Iterate through each thruster's values (since each item in the list is a tuple, we need to initialize them individually)
    for flowRate, exhaustVelocity, thrust in thrust_values:

        # Print to indicate which thruster is being checked
        print(f"Checking Thruster {thruster_Number}:")

        # Calculate thrust to use in malfunction detection
        thrust = flowRate * exhaustVelocity 

        # Check if any of the thruster values exceed their limits
        if flowRate > FLOW_RATE:
            print(f"  Thruster {thruster_Number} Malfunction detected: Flow rate {flowRate} kg/s exceeds limit of {FLOW_RATE} kg/s by {flowRate - FLOW_RATE} kg/s.")
        elif flowRate <= 0:
            print(f"  Thruster {thruster_Number} Malfunction detected: No flow rate detected.")
        elif exhaustVelocity > EXHAUST_VELOCITY:
            print(f"  Thruster {thruster_Number} Malfunction detected: Exhaust velocity {exhaustVelocity} m/s exceeds limit of {EXHAUST_VELOCITY} m/s by {exhaustVelocity - EXHAUST_VELOCITY} m/s.")   
        elif exhaustVelocity <= 0:
            print(f"  Thruster {thruster_Number} Malfunction detected: No exhaust velocity detected.")
        elif thrust > THRUST_LIMIT:
            print(f"  Thruster {thruster_Number} Malfunction detected: Thrust {thrust} N exceeds limit of {THRUST_LIMIT} N by {thrust - THRUST_LIMIT} N.")
        elif thrust <= 0:
            print(f"  Thruster {thruster_Number} Malfunction detected: No thrust detected.")
        else:
            print(f"  Thruster {thruster_Number} GOOD!.")

        # increase thruster number for next iteration to indicate which thruster is being checked
        thruster_Number += 1
    pass

def velocity_change_calculation(mass_flow_rate, exhaust_velocity, time_elapsed):
    """
    Performs calculations to determine the change in velocity resulting from a maneuver event.
    """
    # Create constant for spacecraft mass
    SPACECRAFT_MASS = 500  # Mass of the spacecraft in kg
    
    # IMPORTANT! this is needed to calculate thrust for malfunction detection
    thrust = mass_flow_rate * exhaust_velocity   

    # Calculate the change in velocity using the formula from notes
    delta_v = (thrust * time_elapsed) / SPACECRAFT_MASS

    return delta_v

def main():
    """
    Main function to test the RCS functions.
    """

    # ----------- add in function for the check Plus test cases ---------------

    test_cases = [
        (0.02, 1000, 5),
        (0.06, 1000, 3),
        (0.05, 2000, 10)
    ]
    # Run malfunction detection on all thrusters before calculations
    malfunction_detection(test_cases)

    for i, (m_dot, v_e, t) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        delta_v = velocity_change_calculation(m_dot, v_e, t)
        print(f"Calculated delta_v: {delta_v:.2f} m/s")
        print("-" * 20)

if __name__ == "__main__":
    main()
