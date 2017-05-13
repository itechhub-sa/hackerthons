from sklearn.ensemble import RandomForestClassifier
from app.fraud_engine.utils import DataSample
from sklearn.metrics import accuracy_score


class RandomForestModel:

    def __init__(self):
        self.classifier = RandomForestClassifier()
        self.Xtrain, self.ytrain, self.Xtest, self.ytest, self.Xsim, self.ysim \
            = DataSample()

    def train(self):
        self.classifier.fit(self.Xtrain, self.ytrain)
        #print self.classifier.feature_importances_

    def get_accuracy(self):
        predicted = self.classifier.predict(self.Xtest)
        anomaly_points = predicted.tolist().index(0)
        #print self.Xtest[anomaly_points]
        self.classifier.fit(self.Xtest, self.ytest)
        #print self.classifier.feature_importances
        accuracy = accuracy_score(self.ytest, predicted)
        return accuracy, anomaly_points
