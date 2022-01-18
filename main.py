votA = 0
votB = 0

def on_button_pressed_a():
    global votA
    basic.show_string("A")
    basic.pause(500)
    basic.clear_screen()
    votA += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global votB
    basic.show_string("B")
    basic.pause(500)
    basic.clear_screen()
    votB += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_ab():
    if votA > votB:
        basic.show_string("A castiga cu ")
        basic.show_number(votA)
        basic.pause(500)
        basic.clear_screen()
        basic.show_string("B pierde cu ")
        basic.show_number(votB)
    elif votB > votA:
        basic.show_string("B castiga cu ")
        basic.show_number(votB)
        basic.pause(500)
        basic.clear_screen()
        basic.show_string("A pierde cu ")
        basic.show_number(votA)
    else:
        basic.show_string("Egalitate la voturi")
        basic.show_number(votA)
input.on_button_pressed(Button.AB, on_button_pressed_ab)
