import requests
from config import api_key


# Spoonacular API Implementation
class CustomOrder:
    @staticmethod
    def customer_choice():

        url = "https://api.spoonacular.com/recipes/complexSearch"
        food = input("🍽️ What food you want order: ")
        params = {
            "apiKey": api_key,
            "query": food,
            "number": 5
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            for recipe in data.get("results", []):
                print(f"{recipe['title']} (ID: {recipe['id']})")

        else:
            print(f"Error {response.status_code}: {response.text}")
