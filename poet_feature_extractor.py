import csv
from classifier.classical_classifiers import RFClassifier
from utility.feature_extractor import TextFeature

COLUMN_HEMISTICH_TEXT = 5


def poet_feature_extractor(column_label=1):
    '''
     Extract features based on label column
     :param column_label:
     :return:
     '''
    hemistichs = []
    labels = []
    with open('data/output/poems_labels.csv') as csv_file:
        csv_file.seek(0)
        readCSV = csv.reader(csv_file)
        i = 0
        for row in readCSV:
            i += 1
            if i == 1:
                continue  # ignore header
            hemistichs.append(row[COLUMN_HEMISTICH_TEXT])
            labels.append(row[column_label])
    feature_extractor = TextFeature(hemistichs)

    X = feature_extractor.tf_vec
    y = labels

    rf_classifier = RFClassifier(X, y)

    rf_classifier.model.fit(rf_classifier.X, rf_classifier.Y)

    with open("data/output/features_importance_label_column_" + str(column_label) + ".csv", "w") as output:
        COLUMN_FEATURE = 'feature'
        COLUMN_IMPORTANCE = 'importance'
        fieldnames = [COLUMN_FEATURE, COLUMN_IMPORTANCE]
        writer = csv.DictWriter(output, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(0, len(feature_extractor.feature_names)):
            print(str(i) + " of " + str(len(feature_extractor.feature_names)))
            writer.writerow({COLUMN_FEATURE: feature_extractor.feature_names[i],
                             COLUMN_IMPORTANCE: rf_classifier.model.feature_importances_[i]})


# find Hafez's poems features!
poet_feature_extractor(6)
