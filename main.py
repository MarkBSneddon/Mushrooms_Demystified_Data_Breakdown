import os
import argparse

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
    args = getArgumentsFromUser()
    print("Your API Key is: " + str(args.api_key))

    return

if __name__ == "__main__":
    main()
