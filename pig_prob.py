import sys

class PigProbabilities:
    """ The probabilities of all possible outcomes for a turn when
        rolling until a pre-chosen target is reached.
    """

    def __init__(self, game_target):
        """ Creates an object to hold the probabilities for all possible turn
            targets up to game_target.

            game_target -- an integer greater than or equal to 2
            """
        if game_target < 2:
            raise ValueError("game target must be at least 2 %d" % gameTarget)

        self.max_target = game_target

        self.p_reach = [0.0] * (game_target + 1)
        self.p_end = [];
        for i in range(game_target + 1):
            self.p_end.append([0.0] * 7)
        
        self.p_reach[0] = 1.0
        for i in range(2, self.max_target + 1):
            # reach i by getting to i-2 and rolling a 2, i-3 and rolling a 3... 
            for j in range(2, 7):
                if i - j >= 0:
                    self.p_reach[i] = self.p_reach[i] + self.p_reach[i - j] / 6.0
            
            self.p_end[i][0] = self.p_reach[i]
            self.p_end[i][6] = 1.0 - self.p_end[i][0]
            for j in range(1, 6):
                r = min(6, i + j)
                while r >= 2 and i + j - r < i and i + j - r >= 0:
                    self.p_end[i][j] = self.p_end[i][j] + self.p_reach[i + j - r] / 6.0
                    r = r - 1
                self.p_end[i][6] = self.p_end[i][6] - self.p_end[i][j];

    def p_end_at(self, turn_target, end_score):
         """ Returns the probability of ending a turn at the given score with
             the given target.

             turn_target -- an integer at least 2 and no more than the game
                            target
             end_score an integer
         """

         if turn_target < 2:
             raise ValueError("turn target must be at least 2: %d" % turn_target)

         if turn_target > self.max_target:
             raise ValueError("turn target must be no more than %d: %d" % (maxTarget, turnTarget))

         if end_score == 0:
             return self.p_end[turn_target][6]
         elif end_score >= turn_target and end_score <= turn_target + 5:
             return self.p_end[turn_target][end_score - turn_target]
         else:
             # won't end turn < turn_target or > turn_target + 5
             return 0.0;

def main():
    turn_target = int(sys.argv[1])

    p = PigProbabilities(turn_target)
    print("p(0) = %f" % p.p_end_at(turn_target, 0))
    
    for i in range(0, 6):
        print("p(%d) = %f" % (turn_target + i, p.p_end_at(turn_target, turn_target + i)))
        
if __name__ == "__main__":
    main()