from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import keyboard

print("press 'end' button to terminate the code")

isEndButtonPressed = False

def prKey() : 
    global isEndButtonPressed
    isEndButtonPressed = True

keyboard.on_press_key("end", lambda _: prKey())




# def closeDriver():
#     driver.close()
browserList = list([ 0, 1, 2]) # Firefox , # Chrome , # Edge 
currentBrowserOpenLength = int(0)
currentBrowser = int(1)

def changeCurrentBrowser(driver) : 
    try : 
        global currentBrowserOpenLength
        global currentBrowser
        global browserList
        if currentBrowserOpenLength >= 10:
            plus = currentBrowser + 1
            currentBrowser =  browserList[plus if len(browserList) > plus else 0 ]
            currentBrowserOpenLength = 0
            driver.close()
        else :
            currentBrowserOpenLength += 1
    except AttributeError : '' 

    

def browser(userName,isClose=False):
    try : 
        if currentBrowser == 1 :
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif currentBrowser == 2 : 
            driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        else :
            driver = webdriver.Firefox()

        if isClose : 
            driver.close()


        if userName :
            driver.get('https://www.instagram.com/{0}/?hl=en'.format(userName))
            res = driver.execute_script("return window?._sharedData?.entry_data?.ProfilePage[0];")
            changeCurrentBrowser(driver)
            return res
        else :
            return { "__error__" : 'userName is required' }
    except AttributeError : 
        return { "__error__" : 'userName is required' }



# jsonStr = browser('radha')
# print('jsonStr = ',jsonStr)
# json.dumps(browser())
# pyperclip.copy(jsonStr)
# a = browser()
# time.sleep(5)
# b = browser('rahulbhai')

# for i in b : 
    # print (b[i])
# print('okay a = ',jsonStr['always_show_message_button_to_pro_account'])
# print('okay b = ',b.always_show_message_button_to_pro_account)

