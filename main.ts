input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (A1 >= 1) {
        basic.showString("You won £")
        basic.showString("" + ("" + A1))
        basic.showString("!")
    } else {
        A2 = 1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    if (A2 == 1) {
        basic.showString("lol you thought")
    }
    
})
let A2 = 0
let A1 = 0
A1 = randint(0, 10)
if (A1 >= 5) {
    basic.showString("you lost ha")
    A1 = 0
} else {
    basic.showString("no how win hax")
    A1 = randint(1, 100000000)
}

