from pycm import *

console(BLE)

rpi.mode(2)

DXL(1).mode(const.WHEEL)#wheel
DXL(2).mode(const.WHEEL)#wheel
DXL(5).mode(const.JOINT)#position
DXL(1).torque_on()
DXL(2).torque_on()
DXL(5).torque_on()

#가로해상도의절반값을구하고정수로변환하여변수center_x에저장
center_x=int(rpi.resolution_w()/2)

while True:
    DXL(5).goal_position(2500)
    x=rpi.position_x()
    if x>0:
        if x>center_x:
            DXL(1).goal_velocity(0)
            DXL(2).goal_velocity(200)
            diff=x-center_x
            print('[|',diff,']',sep='')
        else:
            DXL(1).goal_velocity(-200)
            DXL(2).goal_velocity(0)
            diff=center_x-x
            print('[',diff,'|]',sep='')
        buzzer.note(20,100)
        buzzer.wait()
    else:
        DXL(1).goal_velocity(0)
        DXL(2).goal_velocity(0)
