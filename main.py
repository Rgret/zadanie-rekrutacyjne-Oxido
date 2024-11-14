from openai import OpenAI, OpenAIError
from dotenv import load_dotenv
import sys
import os

# system prompt for gpt
prompt = """
Generate an article using appropriate HTML tags to structure the content. Follow these guidelines:
1. HTML Structure:
Use only the content that belongs between <body> and </body> tags. Do not include the <html>, <head>, or <body> tags themselves.

2. Image Placement:
Suggest where images should be placed using the <img> tag with src="image_placeholder.jpg".
Each <img> tag must include an alt attribute containing a detailed prompt for generating the image.
Provide captions for each image using appropriate HTML tags (e.g., <figcaption> inside <figure> tags).

3. Styling Restrictions:
Do not include any CSS or JavaScript in the output.

4. Content Focus:
Ensure the article is logically structured with headings, paragraphs, and lists where appropriate. Use semantic HTML tags such as <h1>, <h2>, <p>, <ul>, and <ol>.
"""

def main(txt_file, API_KEY=None):
    env_file = '.env'

    # check if there is an API key specified, exit if not
    if API_KEY is None:
        if os.path.exists(env_file):
            load_dotenv(env_file)
            API_KEY = os.getenv('OPENAI_API_KEY')
    if API_KEY is None:
        print("No api key has been specified. Exiting...")
        return

    # read contents of the .txt file
    try:
        with open(txt_file, 'r') as file:
            txt_file_content = file.read()
    except FileNotFoundError:
        print(f"The file {txt_file} does not exist. Exiting...")
        return

    # if the file is empty or oonly whitespaces, exit
    if not txt_file_content.strip():
        print("Input file is empty. Exiting...")
        return

    # send the request to OpenAI API
    try:
        client = OpenAI(api_key=API_KEY)
        completion = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {'role':'system', 'content': prompt},
                {
                    'role':'user',
                    'content': txt_file_content
                }
            ]
        )
    except OpenAIError as e:
        print(f"Error: {e}")
        return

    # try to get the content of the resonnse, or print and error and exit
    try:
        html_content = completion.choices[0].message.content
    except OpenAIError as e:
        print(f"Error: {e}")
        return

    # save the response as .html
    with open('artykul.html', "w") as file:
        file.write(html_content)

    print("HTML article saved as 'artykul.html'")


if __name__ == "__main__":
    # in case just the file is specified
    if len(sys.argv) > 1:
        main(sys.argv[1])
    
    # in case the file and API key are specified
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        print("No txt file specified. Exiting...")