import rotate_me
import time
import math
def calculate_rotation(current_orientation, target_orientation):
    """
    Calculates the required rotation to move from the current orientation
    to the target orientation.
    --- Iteration 3 ---
    Current orientation: (99.99, 199.98, 300.00)
    Target orientation reached!
    --- Iteration 3 ---
    Current orientation: (-0.00, -0.01, -0.01)
    Target orientation reached!
    --- Iteration 4 ---
    Current orientation: (3.00, 30.01, 300.00)
    Target orientation reached!
    We utilized Copilot to help with targeting the specific orientations needed to make corrections on the axis.
    """
    # Compute the difference between target and current orientation
    x_correction = target_orientation[0] - current_orientation[0]
    y_correction = target_orientation[1] - current_orientation[1]
    z_correction = target_orientation[2] - current_orientation[2]
    # Return the correction tuple
    return (x_correction, y_correction, z_correction)
def main():
    """
    Main function to run the attitude control simulation.
    """
    target_orientation = (3, 30, 300)
    tolerance = 0.1
    max_iterations = 20
    print(f"Target orientation: {target_orientation}")
    for i in range(max_iterations):
        print(f"\n--- Iteration {i+1} ---")
        current_orientation = rotate_me.read_orientation_from_file(rotate_me.file_name)
        print(f"Current orientation: ({current_orientation[0]:.2f}, {current_orientation[1]:.2f}, {current_orientation[2]:.2f})")
        # Check if we are within tolerance
        error = math.sqrt(sum([(c - t)**2 for c, t in zip(current_orientation, target_orientation)]))
        if error <= tolerance:
            print("Target orientation reached!")
            break
        # Calculate the required corrections
        corrections = calculate_rotation(current_orientation, target_orientation)
        print(f"Applying corrections: {corrections}")
        # Apply the corrections using the rotate_me script
        rotate_me.main(corrections)
        time.sleep(1) # Pause for a moment to see the result
    else:
        print("\nMax iterations reached. Could not reach target orientation.")
if __name__ == "__main__":
    main()
 
 