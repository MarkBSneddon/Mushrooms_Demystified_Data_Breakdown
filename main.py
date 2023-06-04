import os
import argparse
import tiktoken
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
    
    # OpenAPI Client
    openai.api_key = args.api_key

    print("Your API Key is: " + str(args.api_key) + "\n")

    # prepare book for data parsing
    # using default path as shown in the Git Repo
    bookData = loadBook("data/mushrooms_data_only.txt")
    print("Book data successfully loaded.\n")

    # count tokens needed for OpenAI API
    # countTokens(bookData)

    # prepare OpenAI usage
    max_tokens = 4096  # Maximum number of tokens per API call
    stop_sequence = "\n\n"  # Sequence to stop the response at

    # Process the book text in chunks
    offset = 0
    while offset < len(bookData):
        # Generate the response using the ChatGPT API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=bookData[offset : offset + max_tokens],
            temperature=0,
            max_tokens=max_tokens,
            stop=stop_sequence,
            log_level="token_count"
        )

        # extract token usage and present it to the user
        print("Token count: " + str(response['usage']['total_tokns']))
    
        # Extract the relevant information from the response
        generated_text = response.choices[0].text.strip()
        extracted_info = json.loads(generated_text)
    
        # Append the extracted information to the dataset
        dataset.append(extracted_info)
    
        # Update the offset for the next chunk
        offset += max_tokens

    # Save the dataset as a JSON file
    dataset_path = "output/mushrooms_dataset.json"
    with open(dataset_path, "w") as file:
        json.dump(dataset, file, indent=2)

    return

if __name__ == "__main__":
    main()
