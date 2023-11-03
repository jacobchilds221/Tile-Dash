# ================================================================
# Program: Tile Dash 1.0
# Author: Jacob Childs
# Description: Tile Dash (Classes)
# Date Modified: 05/15/2022
# Version: 1.0
# ================================================================
# Imported Libraries
from graphics import *

# ================================================================
# User-defined Functions
class Character:

    def __init__(self, x, y, window, speed, imageLocation):
        self.__x = x
        self.__y = y
        self.__window = window
        self.__character = Image(Point(x, y), imageLocation)
        self.__speed = speed

    def characterUpdate(self):
        """Controls update of character movements."""
        self.__character.undraw()
        self.moveCharacter()
        self.__character.draw(self.__window)

    def moveCharacter(self):
        """Defines which keys move the character and the boundaries of movement."""
        movementKeys = self.__window.checkKeys()

        if "w" in movementKeys and self.__y >= 50:
            self.__y -= self.__speed
        if "s" in movementKeys and self.__y <= 900:
            self.__y += self.__speed
        if "a" in movementKeys and self.__x >= 0:
            self.__x -= self.__speed
        if "d" in movementKeys and self.__x <= 1200:
            self.__x += self.__speed

        self.__character.anchor = Point(self.__x, self.__y)


    def characterGetX(self):
        """Returns the location of the characters x value."""
        return self.__x

    def characterGetY(self):
        """Returns the location of the characters y value."""
        return self.__y

class Tile:

    def __init__(self, x, y, window):
        self.__x = x
        self.__y = y
        self.__window = window
        self.__tiles = []
        self.__loadTiles()
        self.__imageIndex = 0

    def __loadTiles(self):
        """Loads the tiles to the tiles list."""
        self.__tiles.append(Image(Point(self.__x, self.__y), "resources/images/default_tile.png"))
        self.__tiles.append(Image(Point(self.__x, self.__y), "resources/images/phase1.png"))
        self.__tiles.append(Image(Point(self.__x, self.__y), "resources/images/phase2.png"))
        self.__tiles.append(Image(Point(self.__x, self.__y), "resources/images/phase3.png"))
        self.__tiles.append(Image(Point(self.__x, self.__y), "resources/images/phase4.png"))

    def setImageIndex(self, index):
        """Sets the index that retrieves the image."""
        self.__imageIndex = index

    def show(self):
        """Draws the tiles to the window."""
        self.__tiles[self.__imageIndex].draw(self.__window)

    def hide(self):
        """Undraws the tiles from the window."""
        self.__tiles[self.__imageIndex].undraw()

    def tileGetX(self):
        """Returns the tiles x center point."""
        return self.__x

    def tileGetY(self):
        """Returns the tiles y center point."""
        return self.__y

# ================================================================


