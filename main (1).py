class player:
  def play (self):
    print("The player is playing cricket.")

class Batsman(player):
  def play (self):
    print("The batsman in bating.")

class Bowler(player):
  def play(self):
    print("The bowler in bowling.")
batsman=Batsman()
bowler=Bowler()
batsman.play()
bowler.play()

  






  
