import pygame
from colors import palegreen, palegreen3, black, white
import matplotlib.pyplot as plt

# start the program
pygame.init()

# background creation
screen_width = 600
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(palegreen)
pygame.display.flip()
font = pygame.font.SysFont('Arial', 36)

# title creation
title = font.render("Budget Tracker", True, black)
title_pos = title.get_rect(center=(screen_width / 2, 50))
pygame.Surface.fill(screen, white, title_pos)
screen.blit(title, title_pos)
budget = font.render("Budget ($): ", True, black)
budget_pos = budget.get_rect(center=(screen_width / 3, 150))
pygame.Surface.fill(screen, white, budget_pos)
screen.blit(budget, budget_pos)
budget_textpos = pygame.Rect(320, 130, 200, 40)
pygame.Surface.fill(screen, white, budget_textpos)

# plus creation
plus = font.render("category:          cost ($):", True, black)
plus_pos = plus.get_rect(center=(screen_width / 2, 250))
pygame.Surface.fill(screen, white, plus_pos)
screen.blit(plus, plus_pos)

# category creation
runs = True
categories = []
costs = []
text = " "
category_text = font.render(text, True, black)
categorypos = pygame.Rect(90, 300, 200, 40)
pygame.Surface.fill(screen, white, categorypos)
screen.blit(category_text, categorypos)
cash = " "
category_total = font.render(cash, True, black)
category_totalpos = pygame.Rect(340, 300, 200, 40)
pygame.Surface.fill(screen, white, category_totalpos)
screen.blit(category_total, category_totalpos)
new_category = font.render("New Category", True, black)
new_category_pos = new_category.get_rect(center=(screen_width / 4, 400))
pygame.Surface.fill(screen, white, new_category_pos)
done_button = font.render("Done", True, black)
done_button_pos = done_button.get_rect(center=(screen_width / 4 * 3, 400))
pygame.Surface.fill(screen, white, done_button_pos)
screen.blit(new_category, new_category_pos)
screen.blit(done_button, done_button_pos)

# set up game
running = True
done = False
runs = True
while running:
    pygame.display.flip()
    for event in pygame.event.get():
        # Add quit button
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            # running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if budget_textpos.collidepoint(mouse_pos):
                text = " "
                while runs:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE:
                                # Handle backspace key
                                text = text[:-1]
                            elif event.key == pygame.K_RETURN:
                                runs = False
                            else:
                                if event.key != pygame.K_RETURN:
                                    text += event.unicode
                                    budget_text = font.render(text, True, black)
                                    screen.blit(budget_text, budget_textpos)
                                    pygame.display.flip()
                            budget_texts = font.render(text, True, black)
                            pygame.Surface.fill(screen, white, budget_textpos)
                            screen.blit(budget_texts, budget_textpos)
                            pygame.display.flip()
                            final_budget = int(text)
            if categorypos.collidepoint(mouse_pos):
                runs = True
                text = " "
                while runs:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                categories.append(text)
                                runs = False
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                if event.key != pygame.K_RETURN:
                                    text += event.unicode
                                    category_text = font.render(text, True, black)
                                    screen.blit(category_text, categorypos)
                                    pygame.display.flip()
            if category_totalpos.collidepoint(mouse_pos):
                runs = True
                text = " "
                while runs:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                costs.append(text)
                                runs = False
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                if event.key != pygame.K_RETURN:
                                    text += event.unicode
                                    category_total = font.render(text, True, black)
                                    screen.blit(category_total, category_totalpos)
                                    pygame.display.flip()
            if new_category_pos.collidepoint(mouse_pos):
                text = " "
                category_text = font.render(text, True, black)
                categorypos = pygame.Rect(90, 300, 200, 40)
                pygame.Surface.fill(screen, white, categorypos)
                screen.blit(category_text, categorypos)
                cash = " "
                category_total = font.render(cash, True, black)
                category_totalpos = pygame.Rect(340, 300, 200, 40)
                pygame.Surface.fill(screen, white, category_totalpos)
                screen.blit(category_total, category_totalpos)
                pygame.display.flip()
            if done_button_pos.collidepoint(mouse_pos):
                pygame.Surface.fill(screen, palegreen3)
                pygame.display.flip()

                categories.append("excess")

                cost = []
                for num in costs:
                    num = int(num)
                    cost.append(num)

                def percents(size=cost, budget=final_budget) -> list:
                    breakdown = []
                    total = budget
                    leftover = ((budget - sum(size))/total) * 100
                    for num in size:
                        percent = (num / total) * 100
                        breakdown.append(percent)
                    breakdown.append(leftover)
                    return breakdown


                # call this function to create the pie chart
                def create_pie_chart(labels, sizes):
                    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
                    plt.axis('equal')
                    plt.show()


                # test program
                create_pie_chart(categories, percents())
