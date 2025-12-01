from command_dict import command_dict


# Helper function to get subsystem info by code instead of by name from the command_dict
def get_subsystem_by_code(code):
    for full_name, info in command_dict.items():
        if info["Code"] == code:
            return full_name, info
    return None, None


def parse_command(command_string):
    """
    Parses a command string and returns a tuple with the full subsystem name,
    the command description, and the parameter value.
    """

    # Segmentize the command strings into three parts
    segment = command_string.split(":")

    '''
    #test print statements
    #print("Segment: ", segment)
    #print("Length of segment: ", len(segment))
    '''
    # perform a check to verify the format of the command string


    if len(segment) != 3:
        print("Error: Command format is incorrect. Expected format should be: Subsystem:Command:Parameter_Value")
        return (None, None, None)

    # look into the content of each part of the command string
    subsystem_code = segment[0]
    command = segment[1]
    parameter_value = segment[2]

    '''
    #testers
    print("Subsystem TEST: ", subsystem)
    print("Command TEST: ", command) 
    print("Parameter TEST: ", parameter_value)
    print("Command TEST: ", command)
    print("Parameter TEST: ", parameter_value)
    '''

    # Convert the parameter_value string to an integer
    try:
        value = int(parameter_value)
        #print("new value type should be int!!!!!: ", type(value))
    except ValueError:
        print("Error: Parameter value must be an integer.")
        return (None, None, None)

    # Lookup subsystem by CODE instead of key by referencing the function above this section
    subsystem_name, subsystem_info = get_subsystem_by_code(subsystem_code)

    # Lookup subsystem by CODE instead of key by referencing the function above this section
    subsystem_name, subsystem_info = get_subsystem_by_code(subsystem_code)
    # If subsystem not found, return error, do this first before checking command
    if subsystem_info is None:
        print(f"Error: Subsystem code '{subsystem_code}' not found.")
        return (None, None, None)

    # print subsystem found for testing for conformation/reference
    print("Subsystem Found:", subsystem_name)

    # print subsystem found for testing for conformation/reference
    print("Subsystem Found:", subsystem_name)

    # Lookup command in the found subsystem (uppercase 'C' to match keys in command_dict))
    if command in subsystem_info["Commands"]:
        command_description = subsystem_info["Commands"][command][0] # NEED POINTER HERE, only wants the command... not the command andnext value
        print("Command Description Found:", command_description)
    else:
        command_description = None
        print(f"Error: Command '{command}' does not exist in subsystem {subsystem_name}.")
        return (None, None, None)
    
    # Return the full subsystem name, command description, and parameter value
    return (subsystem_name, command_description, value)
