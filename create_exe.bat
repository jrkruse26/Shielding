pyinstaller -w --onefile shielding.py
rmdir /q /s build
rmdir /q /s __pycache__
del shielding.spec
move dist\shielding.exe C:\Users\Jordan\Documents\GitHub\shielding
rmdir /q /s dist