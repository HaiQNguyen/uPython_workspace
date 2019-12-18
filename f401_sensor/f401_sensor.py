'''
Author Nguyen Quang Hai
'''
from machine import I2C

i2c_devices = {}

i2c = I2C(scl=machine.Pin('B8'), sda=machine.Pin('B9'),freq=400000)	
htu21_addr=0x40
found_sensor = False
cmd={}

class HTU21():
	def __ini__(self):
		print("HTU21 sensor")
	
	def reset(self):
		cmd = bytearray(1)
		cmd[0] = 0xFE
		i2c.writeto(htu21_addr, cmd)		
		pyb.delay(1000)
	
	def get_user_reg(self):
		reg = 0xE7
		resp = bytearray(1)
		i2c.readfrom_mem_into(htu21_addr, reg, resp)
		return resp[0]

	def get_raw_temperature(self):
		cmd = bytearray(1)
		cmd[0] = 0xE3
		resp = bytearray(3)
		i2c.writeto(htu21_addr, cmd)
		pyb.delay(100)
		i2c.readfrom_into(htu21_addr, resp)
		print(resp[0])
		print(resp[1])
		print(resp[2])

	def get_hum_raw(self):		
		cmd = bytearray(1)
		cmd[0] = 0xE5
		resp = bytearray(3)
		i2c.writeto(htu21_addr, cmd)
		pyb.delay(100)
		i2c.readfrom_into(htu21_addr, resp)
		return ((resp[0] << 8 | resp[1]))
def main():
	i2c_devices = i2c.scan()
	
	print('sensor list:')
	
	for address in i2c_devices:
		if address == 0x76:
			found_sensor = True
			print('Found MS5637')
		if address == 0x40:
			found_sensor = True
			print('Found HTU21')
	
	if found_sensor == False:
		print('No sensors found')
		quit()

	htu21 = HTU21()
	htu21.reset()
	print(hex(htu21.get_user_reg()))
	print(htu21.get_hum_raw())	
		
main()
