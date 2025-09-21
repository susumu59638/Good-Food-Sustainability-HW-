import random
import pgzrun

WIDTH, HEIGHT = 800, 600
TITLE = "Good Food "
CENTER_X = 400
CENTER_Y = 300
CENTER = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["coke", "friedchicken", "burger", "fries"]

current_lvl = 1
game_over = False
game_end = False

items = []
animations = []

def draw():
    screen.clear()
    screen.blit("bgbuffet", (0, 0))
    for item in items:
        item.draw()

def update():
    pass

def get_options(extra_items):
    items_to_create = ["salad"]
    for i in range(extra_items):
        item = random.choice(ITEMS)
        items_to_create.append(item)
    return items_to_create

def create_items(items_to_create):
    new_items = []
    for option in items_to_create:
        item = Actor(option + "img")
        item.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        new_items.append(item)
    return new_items

items = create_items(get_options(3))


def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1)*gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        dur = START_SPEED-current_lvl
        item.anchor = ("center", "bottom")
        animation = animate(item, duration = dur, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global items,current_lvl
    for item in items:
        if item.collidepoint(pos):
            if "salad" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global current_lvl, game_end, items, animations
    if current_lvl == FINAL_LEVEL:
        game_end = True
    else:
        current_lvl+=1
        items =[]
        animations = []


pgzrun.go()
