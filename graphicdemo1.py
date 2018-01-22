# -*- coding: utf-8 -*-
"""003_static_blit_pretty_template.py"""
import pygame 
import random
import math

def radians_to_degrees(radians):
    return (radians / math.pi) * 180.0
    
def degrees_to_radians(degrees):
    return (degrees * (math.pi / 180.0))


class PygView(object):
    width = 0
    height = 0
    def __init__(self, width=640, height=400, fps=40):
        """Initialize pygame, window, background, font,...
           default arguments """
        pygame.init()
        pygame.display.set_caption("Press ESC to quit")
        self.width = width
        self.height = height
        PygView.width = width
        PygView.height = height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF)
        self.background = pygame.Surface(self.screen.get_size()).convert()  
        self.background.fill((255,255,255)) # fill background white
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.playtime = 0.0
        self.font = pygame.font.SysFont('mono', 24, bold=True)


    def paint(self):
        """painting on the surface"""
        #start = degrees_to_radians()
        #end = degrees_to_radians()
        #pygame.draw.line(self.background, (255,0,0), (0,840),  (400,840), 15)
        #pygame.draw.line(self.background, (255,0,0), (1040,840),  (1440,840), 15)
        #pygame.draw.arc(self.background, (255,0,0), (400,10,150,100), start, end, 15)
        #for x in range(0,4000,100):
            #for y in range(0,3000,100):
                #pygame.draw.line(self.background,(0,0,0),(x,0), (0,y))
                
        
        xpoints = []
        ypoints = []
        xdist = PygView.width // 100
        ydist = PygView.height // 100
        for a in range(100):
            xpoints.append(xdist*a)
        for a in range(100):
            ypoints.append(ydist*a)
        for a in range(100):
            pygame.draw.line(self.background, (255-int(a*2.55),255-int(a*2.55),int(a*2.55)), (0,ypoints[a]), (xpoints[a],PygView.height))     
        for a in range(100):
            pygame.draw.line(self.background, (int(a*2.55),int(a*2.55),255-int(a*2.55)), (PygView.width,ypoints[a]), (xpoints[a],0))
        for a in range(1,100):
            pygame.draw.line(self.background, (int(a*2.55),255-int(a*2.55),255-int(a*2.55)), (xpoints[a],PygView.height), (PygView.width,ypoints[-a]))
        for a in range(1,100):
            pygame.draw.line(self.background, (int(a*2.55),255-int(a*2.55),255-int(a*2.55)), (xpoints[-a],0), (0,ypoints[a]))
        # pygame.draw.line(Surface, color, start, end, width) 
        #pygame.draw.line(self.background, (255,0,0), (0,0), (1450,850), 15)
        # pygame.draw.rect(Surface, color, Rect, width=0): return Rect
        #pygame.draw.rect(self.background, (0,255,0), (50,50,100,25))
        #pygame.draw.rect(self.background, (100,100,100), (0,0,725,425))
        #pygame.draw.rect(self.background, (0,0,100), (720,425,725,425))
        #pygame.draw.rect(self.background, (0,100,0), (720,0,725,425))
        #pygame.draw.rect(self.background, (0,0,0), (0,425,725,425))
        #pygame.draw.rect(self.background, (0,0,0), (500,300,725,400), 1)
        #pygame.draw.ellipse(self.background, (0,0,0), (500,300,725,400), 1)
        #pygame.draw.circle(self.background, (100,100,0), (850,500), 100)
        #pygame.draw.ellipse(self.background, (0,0,0), (840,450,20,100))
        #pygame.draw.line(self.background, (255,0,0), (0,830),  (1450,0), 15) # rect: (x1, y1, width, height)
        # pygame.draw.circle(Surface, color, pos, radius, width=0): return Rect
        #pygame.draw.circle(self.background, (0,0,0), (0,0), 100)
        #pygame.draw.circle(self.background, (0,0,0), (1450,850), 100)
        #pygame.draw.circle(self.background, (0,0,0), (0,850), 100)
        #pygame.draw.circle(self.background, (0,0,0), (1450,0), 100)
        #pygame.draw.circle(self.background, (0,0,0), (725,425), 100)
        #pygame.draw.line(self.background, (255,0,0), (0,415), (1450,415), 15)
        # pygame.draw.polygon(Surface, color, pointlist, width=0): return Rect
        #pygame.draw.line(self.background, (255,0,0), (725,0), (725,850), 15)
        # pygame.draw.arc(Surface, color, Rect, start_angle, stop_angle, width=1): return Rect
        #pygame.draw.arc(self.background, (0,150,0),(400,10,150,100), 0, 3.14) # radiant instead of grad
        #pygame.draw.lines(Surface, color, closed, pointlist, width=1)
        #pygame.draw.lines(self.background, (0,0,0), False, [(0,350), (15,300), (30,400), (45,250), (50,700), (1450, 850), (0,0) ])  
    def run(self):
        self.paint() 
        myball = Ball() # creating the Ball object
        running = True
        while running:
            milliseconds = self.clock.tick(self.fps)
            seconds = milliseconds / 1000.0
            self.playtime += seconds
            self.draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS".format(
                           self.clock.get_fps(), " "*5, self.playtime))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                elif event.type == pygame.KEYDOWN:
                    # keys that you press once and release
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_q: # stopper 
                        myball.dx = 0
                        myball.dy = 0
                        myball.x = PygView.width //3 # one third without remainder
                        myball.y = PygView.height // 2 # one half without remainder
            pressedkeys = pygame.key.get_pressed() # keys that you can press all the time
            if pressedkeys[pygame.K_a]:
                myball.dx -=1
            if pressedkeys[pygame.K_d]:
                myball.dx +=1
            if pressedkeys[pygame.K_w]:
                myball.dy -= 1
            if pressedkeys[pygame.K_s]:
                myball.dy += 1
            pygame.display.flip()
            self.screen.blit(self.background, (0, 0))
            myball.update(seconds)
            myball.blit(self.screen) # blitting it
            # tail
            if len(myball.tail) > 2:
                for a in range(1, len(myball.tail)):
                    pygame.draw.line(self.screen, (100,0,100),
                                     myball.tail[a-1],
                                     myball.tail[a], 10-a//10)                      
                
        pygame.quit()

    def draw_text(self, text):
        """Center text in window"""
        fw, fh = self.font.size(text)
        surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(surface, (50,150))

class Ball(object):
    """this is not a native pygame sprite but instead a pygame surface"""
    def __init__(self, radius = 15, color=(0,0,255), x=320, y=240):
        """create a (black) surface and paint a blue ball on it"""
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        # create a rectangular surface for the ball 50x50
        self.surface = pygame.Surface((2*self.radius,2*self.radius))    
        pygame.draw.circle(self.surface, color, (radius, radius), radius) # draw blue filled circle on ball surface
        self.surface = self.surface.convert() # for faster blitting. 
        # to avoid the black background, make black the transparent color:
        # self.surface.set_colorkey((0,0,0))
        # self.surface = self.surface.convert_alpha() # faster blitting with transparent color
        self.tail = []
   
    def update(self, seconds):
        self.x += self.dx * seconds
        self.y += self.dy * seconds
        # wrap around screen
        if self.x < 0:
            #self.x = PygView.width
            self.x = 0
            self.dx *= -1.111111111111
        if self.x > PygView.width:
            #self.x = 0
            self.x = PygView.width
            self.dx *= -1
        if self.y < 0:
            #self.y = PygView.height
            self.y = 0
            self.dy *= -1
        if self.y > PygView.height:
            #self.y = 0
            self.y = PygView.height
            self.dy *= -1
        self.tail.insert(0,(self.x,self.y))
        self.tail = self.tail[:256]

        
            
    def blit(self, ground):
        """blit the Ball on the background"""
        ground.blit(self.surface, ( self.x, self.y))
        
if __name__ == '__main__':
    PygView(1400, 800).run() # call with width of window and fps
