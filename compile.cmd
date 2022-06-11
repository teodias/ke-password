@ECHO OFF

  pyinstaller --noconfirm --log-level=WARN --clean --onefile --nowindow --add-data="wordlist.txt;." --name ke-password ke-password.pyw

GOTO :EOF