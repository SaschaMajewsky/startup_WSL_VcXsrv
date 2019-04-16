A tiny tool that automates the tedious task of
booting up the vcxsrv, going into your WSL and 
establishing a connection to your server.

**Demo:** <br />
![](demo.gif)

**Features:** <br />
-automatically opens up your WSL Ubuntu with a GUI <br />
-copy and paste between machines is enabled

**Requirements:** <br />
-Windows 10 build 16215 or later <br />
-Ubuntu 16.04 or later installed on your WSL <br />
-xfce4 installed on your Ubuntu WSL <br />
-vcxsrv installed on your Windows 10 host machine <br />

**Info:** <br />
-usage via execution of the startup_wsl_and_vcxsrv.py or the binary. <br />
-the binary needs to be in the root directory of the project
-all used libs are installed in the bundled venv <br />
-to access the venv under windows use venv\Scripts\activate
-used libs are listed in the requirements.txt