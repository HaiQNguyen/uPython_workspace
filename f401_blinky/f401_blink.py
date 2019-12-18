
led0 = pyb.Pin('PA5',pyb.Pin.OUT_PP)
led1 = pyb.Pin('PA1',pyb.Pin.OUT_PP)
led2 = pyb.Pin('PA4',pyb.Pin.OUT_PP)
led3 = pyb.Pin('PB0',pyb.Pin.OUT_PP)
led4 = pyb.Pin('PC1',pyb.Pin.OUT_PP)
led5 = pyb.Pin('PC0',pyb.Pin.OUT_PP)

led_strip = [led1, led2, led3, led4, led5]

def running_led(led_strip):
	for led in led_strip:	 
		led.high()
		pyb.delay(100)
		led.low()
		pyb.delay(100)


def audi_turn_signal(led_strip):
	for led in led_strip:	 
		led.high()
		pyb.delay(50)
	pyb.delay(500)
	for led in led_strip:	 
		led.low()
	pyb.delay(200)
	

	
while True:
	running_led(led_strip)
	#audi_turn_signal(led_strip)
