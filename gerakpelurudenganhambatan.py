y = 0
v = 50
sudut = 35
deltat = 0.01
x = 0
g = -9.8
t = 0

d = 0.0013
m = 0.15

while True :
    print(x,y)

    t = t + deltat
    ax = -(d/m) * v * vx
    ay = g - (d/m) * v * vy
    vx = vx + (ax*deltat)
    vy = vy + (ay*deltat)
    y = y + (vy * deltat)
    x = x + (vx * deltat)
    v = math.sqrt(vx**2+vy**2)

    if y < 0:
        break

# Dibawah dipake untuk melakukan simulasi (menggunakan anaconda -> JupyterLab)
# def solusi_numerik_hambatan(y,v,sudut):
#     deltat = 0.01
#     x = 0
#     g = -9.8
#     t = 0

#     d = 0.0013
#     m = 0.15

#     x_arr_num_hambatan = []
#     y_arr_num_hambatan = []

#     vx = v * math.cos(math.radians(sudut))
#     vy = v * math.sin(math.radians(sudut))

#     while True :
#         x_arr_num_hambatan.append(x)
#         y_arr_num_hambatan.append(y)

#         t = t + deltat
#         ax = -(d/m) * v * vx
#         ay = g - (d/m) * v * vy
#         vx = vx + (ax*deltat)
#         vy = vy + (ay*deltat)
#         y = y + (vy * deltat)
#         x = x + (vx * deltat)
#         v = math.sqrt(vx**2+vy**2)

#         if y < 0:
#             break
#     return x_arr_num_hambatan,y_arr_num_hambatan
    
    
# x_arr_num_hambatan,y_arr_num_hambatan = solusi_numerik_hambatan(0,50,35)

# plt.plot(x_arr_num_hambatan,y_arr_num_hambatan)