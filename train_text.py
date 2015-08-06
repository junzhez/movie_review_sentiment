from sklearn import linear_model, svm, naive_bayes
import numpy as np

if not 'pos' in globals() or not 'neg' in globals():
    from parse_text import pos, neg

clf = svm.SVC(kernel='linear')

precision = []

total_size = 1000
k = 4
test_size = int(total_size / k)
train_size = total_size - test_size

np.random.shuffle(pos)
np.random.shuffle(neg)

for step in np.arange(k):
    x_train = []

    x_train.extend(pos[:step * test_size])
    x_train.extend(neg[:step * test_size])
 
    x_train.extend(pos[(step + 1) * test_size:])
    x_train.extend(neg[(step + 1) * test_size:])
    
    y_train = [1] * train_size
    y_train.extend([0] * train_size)

    x_test = []
    x_test.extend(pos[step * test_size : (step + 1) * test_size])
    x_test.extend(neg[step * test_size : (step + 1) * test_size])

    y_test = [1] * test_size
    y_test.extend([0] * test_size)

    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    val = np.mean(y_pred == y_test)
    print(val)

    precision.append(val)
    
