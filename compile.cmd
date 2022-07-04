@ECHO OFF
  scripts\pyinstaller --noconfirm --log-level=WARN --clean --onefile --nowindow --name ke-password ke-password.pyw
GOTO :EOF