# ================================================================
# Program: Tile Dash 1.0
# Author: Jacob Childs
# Description: Tile Dash (Main body)
# Date Modified: 05/15/2022
# Version: 1.0
# ================================================================
# Imported Libraries

import random
import time
import simpleaudio
from tile_dash_class import *

# ================================================================
# Global Variables

# Components of window
window = GraphWin("Tile Dash 1.0", 1200, 900, autoflush=False)
window.setBackground("gray9")

# Components of display screens
menu = Image(Point(600, 450), "resources/images/menu.png")
endingScreen = Image(Point(600, 450), "resources/images/ending_screen.png")

# Components of scoreboard
scoreBoard = Image(Point(600, 25), "resources/images/score_board.png")
scoreBoard.draw(window)

# Components of score
numScore = 0
scoreText = Text(Point(600, 25), "")
scoreText.setFill("green1")
scoreText.setFace("courier")
scoreText.setStyle("bold")
scoreText.setSize(15)

# Components of final score
finalScore = Text(Point(600, 450), "")
finalScore.setFill("lightgreen")
finalScore.setFace("courier")
finalScore.setStyle("bold")
finalScore.setSize(36)

# Sounds
gameMusic = simpleaudio.WaveObject.from_wave_file("resources/sounds/game_music.wav")
pingNoise = simpleaudio.WaveObject.from_wave_file("resources/sounds/ping_noise.wav")
clickSound = simpleaudio.WaveObject.from_wave_file("resources/sounds/click_sound.wav")

# Character object
character = Character(600, 450, window, 6, "resources/images/alien_character.png")

# All tile objects:
tileList = []
for x in range(94, 1103, 168):
    for y in range(143, 796, 163):
        tileList.append(Tile(x, y, window))

# Shuffles list and defines safe and unsafe tiles
random.shuffle(tileList)
safeTileList = tileList[0:6]
unsafeTileList = tileList[6:35]

# ================================================================
# User-defined Functions

def isCharacterOnSafeTile():
    """Collision detection between the tile and character."""
    for i in range(6):
        if (safeTileList[i].tileGetX() - 74) <= character.characterGetX() <= (safeTileList[i].tileGetX() + 74) and \
                (safeTileList[i].tileGetY() - 73) <= character.characterGetY() <= (safeTileList[i].tileGetY() + 73):
            return True

def tileHideFunction():
    """Hides ALL tiles."""
    for i in range(35):
        tileList[i].hide()

def tileShowFunction():
    """Shows ALL tiles."""
    for i in range(35):
        tileList[i].show()

def safeTileHideFunction():
    """Hides safe tiles."""
    for i in range(6):
        safeTileList[i].hide()

def safeTileShowFunction():
    """Shows safe tiles."""
    for i in range(6):
        safeTileList[i].show()

def unsafeTileHideFunction():
    """Hides unsafe tiles."""
    for i in range(29):
        unsafeTileList[i].hide()

def unsafeTileShowFunction():
    """Shows unsafe tiles."""
    for i in range(29):
        unsafeTileList[i].show()

def unsafeTileImageChangeFunction(x):
    """Sets the index of the image to be returned to the tile class."""
    for tile in unsafeTileList:
        tile.setImageIndex(x)

def scoreFunctionUpdate():
    """Updates and writes the correct score to the scoreboard."""
    scoreText.undraw()
    scoreText.setText(f"Score: {numScore}")
    scoreText.draw(window)

def resetTileImages(x):
    """Resets the tileImage indices back to 0."""
    for tile in tileList:
        tile.setImageIndex(x)

# ================================================================
# Main Function

def main():
    global numScore, tileList, safeTileList, unsafeTileList, gameMusic, pingNoise, clickSound
    counter = 0
    speed = 100
    # Sounds
    lockedTime = int(time.time() * 100)

    while True:
        # Loop that displays menu are continues when mouse is clicked
        menu.undraw()
        menu.draw(window)
        window.update()
        if window.getMouse():
            clickSound.play()
            menu.undraw()
            break                   # Breaks when LMB clicked

    time.sleep(.3)          # Small pause so player can get ready
    gameMusic.play()        # Starts game music

    while not window.closed:
        # Timer that controls animation
        currentTime = int(time.time() * 100)
        if lockedTime != currentTime:
            lockedTime = currentTime

            # Full animation mechanics
            if lockedTime % speed == 0:
                unsafeTileHideFunction()
                counter += 1
                unsafeTileImageChangeFunction(counter % 5)
                unsafeTileShowFunction()
                pingNoise.play()

                # Controls main functions at the end of one cycle
                if isCharacterOnSafeTile() == True and counter % 5 == 0:        # Tests for safe tile collision
                    numScore += 1                          # Score control
                    speed -= 2                             # Speed control
                    scoreFunctionUpdate()
                    tileHideFunction()
                    random.shuffle(tileList)               # Shuffles tiles and resets image
                    unsafeTileList = tileList[6:35]
                    safeTileList = tileList[0:6]
                    resetTileImages(0)
                    if speed == 26:                        # Sets speed limit so it's possible to play
                        speed += 2
                elif isCharacterOnSafeTile() != True and counter % 5 == 0:      # Test for unsafe tile collision
                    break

            # Components that must be updated each frame
            if lockedTime % 1 == 0:
                tileHideFunction()
                tileShowFunction()
                character.characterUpdate()
                isCharacterOnSafeTile()
                window.update()

    while not window.closed:
        endingScreen.undraw()
        endingScreen.draw(window)
        finalScore.undraw()
        finalScore.setText(numScore)
        finalScore.draw(window)
        window.update()

# ================================================================
# Call Main
main()