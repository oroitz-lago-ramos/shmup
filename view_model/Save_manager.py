import json

class Save_manager:
    def __init__(self) -> None:
        self.path = "./model/save.json"
        
    def save_score(self, user_name, score):
        try:
            with open(self.path, 'r') as f:
                scores = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            scores = []

        scores.append({'user_name': user_name, 'score': score})

        with open(self.path, 'w') as f:
            json.dump(scores, f)
        
    def load_scores(self):
        try:
            with open(self.path, 'r') as f:
                scores = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            scores = []

        return scores
    
    def get_best_scores(self):
        scores = self.load_scores()

        scores.sort(key=lambda score: score['score'], reverse=True)

        return scores[:5]  # Change this number to change the number of scores returned
    
    def get_last_score(self):
        scores = self.load_scores()
        if len(scores) > 0:
            return scores[-1]
        return None
    
    def last_score_in_best_scores(self):
        best_scores = self.get_best_scores()
        last_score = self.get_last_score()
        if last_score in best_scores:
            return True
        return False
    
    def get_hall_of_fame(self):
        if self.last_score_in_best_scores():
            return self.get_best_scores()
        else:
            scores = self.get_best_scores()
            last_score = self.get_last_score()
            scores.sort(key=lambda score: score['score'], reverse=True)
            # Insert at index 4
            scores.insert(4, last_score)
            return scores[:5]