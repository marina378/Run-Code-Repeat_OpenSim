# Run-Code-Repeat_OpenSim
**ME396: Group G12**

**Objective:** To create and analyze a musculoskeletal model of the hip while walking within OpenSim and calculate the flexion moment within the sagittal plane.

**To Create the Musculoskeletal Model:**
Download OpenSim: https://simtk.org/frs/?group_id=91

**In Order to Run Our Code and Get the Output: Hip Flexion Moment vs. % Gait Cycle Plots**
Download the OpenSim Package. Look for instructions under "Setting up your Python scripting environment" at https://simtk-confluence.stanford.edu:8443/display/OpenSim/Scripting+in+Python#ScriptinginPython-AccessingelementsofVecXandVectorusingbrackets

**Breakdown of our code (SensitivityAnalysisOfHipFlexion.py):**
**Part 1: Retrieve Data & Add Noise**
1. Import motion data & convert to CSV file using pandas and numpy
2. Add normal Gaussian noise to the inverse kinematics results at different standard deviations & convert back to motion file
   
**Part 2: Hip Flexion Moment Calculation**
1. Use the motion file and scaled OpenSim file to calculate the hip flexion moment
2. Plot the results against the % gait cycle using matplotlib
   
**Part 3: Visual Simulation**
1. Simulate the model with OpenSim using the motion files
