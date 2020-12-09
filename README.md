# AdventOfCode_2020

### Code snippets from Advent of Code 2020. Using as an excuse to drag myself out of R where I am pretty comfortable and get some daily work in with Python.

### Notes:  
- Day 1: Not too bad some quick nested for loops and we're off to the races. 
- Day 2: Got frustrated with pandas, too used to the tidyverse - ended up doing some in excel due to time constraints (got a late start) and the simple frustration of knowing what I wanted to do but struggling to implement it in code.  
- Day 3: Back on track - pretty simple breakdown, follow the instructions, no major snags in this one.
- Day 4: That was a doozy. Had to watch my regex. Been a while since I've used and spent a while debugging why I was off on the final count (by 1!) . Starting to remember to use functions to my advantage.
- Day 5: Went pretty smooth - sure my code could be cleaned up but pulled through this one in a decent time. *Note to self: remember to clear the new line character from text data when parsing... 
- Day 6: Def need to figure out a cleaner way to deal with last line of text files when breaking up groups, but short and sweet.
- Day 7: This was another tough one. My code's a mess, but it does the job for now. Half the challenge was just wrapping mind around the problem and how to solve it. This was the first day I didn't immediately have a good idea how to get to a solution. The recursiveness took a while to wrap my mind around and figure out how to handle. First attempt writting everything to a variable gave memory error. Whoops. Lesson learned. Massive tree structure of suitcases inside of suitcases inside of suitcases... you get it. Besides the mindwarp hit a few snags forgetting that Python will edit a list in place - defining a new list from an old one can get dangerous. But good to break out the dictionaries and experiment with them. Definitly going to look up other solutions to this one as I'm fairly confident the approach I took is not the most efficient.
- Day 8: Phew. Short and sweet, no major roadblocks on this one. Some fairly simple functions to define what should happen at each line and while loops to control the flow. Part 2 was fun, get to use the index to find the solution.
- Day 9: Another relatively easy day. Reused a bit of code from day one to check for the sum in the first part. Second part iterativly approach summing up the rows. There may be a faster way to do this, but the dataset is small enough brute force works just fine.