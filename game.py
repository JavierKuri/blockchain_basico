from block import block
from blockchain import blockchain
from player import player
import random
import json

if __name__ == "__main__":
    
#Initialize variables for the blockchain, the players, and the game itself
    game_transactions = blockchain()
    players = []
    n_of_players = 4
    for i in range (0, n_of_players):
        players.append(player(id=i))
    n_of_transactions = 5

#Generate random transactions between players and add them to the blockchain
    for i in range (0,n_of_transactions):
        playerA = 0
        playerB = 0
        money_sent = 999999
        while (playerA == playerB):
            playerA = random.randint(0,3)
            playerB = random.randint(0,3)
            while (players[playerA].money<money_sent):
                money_sent = random.randint(0,players[playerA].money)
            players[playerA].money -= money_sent
            players[playerB].money += money_sent
        content = f"Player {playerA} sent {money_sent} dollars to player {playerB}"
        game_transactions.add_block(content)

#Save the blockchain in a json file
        with open("./transactions.json", "w") as f:
            json.dump([b.__dict__ for b in game_transactions.chain], f, indent=4)
    
#Print blockchain in a readable way and verify the hashes
    for i, block in enumerate(game_transactions.chain):
        print(f"Block {i}:")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Timestamp: {block.timestamp}")
        print(f"  Content: {block.content}")
        print(f"  Hash: {block.hash}\n")
    game_transactions.verify_hashes()