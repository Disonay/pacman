from util import manhattanDistance


class Shield:
    def __init__(self, pacmanPos, ghostPos, legalActions, action_qval_list, action):
        self.pacmanPos = pacmanPos
        self.ghostPos = ghostPos
        self.legalActions = legalActions
        self.action_qval_list = action_qval_list
        self.apply(action)

    def apply(self, action):
        safe = False
        sorted(self.action_qval_list, key=lambda x: x[1], reverse=True)
        i = 0
        discarded = []
        while not safe and len(self.legalActions) != 0:
            px, py = self.pacmanPos
            if action == 'East':
                px += 1
            elif action == 'West':
                px -= 1
            elif action == 'North':
                py += 1
            elif action == 'South':
                py -= 1

            safe = True
            for j in range(len(self.ghostPos)):
                ghostpos = self.ghostPos[j]
                dist = manhattanDistance((px, py), ghostpos)
                if dist < 2.0:
                    safe = False
                    discarded.append(action)
                    self.legalActions.remove(action)
                    break
            if not safe and i < len(self.action_qval_list):
                action = self.action_qval_list[i][0]
            i += 1

        return action, discarded
