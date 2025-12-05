As previously mentioned, this program was made for Super Smash Brothers Ultimate players who are new to the competitive scene. More specifically, the design was for the Southern Utah University competitive scene, which sees its fair share of new and inexperienced players. Since the program is geared towards newer players that may not have advanced knowledge of With this in mind, the main thought process was to make a simple-to-use project that contains both a command line interface (CLI) and a graphical user interface (GUI). This is just in case there is a pop-up block that does not allow for the GUI to function properly. When creating the CLI, there should be a menu containing only the necessary options for being able to access the information needed. In this case, it was decided that there would be three options for this menu: see list of all available characters, search best stage by character, and exit. The GUI would be a separate file that takes the code of the CLI and creates a more user-friendly interface.

Overall, I was very happy with this program. I learned how to use tkinter for GUIs better and realized the importance of thoroughly structuring out programs before working on a project. Because I learned how to do these things, I was able to do what I wanted my program to do. For the future, it would be ideal to input all of the characters and create more options in the menu for users to choose from (including frame data, best/worst move by character, etc.). On top of this, visual appeal can be greatly improved, including background, text, and button changes.  

Class/Logic Diagram

Stage (class)
Stores all legal stage names
Stage name will be a private attribute

Character (abstract class)
initializes/defines character name, stage, & methods to describe best stage/reasoning.
Stage will be a private attribute

Characters: Pikachu, Mario, Etc. (subclasses)
Inherits from Character
Defines optimal stage & reasoning

Functional Specification

What the user should see:

This program is developed to help users find the best stage for their character.
To see a list of all characters, enter 1
To search the best stage by character, press 2
To exit, press 3
Choose an option:
(1,2,3)

You have chosen option 1: List all characters
Here is a list of all of the playable characters in SSBU:
Mario
Luigi
…  

You have chosen option 2: Search by character
Enter character name:
(Mario)
Mario’s best stage is Battlefield!
Mario relies on up air ladders to get kill confirms, which is much easier on the stage with the most platforms.

OR:

You have chosen option 2: Search by character
Enter character name:
(Tom Holland)
Error. Character not found.
Please enter a character name:
…

You have chosen option 3: Exit
(exits program)

