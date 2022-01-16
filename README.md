# Setting it right:
## Impact of User Settings on the Energy Consumption of Google Maps

This package contains all the software and results needed to reproduce the research conducted in *Setting it right: Impact of User Settings on the Energy Consumption of Google Maps*.


## Setting up the environment
The package uses the included android-runner framework to perform measurements on the android device. This framework must first be setup correctly by following the steps documented in the *README.md* file in the android-runner directory.


## Setting up the Device
### Extracting the Power Profile
While following the above instructions, the device's power_profile.xml should be extracted. This file needs to be copied to the **experiment/** subdirectory also containing the **DOffT/** to **LOnT/** and **Results/** subdirectories. The power_profile file already included there should be replaced with the profile extracted from your own device.

### Installing applications
The package expects the following applications to be installed and operable on the device:
- *Google Maps* version 11.4.3 (released on 28.10.2021)
- *Lockito* - v3.2.1 (released on 29.09.2020)
These applications can be installed directly from the app-store, or manually.

### Setting up lockito
The GPS spoofing application *Lockito* should contain two, and only two routes.
1. The first route should contain a route following some road navigable by car in Google Maps. The route length and traveling speed should be set such that the total drive time is longer than 10 minutes.
2. The second route should be a static location set to the starting position of the first route. This location is used by Google Maps to determine the navigation.

### Setup the Navigation Destination
Unaltered, the package will try to navigate towards *"Veendam"* from whichever starting location is configured in *Lockito*. While it is not strictly required to change this destination, it is recommended to set it according to the first route in *Lockito*. To change this destination, changes must be made in the file **Scripts/after_launch.py** on line 71:
```bash
device.shell('input text "Veendam"')
```
In this line "*Veendam*" should be changed to the correct destination. This must be done in each **Scripts/after_launch.py** file in the subdirectories **DOffT/** to **LOnT/** in the **experiment/** directory.


## Running on the Rasberry Pi
The package is set to run on a *Rasberry Pi*, mounted directly from the directory **/home/pi/external_hdd/**. Any changes made to this location requires changing the locations in the **confic.json** files found in each subdirectory in the **experiment/**" directory (save from the Results subdirectory). The *systrace_path* variable must be set according to the computer used to run the package, and the *power_profile* path must be set according to the path to the **power_profile.xml** file in the experiment directory.


## Clearing the Results
Unaltered, this package contains the results reported on in the original experiment. When reproducing these results, the original results should be removed from the **experiment/Results** subdirectory. All files and subdirectories containing the treatment names such as *DOffT* or *LonS* must be removed.


## Running the Experiments
Several steps must be taken to perform the experiments used in the research. The experiment itself is split up into an online and an offline part. This is due to the fact that for running the offline experiments, a set of manual steps are required different from the online experiments.


### Step 1: Start Environment
Use the following commands to start the virtual environment for *android-runner* (assuming the same file structure is used as discussed above):
```bash
cd /home/pi/external_hdd/android-runner
sudo python3 -m venv .venv
source .venv/bin/activate
cd ../
```
You may replace the first *cd* command to wherever the *android-runner* package is located. Afterwards, the working directory should have been set to the directory this file is located in.
Afterwards, the virtual environment should be running and the working directory should be the one containing this README file.

### Step 2: Online experiments
Before running the online experiments, the device should be freshly booted and both *Google Maps* and *Lockito* should be opened and given time to load into their starting screen once. *Google maps* should be closed afterwards, but *Lockito* should be kept running on its starting screen. Now the following commands can be run from the working directory this file is located in:
```bash
sudo ./runonline.sh
```
This runs all the experiments for all the online treatments.

### Step 3: Offline setup
For running the experiments for the two offline treatments *DOffT* and *LOffT* several manual steps are required. To begin with, the device should be freshly booted. In Google Maps, an offline map containing the starting location, the entire *Lockito route*, and the set destination must be manually selected and downloaded. This needs to only be done once before running the offline experiments. After the map is downloaded, Wifi and Roaming must be turned off on the device to force Google Maps into offline mode. The offline map may now be tested to see if the correct navigation route is selected towards the given destination. If this is not the case, a larger offline map of the region may need to be downloaded.

### Step 4: Offline experiments
If the offline map is correctly downloaded and the Wifi and Roaming on the device turned off, the following command can be used to start the offline experiments:
```bash
sudo ./runoffline.sh
```


## Results
After completing all the steps in running the experiment, the results folder should be populated with a new set of subdirectories consisting of the name of the treatment followed by the date and time of the experiment (E.g. *DOffT_2022.01.16_123456*).

### Data Preparation
The results from each experiment must be extracted before they can be processed in **R**. In the script **gather_total_results.py**, the list of directories should be changed to contain only the 6 subdirectories in the **experiment/Results** directory generated by the experiment previously executed. Afterwards, the script can be executed as follows:
```bash
cd experiment/Results
sudo python3 gather_total_results.py
cd ../../
```
This should generate six files named *total_* followed by a specific treatment name.

### Data Processing
These files can now be processed in **R** to produce the results reported in our research by loading and running the file **datanalysis.R** in RStudio.
