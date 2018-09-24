EeyyStarAlgorithm
===

A Python implementation of the A* algorithm. 

The `app.py` script accepts a filename to a board as argument (see folder `boards/`), 
where `A` denotes start and `B` denotes goal. It will on this 
file attempt to find the shortest path, using Best-First-Search 
and Manhattan Heuristic.

## Run the script

```bash
$ python3 app.py boards/board-1-1.txt
```

Output will be a printed board, whith a proposed path

```text
....................
........oooooooo....
........o######o....
........oooA..#ooB..
.........######.....
....................
....................
```

 