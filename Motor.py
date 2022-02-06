import CONSTANTS
import serial


class StepMotor:
    port = "COM3"
    baud_rate = 9600

    def __init__(self):
        self.com = serial.Serial()
        self.com.port = self.port
        self.com.baudrate = self.baud_rate
        print("init!")

    def start_motor(self):
        self.com.open()

    def step(self, offset):
        if offset == 0:
            return 0

        if offset < 0:
            self._step_amt(CONSTANTS.STEP_INTERVAL)
            return CONSTANTS.STEP_INTERVAL
        else:
            self._step_amt(-CONSTANTS.STEP_INTERVAL)
            return -CONSTANTS.STEP_INTERVAL

    def _step_amt(self, amount: int):
        self.com.write(str(amount).encode('utf-8'))
        print(amount)
