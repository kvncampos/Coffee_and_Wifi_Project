# Flask Coffee Shop Finder

## Overview

This Flask app allows users to add and view coffee shops along with their details such as location, opening/closing times, coffee rank, wifi speed, and power outlets availability.

Installation
- Clone the repository:
```bash
git clone https://github.com/your-username/your-repository.git

python -m pip install -r requirements.txt
```

Run the Flask app:

```bash
python app.py
```

- Open your browser and go to http://localhost:5001 to access the app.

## Usage

    Navigate to http://localhost:5001 in your web browser.

    The home page displays a list of available coffee shops.

    To add a new coffee shop, click on the "Add Cafe" link and fill in the details in the provided form.

    After submitting the form, the new coffee shop will be added, and you will be redirected to the list of cafes.

File Structure

    app.py: The main Flask application file.
    utilities.py: Utility functions for reading, finding, and adding data to the CSV file.
    data_structure.py: Defines the structure of the CoffeeData class and the CafeForm class for handling form submissions.

Dependencies

    Flask
    Flask-Bootstrap5

Contributing

Feel free to contribute to this project by opening issues or creating pull requests.
License

This project is licensed under the MIT License.