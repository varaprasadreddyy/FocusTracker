# FocusTracker
### Track your focus blocks during the day

The idea of creating this script is to track my periods of focus during any given day. I use an online [White Noise Generator](https://mynoise.net/NoiseMachines/whiteNoiseGenerator.php) while I am trying to focus on something (as I usually work in a noisy environment :cry:) and this script reads the play and pause patterns of the white noise generator and outputs the durations of your **focus blocks** (Assuming you are focusing on some task while the white noise is being played and not when it is in paused state).

You need __Python3__ and **'selenium'** python module and a **chromedriver** on your machine to run this script. If you have Python3 and selenium setup already on your machine, you can just directly run main.py to open up the white noise generator in new selenium browser window. Play and Pause the white noise according to when you are focusing on some task and being idle respectively. Just close the browser window after you are done focusing to get the output on your focus blocks.

If not, proceed to install Python3 and selenium and download the appropriate chromedriver from the [downloads](https://googlechromelabs.github.io/chrome-for-testing/) page. You may also need to update the PATH environment variable with the chromedriver's location.

*Note*: The White Noise Generator works best in the ***'Speech Blocker'*** mode from my experience