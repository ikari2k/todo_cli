import json

dataDict = {
    "sampleString": "Great Automation Framework",
    "sampleList": ["Good", "Better", "Best"],
    "sampleTuple": ("Python", "Pytest", "Automation"),
    "sampleObj": {"platform": "Udemy", "Valuable": True},
    "sampleInteger": 555,
    "booleanValue": True,
    "noneValue": None
}

resultJSON = json.dumps(dataDict, sort_keys=True, indent=4)
print(resultJSON)

with open('bonus/example.json', 'r') as file:
    data = json.load(file)
    print(data)
    print(data.keys())
    print('\n\n')

    for key, value in data.items():
        print(key, ': ',value)