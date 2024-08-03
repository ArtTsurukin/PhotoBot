from pathlib import Path
import pandas as pd
import json
from config import path_on_laptop

def create_path_discs(folder: str):
    c = "C:/Users/user/Desktop/Photo_Data/Discs/" + folder
    data_path = []
    p = Path(c)
    for x in p.rglob("*"):
        a = (str(x)).split("\\")
        b = "/".join(a)
        if b[-4:] == ".jpg":
            data_path.append(b)
    return data_path

def create_path_discs_video(folder: str):
    c = "C:/Users/user/Desktop/Photo_Data/Discs/" + folder
    data_path = []
    p = Path(c)
    for x in p.rglob("*"):
        a = (str(x)).split("\\")
        b = "/".join(a)
        if b[-4:] == ".mp4" or b[-4:] == ".MOV":
            data_path.append(b)
    return data_path

def create_path_tyres(folder: str):
    c = "C:/Users/user/Desktop/Photo_Data/Tyres/" + folder
    data_path = []
    p = Path(c)
    for x in p.rglob("*"):
        a = (str(x)).split("\\")
        b = "/".join(a)
        if b[-4:] == ".jpg":
            data_path.append(b)
    return data_path

def create_path_other(folder: str):
    c = "C:/Users/user/Desktop/export/" + folder
    data_path = []
    p = Path(c)
    for x in p.rglob("*"):
        a = (str(x)).split("\\")
        b = "/".join(a)
        if b[-4:] == ".jpg":
            data_path.append(b)
    return data_path

def get_dict_data(path_on_laptop):
    excel_data_df = pd.read_excel(path_on_laptop, sheet_name='Объявления')
    json_str = excel_data_df.to_json(orient='records', force_ascii=False)
    data_dict = json.loads(json_str)
    return data_dict

def send_info(request):
    info = ""
    for i in get_dict_data(path_on_laptop):
        for k, v in i.items():
            if k == "ID_EXT" and str(request).lower() in str(v).lower():
                info = f"""Цена: {int(i['ЦЕНА'])}$
Наименование: {i['НАИМЕНОВАНИЕ ЗАПЧАСТИ']}
Артикул: {i['ID_EXT']} 
Кат. номер: {i['ОРИГИНАЛЬНЫЙ НОМЕР']}
Объявление активно: {["Нет", "Да"][i['АКТИВНОСТЬ']]}
Ссылка: {i['URL на Bamper.by']}
"""
    return info

