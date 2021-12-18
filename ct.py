import time
from pygame import mixer

def play_sound():
    mixer.init()
    mixer.music.load("sn.mp3")
    mixer.music.play()
    while mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)

    play_sound()    

play_sound()


with open('ct.txt') as f:
    lines = f.readlines()

horizontal, deep = 0, 0

for line in lines:
    line = list(line.split(" "))
    if line[0] == "forward":
        horizontal += int(line[1])
    elif line[0] == "up":
        deep -= int(line[1])
    elif line[0] == "down":
        deep += int(line[1])


print(horizontal * deep)


# count = 0
# a = sum(int(ele) for ele in lines[3:])
# for line in lines:
#     print("{} {}".format(a, line))
#     if int(line) > a:
#         count += 1
#     a = int(line)

# count = 0
# while len(lines) >= 4:
#     a = sum(int(ele) for ele in lines[:3])
#     b = sum(int(ele) for ele in lines[1:4])
#     _ = lines.pop(0)
#     if int(b) > int(a):
#         count += 1

# print(count)  

