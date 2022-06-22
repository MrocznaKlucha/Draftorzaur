from Player import Player 

class Game:
    def __init__(self,player):
        print("test")
        for a in player:
            print(a.name)
    def random_first_player(self,player):
        pass
def main():
    player = [Player("Darek"),Player("Dominika")]
    game = Game(player)
    

if __name__ == "__main__":
    main()
    
