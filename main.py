import pyautogui
import time

print('Escolha uma das opções:')
print('1- conta principal')
print('2- conta secundária')
o = int(input('Sua escolha:'))
USERNAME = input("Digite seu username :")
SENHA = input("Digite sua senha: ")
if o == 1 or o == 2:
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.write(r'C:\Users\marco\OneDrive\Desktop\League of Legends.lnk')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(12)
    pyautogui.write(USERNAME)  # coloque seu user da primaria dentro das aspas
    pyautogui.press('tab')
    pyautogui.write(SENHA)  # coloque a senha dentro das aspas
    pyautogui.press('enter')
pass
