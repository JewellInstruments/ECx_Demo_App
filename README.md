# ECx_Demo_App
ECx eCompass demo software for the intended use of Jewell Instruments customers to use as a starting point for communicating with any of Jewell's eCompass products.


# About
Author: Lucas Jameson
Date: 10th June 2024
Written for: Python 3.10.10
Tested on: Windows 10

# Setup
+ Clone the repo to your machine.
+ Create a virtual environment with "py -m venv .venv"
+ Activate the virtual environment with ".venv/Scripts/activate"
+ Install modules with "pip install -r requirements.txt"
+ With the sensor connected to the PC's serial port, run the app with "py EXc_cli.py"

# Usage
This app is a very low level and simple app to communicate with the ECx sensors. The app will ask the user for the com port the sensor communicates over and the buadrate.
Once the app has that information, it will ask the sensor for its identification. After that, the app will continuously poll and display data from the sensor by 
issuing the HTM command (see ECV Technical Guide-B (Long Version).pdf Section 4.1.4.4 pg. 41). Decoding information shown below.


HTM Heading, Tilt, & M a gnet i c F i e ld
$ P T N T H T M , x . x , a ,x . x , a , x .x ,a , x . x , x .x*hh < c r ><l f >
T h i s sentence com b i n e s the p r im a ry measurement and di agno st i c d a t a
r equi r ed by most app li c at i ons . H ea d ing, p it ch, and roll measurements are
inc lud e d as we ll as status and di agno s t i c da t a .
HTM data f ie ld s represent, in o r de r:
1. true head ing (compass measurement + d e v i a t ion + v a r i at i on )
2. magnetometer status character – C, L, M, N, O, P, or H (s ee b el ow)
3. pit ch angl e
4. pit ch status character – N, O, P (s ee b e lo w)
5. roll ang l e
6. roll status character – N, O, P (s ee b e lo w)
7. dip ang l e
8. re l a t ive m agn i tud e hori zon t a l component of ea rth’s m agn e t ic f i e ld
