import pandas as pd
from datetime import datetime
from datetime import timedelta
import requests
import time
import random

payload = [{'equipment_id' : 'packing', 'parameter_id' : 'temp', 'value':50}]

##class for data_generation

def data_generation():
    eq_id = random.randint(1, 3)
    speed = random.randint(20,200)
    date = datetime.today().strftime("%Y-%m-%d")
    time = datetime.now().isoformat()

    return [eq_id, speed, date, time]


if __name__ == '__main__':

    REST_API_URL = 'https://api.powerbi.com/beta/540e766f-1637-42f4-9a15-fac8f41e603d/datasets/b68e3e9c-0d6f-4d24-a6bb-8ea490a01bbf/rows?key=MhZw%2BL0Nr1%2FnHj5ZDa%2Fd1AaSRakXztu0j%2B9ei1KFynlytwtjt0M2vKJRzBOelcuyZFGGSeZdm2%2FPb0zxQg0hyA%3D%3D'

    while True:
        data_raw = []
        for i in range(1):
            row = data_generation()
            data_raw.append(row)
            print("Raw data - ", data_raw)

        # set the header record
        HEADER = ["eq_id", "speed", "date", "time"]

        data_df = pd.DataFrame(data_raw, columns=HEADER)
        data_json = bytes(data_df.to_json(orient='records'), encoding='utf-8')
        print("JSON dataset", data_json)

        # Post the data on the Power BI API
        req = requests.post(REST_API_URL, data_json)

        print("Data posted in Power BI API")
        time.sleep(2)

