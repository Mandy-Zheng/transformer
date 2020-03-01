from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()
clear_screen(screen)
parse_file('script',edges,transform,screen,color)
'''parse_file( 'newscript2.txt', edges, transform, screen, color )
big=[]
t=new_matrix()
parse_file('subscript.txt',big,t,screen,color)
t=new_matrix()
p1=[]
t1=new_matrix()
parse_file( 'quad1.txt', p1, t1, screen, color )
p2=[]
t2=new_matrix()
parse_file( 'quad2.txt', p2, t2, screen, color )
p3=[]
t3=new_matrix()
parse_file( 'quad3.txt', p3, t3, screen, color )
p4=[]
t4=new_matrix()
parse_file( 'quad4.txt', p4, t4, screen, color )
p5=[]
t5=new_matrix()
parse_file( 'quad5.txt', p5, t5, screen, color )
p6=[]
t6=new_matrix()
parse_file( 'quad6.txt', p6, t6, screen, color )

for y in range(14):
    clear_screen(screen)
    draw_lines(edges,screen,color)
    t6=make_translate(10,0,0)
    matrix_mult(t6,p6)
    draw_lines(p6,screen,color)
    t5=make_translate(10,10,0)
    matrix_mult(t5,p5)
    draw_lines(p5,screen,color)
    t4=make_translate(-10,10,0)
    matrix_mult(t4,p4)
    draw_lines(p4,screen,color)
    t3=make_translate(-10,0,0)
    matrix_mult(t3,p3)
    draw_lines(p3,screen,color)
    t2=make_translate(-10,-10,0)
    matrix_mult(t2,p2)
    draw_lines(p2,screen,color)
    t1=make_translate(10,-10,0)
    matrix_mult(t1,p1)
    draw_lines(p1,screen,color)
    save_extension(screen,"pic.png")
    if(y<10):
        save_extension(screen,"image00"+str(y)+".png")
    else:
        save_extension(screen,"image0"+str(y)+".png")
clear_screen(screen)
draw_lines(big,screen,color)
save_extension(screen,"image014.png")
scale=1
for x in range(4):
    clear_screen(screen)
    points=big
    matrix_mult(make_translate(-250,-250,0),points)
    b=scale-0.05*(x+1)
    s=make_scale(b,b,b)
    matrix_mult(s,points)
    matrix_mult(make_translate(250,250,0),points)
    draw_lines(points,screen,color)
    save_extension(screen,"image0"+str(x+15)+".png")
clear_screen(screen)
draw_lines(edges,screen,color)
save_extension(screen,"image019.png")'''
