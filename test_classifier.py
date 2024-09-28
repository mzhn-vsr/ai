import requests
import json
import pandas

data = pandas.read_csv('input.csv')
f = open("output.txt", "w")
for idx, row in data.iterrows():
    q = row['Вопрос пользователя']

    class1 = row['Классификатор 1 уровня']
    class2 = row['Классификатор 2 уровня']
    
    data = {'input': q}

    json_data = json.dumps(data)
    
    response = requests.post(
        "http://localhost:8080/classifier/invoke",
        data=json_data, 
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code == 200:
        output_data = response.json()
        try:
            c1 = output_data['output']['c1']
            c2 = output_data['output']['c2']
        except:
            c1 = "ОТСУТСТВУЕТ"
            c2 = "Отсутствует"
        f.write(f'{class1},{class2},{c1},{c2}\n')
        f.flush()

f.close()