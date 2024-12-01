import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

cwd = os.getcwd()
opt = Options()
service = Service(cwd+"\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=opt)

views = 100

videos = [
    "https://www.youtube.com/watch?v=kX58_vYzATs",
    "https://www.youtube.com/watch?v=r17XAdt3qjk",
    "https://www.youtube.com/watch?v=8fD3cY0nb5Q",
    "https://www.youtube.com/watch?v=PiDtTXhvrVw",
    "https://www.youtube.com/watch?v=Vm_RlJefI3s",
    "https://www.youtube.com/watch?v=R9VY5YtttJk",
    "https://www.youtube.com/watch?v=JVSc8vLFBIY",
    "https://www.youtube.com/watch?v=Sl5cW6HpS8o",
    "https://www.youtube.com/watch?v=fT8Q980g7Bw",
    "https://www.youtube.com/watch?v=mciD2TA48fs",
    "https://www.youtube.com/watch?v=OnDYfiNMyhs",
    "https://www.youtube.com/watch?v=JVsIj67M1ik",
    "https://www.youtube.com/watch?v=Zc91pBs_uuc",
    "https://www.youtube.com/watch?v=r_qvsNVrvg8",
    "https://www.youtube.com/watch?v=sSF9BIhTV7w",
    "https://www.youtube.com/watch?v=O9reVKdcgHk",
    "https://www.youtube.com/watch?v=6_OmsSeAjZE",
    "https://www.youtube.com/watch?v=nR18vXcWvR4",
    "https://www.youtube.com/watch?v=Tsg1-utZj1s",
    "https://www.youtube.com/watch?v=M1jEUJRsmhc",
    "https://www.youtube.com/watch?v=CGb-dGYfmJ4",
    "https://www.youtube.com/watch?v=ICSDePSQYkY",
    "https://www.youtube.com/watch?v=oNrbxvXnLCA",
    "https://www.youtube.com/watch?v=zNHEx9Tigyw"
          ]
for i in range(100):
    for video_link in videos:
        driver.get(video_link)
        v = "document.getElementsByTagName('video')[0]"
        video_title = driver.execute_script("return document.title")
        print("Playing Video: " + video_title)
        video_duration = driver.execute_script("return "+v+".duration")
        driver.execute_script(""+v+".playbackRate=1.5")
        print("Video Playback = 2")
        driver.execute_script(""+v+".play()")
        time.sleep((video_duration/2) + 10)
