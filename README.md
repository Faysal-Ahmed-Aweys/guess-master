# **Guess Master**

Guess master is a game where the player tries to guess the number that the computer is thinking of in 3 tries.
The computer tells them the range and if they guess a number higher than the number that computer is thinking of, the computer tells them to go lower and if they guess a lower number, the computer tells them to go higher.
If they guess the number before the tries finish, they win otherwise they lose.

![Guess master](screenshots/Guess_master.png)

[Click here to play the game](https://guess-master-3f7c0042ba68.herokuapp.com/)

## **Planning stage** 
### **Target Audience**
* Anyone who likes to play guess-the-number games.
* Anyone who likes challenges.

### **Site Aims**
1. Make a fun guess-the-number game
2. Make the game with clear instructions on how to play and where user input is required.
3. Handle errors caused by player inputs and avoid crushing due to wrong inputs by the players. 

### **User stories** 
* Play a fun guess-the-number game
* If the guess of the number is wrong, a hint should be given to the player to improve the guess.
* The player should know the range of the numbers that the guess should be within.
* If the player fails, the number should be displayed. 
* Limit the number of tries the player gets to guess the number to make the game more fun. 

### **The plan to achieve the goals** 
* Build the game with clear instructions guiding the players on how to input and display clear feedback following correct or incorrect user input. 
* Make the game fun by adding a number of tries which the player gets to guess the number that resets each time they start the game. 
* Make the game fun by also adding a hint following each wrong guess.
* Display the range of the number to be guessed and display the number if the player is right or if the tries run out. 

## **Game Flow chart**

The game flow chart at the planning stage did not have the duplicate guess condition,
I have added that condition during the game development process as it would 
make the game more logical and fun.

![Game Flowchart](screenshots/lucid-chart-screenshot.png)

## **Game Features**

### **Welcome page**
The welcome page contains the game title in ASCII art to make it unique and stand out.
I used emojis throughout the game to make it more appealing to the players.
On the welcome page, The players can either start the game or access the game rules to familiarise themselves with how the game works.

![welcome page](screenshots/welcome_page.png)

### **Game-rules page**
The game-rules page explains to the players how the game is played, how to win and how one can lose.
The players can also start the game from this page after reading the rules and understanding how to play the game.

![game rules page](screenshots/game_rules_page.png)

### **Welcome page error handling**
On the welcome page where a player input of 1 or 2 is required, 
the player is asked again to "type 1 or 2" if they type in a number 
that is not 1 or 2. If they type nothing or not type a number 
an error is raised and "please type 1 or 2" is displayed.
 
![welcome page errors](screenshots/welcome_page_errors.png)

### **Game-rules page error handling**
On the game-rules page an error is raised and "You should input either y/n"
is displayed if the player does not input anything or gives a wrong input. 

![game rules page errors](screenshots/game_rules_errors.png)

### **Gameplay page**
At the start of the gameplay, the number of chances the player has to guess the number
and the input requiring the player to guess a number are displayed. 
 
![game page](screenshots/game_page.png)

### **Gameplay page error handling**
During the game play if you send an empty input or not input a number, 
an error is raised and the message "You should input a number" is displayed.
If you input a number not in the required range, a message claiming that
the number is not in the required range is displayed and the player is asked
to guess the number again without losing any of their chances. 
  
![game page errors](screenshots/game_play_errors.png)

### **Higher hint display**
Guessing a number lower than the number to be guessed displays a hint to the player that
they need to "guess a higher number".

![higher hint display](screenshots/higher_hint_display.png)

### **Lower hint display**
Guessing a number higher than the number to be guessed displays a hint to the player that
they need to "guess a lower number".

![lower hint display](screenshots/lower_hint_display.png)

### **Win display**
When the player wins, a message congratulating the player and a cool face emoji doing a thumbs up is displayed
to give the feedback that the player has successfully guessed the number right. The correct number is also displayed.

![win display](screenshots/win_display.png)

### **Lose display**
When the player loses, the message "Game over" and a pensive face emoji is displayed to give 
the feedback that the player has failed to guess the number after using all available tries. 
The correct number is also displayed. 

![lose display](screenshots/lose_display.png)

### **Duplicate number error handling**
Guessing the same number twice is not accepted however, the player does not lose tries for it
instead a message that they already guessed that number is displayed and the player can try again. 

![duplicate number error](screenshots/duplicate_number_error.png)

## **Future-Enhancements**
I believe i have added everything I thought was necessary to include in the game. However, 
the following features will make the game much more fun. 

1. Let the player select the range within which they can guess the number and based on that range,
give the player a certain number of tries so the players can challenge themselves more.
2. A multiplayer version of the game where one player gets a chance to guess the number and if they fail,
the other player gets a chance to guess the number and whoever guesses the number first wins. 

## **Libraries used**
1. random - Used to generate a random number between 0 and 10 for the player to guess. 
2. system from OS - Used to clear the console off of outdated data from previous games
or previous page when a new page is displayed. 
3. emoji - Used to display emojis on the console.

## **Testing**
### **Manual Testing**
* Throughout the game development and after development, 
I tested the game manually on my Mac terminal and Heroku app terminal.
One of the issues i found was when the player has one chance left to guess 
the number, the input was not being checked if it was between 0 and 10 inclusive. 
I fixed this by adding a conditional statement to check for and validate the input.
* During the game development i used print statements to test the correct output 
is being displayed.

#### **Unfixed bugs**
The game works with no errors or bugs. There are no unfixed bugs.

### **Validation**
#### **Code Institute Python Linter** 
![CI Python Linter](screenshots/ci_py_linter.png)
Code institute Python Linter returned some errors.
Almost all of the errors were lines longer than 79 characters
And one error of trailing whitespace.
I shortened the lines and added continuation lines below them and 
thus got no errors after testing my python code again. 

![CI Python Linter Improved](screenshots/ci_py_linter_imoroved.png)

![](screenshots/HTML_validator.png)
I made some changes including adding a background image in layout.html using style tag
and to make sure there were no errors in the HTML and CSS code i did a validation test
which returned no errors.

![](screenshots/CSS_validator.png)



## **Deployment**
I took these steps to deploy the game to [Heroku.com](https://www.heroku.com)

1. Log in to your Heroku account or Create a new account.
2. On the dashboard click new and then create new app.
3. choose and enter a unique name, select the region and click create app.
4. Select the Settings tab in the created app.
5. Scroll down to add buildpack and click on it. 
6. Choose python and press add buildpack. 
7. Repeat step 5 and choose node.js.
8. Navigate to the Deploy tab on top.
10. Select GitHub as the deployment method and connect to GitHub.
11. Search for the repository name of the project and click connect.
12. I enabled automatic deploys in order to deploy each time new code is pushed to the repository.
13. Click Deploy Branch to deploy the project.
 
### **Credits**
#### **Honourable mention** 
I would like to thank my mentor **David Bowers** for his incredible support throughout
the development of my game.

#### **content**
* I used the Code Institute template to enable me to have terminal in the browser for my game to run. 
* I read about the OS library and how to import it from [lewiskori.com](https://lewiskori.com/blog/how-to-clear-screen-in-python-terminal/).
The idea and how to use this library was introduced to me by my mentor **David Bowers**.

#### **Media and Design**
* I made the ASCII art of my game title using [patorjk.com](https://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=).
This was also introduced to me by my mentor **David Bowers**
* The background image is from [123rf.com](https://www.123rf.com/photo_26576728_numbers-background.html)
* The favicon image is from [amazon.co.uk](https://www.amazon.co.uk/JACTheCreator-Guess-The-Number/dp/B0797Z83HK)
* I used [Lucid.app](https://lucid.app/lucidchart/d1802f2b-a899-4c97-9e82-75011db4ea65/edit?beaconFlowId=E01F33C4C6948D91&invitationId=inv_66e53440-8220-4bbd-bac5-c1db3f56feb8&page=0_0#)
to make the game flowchart.
 
