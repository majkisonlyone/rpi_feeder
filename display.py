from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time


class Display:
    I2C_ADDR = 0x27
    I2C_NUM_ROWS = 2
    I2C_NUM_COLS = 16
    lcd = I2cLcd(1, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    
    def print_state(self, is_activated, is_pressed):
        self.lcd.clear()
        if (is_activated):
            self.lcd.putstr("ON")
        else:
            self.lcd.putstr("OFF")
            
        if (is_pressed):
            self.lcd.putstr(" FILLED")
        else:
            self.lcd.putstr(" EMPTY")
        time.sleep(0.2)
