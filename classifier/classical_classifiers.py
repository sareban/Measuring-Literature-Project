from sklearn.ensemble import RandomForestClassifier


class RFClassifier:
    '''
        Random forest classifier
    '''

    def __init__(self, X, Y):
        self.model = RandomForestClassifier(bootstrap=True, criterion='gini',
                                            min_samples_split=2, max_features='auto', min_samples_leaf=1,
                                            n_estimators=1000)
        self.X = X
        self.Y = Y

    def tune_and_eval(self, results_file, params=None, feature_names=None):
        '''
        Tune, evaluate, extract features (if a list of features are provided)
        :param results_file:
        :param params:
        :param feature_names:
        :return:
        '''
        if params is None:
            params = [{"n_estimators": [100, 200, 500, 1000],
                       "criterion": ["entropy"],  # "gini",
                       'max_features': ['sqrt', 'auto'],  # 'auto',
                       'min_samples_split': [2, 5, 10],  # 2,5,10
                       'min_samples_leaf': [1], 'class_weight': ['balanced', None]}]
