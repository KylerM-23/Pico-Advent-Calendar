from machine import Pin
import time

class Button_Matrix:
    matrix_pin_num = []
    matrix_pins_obj = []		#Pin Objects
    
    rows = 0
    cols = 0

    def __init__(self, pin_matrix):
        try:
            self.rows = len(pin_matrix)
            self.cols = len(pin_matrix[0])
            self.matrix_pin_num = pin_matrix
        except:
            raise Exception("Error in matrix formatting.")
        
        row_list = []
        col_list = []
        
        for row in range(self.rows):
            col_list = []
            for col in range(self.cols):
                col_list.append(Pin(self.matrix_pin_num[row][col], Pin.IN, Pin.PULL_UP))
            self.matrix_pins_obj.append(col_list)
        
    def get_input(self, row, col):
        return self.matrix_pins_obj[row][col].value()
    
if __name__ == '__main__':    # Program entrance
    print ('Demo Code for Button Matrix')
    Buttons = Button_Matrix(pin_matrix = [[11,8], [12,13]])
    while True:
        time.sleep(1)
        for row in range(2):
            for col in range(2):
                print("Row", row, "Col", col, "Value:", Buttons.get_input(row, col))
        print()