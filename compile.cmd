@ECHO OFF
  scripts\pyinstaller --noconfirm --log-level=WARN --clean --onefile --nowindow --name ke-password --add-data "wordlist.txt:."  ke-password.pyw
GOTO :EOF