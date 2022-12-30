from csv import reader
import random

with open('./ingles.csv', 'r') as csv_file:
    csv_reader = reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    dicionario_ingles = list(csv_reader)

i0 = random.randint(0, len(dicionario_ingles) - 1)
i1 = random.randint(0, len(dicionario_ingles) - 1)
i2 = random.randint(0, len(dicionario_ingles) - 1)
i3 = random.randint(0, len(dicionario_ingles) - 1)
i4 = random.randint(0, len(dicionario_ingles) - 1)
i5 = random.randint(0, len(dicionario_ingles) - 1)
i6 = random.randint(0, len(dicionario_ingles) - 1)
i7 = random.randint(0, len(dicionario_ingles) - 1)
i8 = random.randint(0, len(dicionario_ingles) - 1)
i9 = random.randint(0, len(dicionario_ingles) - 1)
i10 = random.randint(0, len(dicionario_ingles) - 1)
i11 = random.randint(0, len(dicionario_ingles) - 1)

ingles_amostrado = [
    dicionario_ingles[i0], dicionario_ingles[i1],
    dicionario_ingles[i2], dicionario_ingles[i3],
    dicionario_ingles[i4], dicionario_ingles[i5],
    dicionario_ingles[i6], dicionario_ingles[i7],
    dicionario_ingles[i8], dicionario_ingles[i9],
    dicionario_ingles[i10], dicionario_ingles[i11]
]

print(ingles_amostrado)

with open('./portugues.csv', 'r') as csv_file_p:
    csv_reader_p = reader(csv_file_p)
    # Passing the cav_reader object to list() to get a list of lists
    dicionario_portugues = list(csv_reader_p)

i0 = random.randint(0, len(dicionario_portugues) - 1)
i1 = random.randint(0, len(dicionario_portugues) - 1)
i2 = random.randint(0, len(dicionario_portugues) - 1)
i3 = random.randint(0, len(dicionario_portugues) - 1)
i4 = random.randint(0, len(dicionario_portugues) - 1)
i5 = random.randint(0, len(dicionario_portugues) - 1)
i6 = random.randint(0, len(dicionario_portugues) - 1)
i7 = random.randint(0, len(dicionario_portugues) - 1)
i8 = random.randint(0, len(dicionario_portugues) - 1)
i9 = random.randint(0, len(dicionario_portugues) - 1)
i10 = random.randint(0, len(dicionario_portugues) - 1)
i11 = random.randint(0, len(dicionario_portugues) - 1)

portugues_amostrado = [
    dicionario_portugues[i0], dicionario_portugues[i1],
    dicionario_portugues[i2], dicionario_portugues[i3],
    dicionario_portugues[i4], dicionario_portugues[i5],
    dicionario_portugues[i6], dicionario_portugues[i7],
    dicionario_portugues[i8], dicionario_portugues[i9],
    dicionario_portugues[i10], dicionario_portugues[i11]
]

print(portugues_amostrado)
