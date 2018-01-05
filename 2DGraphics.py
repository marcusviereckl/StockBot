import pygame
import sys
import math
import time

pygame.init()
height = 1000
width = 1000
screen = pygame.display.set_mode((width,height))
blue = (0,0,255)
pink = (255,200,200)
black = (0,0,0)
green = (0,255,0)
red = (255,0,0)

t = 0
circleRadius = 100;
circleCount = 10

ellipseRadius = 120;
ellipseCount = 20
ellipseXStrength = 2.5
ellipseYStrength = 1

x = [1] * circleCount
y = [1] * circleCount
xoval = [1] * ellipseCount
yoval = [1] * ellipseCount

pygame.draw.circle(screen, red, (round(width/2),round(height/2)), round(circleRadius * .1),0)

while (t < 10000) :
	arc = t / 1000 * 2 * math.pi
	circleShift = 2 * math.pi / circleCount
	for i in range(0, circleCount):
		pygame.draw.rect(screen, black, (x[i],y[i],5,5), 5)
		x[i] = width / 2 + circleRadius * math.cos(i * circleShift + arc)
		y[i] = height / 2 + circleRadius * math.sin(i * circleShift + arc)
		pygame.draw.rect(screen, pink, (x[i],y[i],5,5), 5)

	ovalShift = 2 * math.pi / ellipseCount
	for i in range(0, ellipseCount):
		pygame.draw.rect(screen, black, (xoval[i],yoval[i],5,5), 5)
		xoval[i] = width / 2 + (ellipseRadius * math.cos(i * ovalShift - arc)) * ellipseXStrength
		yoval[i] = height / 2 + (ellipseRadius * math.sin(i * ovalShift - arc)) * ellipseYStrength
		pygame.draw.rect(screen, blue, (xoval[i],yoval[i],5,5), 5)

	pygame.display.update()
	t = t + 1

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	time.sleep(.01)