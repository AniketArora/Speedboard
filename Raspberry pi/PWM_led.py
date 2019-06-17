from RPi import GPIO


class PWM_led:  # ctrl shift alt jj
    def __init__(self, pin, frequentie) -> None:
        super().__init__()
        self.pin = pin
        self.frequentie = frequentie
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm_led = GPIO.PWM(pin, frequentie)  # frequentie


    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        if isinstance(value, int):
            self.__pin = value
        else:
            raise ValueError

    ####################################
    def dutyCycle(self, waarde):
        self.pwm_led.ChangeDutyCycle(waarde)

    def start(self, waarde):
        self.pwm_led.start(waarde)

    def stop(self):
        self.pwm_led.stop()
####################################
