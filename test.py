from PIL import Image, ImageDraw
import os

# Long barge initial live cells
initial_live_cells = {
    (2,0), (3,0),
    (1,1), (4,1),
    (1,2), (5,2),
    (3,3), (4,3)
}

WIDTH = 20
HEIGHT = 20
CELL_SIZE = 20  # pixels per cell
GENERATIONS = 20

def get_neighbors(x, y, live):
    offsets = [(-1,-1),(0,-1),(1,-1),
               (-1,0),       (1,0),
               (-1,1),(0,1),(1,1)]
    return sum((x+dx, y+dy) in live for dx, dy in offsets)

def next_generation(live):
    new_live = set()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            n = get_neighbors(x, y, live)
            if (x, y) in live:
                if n in (2, 3):
                    new_live.add((x, y))
            else:
                if n == 3:
                    new_live.add((x, y))
    return new_live

def draw_board(live):
    img = Image.new("1", (WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE), 1)  # white background
    draw = ImageDraw.Draw(img)

    for x, y in live:
        x0 = x * CELL_SIZE
        y0 = y * CELL_SIZE
        draw.rectangle([x0, y0, x0 + CELL_SIZE - 1, y0 + CELL_SIZE - 1], fill=0)  # black cell

    return img

# Run simulation and collect frames
frames = []
live_cells = initial_live_cells.copy()

for gen in range(GENERATIONS):
    frame = draw_board(live_cells)
    frames.append(frame)
    live_cells = next_generation(live_cells)

# Save animated GIF (black and white)
frames[0].save(
    "long_barge.gif",
    save_all=True,
    append_images=frames[1:],
    duration=200,
    loop=0
)

print("Saved as long_barge.gif")
