# WPM
Words_Per_Minute calculator 
 Typing Speed Test – Python CLI Game
This is a fun and interactive command-line Typing Speed Test game written in Python. The game challenges you to type randomly generated sentences as fast and accurately as possible. At the end of each round, your WPM (Words Per Minute) and accuracy are calculated and saved to a local leaderboard.

 Features
 Random sentence generation using custom lists of subjects, verbs, adjectives, and objects.

 Calculates:

Words per minute (WPM)

Typing accuracy (%)

Elapsed time

 Saves your score (with name and timestamp) to a scores.txt file.

 Displays a leaderboard of top performers.

 Option to play again after each round.
 File Structure
sentences.txt – (Optional) You can customize or expand sentence sources.

scores.txt – Stores saved scores (name, WPM, accuracy, time).

 Requirements
Python 3.x

No external libraries needed – uses built-in modules:

random

string

time

datetime

 How to Run
bash
Copy
Edit
python typing_test.py
Follow the prompts in the terminal. You'll type three generated sentences as fast and accurately as you can, then see your results and the current leaderboard.

 Example Session
vbnet
Copy
Edit
Type the following sentences as fast and accurately as you can:

The cat jumps quick on the roof. And A dog sings dark with joy. And An artist runs happy under the stars.

Press enter to start...

Start typing, quickly:
The cat jumps quick on the roof. And A dog sings dark with joy. And An artist runs happy under the stars.

Test complete, Well done!
Time: 19.28 seconds
WPM: 42.1
Accuracy: 100.0%

Enter your name for the leaderboard :) Alice

Leaderboard:
1. Alice - 42.1 WPM - 100.0% - 2025-06-02 10:33:25
 Notes
Make sure scores.txt exists or is created automatically when saving scores.

You can modify the sentence parts in the script to generate more creative challenges.

 Ideas for Improvement
Add difficulty levels (e.g., short vs. long sentences).

Use sentences from a file (already partially integrated).

Add GUI support with tkinter or PyQt.

Track improvement over time with user profiles.

