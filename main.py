Web VPython 3.2
x=box(size = vec(160,90,23),color=vec((255)/255, (133)/255, (144)/255))
z=box(size = vec(130,75,25),pos = vec (-6.5,1.5,0))
y=box(size = vec(135,80,24.5),pos = vec (-6.5,1.5,0),color=vec((182)/255, (44)/255, (55)/255))

board = compound([x,z,y])

==== 분필이 ===
bunpel = group()

body=cylinder(pos = vec(-85,10,15),size = vec(30,7,7),axis=vec(0, 1, 0),group=bunpel)
eye=sphere(pos = vec(-87,34,18),color=vec((0)/255, (0)/255, (0)/255),group=bunpel)
eyet=sphere(pos = vec(-83,34,18),color=vec((0)/255, (0)/255, (0)/255),group=bunpel)
a=ellipsoid(pos=vec(-82,32,18), length=3.5, height=2, width=2, color=vec((249)/255, (165)/255, (158)/255),group=bunpel)
b=ellipsoid(pos=vec(-88,32,18), length=3.5, height=2, width=2, color=vec((249)/255, (165)/255, (158)/255),group=bunpel)
ink=box(pos = vec(-85,11,6),size = vec(1,1,1),color=vec(1,1,1),make_trail=False)

=== 깔공 추가 ===

RR = sphere(pos=vector(70, 35, 10), radius=7, color=color.red)
BB = sphere(pos=vector(70, 19, 10), radius=7, color=color.blue)
YY = sphere(pos=vector(70, 3, 10), radius=7, color=color.yellow)
GG = sphere(pos=vector(70, -13, 10), radius=7, color=color.green)
EE = sphere(pos=vector(70, -29, 10), radius=7)

=== 움직임 ===

while True:
    rate(100)
    k = keysdown()

    if 'd' in k:
        bunpel.pos.x += 0.5

    if 'a' in k:
        bunpel.pos.x -= 0.5

    if 'w' in k:
        bunpel.pos.y += 0.5

    if 's' in k:
        bunpel.pos.y -= 0.5

    # 위치 맞추기
    ink.pos = bunpel.pos + vec(-85,11,14)

    # z 박스 안에있음?
    in_z = (
        z.pos.x - z.size.x/2 <= ink.pos.x <= z.pos.x + z.size.x/2
        and
        z.pos.y - z.size.y/2 <= ink.pos.y <= z.pos.y + z.size.y/2
    )

    # z 안에서만 trail
    if ' ' in k and in_z:
        ink.make_trail = True
    else:
        ink.make_trail = False

        
    # E 누르면 trail 삭제
    if 'e' in k:
        ink.clear_trail()
     # R red
    if 'r' in k:
        ink.trail_color = color.red
    # B blue
    if 'b' in k:
        ink.trail_color = color.blue
    # y yellow
    if 'y' in k:
        ink.trail_color = color.yellow
    # g green
    if 'g' in k:
        ink.trail_color = color.green

        
