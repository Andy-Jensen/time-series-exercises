import pandas as pd
import numpy as np
import os


def get_people():
    if os.path.isfile('people.csv'):
        return pd.read_csv('people.csv')
    else:
        url='https://swapi.dev/api/people/'
        response = requests.get(url)
        data=response.json()
        people=pd.DataFrame(data['results'])
        while data['next']!= None:
            print(data['next'])
            response = requests.get(data['next'])
            data=response.json()
            people=pd.concat([people, pd.DataFrame(data['results'])], ignore_index=True)
            df.to_csv('people.csv', index=False)
        return df


def get_planets():
    if os.path.isfile('planets.csv'):
        return pd.read_csv('planets.csv')
    else:
        url='https://swapi.dev/api/planets/'
        response = requests.get(url)
        data=response.json()
        df=pd.DataFrame(data['results'])
        while data['next']!= None:
            print(data['next'])
            response = requests.get(data['next'])
            data=response.json()
            df=pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
            df.to_csv('planets.csv', index=False)
        return df


def get_starships():
    if os.path.isfile('starships.csv'):
        return pd.read_csv('starships.csv')
    else:
        url='https://swapi.dev/api/starships/'
        response = requests.get(url)
        data=response.json()
        df=pd.DataFrame(data['results'])
        while data['next']!= None:
            print(data['next'])
            response = requests.get(data['next'])
            data=response.json()
            df=pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
            df.to_csv('starships.csv', index=False)
        return df


def get_starwars(x,y,z):
    df=pd.concat([x, y, z], ignore_index=True)
    return df


def opsd():
    if os.path.isfile('OPSD.csv'):
        return pd.read_csv('OPSD.csv')
    else:
        df=pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
        df.to_csv('OPSD.csv', index=False)
        return df