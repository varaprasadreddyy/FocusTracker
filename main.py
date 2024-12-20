from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

def main():
    # Run indefinitely and create a report for each day (or)
    # Run each day between certain timestamps and create a report
    driver = webdriver.Chrome()

    url = 'https://mynoise.net/NoiseMachines/whiteNoiseGenerator.php'
    driver.get(url)
    time.sleep(2)
    attr = 'pointer-events: auto;'
    prev = attr
    xpath = '/html/body/div[6]/div[1]/div/div[5]/div/i'
    elem = driver.find_element(By.XPATH, xpath)

    s1 = 'pointer-events: auto;' # initial
    s2 = 'pointer-events: auto; display: none;' # focus
    s3 = 'pointer-events: auto; display: flex;' # idle

    starts = []
    ends = []
    durs = []

    while True:
        try:
            # check the style attribute each second
            attr = elem.get_attribute('style')
            
            # to start a focus block, prev needs to be either in initial state, or idle state (get timestamp) and attr needs to be in focus state
            if (prev == s1 or prev == s3) and attr == s2:
                timestamp = datetime.now()
                starts.append(timestamp)
            # end a focus block when prev is in focus state, and attr is in idle state
            elif prev == s2 and attr == s3:
                timestamp = datetime.now()
                ends.append(timestamp)
            elif prev == s2 and attr == s2 and len(starts) == 0 and len(ends) == 0: #corner case when the generator starts in the focused state
                timestamp = datetime.now()
                starts.append(timestamp)
            prev = attr
            # interval between each check
            time.sleep(1)

        except:
            driver.quit()
            if len(starts) == len(ends)+1:
                ends.append(datetime.now())
            if len(starts) == len(ends):
                for i in range(len(ends)):
                    delta = str(ends[i] - starts[i])
                    temp = delta.split(':') 
                    hrs = temp[0]
                    mins = temp[1]
                    secs = temp[2][:2]
                    print(f'Focus Block {i+1} -> {str(starts[i])[:-7]} to {str(ends[i])[:-7]} -> {hrs} hours {mins} mins {secs} secs')
            else:
                print("Bad Input")
            break

if __name__ == "__main__":
    main()
