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
        msg = bytearray()
        msg.append(data)
    
        self.i2c.writeto_mem(self.I2C_Addr, reg, msg)
        
    def reg_read(self, reg, nbytes = 2):
        data = self.i2c.readfrom_mem(self.I2C_Addr, reg, nbytes)
        return struct.unpack('>h', data)[0] #unpack data
    
    def check_device_id(self, return_id = False):
        dev_id = self.reg_read(Device_ID_Reg)
        correct_id = dev_id == Device_ID
        
        if return_id:
            return correct_id, dev_id
        else:
            return correct_id
    
    def convert_temp_to_bin(self, temp,  bits = 12):
        mask = (2**bits)-1

        result = int(temp*16)
        if (result < 0):
            result = ((abs(number) ^ mask) + 1) 
            
        return result & mask
    
    def convert_bin_to_temp(self, data, bits = 12):
        mask = (2**bits)-1
        
        result = data
        if (data >> (bits-1)) & 0x01:
            result = ((data- 1) ^ mask) & mask
            result *= -1
    
        return result/16
        
    def get_temp(self, unit = 'C'):
        temp_read = self.reg_read(Temp_Result_Reg)
        temp_read = temp_read >> 4
        temperature = self.convert_bin_to_temp(temp_read)
        
        if (unit == 'K'):
            temperature = temperature + 273.15
        elif (unit == 'F'):
            temperature = (temperature * 9/5) + 32
        return temperature
    
    def config(self, mode = Continuous_Mode, conversion = CR_55_ms,  fault = Fault_1,
               polarity = Active_Low, alert_func = Alert_Comparator):
        
        config_value = (((mode & 0x01) << 15) + ((conversion & 0x03 ) << 13) + ((fault & 0x03) << 11) +
                        ((polarity & 0x01) << 10) + ((mode & 0x01)<< 8))
        
        self.reg_write(Config_Reg, config_value)
        return
    
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