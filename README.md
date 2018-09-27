EeyyStarAlgorithm
===

A Python implementation of the A* algorithm. 

The `app.py` script accepts a filename to a board as argument (see folder `boards/`), 
where `A` denotes start and `B` denotes goal. It will on this 
file attempt to find the shortest path, using Best-First-Search 
and Manhattan Heuristic.

## Run the script directly

```bash
$ python3 app.py boards/board-1-1.txt
```

Output will be an image with the expected path. Bellow is an raw text representation

```text
....................
........xxxxxxxx....
........x######x....
........xxxA..#xxB..
.........######.....
....................
....................
```

 ## Run the script through tests
 
 Alternatively can all the boards be tested at the same time, using tests.
 `./run_tests.sh` will generate images of each solutions inside the folder `images`.
 It will also complain if the solution yields a best-first-path of different length.