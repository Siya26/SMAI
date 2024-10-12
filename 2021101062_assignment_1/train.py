import sys
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

class Knn:
    def __init__(self, k, metric, encoding):
        self.k = k
        self.metric = metric
        self.encoding = encoding

    def predict(self, enc, train_data, validation_data):
        pred = []
        for test in validation_data:
            test = test[enc][0]
            list_distance = []

            for train in train_data:
                train_enc = train[enc][0]
                distance = self.compute_distance(test, train_enc)
                list_distance.append([distance, train[3]])
                
            list_distance.sort(key=lambda x: x[0])
            list_distance = list_distance[:self.k]
            train_labels = [x[1] for x in list_distance]
            pred.append(max(set(train_labels), key = train_labels.count))

        return pred

    def find_encoding(self):
        if self.encoding == 'ResNet':
            return 1
        return 2

    def compute_distance(self, test, train_enc):
        if self.metric == 'euclidean':
            diff = np.subtract(test, train_enc)
            distance = np.sqrt(np.sum(diff * diff))
            return distance
        
        if self.metric == 'manhattan':
            diff = abs(np.subtract(test, train_enc))
            distance = np.sum(diff)
            return distance
        
        if self.metric == 'cosine':
            dot_product = np.dot(train_enc, test)
            train_enc_magnitude = np.linalg.norm(train_enc)
            test_magnitude = np.linalg.norm(test)
            similarity = dot_product / (train_enc_magnitude * test_magnitude)
            return (1 - similarity)
        
    def print_scores(self, val, pred):
        print(accuracy_score(val, pred))
        print(f1_score(val, pred, average='macro'))
        print(precision_score(val, pred, average='macro'))
        print(recall_score(val, pred, average='macro'))

    def score(self, val, pred):
        return accuracy_score(val, pred)

def process_input_file(input_file):
    print(f"Processing the input file: {input_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 train.py <test_file>")
        sys.exit(1)

    test_file = sys.argv[1]
    process_input_file(test_file)
