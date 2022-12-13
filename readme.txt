readme.txt

//aaaaaaaaaaaaaaaaaaa//

This is a Python project for https://adventofcode.com/2022/day/2/

The goal is to run a rock, paper scissors game with different score points per choice and win condition.
The input is a strategy guide of game inputs, split via opponent/player.
For example, the opponent will choose X which is Rock, and you will choose B which is Paper; etc

This prohject takes the input (A X B Z C Y), converts to string, then splits the inputs into 2 lists. One for opponent
actions, another for player actions.

This then calls matchup(opponent[], player[]) to run rps() per incremental item until finished.
rps() runs the rock paper scissors game and tallies the win+choice and returns the sum up through the process.

The result when run gave me my total of 14827, completing the puzzle.

You can run this on your own quiz inputs, or dummy inputs.