from ursina import *

app = Ursina()

window.title = "3D Chess Game"
window.borderless = False
window.fullscreen = False

# Camera
camera.position = (4, 10, -10)
camera.rotation_x = 45

# Board colors
light_color = color.rgb(240, 217, 181)
dark_color = color.rgb(181, 136, 99)

board = []

# Create 8x8 chessboard
for x in range(8):
    for z in range(8):
        square_color = light_color if (x + z) % 2 == 0 else dark_color

        square = Button(
            model='cube',
            color=square_color,
            scale=(1, 0.1, 1),
            position=(x, 0, z)
        )

        board.append(square)

# Example chess pieces
white_pawn = Entity(
    model='sphere',
    color=color.white,
    scale=0.5,
    position=(0, 0.5, 1)
)

black_pawn = Entity(
    model='sphere',
    color=color.black,
    scale=0.5,
    position=(0, 0.5, 6)
)

# Light
DirectionalLight()
AmbientLight(color=color.rgba(100, 100, 100, 0.5))

app.run()