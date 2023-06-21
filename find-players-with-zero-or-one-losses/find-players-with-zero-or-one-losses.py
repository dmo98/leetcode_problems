from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # Using a HashMap to store frequency of wins/losses
        win_counts = defaultdict(int)
        loss_counts = defaultdict(int)
        
        for match in matches:
            winner, loser = match[0], match[1]
            win_counts[winner] += 1
            loss_counts[loser] += 1
            
        
        no_losses = []
        for player in win_counts.keys():
            if player not in loss_counts:
                no_losses.append(player)
        
        one_loss = []
        for player in loss_counts.keys():
            if loss_counts[player] == 1:
                one_loss.append(player)
                
        return [sorted(no_losses), sorted(one_loss)]