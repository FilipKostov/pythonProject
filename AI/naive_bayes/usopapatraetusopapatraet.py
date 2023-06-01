





encoder=ordinalencoder
encoder.fit([row[:-1] for row in dataset])
train=dataset[:int(0.7*len(dataset))]
trainx=[row[:-1] for row in train]
trainy=[row[-1]for row in train]
trainx=encoder.transform(trainx)
test=dataset[int(0.7*len(dataset)):]
testx=[row[:-1] for row in test]
testy=[row[-1] for row in test]
testx=encoder.transform(testx)
classifier=CategoricalNB()
classifier=GaussianNB()

classifier.fit(trainx,trainy)


acc=0
for i in range(test)
    predicted class=classifier.predict([test])
encoder=ordinalencoder()
encoder.fit([row[:-1] for row in dataset]
            )
train=database[:7*kurac]
trainx=[row[:-1] for row in dataset]
train y = row[-1]
trainx=encoder.transform(trainx)

test
classifier=Categoricalnb
classifier.fit(train x,trainy)
accuracy=0

for i in len(testset)
    predict=clasifier.predict([testx[i]])[0]
    corect=testy[i]


predict=clasifier.predict(encod_entry)[0]
encoder =ordinalencoder()
encoder.fit([row[:-1] for row in dataset])

trainset=database[:07 *lendatabase]
trainx=[row for row]
trainy
trainx=encoder.transform()

test


classifier=CategoricalNB() gaussianNB
classifier.fit(trainx,trainy)

acc=0

for i in range(len(testset)):
    predict=classifier.predict([test_x[i]])[0]
    real=test_y[i]
    if real==predict
        acc++

acc=acc/len(testset)
entry=[s for s in input split]

entry=encoder.transform(entry])


