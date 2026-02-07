import pygame
import sys
import time

import tictactoe.tictactoe as ttt

pygame.init()
size = width, height = 600, 400

# Colors
background_color = (135, 206, 235)  # Sky blue
grid_color = (0, 0, 0)  # Black
x_color = (255, 0, 0)  # Red
o_color = (0, 0, 255)  # Blue
button_color = (255, 255, 0)  # Yellow
text_color = (0, 0, 0)  # Black
title_color = (255, 255, 255)  # White

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
board = ttt.initial_state()
ai_turn = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(background_color)

    # Let user choose a player.
    if user is None:

        # Draw title
        title = largeFont.render("Play Tic-Tac-Toe", True, title_color)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Draw buttons
        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, text_color)
        playXRect = playX.get_rect()
        playXRect.center = playXButton.center
        pygame.draw.rect(screen, button_color, playXButton)
        screen.blit(playX, playXRect)

        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playO = mediumFont.render("Play as O", True, text_color)
        playORect = playO.get_rect()
        playORect.center = playOButton.center
        pygame.draw.rect(screen, button_color, playOButton)
        screen.blit(playO, playORect)

        # Check if button is clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.X
            elif playOButton.collidepoint(mouse):
                time.sleep(0.2)
                user = ttt.O

    else:

        # Draw game board as lines
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                row.append(rect)
            tiles.append(row)

        # Draw grid lines
        for i in range(4):
            # Vertical lines
            pygame.draw.line(screen, grid_color, 
                             (tile_origin[0] + i * tile_size, tile_origin[1]), 
                             (tile_origin[0] + i * tile_size, tile_origin[1] + 3 * tile_size), 3)
            # Horizontal lines
            pygame.draw.line(screen, grid_color, 
                             (tile_origin[0], tile_origin[1] + i * tile_size), 
                             (tile_origin[0] + 3 * tile_size, tile_origin[1] + i * tile_size), 3)

        # Draw moves
        for i in range(3):
            for j in range(3):
                if board[i][j] != ttt.EMPTY:
                    color = x_color if board[i][j] == ttt.X else o_color
                    move = moveFont.render(board[i][j], True, color)
                    moveRect = move.get_rect()
                    moveRect.center = tiles[i][j].center
                    screen.blit(move, moveRect)

        game_over = ttt.terminal(board)
        player = ttt.player(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = f"Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player:
            title = f"Play as {user}"
        else:
            title = f"Computer thinking..."
        title = largeFont.render(title, True, title_color)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 30)
        screen.blit(title, titleRect)

        # Check for AI move
        if user != player and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # Check for a user move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if (board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse)):
                        board = ttt.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, text_color)
            againRect = again.get_rect()
            againRect.center = againButton.center
            pygame.draw.rect(screen, button_color, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip()