# 구현과정 설명

## 1단계

지도데이터 문자열을 2차원 배열로 변환 저장     
배열을 통홰 가로크기, 세로크기, 구멍의 수, 공의 수, 플레이어 위치 출력   

## 2단계

check_block 을 통해 block 확인    
print_map 으로 P위치 변환 후 지도 출력     

## 3단계

check_block - block 확인     
move_o - w,a,s,d 에 따라 o 움직임 , block, o, 0일 경우, 밀 수 없음 (if 로 나타냄 -> not in 한줄 요약 가능)      
print_map - O_trace 를 통해 P 가 지나갔더라도 다시 나타남     
check_all_0 - 모든 O가 0 이 됨을 확인    
divide_0_to_o - 0 을 밀면, 다시 o 가 나타남, w,a,s,d 에 따라 다르게 나타남      
main - w,a,s,d 에 따라 다르게 반복 -> 해결방안이 필요, method or  class 를 사용해야        

![image](https://user-images.githubusercontent.com/73508138/144965299-d8bb53b8-fb07-4d7c-a0ac-5aed2585400e.png)  
  
## 4단계

save, undo, redo 를 파악하기 위해 project class 생성       
save - pickle 로 sokoban class Object 저장   
undo, redo - stack으로 저장 후 불러오기   

###구현
save  
![image](https://user-images.githubusercontent.com/73508138/145016438-a8cf3935-225a-4980-b4d3-9c0c8ac40db7.png)
   
undo, redo

![image](https://user-images.githubusercontent.com/73508138/145016564-f819d4fc-244e-4e8c-99bc-a85404689f0b.png)



### 지도 데이터 변환하기 프로그램  
문제 이해를 하지 못하여 코딩 하지 못함      

# game_python
