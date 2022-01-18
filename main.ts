let votA = 0
let votB = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    basic.showString("A")
    basic.pause(500)
    basic.clearScreen()
    votA += 1
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    basic.showString("B")
    basic.pause(500)
    basic.clearScreen()
    votB += 1
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    if (votA > votB) {
        basic.showString("A castiga cu ")
        basic.showNumber(votA)
        basic.pause(500)
        basic.clearScreen()
        basic.showString("B pierde cu ")
        basic.showNumber(votB)
    } else if (votB > votA) {
        basic.showString("B castiga cu ")
        basic.showNumber(votB)
        basic.pause(500)
        basic.clearScreen()
        basic.showString("A pierde cu ")
        basic.showNumber(votA)
    } else {
        basic.showString("Egalitate la voturi")
        basic.showNumber(votA)
    }
    
})
