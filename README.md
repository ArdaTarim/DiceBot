# DiceBot
*a discord bot that can do various tasks, created with discord.py*
### how to add the bot to your server
1. navigate to discord applications page https://discord.com/developers/applications
2. click on the New Application button
3. give the application a name and click create
4. navigate to the bot tab
5. copy bot's token using copy button
6. navigate to the OAuth2 > URL Generator
7. tick the bot checkbox
8. tick the permissions required for the bot to function (i just do Administrator)
9. now the URL can be used to add bot to your server
### how to run the bot:
1. paste your token to **TOKEN = ""** inside the DiceBot.py file
   (invite link is optional)
  <img width="285" alt="image" src="https://github.com/ArdaTarim/zarbot/assets/122305197/457642f9-5bec-4620-a3dd-4211627038c7">

2. run the DiceBot.py file

### bot commands and how to use inside the server:
- use "DiceBotHelp" to see all commands
- you can add activity to bot by changing the **name = ""** inside DiceBot.py

  <img width="469" alt="Ekran Resmi 2024-01-16 17 23 54" src="https://github.com/ArdaTarim/zarbot/assets/122305197/4aae6914-6621-4603-903e-a8aa4d449d11">

*List of commands:*
- **DiceDecide**
  
  makes a random decision between given inputs
  
  ex. input: A,B,C,D
  
  ex. output: C
  
- **DiceMatch**

  matches given inputs to each other
  
  ex. input: A,B,C,D
  
  ex. output: A->B, B->D, D->C, C->A
  
- **DiceTeam size: n**
  
  creates teams of size n from the given inputs
  
  ex. input: A,B,C,D,E
  
  ex. output: Team 1: A,C,E Team 2: B,D
    
