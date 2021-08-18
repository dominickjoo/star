## Star Battle Solver ##

Run `python main.py` in a directory containing `main.py` and `star.py`. Make sure to color every cell before starting.

<img src="sample.gif" width="315" height="427"/>

Fun fact: the solver works on puzzles with non-contiguous regions!

Easy things to improve on:
- Make solver able to solve with more than 2 stars per region (main.py already has some code for this)
- Comment on existence/uniqueness of solution
- Click and drag for coloring grid
- Make maximum number of regions more than 10 (really just need to make the colors list bigger)
- More error catching with bad user inputs

Harder things to improve on:
- Solve more efficiently (basically put in more constraints, but this is probably best done by using a library like Z3)
- Solve things "like a human would" to improve (see [Andrew Stuart's sudoku solver](https://www.sudokuwiki.org/sudoku.htm) for an example of what I mean)