import arcade
import pos
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "cube projection"

camera = pos.Position.VCam().rotateX(0.54630248984).translate(0, 2.5, 5)
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
transformation = [v1,v2,v3,v4,v5,v6,v7,v8]
offsetx = 400
offsety = 400

# spinning cube
def draw(_delta_time):

    arcade.start_render()
    for i in range(len(vertices)):
        draw.theta += 0.004
        transformation[i] = vertices[i].rotateY(draw.theta).cam_transform(camera).project(l=-0.5,r=0.5,t=0.5,b=-0.5,n=2,f=8)
        transformation[i] = pos.Position.to_screen(transformation[i], 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
        arcade.draw_circle_filled(transformation[i][0],transformation[i][1],5,arcade.color.BLACK)
    arcade.draw_line(transformation[0][0],transformation[0][1], transformation[1][0],transformation[1][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[1][0],transformation[1][1], transformation[2][0],transformation[2][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[2][0],transformation[2][1], transformation[3][0],transformation[3][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[3][0],transformation[3][1], transformation[0][0],transformation[0][1], arcade.color.BLACK, 1)

    arcade.draw_line(transformation[4][0],transformation[4][1], transformation[5][0],transformation[5][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[5][0],transformation[5][1], transformation[6][0],transformation[6][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[6][0],transformation[6][1], transformation[7][0],transformation[7][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[7][0],transformation[7][1], transformation[4][0],transformation[4][1], arcade.color.BLACK, 1)

    arcade.draw_line(transformation[0][0],transformation[0][1], transformation[4][0],transformation[4][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[1][0],transformation[1][1], transformation[5][0],transformation[5][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[2][0],transformation[2][1], transformation[6][0],transformation[6][1], arcade.color.BLACK, 1)
    arcade.draw_line(transformation[3][0],transformation[3][1], transformation[7][0],transformation[7][1], arcade.color.BLACK, 1)

draw.theta = 0
    

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    arcade.schedule(draw, 1/60)

    arcade.run()

    arcade.close_window()

if __name__ == "__main__":
    main()
