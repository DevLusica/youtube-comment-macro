import os
import json
import time
import shutil
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

with open('./data/data.json', 'r', encoding='UTF-8') as data:
    userdata = json.load(data)

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

shutil.rmtree("C:/ChromeCommentTEMP")
os.system('start C:\\"Program Files"\\Google\\Chrome\\Application\\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeCommentTEMP"')
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(10)

URL = 'https://studio.youtube.com/video/jeIw5l0KtNs/comments/inbox'
driver.get(url=userdata['url'])
os.chmod("C:/ChromeCommentTEMP/", 0o777)
comment_butten = "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[8]/ytcp-activity-section/div/ytcp-comments-section/ytcp-animatable/div[1]/ytcp-comment-thread[{cnum}]/ytcp-comment/div[1]/div/div[1]/div[2]/div[2]/ytcp-comment-action-buttons/div/ytcp-comment-button/a/paper-button/yt-formatted-string"
comment_box = "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[8]/ytcp-activity-section/div/ytcp-comments-section/ytcp-animatable/div[1]/ytcp-comment-thread[{cnum}]/ytcp-comment/div[2]/ytcp-commentbox/div[1]/div/ytcp-form-input-container/div[1]/div[2]/iron-autogrow-textarea/div[2]/textarea"
comment_save = "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[8]/ytcp-activity-section/div/ytcp-comments-section/ytcp-animatable/div[1]/ytcp-comment-thread[{cnum}]/ytcp-comment/div[2]/ytcp-commentbox/div[1]/div/div/div/ytcp-ve/ytcp-comment-button/a/paper-button/yt-formatted-string"
like_butten = "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[8]/ytcp-activity-section/div/ytcp-comments-section/ytcp-animatable/div[1]/ytcp-comment-thread[{cnum}]/ytcp-comment/div[1]/div/div[1]/div[2]/div[2]/ytcp-comment-action-buttons/div/ytcp-comment-toggle-button[1]/a/yt-icon-button/button/yt-icon"
heart_butten = "/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[8]/ytcp-activity-section/div/ytcp-comments-section/ytcp-animatable/div[1]/ytcp-comment-thread[{cnum}]/ytcp-comment/div[1]/div/div[1]/div[2]/div[2]/ytcp-comment-action-buttons/div/ytcp-comment-creator-heart/yt-icon-button/button/yt-icon"
comment_message = "뽷뽷"
lnum = 1

def xpathexist(xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False

while True:
    if xpathexist("/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[8]/ytcp-activity-section/div/ytcp-comments-section/ytcp-animatable/div[1]/ytcp-comment-thread[{cnum}]" .format(cnum = lnum)) == True:
        driver.find_element_by_xpath(comment_butten .format(cnum = lnum)).click()
        driver.find_element_by_xpath(comment_box .format(cnum = lnum)).send_keys(comment_message)
        driver.find_element_by_xpath(comment_save .format(cnum = lnum)).click()
        driver.find_element_by_xpath(like_butten .format(cnum = lnum)).click()
        driver.find_element_by_xpath(heart_butten .format(cnum = lnum)).click()
        driver.refresh()
    else:
        driver.refresh()