def available_power(voltage, current):
    """
    Calculates the instantaneous incoming power from the solar panels,
    checking for inputs that exceed the solar panels' maximum limits.
    """

    if voltage > 28:
        print(f"Voltage of {voltage} W exceeds maximum limit of 28 W")
        voltage_diff = voltage - 28
        voltage = voltage - voltage_diff
        print(f"Voltage being reduced to {voltage} W")
    if current > 10:
        print(f"Current of {current} A exceeds maximum current of 10 A")
        current_diff = current - 10
        current = current - current_diff
        print(f"Current being reduced to {current} A")
    power = voltage * current
    return power

def battery_charging(power_delivered, time_elapsed):
    """
    Calculates the total energy available for battery charging.
    """
    energy_available = power_delivered * time_elapsed
    return energy_available


def main():
    """
    Main function to test the EPS functions.
    """
    # Example test cases from the project description
    test_cases = [
        (22, 7, 300),
        (40, 7, 60),
        (25, 10, 200),
        (10,4,600),
        (0,7,300),
        (30,10,60),
        (28,10,200),
        (10,10,10)
    ]

    for i, (v, i_current, t) in enumerate(test_cases):
        print(f"--- Test Case {i+1} ---")
        power = available_power(v, i_current)
        print(f"Available Power: {power:.2f} W")
        energy = battery_charging(power, t)
        print(f"Energy for charging: {energy:.2f} J")
        print("-" * 20)

    total_power = 0                                         #initialize total power and total energy variables
    total_energy = 0
    for i, (v,i_current, t) in enumerate(test_cases):
        print(f"--- Test Case {i + 1} ---")
        total_power += available_power(v, i_current)
        print(f"Current Total Power: {total_power:.2f} W")
        total_energy += battery_charging(available_power(v, i_current), t)
        print(f"Current Total Energy for charging: {total_energy:.2f} J")
        print("-"*20)
    print(f"Total Power: {total_power:.2f} W")
    print(f"Total Energy: {total_energy:.2f} J")

if __name__ == "__main__":
    main()
