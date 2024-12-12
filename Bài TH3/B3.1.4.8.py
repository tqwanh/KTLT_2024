import math
pos = [0, 0]
while True:
    s = input("Nhập lệnh di chuyển (hoặc bấm Enter để dừng): ")
    if not s:  
        break
    movement = s.split(" ")
    direction = movement[0].upper()  
    steps = int(movement[1]) 
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
distance = int(round(math.sqrt(pos[0] ** 2 + pos[1] ** 2)))
print(f"Khoảng cách từ vị trí hiện tại đến vị trí ban đầu là: {distance}")
print('Tran Quang Anh, 235752021610095')
