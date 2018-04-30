import csv
from classifier.classical_classifiers import RFClassifier
from utility.feature_extractor import TextFeature

from sklearn.model_selection import cross_val_score

column_names = ["id", "poet_number", "poem_number", "hemistich_number", "verse_number", "hemistich_text", "?"]
COLUMN_POET = 1
COLUMN_HEMISTICH_TEXT = 5

hemistichs = []
labels = []

with open('data/poems_data.csv') as csv_file:
    readCSV = csv.reader(csv_file)
    # i = 0
    for row in readCSV:
        # if i > 9:
        #     break
        # i += 1
        hemistichs.append(row[COLUMN_HEMISTICH_TEXT])
        labels.append(row[COLUMN_POET])

feature_extractor = TextFeature(hemistichs)

print(feature_extractor.tf_vec)
print(len(feature_extractor.feature_names))

X = feature_extractor.tf_vec
y = labels

rf_classifier = RFClassifier(X, y)

rf_classifier.model.fit(rf_classifier.X, rf_classifier.Y)

print("accuracy")
print(cross_val_score(rf_classifier.model, rf_classifier.X, rf_classifier.Y, scoring='accuracy'))


with open("data/output/features_importance.csv", "w") as output:
    COLUMN_FEATURE = 'feature'
    COLUMN_IMPORTANCE = 'importance'
    fieldnames = [COLUMN_FEATURE, COLUMN_IMPORTANCE]
    writer = csv.DictWriter(output, fieldnames=fieldnames)

    writer.writeheader()
    i = 0
    for i in range(0, len(feature_extractor.feature_names)):
        writer.writerow({COLUMN_FEATURE: feature_extractor.feature_names[i],
                         COLUMN_IMPORTANCE: rf_classifier.model.feature_importances_[i]})
