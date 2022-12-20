
def rgb(r, g, b):
    return (r, g, b)

def rgb2(rgb):
    return (int(rgb[0:2], 16), int(rgb[2:4], 16), int(rgb[4:6], 16))

def rgb_to_str(rgb):
    return "{:02X}{:02X}{:02X}".format(rgb[0], rgb[1], rgb[2])

def _interpolate(x0, x1, step, steps):
    x = 0.0
    x += (float(x0)) * ((steps - step - 1.0) / (steps - 1.0))
    x += (float(x1)) * ((float(step)) / (steps - 1.0))
    return int(x)

def interpolate_rgb(c0, c1, step, steps):
    return (
        _interpolate(c0[0], c1[0], step, steps),
        _interpolate(c0[1], c1[1], step, steps),
        _interpolate(c0[2], c1[2], step, steps)
    )

square = [([(0, 0, 0)] * 8) for i in range(0, 7)]

square[0][0] = rgb2("005DFF")
square[0][7] = rgb2("FF00F2")
square[6][0] = rgb2("01FD01")
square[6][7] = rgb2("FD0200")

for i in range(0, 8):
    square[0][i] = interpolate_rgb(square[0][0], square[0][7], i, 8)

for i in range(0, 8):
    square[6][i] = interpolate_rgb(square[6][0], square[6][7], i, 8)

for i in range(0, 7):
    square[i][0] = interpolate_rgb(square[0][0], square[6][0], i, 7)

for i in range(0, 7):
    square[i][7] = interpolate_rgb(square[0][7], square[6][7], i, 7)

# [0,0] [0,1] [0,2] [0,3] [0,4] [0,5] [0,6] [0,7]
# [1,0] [1,1] [1,2] [1,3] [1,4] [1,5] [1,6] [1,7]
# [2,0] [2,1] [2,2] [2,3] [2,4] [2,5] [2,6] [2,7]
# [3,0] [3,1] [3,2] [3,3] [3,4] [3,5] [3,6] [3,7]
# [4,0] [4,1] [4,2] [4,3] [4,4] [4,5] [4,6] [4,7]
# [5,0] [5,1] [5,2] [5,3] [5,4] [5,5] [5,6] [5,7]
# [6,0] [6,1] [6,2] [6,3] [6,4] [6,5] [6,6] [6,7]

for i in range(1, 6):
    for j in range(1, 7):
        # print("({},{}): ({},{})->({},{}) step {} of {}, ({},{})->({},{}) step {} of {}".format(
        #    i, j,
        #    i, 0, i, 7, j, 8,
        #    0, j, 6, j, i, 7
        #))
        c0 = interpolate_rgb(square[i][0], square[i][7], j, 8)
        c1 = interpolate_rgb(square[0][j], square[6][j], i, 7)
        square[i][j] = (int((c1[0]+c0[0])/2.0), int((c1[1]+c0[1])/2.0), int((c1[2]+c0[2])/2.0))

for row in square:
    print([rgb_to_str(col) for col in row])

