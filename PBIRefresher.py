import os
import subprocess
import time
import pyautogui


class PbiRefresher:

    def open_file(self, name):
        print("Opening the pbix file . . .")
        pyautogui.hotkey('alt', 'f')
        time.sleep(1)
        pyautogui.press('down')
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.typewrite(name[0], interval=0)
        time.sleep(1)
        pyautogui.press('down')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(7)
        pyautogui.hotkey('alt', 'h')
        time.sleep(1)
        pyautogui.typewrite('r', interval=0)
        time.sleep(10)
        pyautogui.hotkey('alt', 'h')
        time.sleep(1)
        pyautogui.typewrite('r', interval=0)
        print("Refresh Done!")
        self.saving_file()

    def saving_file(self):
        # save
        time.sleep(8)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')
        print("File was saved !")
        self.publish_file()

    def publish_file(self):
        # publish
        time.sleep(5)
        pyautogui.hotkey('alt', 'h')
        time.sleep(1)
        pyautogui.typewrite('pu', interval=0)
        time.sleep(3)
        pyautogui.press('enter')
        time.sleep(3)
        pyautogui.press('enter')
        print("Published !")
        self.closing_app()

    def closing_app(self):
        # closing
        time.sleep(20)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.press('enter')
        print("Sub window closed !")

        # close the program
        time.sleep(2)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(5)
        pyautogui.hotkey('alt', 'f4')
        print("Program was closed ! \n PBI ZEPPA Disbursements file was successfully refreshed, saved and published !")


if __name__ == "__main__":
    file_name = input(
        "Please type name of pbix file to manipulate for, located in your Documents' folder in advance!\n")
    #
    path_pbi_file = input("Please type the full path to the PBIDesktop.exe:\n "
                          "for example: C:\Program Files\Microsoft Power BI Desktop\\bin\PBIDesktop.exe\n")
    p = subprocess.Popen(path_pbi_file, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         universal_newlines=True, shell=False)
    time.sleep(18)
    print("The process started . . .")
    pbix = PbiRefresher()
    pbix.open_file(file_name)
