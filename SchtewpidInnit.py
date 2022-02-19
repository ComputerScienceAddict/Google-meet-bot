from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from churchillspeech import *
from pynput.keyboard import Key, Controller
import speech_recognition as sr
import time
def yourInput():
	link = " ";
	meetings = open("gmeetlinks.txt", "r");	
	daysList1 = ["m","w"];
	daysList2 = ["t", "th"];
	Day = input("What day is it: ");
	for i in range(len(daysList1)):
		if Day == daysList1[i]:
			link = meetings.readlines()[2];
			print(link);
		elif Day == daysList2[i]:
			link = meetings.readlines()[1]
			print(link);
	AMethod(link);




def AMethod(link):
	Keyboard = Controller();
	options = Options();
	options.add_experimental_option("prefs", { \
   		"profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
   		"profile.default_content_setting_values.media_stream_camera": 1,
   		"profile.default_content_setting_values.notifications": 1
 	})	
	PATH = "C:\Program Files (x86)\chromedriver";
	driver = webdriver.Chrome(PATH,options = options);
	driver.get("https://www.stackoverflow.com");



	time.sleep(2);
	driver.find_element_by_xpath("/html/body/header/div/ol[2]/li[2]/a[2]").click();
	time.sleep(2);
	driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/button[1]").click();
	time.sleep(2);
	driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Email, Keys.RETURN);
	time.sleep(4);
	driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys(Password, Keys.RETURN);
	time.sleep(2);
	driver.get(link);
	time.sleep(5);
	KeysBecauseWhyNot();
	goingToChat(driver);


def KeysBecauseWhyNot():
	Keyboard = Controller();
	for i in range(1,7):
		Keyboard.press(Key.tab);
		Keyboard.release(Key.tab)
		print(i);
		if i== 3 or i == 6:
			Keyboard.press(Key.enter);
			Keyboard.release(Key.enter);
			time.sleep(1);



def goingToChat(driver):
	Keyboard = Controller();
	for i in range(1, 3):
		Keyboard.press(Key.tab);
		if i == 2:
			Keyboard.press(Key.enter);
	SpeechRecognition(driver);




def SpeechRecognition(driver):
	r = sr.Recognizer();
	List = ["Joshua", "Josh", "Joshua Suarez", "Josh juarez", "Total War"]

	while(True):
		with sr.Microphone() as source:
			print("oi Bloike say something");
			audio = r.listen(source);
			voice_data = r.recognize_google(audio);
			print(voice_data);
			for i in range(len(List)):
				if voice_data == "Total War":
					playsound("Soldatenlieder - Erika - Version 3.mp3");
				if voice_data == "Joshua Suarez are you here" and i == 1:
					driver.find_element_by_xpath("/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[3]/div/div[2]/div[2]/div[2]/span[2]/div/div[3]/div[1]/div[1]/div[2]/textarea").send_keys("here",Keys.RETURN);


yourInput()