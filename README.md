### Twitter to Discord

📄 Twitter to Discord will allow you to effortlessly send links from Twitter to Discord with previews, just like in the past, using my script and vx proxy. 
Just run the program, and it will work in the tray, converting links from Twitter through the proxy into Discord-friendly links with previews.
The program only responds to links from Twitter, preventing phantom triggers.

![Example](https://github.com/YuriyAvengeR/Twitter-to-Discord/blob/master/images/TwitterDiscord720p.gif)

🍉 **HOW TO USE**

To run the script, download and execute Twitter to Discord.exe. 
Download it in [releases tab](https://github.com/YuriyAvengeR/Twitter-to-Discord/releases).
After that, a white square will appear in the system tray, indicating that the script is active. To close it, right-click and choose 'Close.'

> [!WARNING]
> Windows may notify you that it has protected your PC when running my .exe file due to it being [created through pyinstaller](https://www.reddit.com/r/learnpython/comments/e99bhe/why_does_pyinstaller_trigger_windows_defender/).
> You can click 'More Info' - 'Run anyway' to proceed. Alternatively, check the option below.

> [!CAUTION]
> If you consider running my .exe file unsafe, you can create it yourself.

- Clone my repository and install the libraries from the requirements.txt file.

- Enter the following command in the terminal:
  
_pyinstaller --noconfirm --onefile --windowed --name "Twitter to Discord" "path to python file "tray_version.py"_

Where the path to the python tray_version.py file. 

For example: 

_pyinstaller --noconfirm --onefile --windowed --name "Twitter to Discord" "F:/Twittertodiscordl/tray_version.py"_

- Please wait for the creation of the .exe file based on my script, which you can inspect for malicious code before use. After completion, your .exe file will be in the project directory in the 'dist' folder."

> [!TIP]
> There is also a terminal version available!
Install the libraries corresponding to requirements.txt in your system and download the files 'Terminal.bat' and 'terminal_version.py.' 
Afterward, run 'Terminal.bat.
