# Daraja M-Pesa Integration

This project demonstrates the integration of the Daraja M-Pesa API using Flask. It allows users to make payments through the M-Pesa platform.

## Features

- Obtain access token from Safaricom API
- Make payment requests using the access token
- Display response messages to the user

## Prerequisites

- Python 3.x
- Flask
- Requests library

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create a virtual environment and activate it:

    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```
    flask run
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`.

3. Enter your phone number and the amount, then click the "Pay" button.

4. Follow the instructions on your phone to complete the transaction.

## Project Structure

GitHub Copilot
Here is an example of a README.md file for your project:

. ├── app.py ├── access_token.py ├── templates │ └── index.html ├── .gitignore └── README.md

- [app.py](http://_vscodecontentref_/0): Main Flask application file.
- [access_token.py](http://_vscodecontentref_/1): Contains functions to get the access token and make payment requests.
- [index.html](http://_vscodecontentref_/2): HTML template for the payment form.
- [.gitignore](http://_vscodecontentref_/3): Git ignore file.
- `README.md`: Project documentation.

## Acknowledgements

- [Safaricom Daraja API](https://developer.safaricom.co.ke/daraja/apis/post/safaricom-sandbox)
- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
