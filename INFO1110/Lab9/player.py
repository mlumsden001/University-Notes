class Player:
    def __init__(self, name, score):
        self._name = name
        self._score = score


    def score(self):
        return self._score

    def name(self):
        return self._name

    def best_score(players):
        best = p1
        i = 1
        while i < len(players):
            if players[i].score > best.score:
                best = players[i]
            i += 1
        return best

if __name__ == "__main__":
    p1 = Player('Candy', 50)
    p2 = Player('Ferb', 250)
    p3 = Player('Phineas', 150)
    ls = [p1, p2, p3]
    best = Player.best_score(ls)
    msg = '{} has the best score, with {} points!'.format(best._name, best._score)
    print(msg)
