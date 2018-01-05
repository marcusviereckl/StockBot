import pygame
import sys
import math
import time
import random

pygame.init()
height = 1200
width = 1200
screen = pygame.display.set_mode((width,height))
blue = (255,0,0)
black = (0,0,255)


t = 0
bodyCount = 50
tstep = 1

bodyX = [random.randint(0,width) for r in range(0,bodyCount)]
bodyVx = [random.randint(0,0) for r in range(0,bodyCount)]
bodyY = [random.randint(0,height) for r in range(0,bodyCount)]
bodyVy = [random.randint(0,0) for r in range(0,bodyCount)]
bodyM = [random.randint(1,10) for r in range(0,bodyCount)]

momentumRule = "inelastic"

bodyX[5] = 600
bodyY[5] = 600
bodyM[5] = 20
while (t < 10000) :
	for outer in range(0, bodyCount): 
		if bodyM[outer] == 0:
			continue
		pygame.draw.circle(screen, black, (round(bodyX[outer]),round(bodyY[outer])),2*round(math.sqrt(bodyM[outer])), 0)
		for inner in range(0, bodyCount):
			if bodyM[inner] == 0:
					continue
			if outer==inner:
				continue
			dx = bodyX[inner] - bodyX[outer] 
			dy = bodyY[inner] - bodyY[outer] 
			if (abs(dx)<3 and abs(dy)<3):
				if abs(bodyM[outer] - bodyM[inner]) < 5:
					totalMass = bodyM[outer] + bodyM[inner]
					bodyX[outer] = bodyX[inner]
					bodyY[outer] = bodyY[inner]
					bodyVx[outer] = bodyVx[inner] * bodyM[inner] / totalMass + bodyVx[outer] * bodyM[outer]/ totalMass
					bodyVy[outer] = bodyVy[inner] * bodyM[inner] / totalMass + bodyVy[outer] * bodyM[outer]/ totalMass
					bodyM[outer] = totalMass
					bodyM[inner] = 0
				else:
					totalMass = bodyM[outer] + bodyM[inner]
					dominantXVelocity = bodyVx[inner] if bodyM[inner] > bodyM[outer] else bodyVx[outer]
					dominantYVelocity = bodyVy[inner] if bodyM[inner] > bodyM[outer] else bodyVy[outer]
					dominantMass = bodyM[inner]if bodyM[inner] > bodyM[outer] else bodyM[outer]
					bodyX[outer] = bodyX[inner]
					bodyY[outer] = bodyY[inner]
					bodyVx[outer] = dominantYVelocity * dominantMass / totalMass
					bodyVy[outer] = dominantYVelocity * dominantMass / totalMass
					bodyM[outer] = totalMass
					bodyM[inner] = 0
				continue
			magnitude =  bodyM[inner] / (math.pow(dx,2) + math.pow(dy,2))
			bodyVx[outer] = bodyVx[outer] + magnitude * dx / (abs(dx) + abs(dy)) * tstep
			bodyVy[outer] = bodyVy[outer] + magnitude * dy / (abs(dx) + abs(dy)) * tstep
		bodyX[outer] = bodyX[outer] + bodyVx[outer]  * tstep
		bodyY[outer] = bodyY[outer] + bodyVy[outer]  * tstep
		pygame.draw.circle(screen, blue, (round(bodyX[outer]),round(bodyY[outer])),2*round(math.sqrt(bodyM[outer])), 0)
	t = t + 1
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	time.sleep(.01)