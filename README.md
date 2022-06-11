[TOC]

# ke-password
password generator

I developed this app to help my users for finding easy memorable and secure passwords.

In the past my users tend to put personal information in their passwords like husband name, childrens date of birth or pet name.
This type of information can be guessed by social engineering and in my opinion it's not a good base for using in passwords.
Also after beeing forced by a company polica to change this after some weeks, they get confused about the similiarity of ther own chossen passwords.
Was it pet's name and then child's DOB ? Or vice versa?
Moreover, after implementing a policy with password history (the servers remeber the last used 5 or 10 passwords) the user's had to try many passwords before the server accepted it.
And guess what happened next day? They were so confused about trying 5-6 password they do not remember which one was accepted by the system...

So here comes my attempt to help them.
This app creates a password from a wordlist with symbols, numbers and an optional lowercase char.
There are no personal information in this password and it's not to hard to remember it.
The safety aspect is not the complexity of the password (brute force algorithms are not getting confused by complexity ;) only humans do :D) it's the lentgh.
This passwords can get quite long but are still easy to remember.
In my opinion longer passwords are ways better then shorter and complexer ones.

# requirements
- You need python installed: Find any distri suiting your needs. I personally like PySchool-slim from SourceForge.
- You need git installed: I prefer the portable package, but you choose what's the best for you.

# download

1. Open a terminal in your projects folder
2. The next step will create the subfolder 'ke-password' in this folder
3. Clone the repository with:  
```git clone https://github.com/teodias/ke-password.git```

# virtual environment
you might want to create a virtual environment with:  
```python.exe -m venv 'drive:\path\to\kee-password' --copies --upgrade-deps```

Remember to activate this everytime you use it from the scripts folder!

# modules
Now you can install the needed modules with:  
```pip install pysimplegui pyinstaller```

and check the successfull installation with:  
```pip list```

# build the Windows app
With the `compile.cmd` you can create the EXE file to run this app with a python developing environment.


contact me for any suggestions or questions,
Teo