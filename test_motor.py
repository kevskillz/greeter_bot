from Motor import StepMotor
import time
motor = StepMotor()
motor.start_motor()
motor._step_amt(1)
time.sleep(5)

x = 2
while x != 0:
    motor._step_amt(30)


    x -= 1

