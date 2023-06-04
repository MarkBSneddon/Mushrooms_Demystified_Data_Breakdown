import openai
import json
import openai

def loadBook(path):
    # loads the book "Mushrooms Demystified" and returns it as a variable
    # assuming book in a txt format

    with open(path, "r") as file:
        bookText = file.read()
    return bookText

'''

#####################
# Mark's Old Code, keep on hand until we have an adequate replacement #
#####################

def ask_question(question):
    response = openai.Completion.create(
        engine='davinci',
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        #top_p=1,
        #frequency_penalty=0,
        #presence_penalty=0
    )
    return response.choices[0].text

questions = []
while True:
    question = input("Enter your question (or 'q' to exit): ")
    if question.lower() == 'q':
        break
    questions.append(question)


# Create a new workbook
workbook = Workbook()

for i, question in enumerate(questions):
    # Get answer from ChatGPT
    answer = ask_question(question)
    print(answer)

#    # Create a new sheet in the workbook
#    sheet = workbook.create_sheet(title=f"Question {i + 1}")

#    # Write the question and answer to the sheet
#    sheet['A1'] = "Question"
#    sheet['B1'] = "Answer"
#    sheet['A2'] = question
#    sheet['B2'] = answer

## Save the workbook to an Excel file
#workbook.save("answers.xlsx")

'''
