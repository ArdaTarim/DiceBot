import re
import discord
import random
from Exceptinos import InputError
from CircularLinkedList import CircularLinkedList


TOKEN = ""
invite_link = ""

class DiceBot(discord.Client):
    """DiceBot, discord bot"""
    def __init__(self, intents, activity):
        super().__init__(intents=intents, activity=activity)

    async def on_ready(self):
        print(f"Bot is online! Logged in as {self.user}")

    async def on_message(self, message):
        if message.author.bot or message.author == self.user:
            return

        if message.content.startswith("DiceDecide"):
            try:
                await self.diceDecide(message)
                await message.add_reaction("👍")
            except InputError as e:
                await message.channel.send("Please enter a valid input.")
                print(f"An unexpected error occurred: {e}")
                await message.add_reaction("👎")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                await message.add_reaction("👎")

        if message.content.startswith("DiceMatch"):
            try:
                await self.diceMatch(message)
                await message.add_reaction("👍")
            except InputError as e:
                await message.channel.send("Please enter a valid input.")
                print(f"An unexpected error occurred: {e}")
                await message.add_reaction("👎")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                await message.add_reaction("👎")
        
        if message.content.startswith("DiceTeam"):
            try:
                await self.diceTeam(message)
                await message.add_reaction("👍")
            except InputError as e:
                await message.channel.send("Please enter a valid input.")
                print(f"An unexpected error occurred: {e}")
                await message.add_reaction("👎")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                await message.add_reaction("👎")

        if message.content == "DiceBotHelp":
            await message.channel.send("""
                                                
            DiceDecide <A, B, C>
ex. output: B
                                       
DiceMatch <A, B, C, D, E>
ex. output: A->B, B->D, D->C, C->E, E->A 
                                       
DiceTeam <A, B, C, D, E, F, size:3>
ex. output: A,E,D and B,C,F
    
            """)
    
    async def diceDecide(self, message):
        try:
            text: str = message.content
            text = text.replace("DiceDecide ", "")
            decisions = list()
            decisions = text.split(",")
            for _ in decisions:
                if " " in _:
                    _.replace(" ", "")
            
            await message.channel.send(f"I decided, {random.choice(decisions)}")
        except Exception as e:
            raise InputError()
        finally:
            print(f"DiceDecide called")

    async def diceMatch(self, message):
        linkedList = CircularLinkedList()
        try:
            text: str = message.content
            text = text.replace("DiceMatch ", "")
            elements = list()
            elements = text.split(",")
            for _ in elements:
                if " " in _:
                    _.replace(" ", "")
            for _ in elements:
                linkedList.append(_)
            linkedList.shuffle()
            await message.channel.send(f"Matches are, {linkedList.asPrint()}")
        except Exception as e:
            raise InputError()
        finally:
            print(f"DiceMatch called")

    async def diceTeam(self, message):
        try:
            text: str = message.content
            text = text.replace("DiceTeam ", "")
            pattern = r'size\s*:\s*(\d+)'
            match = re.search(pattern, text)
            try:
                size = int(match.group(1))
            except Exception as e:
                message.channel.send("Invalid team size.")
                raise InputError
            
            players = list()
            players = text.split(",")
            for _ in players:
                if " " in _:
                    _.replace(" ", "")
            
            noTeams =  (int) (len(players)/size) if len(players)%size==0 else (int) (len(players)/size + 1)

            result = ""
            for _ in range(noTeams):
                result += "".join(f"Team {_+1} : ")
                for i in range(size):
                    player = random.choice(players)
                    result+= "".join(f"{player} ")
                    players.remove(player)
                result += "\n"
            
            await message.channel.send(f"{result}")

        except Exception as e:
            raise InputError()
        finally:
            print(f"DiceMatch called")


activity = discord.Activity(name="",
                            type=discord.ActivityType.watching)
intents = discord.Intents.default()
intents.message_content = True

# bot runs here
bot = DiceBot(intents=intents, activity=None)
bot.run(token=TOKEN)
