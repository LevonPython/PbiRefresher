# Power BI refresher (easy way)
Script for automation of refreshing Power BI workbooks. Built on Python 3.7 and pyautogui.

Developed for Power BI Desktop May 2019 Update (.69.5467.2151) on Windows 10 64-bit with English locale.

# Installation
Install using pip

pip install opencv-python <br/>                                                                                                          pip install pyautogui

you can find in requirements.txt file


# Usage  
python PBIRefresher.py    <br/>                                                                                                      Sample.pbix              <br/>                                                                                                         C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe<br/>

WHERE<br/>
python <py file> is PBIRefresher.py file         <br/>                                                                                   <.pbix file> is pbix format file, you are going to manipulate with  <br/>                                                               <absolute path to PBIDesktop.exe> is the full path to the pbix exe file to run<br/>

Keep in mind that that user of pbix should be logged in order to be able to publish it.     <br/>                                        Please keep in mind that this script uses GUI of Power BI Desktop and it needs that a user is logged in Windows session. 

# how it works

See how it works
https://drive.google.com/file/d/1FOfdqvMdLNUcRwF8KwhmoDWiw97vqNFU/view?usp=sharing

# Bug reporting
Create Github issue. Please write version of your Power BI Desktop, OS and attach command line result and screenshot.
