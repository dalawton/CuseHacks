import pygame
import matplotlib.pyplot as plt
from colors import white, black, seagreen, seagreen1, seagreen2, seagreen3, palegreen, palegreen1, palegreen2, palegreen3, palegreen4

# start the program
pygame.init()

# Sample data
labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]

# call this function to create the pie chart 
def create_pie_chart(labels, sizes):
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

# test program
create_pie_chart(labels, sizes)

# background creation
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(palegreen)
pygame.display.flip()
font = pygame.font.SysFont('Arial', 36)

# title creation
title = font.render("Budget Tracker", True, black)
title_pos = title.get_rect(center=(screen_width/2, 50))
pygame.Surface.fill(screen, palegreen3, title_pos)
screen.blit(title, title_pos)


# set up game
running = True
while running: 
  pygame.display.flip()
  for event in pygame.event.get():
    # mouse detection
    if event.type == pygame.MOUSEBUTTONDOWN:
      mouse_pos = pygame.mouse.get_pos()
      
    # Add quit button
    if event.type == pygame.QUIT:
      running = False

