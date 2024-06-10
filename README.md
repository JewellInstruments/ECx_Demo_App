# ECx_Demo_App
ECx eCompass demo software for the intended use of Jewell Instruments customers to use as a starting point for communicating with any of Jewell's eCompass products.


# About
+ Author: Lucas Jameson
+ Date: 10th June 2024
+ Written for: Python 3.10.10
+ Tested on: Windows 10

# Setup
+ Clone the repo to your machine.
+ Create a virtual environment with "py -m venv .venv"
+ Activate the virtual environment with ".venv/Scripts/activate"
+ Install modules with "pip install -r requirements.txt"
+ With the sensor connected to the PC's serial port, run the app with "py EXc_cli.py"

# Usage
This app is a very low level and simple app to communicate with the ECx sensors. The app will ask the user for the com port the sensor communicates over and the buadrate.
Once the app has that information, it will ask the sensor for its identification. After that, the app will continuously poll and display data from the sensor by 
issuing the HTM command (see ECV Technical Guide-B (Long Version).pdf Section 4.1.4.4 pg. 41).
