import pygame
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()

# Load the image 'pipe.png' into the 'images' dictionary under the key "pipe"

groundx=0
speed=0
class Bird:
    bird=pygame.Rect(100,250,30,30)
    
    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        speed=speed-10
    def display(self):
        screen.blit(images["bird"],self.bird)
        
# Create a class 'Pipe'

    # Create a rectangle at [250,400] with 40,320 as width and height. Name it as 'bpipe'
    
    # Define a method 'display()' to display the pipe image over the 'bpipe' rectangle
    
      
bird1=Bird()
# Create an object 'pipe1' for the 'Pipe' class

while True:  
  screen.blit(images["bg"],[0,0])
  groundx-=5
  if groundx<-450:
      groundx=0
  screen.blit(images["ground"],[groundx,550])
  bird1.movedown()
  bird1.display()
  # Call the function 'display()' using the 'pipe1' object
 
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
            bird1.moveup()  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
