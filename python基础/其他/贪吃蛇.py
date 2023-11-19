#初始框架
import pygame

#初始化
pygame.init()
W = 800
H = 600

size = (W, H)
window = pygame.display.set_mode(size)
pygame.dispaly.set_caption('贪吃蛇')

#游戏循环
quit = True
clock = pygame.time.Clock()
while quit:
    #处理事件
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            quit = False
    #渲染——画出来的
    pygame.display.flip()


    #设置帧率
    clock.tick(60)

