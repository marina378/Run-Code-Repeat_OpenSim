# Run-Code-Repeat_OpenSim
**ME396: Group G12**

**Objective:** To create and analyze a musculoskeletal model of the hip while walking within OpenSim and calculate the flexion moment within the sagittal plane.

**To Create the Musculoskeletal Model:** Download OpenSim at https://simtk.org/frs/?group_id=91

**In Order to Run Our Code and Get the Output - Hip Flexion Moment vs. % Gait Cycle Plots:** Download the OpenSim Package and look for instructions under "Setting up your Python scripting environment" at https://simtk-confluence.stanford.edu:8443/display/OpenSim/Scripting+in+Python#ScriptinginPython-AccessingelementsofVecXandVectorusingbrackets

**To Visually Simulate the Musculoskeletal Model:** 
Download the OpenSim GUI from the first link and locate your model (".osim") and the motion file (".mot").
Once you open the OpenSIM GUI, click on File -> Open Model... and import the .osim model. 
Once the model has appeared in the visual window, click on File -> Load Motion... and select the desired .mot file to view the motion.
Once the motion file is loaded, press play on the top of the screen.

**Breakdown of our code (SensitivityAnalysisOfHipFlexion.py):**

**Part 1: Retrieve Data & Add Noise**
1. Import motion data
2. Convert to CSV file using pandas and numpy
3. Add normal Gaussian noise to the inverse kinematics results at different standard deviations
4. Convert CSV back to motion file
   
**Part 2: Hip Flexion Moment Calculation**
1. Use the motion file, the ground reaction force file, and the scaled OpenSim file to calculate the hip flexion moment (all files are within the 'Sensitivity Analysis Of Hip Flexion' Folder)
   
**Part 3: Hip Flexion Moment vs. % Gait Cycle Plots**
1. Plot the results against the % gait cycle using matplotlib

**The Models and Plots from are Presentation are shown in the 'OurResults' Folder**

Note: the hip flexion moment values on the y-axis of the plots do not match measured hip flexion moments found in research. 

