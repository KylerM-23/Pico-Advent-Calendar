import machine, struct, time

Device_ID 	= 0x7500
    
'''REGISTER MAP'''
Temp_Result_Reg = 0x00
Config_Reg		= 0x01
Low_Limit_Reg	= 0x02
High_Limit_Reg 	= 0x03
Device_ID_Reg 	= 0x0F

'''Conversion Mode'''
Continuous_Mode	= 0x00
One_Shot_Mode	= 0x01
Shutdown_Mode 	= 0x03

'''Conversion Rates'''
CR_27p5_ms 	= 0x00
CR_55_ms	= 0x01
CR_110_ms	= 0x02
CR_220_ms	= 0x03

'''Fault Values'''
Fault_1	= 0x00
Fault_2	= 0x01
Fault_3	= 0x02
Fault_4	= 0x03

'''Alert Polarity'''
Active_Low = 0x00
Active_High = 0x01

'''Alert Function'''
Alert_Comparator = 0x00
Alert_Interrupt  = 0x01
    
class TMP1075:
    SDA_Pin 	= None
    SCL_Pin 	= None
    i2c 		= None
    I2C_Addr	= None
    
    def __init__(self, i2c_obj = None, i2c_addr = 0, sda = 0, scl = 0, port = 0, freq = 400000):
        self.I2C_Addr = i2c_addr
        
        if i2c_obj == None:
            self.SDA_Pin = machine.Pin(sda)
            self.SCL_Pin = machine.Pin(scl)
            self.i2c 	 = machine.I2C(port, sda = self.SDA_Pin, scl = self.SCL_Pin, freq = freq)
        else:
            self.i2c = i2c_obj

    def reg_write(self, reg, data):
        #
        
    def reg_read(self, reg, nbytes = 2):
        #
    
    def check_device_id(self, return_id = False):
        #
    
    def convert_temp_to_bin(self, temp,  bits = 12):
        #
    
    def convert_bin_to_temp(self, data, bits = 12):
        #
        
    def get_temp(self, unit = 'C'):
        #
    
    def config(self, mode = Continuous_Mode, conversion = CR_55_ms,  fault = Fault_1,
               polarity = Active_Low, alert_func = Alert_Comparator):
        
        #
    
    def set_limits(self, high_limit = None, low_limit = None):
        if (high_limit != None):
            data = self.convert_temp_to_bin(high_limit)
            data << 4
            self.reg_write(High_Limit_Reg, data)
            
        if (low_limit != None):
            data = self.convert_temp_to_bin(low_limit)
            data << 4
            self.reg_write(Low_Limit_Reg, data)
    
if __name__ == "__main__":
    tmp = TMP1075(i2c_addr = 0x48, sda = 0, scl = 1)
    tmp.config(mode = Continuous_Mode)
    unit = 'F'
    print(tmp.check_device_id(True))
    while True:
        print(tmp.get_temp(unit), unit)
        time.sleep(1)
