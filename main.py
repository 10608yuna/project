Web VPython 3.2
box(size = vec(160,90,3),color=vec((255)/255, (133)/255, (144)/255))
box(size = vec(130,75,5)compound([body, head], pos=vector(0, 0, 0)))
box(size = vec(135,80,4.5),pos = vec (-6.5,1.5,0),color=vec((182)/255, (44)/255, (55)/255))

==== 분필이 ===
body=cylinder(pos = vec(200,10,8),size = vec(30,7,7),axis=vec(0, 1, 0))
eye=sphere(pos = vec(200,10,8),color=vec((0)/255, (0)/255, (0)/255),pos = vec(202,34,13))
eyet=sphere(pos = vec(200,10,8),color=vec((0)/255, (0)/255, (0)/255),pos = vec(198,34,13))
a=ellipsoid(pos=vec(203,32,11), length=3.5, height=2, width=2, color=vec((249)/255, (165)/255, (158)/255))
b=ellipsoid(pos=vec(197,32,11), length=3.5, height=2, width=2, color=vec((249)/255, (165)/255, (158)/255))
ink=box(pos = vec(200,10.3,10),size = vec(4,4,4),color=vec((0)/255, (0)/255, (0)/255),(make_trail=True))
bunpel = compound([body,eye,eyet,a,b,ink], pos=vector(-90, 0, 6))

=== 움직임 ===
while True :
    rate(100)
    k = keysdown()
    if 'd' in k : 
        bunpel.pos.x = bunpel.pos.x + 0.5
    if 'a' in k : 
        bunpel.pos.x = bunpel.pos.x + -0.5
    if 'w' in k : 
        bunpel.pos.y = bunpel.pos.y + 0.5
    if 's' in k : 
        bunpel.pos.y = bunpel.pos.y + -0.5

==== 선 그리기 ===

        
        
