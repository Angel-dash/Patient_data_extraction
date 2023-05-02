with open("output.txt", "r") as f:
    paragraphs = f.read().split("\n\n")

data = []

for paragraph in paragraphs:
    tokens = paragraph.split()

    age = None
    sex = None
    pulse_rate = None
    blood_pressure = None
    alcohol_consumption = None
    smoking_habits = None

    for i, token in enumerate(tokens):
        if token == "yearold":
            age = tokens[i-2]
        elif token in ["male", "female", "man", "boy", "woman"]:
            sex = token
        elif token == "pulse" and tokens[i+1] == "rate":
            pulse_rate = tokens[i+2].replace("/min", "")
        elif token == "blood" and tokens[i+1] == "pressur":
            blood_pressure = tokens[i+2].replace("mmhg", "")
        elif token == "drink" and tokens[i+2] == "unit" and tokens[i+3] == "alcohol":
            alcohol_consumption = tokens[i+1]
        elif token in ["nonsmok", "smok"]:
            smoking_habits = token

    data.append({
        "Age": age,
        "Sex": sex,
        "Pulse Rate": pulse_rate,
        "Blood Pressure": blood_pressure,
        "Alcohol Consumption": alcohol_consumption,
        "Smoking Habits": smoking_habits
    })

print(data)
