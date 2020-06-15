# Gess_Game
Plays an abstract strategy board game called Gess

portfolio-project

Write a class named GessGame for playing an abstract board game called Gess. You can see the rules here: 
https://www.chessvariants.com/crossover.dir/gess.html

Note that when a piece's move causes it to overlap stones, any stones covered by the footprint get removed, not just those covered by one of the piece's stones. It is not legal to make a move that leaves you without a ring. It's possible for a player to have more than one ring. A player doesn't lose until they have no remaining rings.

Locations on the board are specified using columns and rows labeled 1-20.  The actual board is only columns and rows 2-19.  The center of the piece being moved must stay within the boundaries of rows and columns 2-19. An edge of the piece may go into columns or rows 1 or 20, but any pieces there are removed at the end of the move. Black goes first.

There's an online implementation you can try here:
https://gess.h3mm3.com/
but it's not 100% consistent with the rules. In the case of any discrepancy between the online game and the rules, you should comply with the rules. One example is that the online game lets you make moves that leave you without a ring, which isn't allowed (if a player wants to end the game, they can just resign). Another example is that the online game lets you choose a piece whose center is off the board (in columns or in rows 1 or 20), which isn't allowed.

The file must be named: GessGame.py

