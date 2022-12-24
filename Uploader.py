import time
import logging
import platform, os
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from Constant import Constant

class YouTubeUploader:
	def __init__(self):
		is_mac = False
		if not any(os_name in platform.platform() for os_name in ["Windows", "Linux"]):
			is_mac = True
		profile_path=str(Path.cwd()) + "/profile"
		options = Options()
		options.add_argument("-profile")
		options.add_argument(profile_path)
		options.headless = Constant.HEADLESS
		self.browser = webdriver.Firefox(options=options,service=Service(GeckoDriverManager().install())) 
		self.browser.get(Constant.YOUTUBE_URL)
	
	def sleep(self,t):
		for i in range(0, t):
			time.sleep(1)
			print(f"{str(i)} out of {str(t)}", end="\r")

	def UPLOADER(self,title: str, description: str, video_path: str):
		browser=self.browser
		browser.get(Constant.YOUTUBE_URL)
		self.sleep(Constant.USER_WAITING_TIME)
		browser.get(Constant.YOUTUBE_UPLOAD_URL)
		self.sleep(Constant.USER_WAITING_TIME)

		absolute_video_path = video_path
		browser.find_element(By.XPATH, Constant.INPUT_FILE_VIDEO).send_keys(
						absolute_video_path)


        #check for Upload Progress


        #proceed further
		self.sleep(30)
		title_field, description_field = browser.find_elements(By.ID, Constant.TEXTBOX_ID)


		title_field.clear()
		title_field.send_keys(title)
		self.sleep(5)



		description_field.click()
		description_field.send_keys(description)
		self.sleep(5)


		kids_section = browser.find_element(By.NAME, Constant.NOT_MADE_FOR_KIDS_LABEL)
		kids_section.location_once_scrolled_into_view
		xpath="/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]"
		browser.find_element(By.XPATH, xpath).click()
		self.sleep(5)


		cl=browser.find_element(By.ID, Constant.NEXT_BUTTON)
		cl.location_once_scrolled_into_view
		cl.click()
		self.sleep(5)
		browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
		self.sleep(5)
		browser.find_element(By.ID, Constant.NEXT_BUTTON).click()
		self.sleep(10)

		cl=browser.find_element(By.XPATH,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[2]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]/div[1]")
		cl.click()
		self.sleep(10)
		
        done_button = browser.find_element(By.ID, Constant.DONE_BUTTON)
		done_button.click()
		self.sleep(20)
		
        #get video Url
        # el="//*[@id='share-url']"
		# url=browser.find_element(By.XPATH, el).text
		# print(url)

        #close window
		# url=browser.find_element(By.ID, "close-icon-button")
		# url.click()

        #quit browser
		browser.quit()




if __name__ == "__main__":
    objName = Name()
    objName.main() 
# title="Unexpected"
# description="r/Unexpected"
# video_path="~/waste/video.mp4"
# url="https://www.reddit.com/r/Unexpected/comments/zt5zdx/one_of_the_best_scene_in_television_history/"

# os.system(f"rm -rf ~/waste/video.mp4 && yt-dlp -o ~/waste/video.mp4 {url}")
# UPLOADER(title, description, video_path)




