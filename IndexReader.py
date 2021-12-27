"""
Names: Majd Jaber, ID: 208488692
       Saed Jaber, ID: #########
"""

import pandas as pd
import os
import string
import re

class IndexReader:
    def __init__(self, dir):
        self.dir = dir

    def getProductId(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        product_id = df.loc[reviewId-1]["productId"]

        if product_id == ' ':
            return "None"

        return product_id

    def getReviewScore(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        score = df.loc[reviewId - 1]["score"]

        if score == ' ':
            return "None"

        return score

    def getReviewHelpfulnessNumerator(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        helpfulness = df.loc[reviewId - 1]["helpfulness"]
        numerator = helpfulness[0]

        if helpfulness == ' ':
            return "None"

        return numerator

    def getReviewHelpfulnessDenominator(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        helpfulness = df.loc[reviewId - 1]["helpfulness"]
        denominator = helpfulness[-1]

        if helpfulness == ' ':
            return "None"

        return denominator

    def getReviewLength(self, reviewId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\All_Data.csv')

        if reviewId >= len(df):
            return "None"

        text = df.loc[reviewId - 1]["text"]
        if text == ' ':
            return "None"

        temp = 0
        text.translate(string.punctuation)
        regex = r'\w+'
        word_list = re.findall(regex, text)

        for each_word in word_list:
            temp += 1
        return temp

    def getTokenFrequency(self, token):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\token_dictionary.csv')
        counter = 0
        appearance = ''
        for i in range(0, len(df)):

           #  Find the token in the table
            if token == df.loc[i]["word"]:
                appearance = df.loc[i]["Appearances (ReviewId, Frequency)"]
        # Then we count how many reviews the token appeared in from the table
        for item in appearance:
            if item == ')':
                counter += 1
        return counter

    def getTokenCollectionFrequency(self, token):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\token_dictionary.csv')
        frequency = 0
        for i in range(0, len(df)):

           #  Find the token in the table
            if token == df.loc[i]["word"]:
                frequency = df.loc[i]["frequency"]

        return frequency

    def getReviewsWithToken(self, token):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\token_dictionary.csv')
        series = '()'
        for i in range(0, len(df)):

           #  Find the token in the table
            if token == df.loc[i]["word"]:
                series = df.loc[i]["Appearances (ReviewId, Frequency)"]
        return series

    def getNumberOfReviews(self):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\Total_Sum_Reviews_and_Tokens.csv')
        total_reviews = df.loc[0]["total_reviews"]

        return total_reviews

    def getTokenSizeOfReviews(self):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\Total_Sum_Reviews_and_Tokens.csv')
        token_size = df.loc[0]["token_size"]

        return token_size

    def getProductReviews(self, productId):
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)
        df = pd.read_csv(path + r'\ProductIDs_and_Reviews.csv')
        all_reviews = '()'
        for i in range(0, len(df)):

           #  Find the product ID in the table
            if productId == df.loc[i]["Products"]:
                all_reviews = '('
                all_reviews += df.loc[i]["ReviewIDs"]
                all_reviews += ')'
        return all_reviews
