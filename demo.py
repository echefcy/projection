import arcade
import pos
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "hi"

# top 4 vertex
v1 = pos.Position(1,1,1)
v2 = pos.Position(-1,1,1)
v3 = pos.Position(-1,1,-1)
v4 = pos.Position(1,1,-1)
# bottom 4 vertex
v5 = pos.Position(1,-1,1)
v6 = pos.Position(-1,-1,1)
v7 = pos.Position(-1,-1,-1)
v8 = pos.Position(1,-1,-1)
vertices = [v1,v2,v3,v4,v5,v6,v7,v8]
offsetx = 400
offsety = 400

# spinning cube
def draw(_delta_time):

    arcade.start_render()
    for i in range(len(vertices)):
        draw.theta += 0.005
        vec = vertices[i].rotateY(draw.theta).cam_transform([[0],[0],[5]]).project(l=-0.5,r=0.5,t=0.5,b=-0.5,n=2,f=8)
        vec = pos.Position.to_screen(vec, 0, 0, 800, 800)
        arcade.draw_circle_filled(vec[0],vec[1],5,arcade.color.BLACK)

draw.theta = 0
    

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    arcade.schedule(draw, 1/60)

    arcade.run()

    arcade.close_window()

if __name__ == "__main__":
    main()
