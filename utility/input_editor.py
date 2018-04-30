import csv

__author__ = 'maryam'

column_names = ["id", "poet_number", "poem_number", "hemistich_number", "verse_number", "hemistich_text",
                "Hafez", "Saadi", "Molavi", "Attar", "Sanaee", "Vahshi", "Khaghani", "Anvari", "Ouhadi", "Khajoo",
                "Eraghi", "Bahar", "Hatef", "Saeb Tabrizi", "Kashani", "Amir Khosro", "Bahaee", "Shahriar",
                "Shah Nematollah", "Seyf Farghani", "Salman", "Ghaani", "Orfi", "Obeyd", "Helali",
                "Forooghi", "Feyz", "Bidel", "Razi", "Rahi"]

COLUMN_ID = 0
COLUMN_POET = 1
COLUMN_POEM = 2
COLUMN_HEMISTICH_NUMBER = 3
COLUMN_VERSE_NUMBER = 4
COLUMN_HEMISTICH_TEXT = 5

with open("../data/output/poems_labels.csv", "w") as output:
    writer = csv.DictWriter(output, fieldnames=column_names)

    writer.writeheader()

    with open('../data/poems_data.csv') as csv_file:
        readCSV = csv.reader(csv_file)
        for row in readCSV:
            writer.writerow({
                column_names[0]: row[COLUMN_ID],
                column_names[1]: row[COLUMN_POET],
                column_names[2]: row[COLUMN_POEM],
                column_names[3]: row[COLUMN_HEMISTICH_NUMBER],
                column_names[4]: row[COLUMN_VERSE_NUMBER],
                column_names[5]: row[COLUMN_HEMISTICH_TEXT],
                column_names[6]: 1 if row[COLUMN_POET] == "1" else 0,
                column_names[7]: 1 if row[COLUMN_POET] == "2" else 0,
                column_names[8]: 1 if row[COLUMN_POET] == "3" else 0,
                column_names[9]: 1 if row[COLUMN_POET] == "4" else 0,
                column_names[10]: 1 if row[COLUMN_POET] == "5" else 0,
                column_names[11]: 1 if row[COLUMN_POET] == "6" else 0,
                column_names[12]: 1 if row[COLUMN_POET] == "7" else 0,
                column_names[13]: 1 if row[COLUMN_POET] == "8" else 0,
                column_names[14]: 1 if row[COLUMN_POET] == "9" else 0,
                column_names[15]: 1 if row[COLUMN_POET] == "10" else 0,
                column_names[16]: 1 if row[COLUMN_POET] == "11" else 0,
                column_names[17]: 1 if row[COLUMN_POET] == "12" else 0,
                column_names[18]: 1 if row[COLUMN_POET] == "13" else 0,
                column_names[19]: 1 if row[COLUMN_POET] == "14" else 0,
                column_names[20]: 1 if row[COLUMN_POET] == "15" else 0,
                column_names[21]: 1 if row[COLUMN_POET] == "16" else 0,
                column_names[22]: 1 if row[COLUMN_POET] == "17" else 0,
                column_names[23]: 1 if row[COLUMN_POET] == "18" else 0,
                column_names[24]: 1 if row[COLUMN_POET] == "19" else 0,
                column_names[25]: 1 if row[COLUMN_POET] == "20" else 0,
                column_names[26]: 1 if row[COLUMN_POET] == "21" else 0,
                column_names[27]: 1 if row[COLUMN_POET] == "22" else 0,
                column_names[28]: 1 if row[COLUMN_POET] == "23" else 0,
                column_names[29]: 1 if row[COLUMN_POET] == "24" else 0,
                column_names[30]: 1 if row[COLUMN_POET] == "25" else 0,
                column_names[31]: 1 if row[COLUMN_POET] == "26" else 0,
                column_names[32]: 1 if row[COLUMN_POET] == "27" else 0,
                column_names[33]: 1 if row[COLUMN_POET] == "28" else 0,
                column_names[34]: 1 if row[COLUMN_POET] == "29" else 0,
                column_names[35]: 1 if row[COLUMN_POET] == "30" else 0,
            }
            )
