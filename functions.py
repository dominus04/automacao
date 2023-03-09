def read_layout():
    print("Cole o layout da etiqueta e aperte CTRL-D:")

    layout = ""
    i = 0

    while True:
        try:
            line = input()
        except EOFError:
            break
        if i > 0:
            layout += "\n" + line
        else:
            layout += line
            i = 1
    return layout.encode().hex()


def read_varname():
    return input("Digite o nome da variavel: ")


def read_window():
    return input("Digite o nome da janela com todos os detalhes: ")


def set_layout(layout, var_name, window_name, Key=None):
    import win32gui
    import win32con
    from time import sleep
    from pynput.keyboard import Key, Controller

    main_window = win32gui.FindWindow(None, window_name)
    child_window = win32gui.GetWindow(main_window, win32con.GW_CHILD)
    win32gui.SetForegroundWindow(child_window)

    keyboard = Controller()
    var_sub = "?".encode().hex()
    cnt_var = 0

    for i in range(0, len(layout), 4):
        try:

            hex1 = str(layout[i])
            hex2 = str(layout[i + 1])
            hex3 = str(layout[i + 2])
            hex4 = str(layout[i + 3])
            char1 = hex1 + hex2
            char2 = hex3 + hex4

            script = str(cnt_var)
            keyboard.press("m")
            keyboard.press("O")
            keyboard.press("V")
            keyboard.press(" ")
            keyboard.press("#")
            sleep(0.1)
            keyboard.press(hex1)
            sleep(0.1)
            keyboard.press(hex2)
            sleep(0.1)
            keyboard.press(hex3)
            sleep(0.1)
            keyboard.press(hex4)
            sleep(0.1)
            keyboard.press(" ")
            for letter in var_name:
                sleep(0.1)
                keyboard.press(letter)
            keyboard.press("[")
            for n in range(len(script)):
                sleep(0.1)
                keyboard.press(script[n])
            keyboard.press("]")
            keyboard.press(Key.enter)
            keyboard.press(Key.end)
            if cnt_var % 79 == 0 and cnt_var != 0:
                keyboard.press(Key.down)
            sleep(0.5)
            cnt_var += 1

        except IndexError:
            hex1 = str(layout[i])
            hex2 = str(layout[i + 1])
            script = str(cnt_var)

            keyboard.press("m")
            keyboard.press("O")
            keyboard.press("V")
            keyboard.press(" ")
            keyboard.press("#")
            sleep(0.1)
            keyboard.press(hex1)
            sleep(0.1)
            keyboard.press(hex2)
            keyboard.press(" ")
            for letter in var_name:
                sleep(0.1)
                keyboard.press(letter)
            keyboard.press("[")
            for n in range(len(script)):
                sleep(0.1)
                keyboard.press(script[n])
            keyboard.press("]")
            keyboard.press(Key.enter)
            sleep(0.5)
            keyboard.press(Key.enter)
            keyboard.press(Key.end)
            sleep(0.5)
            cnt_var += 1




