import game_framework
import random
from pico2d import *

from ball import Ball

import game_world

# Boy Run Speed
PIXEL_PER_METER = (10 / 0.02)  # 참새의 크키는 구글에 쳐보니 10~20cm여서 10cm로 정하고 10 pixel 2cm정도로 해주었습니다.
RUN_SPEED_KMPH = 160  # Km / Hour 참새의 평균 속도는 160이므로 속도 값을 넣어 주었습니다. / 새의 속도가 너무 빨라서 충돌이 잘 보이시지 않는다면 속도 값을 20정도로 설정하시고 검사하시는걸 권장합니다.
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

random.random()


# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

# class IdleState:
#
#     def enter(boy, event):
#         if event == RIGHT_DOWN:
#             boy.velocity += RUN_SPEED_PPS
#         elif event == LEFT_DOWN:
#             boy.velocity -= RUN_SPEED_PPS
#         elif event == RIGHT_UP:
#             boy.velocity -= RUN_SPEED_PPS
#         elif event == LEFT_UP:
#             boy.velocity += RUN_SPEED_PPS
#         boy.timer = 1000
#
#
#
#
#
#
#     def exit(boy, event):
#         if event == SPACE:
#             boy.fire_ball()
#
#     def do(boy):
#         boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
#         boy.timer -= 1
#         if boy.timer == 0:
#     def draw(boy):
#             if (boy.x > 0):
#               boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)
#               boy.x += 1
#             elif (boy.x == 8):
#                # boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)
#                 boy.x -=2
#
#
#
#             boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x2, boy.y2)
#             boy.add_event(SLEEP_TIMER)




class RunState:

    def enter(boy, event):

        boy.dir = clamp(-1, boy.x, 1)
        boy.dir2 = clamp(-1, boy.x2, 1)
        boy.dir3 = clamp(-1, boy.x3, 1)
        boy.dir4 = clamp(-1, boy.x4, 1)
        boy.dir5 = clamp(-1, boy.x5, 1)

    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    def do(boy):

        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time


        if (boy.dir == -1):
            boy.x += RUN_SPEED_MPS
            if (boy.x > 1500):
                 boy.x -= RUN_SPEED_MPS
                 boy.dir = 1

        if (boy.dir == 1):
            boy.x -= RUN_SPEED_MPS
            if (boy.x <= 25):
                boy.x += RUN_SPEED_MPS
                boy.dir = -1

        if (boy.dir2 == -1):
            boy.x2 += RUN_SPEED_MPS
            if (boy.x2 > 1500):
                 boy.x2 -= RUN_SPEED_MPS
                 boy.dir2 = 1

        if (boy.dir2 == 1):
            boy.x2 -= RUN_SPEED_MPS
            if (boy.x2 <= 25):
                boy.x2 += RUN_SPEED_MPS
                boy.dir2 = -1

        if (boy.dir3 == -1):
            boy.x3 += RUN_SPEED_MPS
            if (boy.x3 > 1500):
                 boy.x3 -= RUN_SPEED_MPS
                 boy.dir3 = 1

        if (boy.dir3 == 1):
            boy.x3 -= RUN_SPEED_MPS
            if (boy.x3 <= 25):
                boy.x3 += RUN_SPEED_MPS
                boy.dir3 = -1

        if (boy.dir4 == -1):
            boy.x4 += RUN_SPEED_MPS
            if (boy.x4 > 1500):
                 boy.x4 -= RUN_SPEED_MPS
                 boy.dir4 = 1

        if (boy.dir4 == 1):
            boy.x4 -= RUN_SPEED_MPS
            if (boy.x4 <= 25):
                boy.x4 += RUN_SPEED_MPS
                boy.dir4 = -1

        if (boy.dir5 == -1):
            boy.x5 += RUN_SPEED_MPS
            if (boy.x5 > 1500):
                 boy.x5 -= RUN_SPEED_MPS
                 boy.dir5 = 1

        if (boy.dir5 == 1):
            boy.x5 -= RUN_SPEED_MPS
            if (boy.x5 <= 25):
                boy.x5 += RUN_SPEED_MPS
                boy.dir5 = -1



    def draw(boy):

        boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)

        boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x2, boy.y2)

        boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x3, boy.y3)

        boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x4, boy.y4)

        boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x5, boy.y5)


# class SleepState:
#
#     def enter(boy, event):
#         boy.frame = 0
#
#     def exit(boy, event):
#         pass
#
#     def do(boy):
#         boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
#
#     def draw(boy):
#         if boy.dir == 1:
#             boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
#         else:
#             boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)






# next_state_table = {
#     IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: RunState, SPACE: IdleState},
#     RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
#     SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
# }

class Boy:

    def __init__(self):
        self.x = random.randint(50, 1550)
        self.y = random.randint(90, 550)
        self.x2 = random.randint(50, 1550)
        self.y2 = random.randint(90, 550)
        self.x3 = random.randint(50, 1550)
        self.y3 = random.randint(90, 550)
        self.x4 = random.randint(50, 1550)
        self.y4 = random.randint(90, 550)
        self.x5 = random.randint(50, 1550)
        self.y5 = random.randint(90, 550)
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird100x100x14.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0


    def fire_ball(self):
       # ball = Ball(self.x, self.y, self.dir * RUN_SPEED_PPS * 10)
        #game_world.add_object(ball, 1)
       pass


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            #self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #fill here


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

