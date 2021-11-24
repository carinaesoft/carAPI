import requests
import urllib3
import json


urllib3.disable_warnings()

make = model = ''


def check_car(data):
    make = data['make']
    model = data['model']
    #print(model)
    outcome = ''

    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{make}?format=json'
   # print(url)
    request_for_car_info = requests.get(url, verify=False)
    #print(request_for_car_info.json())

    if request_for_car_info.json()['Count'] == 0:
        #print('Empty response')
        outcome = 'Empty response'
        return outcome
    else:
        list_of_models = request_for_car_info.json()['Results']
        for result in list_of_models:
            print(result)
            for make, models in result.items():

                if models == model:
                    print('Got the model')
                    outcome = 'Found'
        return outcome





if __name__ == "__main__":
    data = {'make': 'ferrari', 'model': 'F430 Coupe'}
    check_car(data)