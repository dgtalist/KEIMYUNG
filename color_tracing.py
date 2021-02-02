from pycm import *

console(BLE)

rpi.mode(1) # 1-색상인식, 2-얼굴인식, 3-스트리밍
rpi.sub_mode(1)  # 1-빨강, 2-오렌지, 3-노랑, 4-초록, 5-파랑, 6-보라, 7-흰색

DXL(1).mode(const.WHEEL)#wheel
DXL(2).mode(const.WHEEL)#wheel
DXL(5).mode(const.JOINT)#position
DXL(1).torque_on()
DXL(2).torque_on()
DXL(5).torque_on()

#가로해상도의절반값을구하고정수로변환하여변수center_x에저장
center_x=int(rpi.resolution_w()/2)
speed= 70
while True:
    DXL(5).goal_position(2500)
    x=rpi.position_x()
    if x>0 :
        if x>center_x: # 인식위치가 중앙보다 오른쪽
            speed_r=x-center_x  # 중앙과 위치차이값
            speed_r=speed_r*2  # 중앙과 위치차이값에 *2를 해서 속도에 더해주기
            DXL(1).goal_velocity(-speed)
            DXL(2).goal_velocity(speed+speed_r)
            diff=x-center_x
            print('[|',diff,']',sep='')
        elif x < center_x :  # 인식위치가 중앙보다 왼쪽
            speed_l=center_x-x
            speed_l=speed_l*2
            DXL(1).goal_velocity(-speed-speed_l) 
            DXL(2).goal_velocity(speed)
            diff=center_x-x
            print('[',diff,'|]',sep='')
        elif x == center_x :  # 중앙과 인식위치가 같은경우는 speed로 직진
            DXL(1).goal_velocity(-speed)  
            DXL(2).goal_velocity(speed)
    else :
        DXL(1).goal_velocity(0)
        DXL(2).goal_velocity(0)
