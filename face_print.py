
from pycm import *

console(BLE)

rpi.mode(2)

center_x=int(rpi.resolution_w()/2)

while True:
    DXL(5).goal_position(2500)
    x=rpi.position_x()
    if x>0:
        if x>center_x: 
                diff=x-center_x
                print('[|',diff,']',sep='')
        else:
                diff=center_x-x
                print('[',diff,'|]',sep='')

        buzzer.note(20,100)
        buzzer.wait()

    delay(200)
