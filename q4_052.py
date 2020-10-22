#!/usr/bin/env python

import sys

d = {
    "almonds": "795",
    "apple pie": "405",
    "asparagus": "15",
    "avocdo": "340",
    "banana": "105",
    "blackberries": "75",
    "blue cheese": "100",
    "blueberries": "80",
    "muffin": "135",
    "blueberry pie": "380",
    "broccoli": "40",
    "butter": "100",
    "cabbage": "15",
    "carrot cake": "385",
    "cheddar cheese": "115",
    "cheeseburger": "525",
    "cherry pie": "410",
    "chicken noodle soup": "75",
    "chocolate chip cookie": "185",
    "cola": "160",
    "cranberry juice": "145",
    "croissant": "235",
    "danish pastry": "235",
    "egg": "75",
    "grapefruit juice": "95",
    "ice cream": "375",
    "lamb": "315",
    "lemon meringue pie": "355",
    "lettuce": "5",
    "macadamia nuts": "960",
    "mayonnaise": "100",
    "mixed grain bread": "65",
    "orange juice": "110",
    "potatoes": "120",
    "pumpkin pie": "320",
    "rice": "230",
    "salmon": "150",
    "spaghetti": "190",
    "spinach": "55",
    "strawberries": "45",
    "taco": "195",
    "tomatoes": "25",
    "tuna": "135",
    "veal": "230",
    "waffles": "205",
    "watermelon": "50",
    "white bread": "65",
    "wine": "75",
    "yogurt": "230",
    "zuchini": "16"
}


def main():
    with open(sys.argv[1], "r") as f:
        f = f.readlines()
        for lines in f:
            line = lines.strip().split("\n")
            #print (line)
            for char in line:
                words = char.split(",")
                name = words[0]
                foods = words[1:]
                total = 0
                for tokens in foods:
                    if tokens in d:
                        token = int(tokens)
                        total = total + int(token)
                    else:
                        total += 100
                    return total
                

if __name__ == '__main__':
    main()
        