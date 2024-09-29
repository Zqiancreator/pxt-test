input.onPinPressed(TouchPin.P0, function () {
    basic.showNumber(0)
    motor.servo(motor.Servos.S1, 0)
})
input.onButtonPressed(Button.A, function () {
    motor.servo(motor.Servos.S1, 100)
    basic.showNumber(2)
    basic.showNumber(0)
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.StickFigure)
})
input.onPinPressed(TouchPin.P1, function () {
    basic.showNumber(1)
})
if (true) {
	
}
if (false) {
    led.plot(0, DFRobot_S12SD.readUv())
    basic.showNumber(1111)
}
basic.forever(function () {
	
})
