from bs4 import BeautifulSoup
from typing import List
import requests
import pandas as pd
from config import url, database_dict, number_of_pages


def get_links(blank_url: str, number_of_pages_: int) -> List[str]:
    """
    A function that returns url links to each car from different pages
    :param blank_url: Url to car model without last digit of page number
    :param number_of_pages_: Number of pages on which the model appears
    :return: List of cars url links
    """
    all_links = []
    for page_number in range(1, number_of_pages_ + 1):
        url_num = blank_url + str(page_number)
        result = requests.get(url_num)
        doc = BeautifulSoup(result.text, "html.parser")
        h2_list = doc.find_all("h2", class_="e1b25f6f13")
        for i in range(0, len(h2_list)):
            a_list = h2_list[i].find_all("a", href=True)
            if a_list[0]['href']:
                link = a_list[0]['href']
                all_links.append(link)
    return all_links


def get_dict(database_dict_: dict, list_of_url_: List[str]) -> None:
    """
    The function saves the data from each tested car from the url link list. Missing values are saved as "null".
    Function generates finished database and saves it in data folder.
    :param database_dict_: Dictionary with selected variables for the database
    :param list_of_url_: List of links to specific cars
    """
    cars_added = 0
    number_of_links = len(list_of_url_) + 1
    # Iterating across every car from list_of url
    for link in list_of_url_[:10]:
        cars_added = cars_added+1
        print(f"\rNumber of sets: {cars_added}/{number_of_links}", end='')
        result = requests.get(link)
        doc = BeautifulSoup(result.text, "html.parser")
        ver4 = doc.find_all("span", class_="offer-price__number")
        ver = doc.find_all("li", class_="offer-params__item")
        items = doc.find_all("span", class_="offer-params__label")
        for i in range(0, len(ver)):
            ver2 = ver[i].find_all("div")
            # When a category does not have a link in it
            if not ver2[0].find_all("a"):
                value_result = ver2[0].string
                if items[i].string in list(database_dict_.keys()):
                    database_dict_[items[i].string].append(value_result.strip())
            # When a category has a link in it. Then you have to enter the <a> tag
            else:
                ver3 = ver2[0].find_all("a")
                value_result2 = ver3[0].string
                if items[i].string in list(database_dict_.keys()):
                    database_dict_[items[i].string].append(value_result2.strip())
        # Adding price
        database_dict_["Cena"].append(int(str(ver4[0])[34:45].replace(" ", "")))
        for j in range(len(database_dict_)):
            if len(database_dict_[list(database_dict_.keys())[j]]) < cars_added:
                database_dict_[list(database_dict_.keys())[j]].append("null")
    # Saving dict as dataframe and exporting it and saving in data folder
    car_dataframe = pd.DataFrame.from_dict(database_dict_)
    car_dataframe.to_csv('data/car_dataframe_10obs.csv')


list_of_url = get_links(url, number_of_pages)
get_dict(database_dict, list_of_url)