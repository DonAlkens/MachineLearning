import random

rows = 200
cols = 10

data = ""
for row in range(rows):
    data += str(random.randrange(1234567,9876543)) + ","
    for col in range(cols):
        if col == 9:
            result = ["2", "4"]
            data += str(result[random.randrange(0,2)]) + "\n"
        else:
            data += str(random.randrange(0, 9)) + ","

with open("breast_cancer.data.txt","w") as f:
    f.write(data)
