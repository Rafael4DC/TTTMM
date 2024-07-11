import math

import pygame

from jogo_do_galo.galo import *
from jogo_do_galo.minmax import findBestMove

pygame.init()

# Constantes
screen_width = 400
screen_height = 400
color = pygame.Color('chartreuse4')
user_text = ''
activity_get_name = True
activity_game_over = False
player1 = None
player2 = None
ttt = None

x_img = pygame.image.load("..\\imgs\\X.png")
x_img = pygame.transform.scale(x_img, (screen_width / 3, screen_height / 3))

o_img = pygame.image.load("..\\imgs\\circle.png")
o_img = pygame.transform.scale(o_img, (screen_width / 3, screen_height / 3))

# Coisas instanciadas
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo do galo")

icon = pygame.image.load("../imgs/galinhapintadinha.jpg")
pygame.display.set_icon(icon)

base_font = pygame.font.Font(None, 32)


# metodos ao calhas
def get_player(user_text, player_name):
    max_width = 300
    sqr_height = 32
    input_rect = pygame.Rect(screen_width // 2, screen_height // 2, 140, sqr_height)
    color = pygame.Color('lightskyblue3')

    # Calculate width based on text length, ensuring it does not exceed max_width
    width = max(140, min(max_width, base_font.size(user_text)[0] + 10))
    input_rect.width = width
    input_rect.center = (screen_width // 2, screen_height // 2)

    # Draw the textbox
    pygame.draw.rect(screen, color, input_rect)

    # Render the user text inside the textbox876
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

    # Render the player's name above the textbox
    player_text_surface = base_font.render(player_name, True, (255, 255, 255))
    player_text_rect = player_text_surface.get_rect()
    player_text_rect.center = (screen_width // 2, screen_height // 2 - 40)
    screen.blit(player_text_surface, player_text_rect)


def get_player_by_event(event):
    global player1
    global player2
    global user_text
    global activity_get_name
    global ttt
    if event.type == pygame.KEYDOWN and activity_get_name:
        if event.key == pygame.K_RETURN:
            if user_text == '': return
            if player1 is None:
                player1 = Player(user_text, Symbol.X)
                user_text = ''
            elif player2 is None:
                player2 = Player(user_text, Symbol.O)
                user_text = ''
                activity_get_name = False
                ttt = TicTacToe(player1, player2)
        elif event.key == pygame.K_BACKSPACE:
            user_text = user_text[:-1]
        else:
            user_text += event.unicode


def show_icons(ttt):
    for i in range(3):
        for j in range(3):
            if ttt.board[i][j] == Symbol.X:
                screen.blit(x_img, (j * screen_width / 3, i * screen_height / 3))
            if ttt.board[i][j] == Symbol.O:
                screen.blit(o_img, (j * screen_width / 3, i * screen_height / 3))


def show_gameplay():
    global ttt
    global screen_width
    global screen_height
    line_color = (0, 0, 0)
    pygame.display.set_caption(f"É a tua vez {ttt.get_current_player()} using {ttt.turn.value} ")

    show_icons(ttt)

    # drawing vertical lines
    pygame.draw.line(screen, line_color, (screen_width / 3, 0), (screen_width / 3, screen_height), 7)
    pygame.draw.line(screen, line_color, (screen_width / 3 * 2, 0), (screen_width / 3 * 2, screen_height), 7)

    # drawing horizontal lines
    pygame.draw.line(screen, line_color, (0, screen_height / 3), (screen_width, screen_height / 3), 7)
    pygame.draw.line(screen, line_color, (0, screen_height / 3 * 2), (screen_width, screen_height / 3 * 2), 7)


def player_click(event):
    global user_text
    global activity_get_name
    global activity_game_over
    global ttt
    if event.type == pygame.MOUSEBUTTONDOWN and activity_get_name is not True:
        x = event.pos[0]
        y = event.pos[1]
        X_sqr = math.floor(x / (screen_width / 3))
        Y_sqr = math.floor(y / (screen_height / 3))
        ans = ttt.make_move(X_sqr, Y_sqr)
        if ans is not True: return
        winner = ttt.victory_condi()
        if winner is not None:
            activity_game_over = True
            pygame.display.set_caption(f"Parabéns ganhou o {winner.value} ")
            pygame.display.update()

        bestMove = findBestMove(ttt.board)
        ttt.make_move(bestMove[1], bestMove[0])
        winner = ttt.victory_condi()
        if winner is not None:
            activity_game_over = True
            pygame.display.set_caption(f"Parabéns ganhou o {winner.value} ")
            pygame.display.update()


running = True
while running:
    screen.fill((152, 163, 217))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        get_player_by_event(event)
        player_click(event)

    # Event reader
    current_player = "Player1" if player1 is None else "Player2"
    if activity_get_name: get_player(user_text, current_player)

    if not activity_get_name and not activity_game_over:
        show_gameplay()
    if activity_game_over is False: pygame.display.update()
