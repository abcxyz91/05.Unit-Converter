# Unit Conversion Web Application

A Flask-based web application that performs various unit conversions including length, weight, and temperature measurements.

This is one of the exercises at roadmap.sh   
[Link to the project](https://roadmap.sh/projects/unit-converter)

## Features

- Length Conversion
  - Supports millimeters (mm), centimeters (cm), meters (m), kilometers (km), inches, feet, yards, and miles
  - All conversions use meter as the base unit

- Weight Conversion
  - Supports milligrams (mg), grams (gr), kilograms (kg), ounces, and pounds
  - All conversions use gram as the base unit

- Temperature Conversion
  - Supports Celsius, Fahrenheit, and Kelvin
  - Direct conversion between any temperature units

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install flask
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Select the type of conversion you want to perform (length, weight, or temperature)

4. Enter the value you want to convert
   - If no value is entered, the default value is 1
   - Invalid inputs will result in an error page

## Project Structure

- `app.py`: Main application file containing all routes and conversion logic
- `templates/`: Directory containing HTML templates
  - `index.html`: Home page
  - `length.html`: Length conversion page
  - `weight.html`: Weight conversion page
  - `temperature.html`: Temperature conversion page
  - `error.html`: Error page for invalid inputs
- `static/`: Directory containing CSS templates
  - `styles.css`: CSS style for the webapp

## Technical Details

- Built with Flask framework
- Uses Flask's routing system to handle different conversion types
- Implements POST and GET methods for form handling
- Includes input validation and error handling
- Uses dictionaries to store conversion factors for length and weight
- Implements custom formulas for temperature conversions

## Error Handling

The application includes error handling for:
- Missing form inputs
- Invalid numeric values
- Invalid conversion unit selections

## Contributing

Feel free to submit issues and enhancement requests. Contributions are welcome!