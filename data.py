import pandas as pd

# Creating the table data
data = {
    "Ingredient": [
        "Lamb/Beef", "Chicken", "Eggplant", "Tomato", "Kashk (Whey)", "Garlic", "Onion", "Kidney Beans", "Dried Limes", "Turmeric",
        "Black Pepper", "Salt", "Water", "Tomato Paste", "Pomegranate Molasses", "Rice", "Saffron", "Butter/Oil"
    ],
    "Ghormeh Sabzi": [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    "Gheimeh": [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    "Karafs": [1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    "Fesenjan": [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    "Lobia Polo": [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0],
    "Sabzi Polo": [0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    "Addas Polo": [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
    "Kabab Barg": [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    "Kabab Koobideh": [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    "Joojeh Kabab": [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    "Zereshk Polo ba Morgh": [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    "Kabab Vaziri": [1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    "Kashk Bademjan": [0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    "Mirza Ghasemi": [0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
}

# Creating DataFrame
df = pd.DataFrame(data)

# Exporting to Excel
file_path = "Persian_Dishes_Ingredients.xlsx"
df.to_excel(file_path, index=False)
