from command_dict import command_dict

def parse_command(command_string):
    """
    Parses a command string and returns a tuple with the full subsystem name,
    the command description, and the parameter value.
    """
    
    # Segmentize the command strings into three parts
    segment = command_string.split(":")

    # perform a check to verify the format of the command string
    if len(segment) != 3:
        print("Error: Command format is incorrect. Expected format should be: Subsystem:Command:Parameter_Value")
        return (None, None, None)

    # look into the content of each part of the command string
    subsystem = segment[0]
    command = segment[1]
    parameter_value = segment[2]

    # Convert the parameter_value string to an integer
    try:
        value = int(parameter_value)
    except ValueError:
        print("Error: Parameter value must be an integer.")
        value = None

    # Initialise the output variables
    subsystem_name = None
    command_description = None

    # Check the command dictionary if the subsystem is present
    if subsystem in command_dict:
        subsystem_info = command_dict[subsystem]
        subsystem_name = subsystem_info["full_name"]

        # Check if command code exists within the subsystem folder
        if command in subsystem_info["commands"]:
            command_description = subsystem_info["commands"][command]

    # Check if command description is available, else inform the satellite operator
    if command_description is None:
        print("Error: Command code does not exist in the subsystem dictionary.")

    # Return the subsystem name, command description, and the parameter value
    return (subsystem_name, command_description, value)

def main():
    """
    Main function to test the command parser.
    """
    test_commands = [
        "EPS:CMD01:0",
        "ACS:CMD04:-1",
        "RCS:INVALID:0"
    ]

    for cmd in test_commands:
        subsystem, description, value = parse_command(cmd)
        print(f"Command: {cmd}")
        print(f" -> Subsystem: {subsystem}")
        print(f" -> Description: {description}")
        print(f" -> Value: {value}")
        print("-" * 20)

if __name__ == "__main__":
    main()
