Web VPython 3.2
box(size = vec(160,90,3),color=vec((255)/255, (133)/255, (144)/255))
box(size = vec(130,75,5)compound([body, head], pos=vector(0, 0, 0)))
box(size = vec(135,80,4.5),pos = vec (-6.5,1.5,0),color=vec((182)/255, (44)/255, (55)/255))

board = compound([x,z,y])

==== 분필이 ===
bunpel = group()

box(size = vec(160,90,3),color=vec((255)/255, (133)/255, (144)/255))
box(size = vec(130,75,5),pos = vec (-6.5,1.5,0))
box(size = vec(135,80,4.5),pos = vec (-6.5,1.5,0),color=vec((182)/255, (44)/255, (55)/255))
body=cylinder(pos = vec(-85,10,7),size = vec(30,7,7),axis=vec(0, 1, 0),group=bunpel)
eye=sphere(pos = vec(-87,34,10),color=vec((0)/255, (0)/255, (0)/255),group=bunpel)
eyet=sphere(pos = vec(-83,34,10),color=vec((0)/255, (0)/255, (0)/255),group=bunpel)
a=ellipsoid(pos=vec(-82,32,10), length=3.5, height=2, width=2, color=vec((249)/255, (165)/255, (158)/255),group=bunpel)
b=ellipsoid(pos=vec(-88,32,10), length=3.5, height=2, width=2, color=vec((249)/255, (165)/255, (158)/255),group=bunpel)
ink=box(pos = vec(-85,11,7),size = vec(1,1,1),color=vec(0.5,1,0),make_trail=True)

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
    ink.pos = bunpel.pos + vec(-85,11,6)

    # 스페이스바 누를 때만 trail
    if ' ' in k:
        ink.make_trail = True
    else:
        ink.make_trail = False
    # E 누르면 trail 삭제
    if 'e' in k:
        ink.clear_trail()
    # R 누르면 trail 색 빨강
    if 'r' in k:
        ink.trail_color = color.red
    # B 누르면 trail 색 blue
    if 'b' in k:
        ink.trail_color = color.blue
    # y 누르면 trail 색 빨강
    if 'y' in k:
        ink.trail_color = color.yellow

        
