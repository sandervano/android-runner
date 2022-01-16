#!/bin/bash
echo "Beginning Treatment 1: LOnS"
python3 android-runner experiment/LOnS/config.json
echo "Beginning Treatment 2: LOnT"
python3 android-runner experiment/LOnT/config.json
echo "Beginning Treatment 3: DOnS"
python3 android-runner experiment/DOnS/config.json
echo "Beginning Treatment 4: DOnT"
python3 android-runner experiment/DOnT/config.json
echo "FINISHED ALL"
