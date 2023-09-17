# PyScrape

A Python scraper that scrapes prices from e-commerce websites like Amazon and Flipkart and sends an email based on the price limit set by the user.

## Installation

### Windows

1.  Create a virtual environment:  
    ```powershell
    py -m venv venv
    ```
2.  Activate the virtual environment:  
    ```powershell
    venv\Scripts\activate
    ```
3.  Install dependencies from requirements.txt:  
    ```powershell
    pip install -r requirements.txt
    ```

### macOS

1.  Create a virtual environment:  
    ```sh
    python3 -m venv venv
    ```
2.  Activate the virtual environment:  
    ```sh
    source venv/bin/activate
    ```
3.  Install dependencies from requirements.txt:  
    ```sh
    pip install -r requirements.txt
    ```

### Linux

1.  Create a virtual environment:  
    ```sh
    python3 -m venv venv
    ```
2.  Activate the virtual environment:  
    ```sh
    source venv/bin/activate
    ```
3.  Install dependencies from requirements.txt:  
    ```sh
    pip install -r requirements.txt
    ```


## Configuration

1. Create a `.env` file in the root of your project.

2. Add the following environment variables to the `.env` file:
   ```python
 	 BREVO_API_KEY=your_brevo_api_key
     JSON_FILE_PATH=path_to_json_file
     USER_AGENT=your_browser_user_agent
     SENDER=senders_email
     RECEIVER_NAMES=names_of_receivers # seperated by comma if more than 1
     RECEIVER_EMAILS=emails_of_receivers # seperated by comma if more than 1
	 ```

3. `JSON_FILE_PATH` should contain the path to json file, which will contains the product details in the following format:
   ```json
       {
          "amazon": [
              {
                  "name": "name_as_per_user",
                  "price_required": 1000,
                  "url": "product_url_from_amazon"
              }
          ],
          "flipkart": [
              {
                  "name": "name_as_per_user",
                  "price_required": 1000,
                  "url": "product_url_from_flipkart"
              }
          ]
       }
   ```
	




