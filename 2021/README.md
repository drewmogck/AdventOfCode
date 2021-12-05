# AdventOfCode_2021

### Code snippets from Advent of Code 2021.

### Notes:  
* Day 1: 
    * Part 1 - super easy. Oh hey I should build a function for this just to be good about it.
    * Part 2. Oh yeah. glad I built the function. Learned how to build the sectional subset with list comprehension. Python always amazes me with its simplicity.

* Day 2: Another fairly simple day where building the code smartly for part 1 pays off handsomely in part 2. Pretty straightforward.

* Day 3: 
    * Part 1: Pretty straightforward.
    * Part 2: Got hung up trying to get too fancy storing things in a dictionary. Finally realized much simpler in this case just to store to list and busted out the answer. Initial code is messy, will clean up at later point for part 2, there is a much more streamlined way of doing this than duplicating the code but wanted to get the answer in and it was getting late. Back to it tomorrow...

        * Day 3 part 2 edit: cleaned up part 2 to be simpler and use single function to run both O2 and CO2 numbers

* Day 4:
    * Part 1: Ooof. Knew right away this was going to be a bit tricker. Seems to be a trend with day 4 on AoC. Set up dictionaries to hold bingo boards and values, then assign ability to flip them and check for winning bingos. Thankfully diagonals didn't have to be considered. Overall, took a bit of work, but nothing too crazy. Had same confusion I remember having last year when I use x,y as positioning when dealing with row columns. I implicitly use x, y as col,row, but whenever I think about it I want to think of it as row,col, so I inevitably end up mixing something up. Slow and steady works out though... Probably a much better way to break out of my loop for checking the winners than the way I have it setup, but hey... it works.
    * Part 2: This was fairly simple once I correctly interpreted the question. Initially read it as playing all possible plays and getting the last winning row/colunm, but in reality needed to stop when the last board has its first win. Once I figured this out, pretty straightforward to modify code from part one to work... It's UGLY though. Want to come back and rework this one if I ever have the time.

* Day 5:
    * Part 1: OK. Not too crazy. Set up a dictionary to store the locations of the lines, then loop through and set the values. Not too bad in the horizontal and vertical direction only... but I'm sure thats where part 2 comes in...
    * Part 2: Yep. here's the diagonals. Thankfully limited to only 45 degrees, that makes things simpler. I can just take if absolute values of the differences between them are the same to check if diagonal, then determine the line from there.... was a little trickier than I anticipated at first, mostly because I had to figure out how to account for the directionality of the pairs. My original code didn't care about that and had to edit to account for it. But makes overall function cleaner for both parts.