# FocusTracker
**Track your focus blocks during the day**

The idea of creating this script is to track my periods of focus during any given day. I use an online [White Noise Generator](https://mynoise.net/NoiseMachines/whiteNoiseGenerator.php) while I am trying to focus on something (as I usually work in a noisy environment :cry:) and this script reads the play and pause patterns of the white noise generator and outputs the durations of your **focus blocks** (Assuming you are focusing on some task while the white noise is being played and not when it is in paused state).

You need __Python3__ and **'selenium'** python module installed on your machine to run this script. If you have Python3 and selenium setup already on your machine, you can just directly run main.py. If not, proceed to install Python3 and selenium.

Steps to install Selenium
1. Clone this repository somewhere on your machine and navigate inside of the repository directory in command prompt/terminal
2. pip install -r requirements.txt (You may do this in a new virtual environment)
3. Download the appropriate chrome driver from the [downloads](https://googlechromelabs.github.io/chrome-for-testing/) page and update the PATH environment variable with the driver's location
4. Run main.py to track your focus blocks :smile:

Note: The White Noise Generator works best in the ***'Speech Blocker'*** mode from my experience