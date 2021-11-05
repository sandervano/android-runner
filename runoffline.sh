#!/bin/bash
cd ../
echo "Beginning Treatment 1: DOnS"
python3 android-runner android-runner/experiment/DOffT/config.json
echo "Beginning Treatment 2: DOnT"
python3 android-runner android-runner/experiment/LOffT/config.json
echo "FINISHED ALL"
cd android-runner/
