def on_button_pressed_a():
    global A2
    if A1 >= 1:
        basic.show_string("You won £")
        basic.show_string("" + str((A1)))
        basic.show_string("!")
    else:
        A2 = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if A2 == 1:
        basic.show_string("lol you thought")
input.on_button_pressed(Button.B, on_button_pressed_b)

A2 = 0
A1 = 0
A1 = randint(0, 10)
if A1 >= 5:
    basic.show_string("you lost ha")
    A1 = 0
else:
    basic.show_string("no how win hax")
    A1 = randint(1, 100000000)