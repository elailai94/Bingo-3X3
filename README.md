# Bingo 3X3
### About
Bingo 3X3 is a simple game of chance, which is inspired by [Bingo](http://en.wikipedia.org/wiki/Bingo_(U.S.)). It is written entirely in Python.

### Screenshots
#### Sample Game Interaction
![Bingo-3X3_Screenshot](https://cloud.githubusercontent.com/assets/7763904/7335138/75a0938e-eb78-11e4-8604-2a2c0abf6342.png)

### Execution
#### Direct Execution
```Bash
./game.py [bingo_card] [numbers_drawn]
```
> Note: **bingo_card** is the card with 9 numbers for the game and **numbers_drawn** is a list of 5 numbers drawn. For example, *./game.py '5 2 9 17 23 26 33 38 44' '2 5 9 30 45'* would print out a bingo card 3 rows high and 3 columns wide with a vertical match (as indicated by a vertical row of negative numbers).

#### Interpreter Invocation
```Bash
python game.py [bingo_card] [numbers_drawn]
```
> Note: **bingo_card** is the card with 9 numbers for the game and **numbers_drawn** is a list of 5 numbers drawn. For example, *python game.py '5 2 9 17 23 26 33 38 44' '2 5 9 30 45'* would print out a bingo card 3 rows high and 3 columns wide with a vertical match (as indicated by a vertical row of negative numbers).

### License
Bingo 3X3 is licensed under the [MIT license](https://github.com/elailai94/Bingo-3X3/blob/master/LICENSE.md).
