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