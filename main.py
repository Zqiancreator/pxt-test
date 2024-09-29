def on_pin_pressed_p0():
    basic.show_number(0)
    motor.servo(motor.Servos.S1, 0)
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    motor.servo(motor.Servos.S1, 100)
    basic.show_number(2)
    basic.show_number(0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.STICK_FIGURE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_pin_pressed_p1():
    basic.show_number(1)
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

if True:
    pass
if False:
    led.plot(0, DFRobot_S12SD.read_uv())
    basic.show_number(1111)

def on_forever():
    pass
basic.forever(on_forever)
