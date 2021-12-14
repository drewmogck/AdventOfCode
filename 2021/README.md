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

* Day 6:
    * Part 1: Could brute force this. Got hung up knowing a part two was coming where brute force wouldn't work. Low on time. Went to reddit for inspiration. Brute forced part 1 anyways because easy. Solution inspired by https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnfis0v/?utm_source=share&utm_medium=web2x&context=3
    * Part 2: Knew this was coming. Reddit solution was pretty ingenious actually. Just dealing with the group counts. So clean. Wish I could say it was my idea ha. I was on the right track, thinking there was a way to do this by just thinking of each group individually, but couldn't think of how to implement it.

* Day 7:
    * Part 1: Whoo! I know how to do this one. Just check sums of absolute values of data minus each possible position. Super quick. Works great.
    * Part 2: OK... same as part 1, but need to loop thorugh and sum the total cost at each given distance. I'm sure there's a more elegant way to do this given the time it took to run, but right before I was about to stop the code because it was taking a while it computed. So I'll take the win. Tomorrow will maybe look to see how it can be optimized to run faster.

* Day 8:
    * Part 1: ok part 1 isn't bad, I'm sure part two will be a doozy thoough. Simple count of number of unique numbers. A little dictionary and counting and we are through
    * Part 2: I think I have an idea of how to do this, but its going to be time consuming. Maybe will come back to this one later, or look for inspiration on the forums. INCOMPLETE RIGHT NOW

* Day 9:
    * Part 1: Not too bad. Need to index where things are at in a dictionary and just check around each point to see if its a min. Used 99 instead of null at edges just so didn't have to deal with checking values against 'None'.
    * Part 2: A lot trickier. Had to set up to initialize at the minimums, check the y and x directions for any in a given "basin" then go back and check all the points that were in a given basin the same way. Keep going until all points are checked. Once I figured out the methodology it wasn't too bad. Other than dealing with edge cases (eg left, right, top bottom) which always seem to bite me on these sorts of problems in AoC. Need to clean up the code for readability, but it works.

* Day 10:
    * Part 1: Took a bit to think through, but once I figured out how to structure the dict to store the information it wasn't too bad.
    * Part 2: Love it when planning pays off. The way I set up part 1 was perfect to be able to continue part 2. Pretty simple to get once I figured out exactly what the problem statement was looking for in the answer. Oh yeah and not trying to calculate the full solution with the example input... Doh!

* Day 11:
    * Part 1: Trick here was to use energy level 10 as the key rather than >9. This forces them to only flash once. Realized that after getting stuck in an endless loop of flashing the first time I ran the code. Other than that it was just a matter of going slow and steady and makeing sure directions (up, down, up-right, down right etc) were actually defined properly.  Code could use some cleaning but that's for another day.
    * Part 2: Took me alittle longer than it should have because I forgot to reinitialize the grid so it was counting from 100 starting. Also tried checking for when all values were 9 rather than 0, thinking that would actually be the step right before they all fliped. Before realizing that they don't all flip simultaneously just because they are 9's. Other than those little blips, it was really pretty simple based on the way I set up part 1.

* Day 12:
    * Part 1: Messed around for quite a while here (Day13.py). Was getting hung up on how to get through it and pretty sure I was heading down some rabbit holes so I gave it up for the night. Pulled an interesting solution from the Reddit threads https://www.reddit.com/r/adventofcode/comments/rehj2r/comment/ho7x83o/?utm_source=share&utm_medium=web2x&context=3 Plan to come back to this one to better understand the solution because it's really clean but I'm not 100% on how it works.
    * Part 2: See part 1.

* Day 13:
    * Part 1: Happy to get back on track. This was a fun one. Got to play around with a lot of numpy functionality to flip/append etc. Use the where clause for the actual overlay. The example being setup to only use exactly equal folds was a bit of a ruse. Got a working solution that instantly blew up on the real data because of course the page isn't always folded down the middle. Was interesting to think about how to set it up to account for the different sizes. Thankfully the folded part never was large enough to overlap and reset the 0 indices or this would have gotten a lot harder.
    * Part 2: Not bad. Code was already completely set up to run, just had to refresh on how to plot the image from the array. Even made up some ground in the leaderboard instead of losing for a change. Overall really enjoyed this approach tonight and gave me a greater appreciation for the functionality in numpy.

* Day 14:
    * Part 1: This one was pretty straightforward, just took a bit of thought of how to handle the insertions without double adding letters. Ended up doing an odd/even check. Just had to make sure to catch the last letter propperly. Used Counter from collections for first time to count the occurances... purely happenstance, becasue this turned out to be key for part 2.
    * Part 2: Pretty obvious that this was setup so the brute force method from 1 wouldn't work. Had an inkling we needed to do something like count the number of pairs for this to not blow up, but wasn't sure how to implement it. Went to the forums to look and found a nice simple solution here: https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hoh8xq2/?utm_source=share&utm_medium=web2x&context=3 that used the Counter that made perfect sense to me. Modified to match my syntax and away we go. Like the challenges where I learn something new, even if it means I have to get some help along the way. That's half the reason I do these challenges is to broaden my scope of knowledge.