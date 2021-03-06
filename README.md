# US Citizenship Civics Test Study Aid

A text-based tool to ask random questions from the [2008 Civics Test](https://www.uscis.gov/sites/default/files/document/questions-and-answers/100q.txt).  After each question, hit RETURN to see the answers then assign a weight 0-9 to this question. Questions with higher weights will be asked more frequently and a weight of 0 prevents a question ever being asked.

The first time you run this script, all questions will have weight 5.  Weights are stored in a plain text file `weights.dat` that is updated after each question (with a backup saved as `weights.dat.bak`).  Rename or delete this file to reset all weights to 5.

The questions are stored in a plain text file `questions.txt`. Some answers depend on your current elected officials but you can edit this file to make any changes.  The current answers are for California's 45th congressional district in 2021.

When you exit the script (by entering `q`) a file `sorted.txt` is written containing the 100 questions in order of decreasing difficulty (weight), for convenient studying away from your computer.

Good luck with your test!

## Instructions

To make a local copy of the questions and python script use:
```
git clone https://github.com/dkirkby/civics.git
cd civics
```
To run the script use:
```
python civics.py
```
