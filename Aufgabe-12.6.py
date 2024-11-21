import csv
import xml.etree.ElementTree as ET

# Erstelle das XML-Dokument
root = ET.Element('root')  # Root-Element der XML-Datei

# Öffne die CSV-Datei und lese die Inhalte
with open('Vokabel.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')

    # Gehe durch jede Zeile der CSV-Datei
    for row in csvreader:
        if len(row) >= 2:  # Wenn mindestens 2 Spalten existieren (z.B. Vokabel und Übersetzung)
            vokabel_element = ET.SubElement(root, 'vokabel')
            vokabel = ET.SubElement(vokabel_element, 'deutsch')
            vokabel.text = row[0]  # Die erste Spalte ist die deutsche Vokabel
            uebersetzung = ET.SubElement(vokabel_element, 'uebersetzung')
            uebersetzung.text = row[1]  # Die zweite Spalte ist die Übersetzung

# Erstelle die XML-Baumstruktur
tree = ET.ElementTree(root)

# Schreibe die XML in eine Ausgabedatei (im Textmodus)
with open('Vokabeln.xml', 'w', encoding='utf-8') as xml_file:
    tree.write(xml_file, encoding='utf-8', xml_declaration=True)

print("XML-Datei wurde erfolgreich erstellt!")
