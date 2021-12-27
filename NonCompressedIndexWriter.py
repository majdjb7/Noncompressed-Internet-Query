"""
Names: Majd Jaber, ID: 208488692
       Saed Jaber, ID: 208480632
"""

import os
import pandas as pd
import shutil
import string
import csv
import stat

import errno
import re


# Function that creates lists of alphabetical tokens database, saving the tokens in each text
def create_alphabetical_database(text, review_counter, a_dict):
    exists = False  # Variable that checks if word is already in the dictionary
    create_new = False
    # Here we make all words lowercase, then separate them
    text2 = text.lower()
    text2.translate(string.punctuation)
    regex = r'\w+'

    word_list = re.findall(regex, text2)

    for each_word in word_list:
        new_word = each_word[0:25]

        w_frequency = 0  # The overall word frequency
        appear_in_review = 0  # Represents frequency of word in each individual review
        appearances = []  # Will contain all review IDs and frequency of the word for each review
        for all_words in range(len(a_dict)):
            # If this product is already in dictionary or not, we determine here and assign boolean to it
            if new_word == a_dict[all_words]["word"]:
                exists = True
                break
            else:
                exists = False

        # If the word isn't saved in our dictionary
        if not exists:
            w_frequency += 1
            appear_in_review += 1

            per_review = (review_counter, appear_in_review)

            appearances.append(per_review)

            item = {'word': new_word,
                    'frequency': w_frequency,
                    'Appearances (ReviewId, Frequency)': appearances}

            a_dict.append(item)
        # IF the word is in the dictionary
        elif exists:
            appear_in_review += 1
            per_review = (review_counter, appear_in_review)

            length = len(list(a_dict[all_words]["Appearances (ReviewId, Frequency)"]))

            a_dict[all_words]["frequency"] += 1

            change = a_dict[all_words]["Appearances (ReviewId, Frequency)"][length - 1]
            if change[0] == review_counter:
                y = list(change)
                y[1] += 1
                appear_in_review += 1
                change = tuple(y)
                a_dict[all_words]["Appearances (ReviewId, Frequency)"][length - 1] = change
                appear_in_review +=1
            else:
                appearances.append(per_review)
                a_dict[all_words]["Appearances (ReviewId, Frequency)"] += appearances
        else:
            pass

#Function that counts the total size of tokens from all the texts
def token_counter(counter, text2):
    temp = 0
    text2.translate(string.punctuation)
    regex = r'\w+'
    word_list = re.findall(regex, text2)

    for each_word in word_list:
        temp += 1
    return temp


#Create the first file, our general database for all features relating to the product ID
def create_general_review_database(dictionary, dir2):
    data = pd.DataFrame(dictionary)

    # ----------------------------------------------------------------------------------------------------------- #
    # ---------------- Here we set the path of the directory for this file and all following files ----------------
    # Parent Directories
    parent_dir = os.getcwd()


    # Path
    path = os.path.join(parent_dir, dir2)

    if os.path.exists(path):  # If path exists already, delete it and create new one
        shutil.rmtree(path)
        os.makedirs(path)
    else:
        os.makedirs(path)

    # ----------------------------------------------------------------------------------------------------------- #
    data.to_csv(path + r'\All_Data.csv', index=False)


# Function that creates our third file (database) containing only total sum of reviews, and total token size
def create_special_database(dictionary, dir2):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir2)
    data = pd.DataFrame(dictionary)
    data.to_csv(path + r'\Total_Sum_Reviews_and_Tokens.csv', index=False)


# Function that creates our fourth file (database) containing product IDs and all the reviews belonging to each one
def create_product_review_database(dictionary, dir4):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir4)
    data = pd.DataFrame(dictionary)
    data.to_csv(path + r'\ProductIDs_and_Reviews.csv', index=False)



def create_file_alphabetical(dictionary2, dir2):
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, dir2)
    data2 = pd.DataFrame(dictionary2)
    data2.to_csv(path + r'\token_dictionary.csv', index=False)




class NonCompressedIndexWriter:
    def __init__(self, inputFile, dir):
        self.dir = dir
        number_of_reviews = 0
        token_size_of_reviews = 0

        pIDFind = 0
        helpFind = 0
        scoreFind = 0
        textFind = 0
        review_counter = 0
        dictionary = []  # Dictionary will contain the list of all products/reviews and their infos
        dictionary2 = []  # Special dictionary that holds total number of reviews and total token size
        dictionary3 = []  # Dictionary containing product IDs and all the reviews belonging to each one
        # Initialize all the alphabetical dictionaries where each one
        token_dict = []

        # -- Open file, loop over each line, identify the key variables and save them into a dictionary, close file
        read_file = open(inputFile, "r")         # opening the text file



        # Loop that goes over each line
        for line in read_file:
            # reading each word
            for word in line.split():
                if pIDFind == 1:  # When we identified the productID
                    review_counter += 1  # We start the 1st review with 1, and then increment accordingly

                    product_id = word
                    pIDFind -= 1
                    """
                    HERE WE TRY TO CREATE FILE 4 (for product IDs and all the reviews numbers relating to them)
                    """
                    exists = False

                    for dic_items in dictionary3:
                        if product_id in dic_items.values():
                            exists = True
                            for s in range(len(dictionary3)):
                                # If this product is already in dictionary
                                if product_id == dictionary3[s]["Products"]:
                                    dictionary3[s]["ReviewIDs"] += ', ' + str(review_counter)
                                    # exists = True
                        else:
                            exists = False
                    if exists == False:
                        item2 = {'Products': product_id,
                                 'ReviewIDs': str(review_counter)}

                        dictionary3.append(item2)


                if word == "product/productId:":  # Helps us identify the productID
                    pIDFind += 1

                if helpFind == 1:  # When we identified the helpfulness
                    helpfulness = word
                    helpFind -= 1
                if word == "review/helpfulness:":  # Helps us identify the helpfulness
                    helpFind += 1

                if scoreFind == 1:  # When we identified the score
                    score = word
                    scoreFind -= 1
                if word == "review/score:":  # Helps us identify the score
                    scoreFind += 1

                if textFind == 1:  # When we identified the text
                    text = line[len(delete):len(line)].lstrip()


                    token_size_of_reviews += token_counter(token_size_of_reviews, text)

                # --------------------------------------------------------------------------------------------------- #
                # Call to function that creates lists of alphabetical tokens database

                    create_alphabetical_database(text, review_counter, token_dict)

                # --------------------------------------------------------------------------------------------------- #
                    textFind -= 1
                    """We add all the info to the dictionary after we have found the text, since it means
                    we have found all the other variables we were looking for (end of review)"""
                    # We temporarily copy the info to "item" since its the only way to append to the dictionary
                    item = {'review_num': review_counter,
                           'productId': product_id,
                           'helpfulness': helpfulness,
                           'score': score,
                           'text': text}
                    dictionary.append(item)
                if word == "review/text:":  # Helps us identify the text
                    delete = word
                    textFind += 1
        read_file.close()
        # ----------------------------------------------------------------------------------------------------------- #
        # Create the first file, our general database for all features relating to the product ID
        create_general_review_database(dictionary, dir)

        # -------------------------------  Here we create our third file ------------------------------------------- #
        number_of_reviews = review_counter  # Total number of reviews
        item = {'total_reviews': number_of_reviews,
                'token_size': token_size_of_reviews}
        dictionary2.append(item)
        # Call function that creates the third file
        create_special_database(dictionary2, dir)
        # -------------------------------  Here we create our fourth file ------------------------------------------- #
        # Call function that creates the third file
        create_product_review_database(dictionary3, dir)

        # ----------------------------------------------------------------------------------------------------------- #

        create_file_alphabetical(token_dict, dir)



    def removeIndex(self, dir):
       # path_del = os.path.dirname(os.path.abspath(dir))  # Get the path of directory we want to delete
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, self.dir)

        if os.path.exists(path):  # If path exists already, delete it and create new one


            for file in os.scandir(path):
                os.remove(file)

            directory = os.listdir(path)  # Check if directory is empty

            try:  # We will try to delete the empty directory (after we remove all files in it)
                if len(path) == 0:
                    os.rmdir(path)
                else:
                    shutil.rmtree(path)
            except OSError as e:
                print("Error: %s : %s" % (path, e.strerror))
