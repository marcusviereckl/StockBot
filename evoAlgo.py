
import xlrd
import pygame
import time
#----------------------------------------------------------------------
def open_file(path):

	pygame.init()
	height = 1200
	width = 1400
	blue = (0,0,255)
	black = (0,0,0)
	screen = pygame.display.set_mode((width,height))
	book = xlrd.open_workbook(path)
	
	cellVal = 0
	first_sheet = book.sheet_by_index(0)
	print(first_sheet.nrows )
	for i in range(4000, first_sheet.nrows - width ):
		for t in range(1,800):
			cellVal = first_sheet.cell(i+t-1,3).value
			pygame.draw.rect(screen, black, (t+1,height-cellVal+500,5,5), 5)
		for t in range(1,800):
			cellVal = first_sheet.cell(i+t,3).value
			pygame.draw.rect(screen, blue, (t,height-cellVal+500,5,5), 5)
		time.sleep(.01)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

if __name__ == "__main__":
    path = "dailypricehistory.xls"
    open_file(path)