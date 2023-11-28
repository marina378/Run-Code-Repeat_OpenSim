import opensim as osim
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Convert mot to csv
def mot_to_csv(input_mot_file, output_csv_file):
    with open(input_mot_file, 'r') as mot_file:
        with open(output_csv_file, 'w') as csv_file:

            for line in mot_file:
                columns = line.strip().split(',')
                csv_file.write(','.join(columns) + '\n')

# add the noise to the csv file
def noise(input_csv, output_csv, std):
    file_path = input_csv
    num_columns = 24
    data = pd.read_csv(file_path, delimiter='\t', skiprows=11, header=None, names=range(num_columns))

    numerical_columns = data.iloc[:, 1:]
    noise_mean = 0
    noise_std = std
    for column in numerical_columns:
        data[column] += np.random.normal(noise_mean, noise_std, size=len(data))
    output_file_path = output_csv
    data.to_csv(output_file_path, sep='\t', index=False, header=False)

# convert csv to mot 
def csv_to_mot_with_headers(input_csv_file, output_mot_file):
    headers = ("Coordinates\n"
               "version=1\n"
               "nRows=121\n"  
               "nColumns=24\n"  
               "inDegrees=yes\n"
               "\n"
               "Units are S.I. units (second, meters, Newtons, ...)\n"
               "If the header above contains a line with 'inDegrees', this indicates whether rotational values are in degrees (yes) or radians (no).\n"
               "\n"
               "endheader\n"
               "time\tpelvis_tilt\tpelvis_list\tpelvis_rotation\tpelvis_tx\tpelvis_ty\tpelvis_tz\t"
               "hip_flexion_r\thip_adduction_r\thip_rotation_r\tknee_angle_r\tankle_angle_r\t"
               "subtalar_angle_r\tmtp_angle_r\thip_flexion_l\thip_adduction_l\thip_rotation_l\t"
               "knee_angle_l\tankle_angle_l\tsubtalar_angle_l\tmtp_angle_l\tlumbar_extension\t"
               "lumbar_bending\tlumbar_rotation\n")

    with open(input_csv_file, 'r') as csv_file:
        with open(output_mot_file, 'w') as mot_file:
            mot_file.write(headers)
            for line in csv_file:
                columns = line.strip().split(',')
                reconstructed_mot_data = '\t'.join(columns)
                mot_file.write(f"{reconstructed_mot_data}\n")

# insert force calculation code:
#from Kaleigh's code
##Calculating Inverse Dynamics of OpenSim scaled model (model 2392) ##

def ID(osimFile, grfFile, motFile):
    # opensim scaled model 
    scaled_model_path = osimFile #change for your path
    osim_scaled_model = osim.Model(scaled_model_path)

    # Ground reaction forces
    GRF_path = grfFile #change for your path

    # Create a storage object for the prescribed motion data
    motion_file_path = motFile #change for your path
    motion_data = osim.Storage(motion_file_path)

    # Create an Inverse Dynamics Tool
    inverse_dynamics_tool = osim.InverseDynamicsTool()

    # Set the model for the Inverse Dynamics Tool
    inverse_dynamics_tool.setModel(osim_scaled_model)

    # Set the motion data for the Inverse Dynamics Tool
    inverse_dynamics_tool.setCoordinatesFileName(motion_file_path)

    # Set the external loads file for the Inverse Dynamics Tool
    inverse_dynamics_tool.setExternalLoadsFileName(GRF_path)

    # Set low pass cut off frequency 
    inverse_dynamics_tool.setLowpassCutoffFrequency(6) #must be 30 Hz or below

    # Set the name of the generated force results file
    inverse_dynamics_tool.setOutputGenForceFileName("inverse_dynamics.sto") #saves to the directory of this python script

    # Set the time range for the analysis
    inverse_dynamics_tool.setStartTime(motion_data.getFirstTime())
    inverse_dynamics_tool.setEndTime(motion_data.getLastTime())

    # Run the Inverse Dynamics analysis
    inverse_dynamics_tool.run()

    ## Plot the right hip flexion moment vs time ##

    # Load data from .sto file into a Pandas DataFrame
    sto_file_path = "inverse_dynamics.sto" #change for your path
    data = pd.read_csv(sto_file_path, delimiter='\t', skiprows=7, index_col=False)

    column_names = [
    'time', 'pelvis_tilt_moment', 'pelvis_list_moment', 'pelvis_rotation_moment',
    'pelvis_tx_force', 'pelvis_ty_force', 'pelvis_tz_force',
    'hip_flexion_r_moment', 'hip_adduction_r_moment', 'hip_rotation_r_moment',
    'hip_flexion_l_moment', 'hip_adduction_l_moment', 'hip_rotation_l_moment',
    'lumbar_extension_moment', 'lumbar_bending_moment', 'lumbar_rotation_moment',
    'knee_angle_r_moment', 'knee_angle_l_moment',
    'ankle_angle_r_moment', 'ankle_angle_l_moment',
    'subtalar_angle_r_moment', 'subtalar_angle_l_moment',
    'mtp_angle_r_moment', 'mtp_angle_l_moment'
    ]

# Assign the column names to the DataFrame
    data.columns = column_names
    total_duration = data['time'].max()

    # Modify the 'time' column to be a percentage of the gait cycle
    data['time_percent'] = (data['time'] / total_duration) * 100
    #grab x
    xdata = data['time_percent']
    #grab y
    ydata = data['hip_flexion_r_moment']
    # Plot the 'time_percent' vs 'hip_flexion_r_moment'
    data.plot(x='time_percent', y='hip_flexion_r_moment', kind='line', legend=True)

    # Set plot labels and title
    plt.xlabel('(%) Gait Cycle ')
    plt.ylabel('Hip Flexion Moment (Nm)')
    plt.title('Gait Cycle Percentage vs Hip Flexion Moment (Right)')

    # Show the plot
    plt.show()
    #returns the data
    return xdata, ydata

# Multiple line plot
def plots(inputx, inputy, noise):
    xNums = inputx[0]
    for i, y_values in enumerate(inputy):
        plt.plot(xNums, y_values, label=f'{noise[i]} STD Noise')
    plt.title('Combined Hip Moment vs Percent Gait Cycle (%)')
    plt.xlabel('Hip Flexion Moment (Nm)')
    plt.ylabel('Percent Gait Cycle (%)')
    plt.legend()
    plt.grid(True)
    plt.show()

#main function to run
if __name__ == "__main__":
    noiselevel = [0,0.5,2,5]
    index = list(range(0,len(noiselevel)))
    #insert OSIM file:
    osimF = 'gait2392_simbody_scaled.osim'
    #insert grf file:
    grf = "subject01_walk1_grf.xml"

    x = []
    y = []
    for i in index:
        mot_to_csv('subject01_walk1_ik.mot', 'subject01_walk1_ik.csv')
        noise('subject01_walk1_ik.csv','noisedata.csv', noiselevel[i])
        motname = "noisedata" + str(noiselevel[i]) + ".mot"
        csv_to_mot_with_headers('noisedata.csv', motname)
        xdata, ydata = ID(osimF, grf, motname)
        x.append(xdata)
        y.append(ydata)
    plots(x,y,noiselevel)
        #insert function call to force calculations
        ###in this section save all the force calculations in outside list for combined plot

    

