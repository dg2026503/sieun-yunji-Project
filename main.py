
Web VPython 3.2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

body= sphere(pos=vec(0, 0, 0), radius=7, color=color.green)
eye1= sphere(pos=vec(3, 2, 6), radius=0.7, color=color.black)
eye2= sphere(pos=vec(-3, 2, 6), radius=0.7, color=color.black)
lip1= ellipsoid(pos=vec(0, 0, 6), length=6, height=2, width=15, color = vec(0,0.816,0))
lip2= ellipsoid(pos=vec(0, -0.5, 6), length=6, height=2, width=15, color = vec(0,0.816,0))
cheek1= sphere(pos=vec(3, 0, 4.2), radius=2.2,  color = vec(0.816,0.816,0))
cheek2= sphere(pos=vec(-3, 0, 4.2), radius=2.2,  color = vec(0.816,0.816,0))
j = compound([body,eye1, eye2, lip1, lip2, cheek1, cheek2])

ring1= ring(pos=vec(7, 7, 0), axis=vec(5, 0, 0), radius = 15, thickness = 0.2, color = vec(1.02,0,0.508))
ring2= ring(pos=vec(25, 14, 0), axis=vec(5, 0, 0), radius = 15, thickness = 0.2, color = vec(1.02,0,0.508))
ring3= ring(pos=vec(50, 20, 0), axis=vec(5, 0, 0), radius = 15, thickness = 0.2, color = vec(1.02,0,0.508))


while True :
    rate(100)
    k = keysdown()
    if 'left' in k :
        j.pos.x = j.pos.x - 1
    if 'right' in k :
        j.pos.x = j.pos.x + 1
    if 'up' in k :
        j.pos.y = j.pos.y + 1
    if 'down' in k :
        j.pos.y = j.pos.y - 1
    if 'z' in k :
        j.pos.z = j.pos.z + 1
    if 'x' in k :
        j.pos.z = j.pos.z - 1

