# Run-Code-Repeat_OpenSim
**ME396: Group G12**

**Objective:** To create and analyze a musculoskeletal model of the hip while walking within OpenSim and calculate the flexion moment within the sagittal plane.

**You MUST download all required files in order to:**
1. Run our code and output the Hip Flexion Moment vs. % Gait Cycle Plots
2. Create the different musculoskeletal models

   To run our code to get desired outputs (Hip Flexion Moment vs. % Gait Cycle Plots): 
      1. Navigate to OpenSim at https://simtk-confluence.stanford.edu:8443/display/OpenSim/Scripting+in+Python#ScriptinginPython-
         - Follow the instructions for your specific environment under "Setting up your Python scripting environment" to import the OpenSim Package
      2. Run our code (SensitivityAnalysisOfHipFlexion.py)
         - Check results of plots 

   To Create the Musculoskeletal Model: Download OpenSim at https://simtk.org/frs/?group_id=91
      1. Download the OpenSim GUI
            - Navigate to the model ("gait2392_simbody_scaled.osim")
      2. Open the OpenSim GUI
            - Click on File
               - Open Model
                  - Import the "gait2392_simbody_scaled.osim" model
      3. Once the model has appeared in the visual window…
            - Click on File
               - Load Motion
                     - Select Original Data: "subject01_walk1_ik.mot" or Noisy Data: "noisedata0.5.mot",  "noisedata1.mot", or "noisedata2.mot" 
      4. Once the desired motion file is loaded…	
            - Press play on the top of the screen
               - Check results of simulations

**Breakdown of our code (SensitivityAnalysisOfHipFlexion.py):**

Part 1: Retrieve Data & Add Noise
   1. Import motion data (“subject01_walk1_ik.mot”)
   2. Convert to CSV file using pandas and numpy
   3. Add normal Gaussian noise to the inverse kinematics results at different standard deviations
   4. Convert CSV back to motion file:
      - Original Data: "subject01_walk1_ik.mot"
      - Noisy Data: "noisedata0.5.mot",  "noisedata1.mot", "noisedata2.mot"
     
Part 2: Hip Flexion Moment Calculation
   1. To calculate the hip flexion moment using the inverse dynamics module from the OpenSim package make sure the following is downloaded:
      - The inverse kinematics motion file (“subject01_walk1_ik.mot”)
      - The experimental ground reaction force data file (“subject01_walk1_grf.xml”)
      - The scaled OpenSim file (“gait2392_simbody_scaled.osim”)
  
Part 3: Hip Flexion Moment vs. % Gait Cycle Plots
   1. Plot the Hip Flexion Moment vs. % Gait Cycle with the original data using matplotlib
   2. Plot the individual Hip Flexion Moment vs. % Gait Cycle with the added standard deviations of noise using matplotlib (created within the Inverse Dynamics function (ID(...)))
   3. Plot a combined plot of all the individual plots from the step above (created within the plots(...) function)

**The Models and Plots from are Presentation are shown in the 'OurResults' Folder**
Note: The hip flexion moment values on the y-axis do not match measured hip flexion moments found in research. We plan to investigate and troubleshoot the code to resolve for future use in our research.
