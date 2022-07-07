# ke-password
password generator

I developed this app to help my users for finding easy memorable and secure passwords.

In the past my users tend to put personal information in their passwords like husband name, childrens date of birth or pet name.
This type of information can be guessed by social engineering and in my opinion it's not a good base for using in passwords.
Also after beeing forced by a domain policy to change this after a quite short time, they get confused about the similiarity of their own choosen passwords.
Was it pet's name and then child's DOB ? Or vice versa?
Moreover, after implementing a policy with password history (the servers remember the last used 5 or 10 passwords) the users had to try many passwords before the server accepted it.
And guess what happened next day? They were so confused about trying 5-6 passwords they do not remember which one was accepted by the system...

So here comes my attempt to help:
This app creates a password from a wordlist with symbols, numbers and an optional lowercase char.
There are no personal information in this password and it's not to hard to remember it.
The safety aspect is not the complexity of the password (brute force algorithms are not getting confused by short but very complex passwords ;) only humans do :D) it's the lentgh of the password.
This passwords can get quite long but are still easy to remember.
In my opinion longer passwords are ways better then shorter and complexer ones.

# requirements
- You need python installed
- You need git installed

# download
1. Open a terminal in your projects folder
2. The next step will create the subfolder 'ke-password' in this folder
3. Clone the repository with:  
```git clone https://github.com/teodias/ke-password.git```

# virtual environment
You might want to create a virtual environment with:  
```python.exe -m venv 'drive:\path\to\ke-password' --copies --upgrade-deps```
Remember to activate this on every use  from the ke-password\scripts folder!

# modules
Now you can install the needed modules with:  
```pip install -r requirements.txt```
This project use only pysimplegui and pyinstaller at the moment.
As my IDE has pylint and flake implemented (it's Spyder IDE from the winpython distribution), I don't need those modules in the project environment.

You can check the successfull installation of the modules with:  
```pip list``` or ```pip check```

# build the Windows app
With the `compile.cmd` you can create an EXE file to run this app without a separately installed python compiler.


contact me for any suggestions or questions,  
Teo