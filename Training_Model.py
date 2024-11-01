import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Convert labels to integers
unique_labels = np.unique(labels)
label_to_int = {label: i for i, label in enumerate(unique_labels)}
int_to_label = {i: label for label, i in label_to_int.items()}
int_labels = np.array([label_to_int[label] for label in labels])

x_train, x_test, y_train, y_test = train_test_split(data, int_labels, test_size=0.2, shuffle=True, stratify=int_labels)

model = RandomForestClassifier()
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly!'.format(score * 100))

# Save the model and label mappings
with open('model.p', 'wb') as f:
    pickle.dump({'model': model, 'int_to_label': int_to_label}, f)