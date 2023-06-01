import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB
def read_file(file_name):
    with open(file_name) as doc:
        csv_reader=csv.reader(doc, delimiter=',')
        dataset=list(csv_reader)[1:]
    return dataset


if __name__ == '__main__':
    dataset = read_file('cars.csv')
    encoder=OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])


    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)



    accuracy = 0

    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(f'Accuracy: {accuracy}')

    entry = [el for el in input().split(' ')]

    encoded_entry = encoder.transform([entry])

    predicted_class = classifier.predict(encoded_entry)[0]

    print(predicted_class)


encoder=OrdinalEncoder()
encoder.fit([row:-1 for row in dataset])

trainset(:7*lendataset)
trainx
train_
encoder

classifier=DecisionTreeClassifier(criterion'entropy, rasndomstate=0' \
                                           '')
        RandomForestClassifier
clasifier.fit(traainx,trainy)

printDepth clasifier.get_depth
clasifier get_n_leaves
accurac

feature_importances=list(classifier.feature_importances-)

most important feature importances.index(max(feature))

train_x
for t in trainset
    trainx.append([t[i]]) for i in range len t if i!=mo