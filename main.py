import os
import argparse
from Mushrooms_Demystified_Data_Breakdown import *

def getArgumentsFromUser():
    parser = argparse.ArgumentParser(description="Convert Mushrooms Demystified book into a dataset")
    parser.add_argument("-k", "--api-key", type=str, help="OpenAI API key")
    args = parser.parse_args()
    
    # API key error checking
    if args.api_key:
        return args
    else:
        print("ERROR: Provide an OpenAPI API KEY. Use --help to learn more")
        exit()

def main():

    # prepare API key
    args = getArgumentsFromUser()
    print("Your API Key is: " + str(args.api_key) + "\n")

    # prepare book for data parsing
    # using default path as shown in the Git Repo
    bookData = loadBook("data/epdf.pub_mushrooms-demystified.txt")
    print("Book data successfully loaded.\n")

    return

if __name__ == "__main__":
    main()
