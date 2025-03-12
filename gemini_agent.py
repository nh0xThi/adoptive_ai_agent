# Importing the 'requests' library, which allows us 
# to send HTTP requests in Python.
import requests  
# Read as: "import the requests module to handle HTTP requests."

# Defining the URL for the Gemini 1.5 API.
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"  
# Read as: "API_URL is a string variable that stores 
# the endpoint URL of the Gemini API."

# API key required to authenticate API requests.
API_KEY = "AIzaSyC710U4fKzWZytpLIDyPIRrda3ZFNzVjLI"  
# Read as: "API_KEY is a string that holds the secret key 
# used to access the API."

# Defining a function to call the Gemini API with a user-provided prompt.
def call_gemini(prompt):
    """
    Sends a request to the Gemini 1.5 API with the given prompt.

    Args:
        prompt (str): The input text.

    Returns:
        str: The AI's response or an error message.
    """
    
    # Creating a dictionary for HTTP headers.
    
    # Read as: 
    # - "payload is a dictionary."
    # - "It has a key 'contents' that stores a list."
    # - "Inside the list is a dictionary with a key 'parts'."
    # - "'parts' contains another list, 
    # which has a dictionary storing the prompt text."

    try:
        # Sending an HTTP POST request to the API.
        response = requests.post(API_URL, params=params, json=payload, headers=headers)  
        # Read as: 
        # - "Use requests.post() to send data."
        # - "The URL is API_URL."
        # - "The API key is passed in params."
        # - "The JSON data (prompt) is passed in payload."
        # - "Headers specify JSON format."

        # Checking for any HTTP errors (e.g., 404, 500).
        response.raise_for_status()  
        # Read as: "If the response has an HTTP error status, 
        # raise an exception."

        # Parsing the JSON response from the API.
        result = response.json()  
        # Read as: "Convert the API response to a Python dictionary 
        # using .json()."

        # Checking if the response contains AI-generated text.
        if 'candidates' in result and result['candidates']:  
            # Read as: "Check if the key 'candidates' exists 
            # and contains at least one result."

            # Extracting the AI's response text from the first result.
            return result['candidates'][0]['content']['parts'][0]['text']  
            # Read as: 
            # - "Access the first item in the 'candidates' list."
            # - "Go to its 'content' key."
            # - "Inside 'content', go to 'parts'."
            # - "Get the first element in 'parts', and retrieve its 'text'."

        else:
            return "No content returned by the API."  
            # Read as: "If no AI-generated text is found, 
            # return a default message."

    except requests.exceptions.RequestException as e:  
        # Read as: "If an error occurs during the request, 
        # catch the exception."

        return f"Error: {e}"  
        # Read as: "Return a formatted string that includes 
        # the error message."

# The script starts execution from here when run.
if __name__ == "__main__":  
    # Read as: "This ensures the following code runs only if 
    # this script is executed directly."

    # Infinite loop to repeatedly ask for user input.
    while True:  
        # Read as: "Start a loop that will keep running until 
        # explicitly stopped."

        # Asking the user for a prompt.
        prompt = input("Enter a prompt (type 'exit' to quit): ").strip()  
        # Read as: 
        # - "Display a message and wait for user input."
        # - "Remove any extra spaces from the input using .strip()."

        # Checking if the user wants to exit.
        if prompt.lower() == "exit":  
            # Read as: "Convert input to lowercase and check if 
            # it is 'exit'."

            print("Exiting...")  
            # Read as: "Display 'Exiting.' message."

            break  # Stop the loop.
            # Read as: "Exit the while loop and terminate the program."

        # Calling the API function with the user's input.hi
        response = call_gemini(prompt)  
        # Read as: "Pass the user input to the call_gemini function 
        # and store the result in 'response'."

        # Displaying the AI's response.
        print(f"Response: {response}")  
        # Read as: 
        # - "Use an f-string to format the output."
        # - "Insert the value of 'response' into the string."
        # - "Print the formatted string."
