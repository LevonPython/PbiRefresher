.. image:: https://github.com/LevonPython/PBI_refresher_Zeppa/blob/master/PBI%20refresher%20pic.png
   :align: center
   :target: https://powerbi.microsoft.com/en-us/
   :alt: Power BI refresher Logo
   
  
============
Power BI refresher (easy way)
============
- `Introduction`_
- `Installation`_
- `Usage`_
- `How it works`_
- `Bug reporting`_


============
Introduction
============
Script for automation of refreshing Power BI workbooks. Built on Python 3.7 and pyautogui.

Developed for Power BI Desktop May 2019 Update (.69.5467.2151) on Windows 10 64-bit with English locale.

============
Installation
============
Install using pip

pip install opencv-python                                                                                                           pip install pyautogui

you can find in requirements.txt file


============
Usage
============ 
python PBIRefresher.py    
Sample.pbix                                                                                                                       C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe

WHERE
python <py file> is PBIRefresher.py file                                                                                            <.pbix file> is pbix format file, you are going to manipulate with                                                                absolute path to PBIDesktop.exe> is the full path to the pbix exe file to run

Keep in mind that that user of pbix should be logged in order to be able to publish it.                                             Please keep in mind that this script uses GUI of Power BI Desktop and it needs that a user is logged in Windows session. 

============
How it works
============

See how it works
https://drive.google.com/file/d/1FOfdqvMdLNUcRwF8KwhmoDWiw97vqNFU/view?usp=sharing

============
Bug reporting
============
Create Github issue. Please write version of your Power BI Desktop, OS and attach command line result and screenshot.
