import os

X_OFFSET = 0
Y_OFFSET = 300
def str_to_pair(string):
    s = string.split(',')
    x = float(s[0]) * 3.78
    y = float(s[1]) * 3.78
    return x, y

def draw_path(string):
    coords = string.split(' ')
    loop = False
    if coords[-1] == 'z':
        loop = True
        coords.pop(-1)
    x1, y1 = str_to_pair(coords[0])
    x1 = x1+ X_OFFSET
    y1 = y1 + Y_OFFSET

    startx1, starty1 = x1, y1
    coords.pop(0)
    for coord in coords:
        if ',' in coord:
            x2delta, y2delta = str_to_pair(coord)
            x2 = x1 + x2delta
            y2 = y1 + y2delta
            os.system(f'adb shell input touchscreen swipe {x1} {y1} {x2} {y2}')
            x1 = x2
            y1 = y2
    if loop:
        os.system(f'adb shell input touchscreen swipe {x1} {y1} {startx1} {starty1}')

with open('cashcard.svg') as f:
    lines = [line.strip() for line in f.readlines()]
    for line in lines:
        if line.startswith('d="m '):
            draw_path(line.replace('d="m ','').replace('"',''))