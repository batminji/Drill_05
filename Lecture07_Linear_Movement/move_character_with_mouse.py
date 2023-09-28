from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
keroro_left = load_image('keroro_left.png')
keroro_right = load_image('keroro_right.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

can_make = True
def produce_hand():
    global hand_x, hand_y, can_make
    if can_make:
        hand_x = random.randint(0,TUK_WIDTH)
        hand_y = random.randint(0, TUK_HEIGHT)
        can_make = False
    elif not can_make:
        pass


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    produce_hand()
    hand.draw(hand_x, hand_y)

    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.05)

close_canvas()




