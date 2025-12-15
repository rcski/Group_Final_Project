# SS1100: Intro to Programming for Space Applications
## Final Project: Programming Spacecraft Systems

This repository contains the starter code and resources for the SS1100 Final Project. The goal of this project is to apply your programming skills to solve a variety of problems related to spacecraft subsystems.

### Project Structure

The project is organized into folders, one for each spacecraft subsystem:

- :white_check_mark: **/RCS/**: Reaction Control Subsystem --> Completed
- :white_check_mark: **/TCS/**: Thermal Control Subsystem --> Completed
- :white_check_mark: **/ADC/**: Attitude Control Subsystem (Note: ADC is used in the folder name for brevity) --> working
- :white_check_mark: **/C&DH/**: Command and Data Handling --> Completed
- :white_check_mark: **/EPS/**: Electrical Power Subsystem --> Completed
- :white_check_mark: **/Payload/**: Remote Sensing Payload --> Completed

Each folder contains the necessary scripts and data files for that subsystem's tasks.

### Getting Started

For each subsystem, you will find a primary Python script (e.g., `rcs_script.py`, `thermal_control.py`, etc.). Your task is to complete the functions within these scripts according to the instructions in the main project document (`Final Project Instructions.pdf`).

### Verifying Your Code with Unit Tests

Each subsystem folder also contains a `/test` directory with a unit test script (e.g., `test_rcs.py`). These tests are designed to help you verify that your code is working correctly.

To run the tests for a specific subsystem, navigate to that subsystem's directory in your terminal and run the test script. For example, to test your RCS code:

```bash
cd RCS
python test/test_rcs.py
```

If your functions are implemented correctly, the tests should pass without errors.

### Capstone: Mission Simulation

Once you have completed the tasks for all the individual subsystems, you can tackle the final capstone challenge in `mission_simulation.py`. This script, located in the root directory, is designed to integrate the functions you've written into a single, cohesive mission sequence.

---

## Questions for Writeup

1.  **What was your experience in collaborating?**
   Our team collaboration balanced structure with flexibility. We divided the workload by modules of the satellite system, first meeting the “check” criteria and then aiming for “check plus.” Tasks were also aligned with each member’s interests and willingness to challenge themselves. One member with stronger coding experience naturally took on the role of “chief editor,” guiding the team, refining code, and ensuring standards were met. We used GitHub to upload edits for peer review, which helped integrate contributions smoothly, though learning the buttonology and file paths was initially challenging. Regular check-ins kept everyone aligned and ensured our individual pieces fit together cohesively.
2.  **What was the most challenging section, and why?**
   Individually, the most challenging parts varied. One member struggled with the ISR payload code, particularly using np.dstack to combine RGB CSVs, which required extensive troubleshooting to understand the inputs and image construction. Another found difficulty in structuring the command dictionary correctly and ensuring the parser extracted the right fields. As a team, we anticipate challenges in integrating independently developed sections, since inconsistencies in logic flow and function structure may arise. Debugging these integration issues will require careful testing to ensure the program works end-to-end.
3.  **If you employed Generative AI tools, how did you do so?**
   We used generative AI tools such as ChatGPT primarily for troubleshooting and clarifying Python syntax. When encountering errors that were difficult to distill, we pasted code snippets and asked for explanations. This was especially helpful in understanding complex structures like the 3D arrays created by RGB images. We also described specific sections of code and our expectations, then adapted AI-generated suggestions and manually tested them to confirm validity. This iterative process made debugging more efficient and improved our understanding of the code.
4.  **What other resources did you use to find solutions?**
   Beyond AI tools, we relied on external resources to validate our approaches. Stack Overflow and the official Numpy documentation were used to confirm correct function usage, while lecture materials and YouTube tutorials provided broader explanations of programming concepts. These references helped ensure that the AI-generated outputs were accurate and that we understood the underlying principles behind the code.
5.  **In what way could this project be improved for future quarters?**
   This project overall was a lot of fun, and each subsystem had a unique feel and challenge. This tests each person to either feel like they can attempt a challenge to learn something new, or to stick with what they are comfortable with. 
