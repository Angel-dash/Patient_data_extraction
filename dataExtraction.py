# this code create a csv files from txt files
# here the re uses unclenead files
import re
import csv

with open("Medical-records.txt", "r") as f:
    paragraphs = f.read().split("\n\n")

data = []

for paragraph in paragraphs:
    age = re.search(r"A ([0-9]+)-year-old", paragraph)
    sex = re.search(
        r"A [0-9]+-year-old (male|female|man|boy|woman|female|girl|lady)", paragraph)
    pulse_rate = re.search(r"pulse rate is ([0-9]+)/min", paragraph)
    blood_pressure = re.search(
        r"(blood pressure) ([0-9]+/[0-9]+) mmHg", paragraph)
    alcohol_consumption = re.search(
        r"drinks ([0-9]+) units of alcohol per week", paragraph)
    smoking_habits = re.search(r"(non-smoker|smoker)", paragraph)

    data.append({
        "Age": age.group(1) if age else None,
        "Sex": sex.group(1) if sex else None,
        "Pulse Rate": pulse_rate.group(1) if pulse_rate else None,
        "Blood Pressure": blood_pressure.group(1) if blood_pressure else None,
        "Alcohol Consumption": alcohol_consumption.group(1) if alcohol_consumption else None,
        "Smoking Habits": smoking_habits.group(1) if smoking_habits else None
    })

with open("outputFromMedical_records.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames=[
                            "Age", "Sex", "Pulse Rate", "Blood Pressure", "Alcohol Consumption", "Smoking Habits"])
    writer.writeheader()
    writer.writerows(data)
