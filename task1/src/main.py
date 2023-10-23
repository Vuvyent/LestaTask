from dataclasses import dataclass, field
import pandas as pd
import requests
import numpy as np


@dataclass(frozen=True, order=True)
class Website:
    name: str = ""
    popularity: int = 0
    frontend: list[str] = field(default_factory=list)
    backend: list[str] = field(default_factory=list)
    database: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass(frozen=True, order=True)
class Table:
    list_of_websites: list[Website]


def main():
    url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[0]
    for item in df["Popularity (unique visitors per month)[1]"]:
        idx = item.find("(")
        if idx != -1:
            new_item = item[0:idx]
            df.replace(item, new_item, inplace=True)
    data = df.to_numpy()
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if type(data[i][j]) != float:
                idx = data[i][j].find("[")
                while idx != -1:
                    end_idx = data[i][j].find("]")
                    data[i][j] = data[i][j][0:idx] + data[i][j][end_idx+1:]
                    idx = data[i][j].find("[")
    for i in range(data.shape[0]):
        data[i][1] = data[i][1].replace(",", "")
        data[i][1] = data[i][1].replace(".", "")
        data[i][1] = data[i][1].replace(" ", "")

    sites = []
    for i in range(data.shape[0]):
        name = data[i][0]
        popularity = int(data[i][1])
        frontend = data[i][2].split(", ")
        backend = data[i][3].split(", ")
        database = data[i][4].split(", ")
        notes = data[i][5]
        sites.append(Website(name, popularity, frontend, backend, database, notes))
        table = Table(sites)

    return table
