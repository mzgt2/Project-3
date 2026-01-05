# Day-3-Project

## Treasure Island

A text-based adventure game where you make choices to find treasure while avoiding various dangers.

## About

Built this as a Python learning project to practice conditionals, user input, and control flow. You make a series of choices (left/right, wait/swim, which door) and each choice leads to either progression or a game over.

## How to Play

Run the game:
```bash
python treasure_island.py
```

Follow the prompts and make your choices:
- **First choice:** Left or Right path
- **Second choice:** Wait or Swim across the lake
- **Third choice:** Red, Yellow, or Blue door

Only one path leads to the treasure. Most choices result in... creative deaths.

## Example Playthrough
```
Welcome to Treasure Island.
Your mission is to find the treasure.
Choose your path, left or right?
> left
You traverse a dense jungle when suddenly you get ensnared in a rope trap but you manage to escape.
You continue through the jungle until you come across a lake. Swim or wait?
> wait
You wait for while until you see a small boat down the shoreline. You use the boat to traverse the lake.
You reach the other side and approach the abandoned mansion...
[etc.]
```

## Game Outcomes

There are multiple ways to die (cannibals, sirens, dragon, iron knight, zombies) and only one way to win. Good luck!

**Hint:** Not all paths are created equal. Some choices are... significantly worse than others.

## What I Learned

- Using `if/elif/else` statements for branching logic
- Getting user input with `input()`
- String methods like `.lower()` for input validation
- Using `exit()` to end the program
- Checking multiple values with `in` operator
- ASCII art (the treasure chest at the beginning)

## Code Structure

Pretty straightforward:
1. Display ASCII art treasure chest
2. Get first choice → validate → continue or game over
3. Get second choice → validate → continue or game over  
4. Get third choice → validate → win or game over

Each wrong choice calls `exit()` to end the game.

## Potential Improvements

If I expand this later:
- Add more paths and choices
- Track player stats (health, items)
- Save/load game state
- Add random encounters
- Multiple endings based on choices made

---

*Day [X] learning project - practicing Python conditionals and user input*
