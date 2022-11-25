import json
from datetime import date
from datetime import datetime
from pathlib import Path

import bs4
import requests
def mirarMes(todayMonth):
    if todayMonth == '1':
        mes = 'ene'
    elif todayMonth == '2':
        mes = 'feb'
    elif todayMonth == '3':
        mes = 'mar'
    elif todayMonth == '4':
        mes = 'abr'
    elif todayMonth == '5':
        mes = 'may'
    elif todayMonth == '6':
        mes = 'jun'
    elif todayMonth == '7':
        mes = 'jul'
    elif todayMonth == '8':
        mes = 'ago'
    elif todayMonth == '9':
        mes = 'sept'
    elif todayMonth == '10':
        mes = 'oct'
    elif todayMonth == '11':
        mes = 'nov'
    elif todayMonth == '12':
        mes = 'dic'
    return mes


def obtenerFecha():
    today = datetime.today().strftime('%d')
    todayMonth = datetime.today().strftime('%m')
    mes = mirarMes(todayMonth)
    diames = str(today) + mes + '.'
    return diames
