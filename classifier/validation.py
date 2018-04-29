from sklearn.model_selection import cross_val_score


class Validator(object):
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.scoring = {
            'accuracy': 'accuracy',
            'scores_p_1': 'precision',
            'scores_r_1': 'recall',
            'scores_f_1_1': 'f1'}

    def accuracy_validation(self, model):
        cross_val_score(model, self.X, self.Y, scoring='accuracy')
