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
    global hand_x, hand_y
    hand_x = random.randint(0,TUK_WIDTH)
    hand_y = random.randint(0, TUK_HEIGHT)

def move_keroro(keroro_x, keroro_y, hand_x, hand_y):
    frame = 0
    for i in range(0, 100 + 1, 4):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
        hand.draw(hand_x, hand_y)
        t = i / 100
        x = (1 - t) * keroro_x + t * hand_x
        y = (1 - t) * keroro_y + t * hand_y
        if hand_x > keroro_x:
            keroro_right.clip_draw(frame * 250, 0, 250, 345, x, y, 125, 160)
        elif hand_x < keroro_x:
            keroro_left.clip_draw(frame * 250, 0, 250, 345, x, y, 125, 160)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.08)

running = True
keroro_x, keroro_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
hide_cursor()
produce_hand()

while running:
    if keroro_x == hand_x and keroro_y == hand_y:
        produce_hand()
    else :
        move_keroro(keroro_x, keroro_y, hand_x, hand_y)
        keroro_x, keroro_y = hand_x, hand_y
    handle_events()


close_canvas()




