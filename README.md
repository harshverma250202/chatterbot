# ChatterBot API

ChatterBot API is a conversational dialog chat bot developed for E-Cell. It is built using Django and the ChatterBot Python library.

## Features

- Provides an API endpoint to interact with ChatterBot.
- Processes user input and returns a response based on the input.
- Supports POST requests with JSON data containing user input.

## Getting Started

### Prerequisites

Ensure that you have the following installed on your system:

- Python
- Django

### Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/harshverma250202/chattterbot.git
    ```

2. Navigate to the project directory and install the required packages:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

1. Run the Django project using the manage.py script:

    ```shell
    python manage.py runserver
    ```

2. Send a POST request to `https://ecellbot.herokuapp.com/bot/` with the following JSON body:

    ```json
    {
      "user": "your question"
    }
    ```

    Ensure that the Content-Type is set to "application/json".

## API Endpoint

- URL: `https://ecellbot.herokuapp.com/bot/`
- Method: POST
- Data Params: `{"user": "your question"}`

## Example

Sending a POST request with the question "How are you?" will return a response from the bot.

**Request:**

```shell
curl -X POST -H "Content-Type: application/json" -d '{"user":"How are you?"}' https://ecellbot.herokuapp.com/bot/
```
## Code Structure

- chatterbot/chatterbot.py: Contains the main functionality of the ChatterBot.
- botapi/views.py: Defines the API view for interacting with ChatterBot.
- botapi/urls.py: Contains the URL pattern for the API endpoint.
- requirements.txt: Lists the required packages for the project.
- manage.py: Django's command-line utility for administrative tasks.


**Developed by Harsh Verma IIT KGP**
