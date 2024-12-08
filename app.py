from flask import Flask, flash, redirect, render_template, request, session

"""Initialize the webapp"""
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/length", methods=["GET", "POST"])
def convert_length():
    """Create a dictionary contains all length units in meter"""
    LENGTH = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.344,
    }

    """Make a list of all length units"""
    units = LENGTH.keys()

    if request.method == "POST":
        """User reached route via POST (as by submitting a form via POST)"""
        """Validate user input"""
        if not request.form.get("length"):
            value = 1
        else:
            value = request.form.get("length")
        if not request.form.get("convert_from"):
            return render_template("error.html")
        else:
            convert_from = request.form.get("convert_from")
        if not request.form.get("convert_to"):
            return render_template("error.html")
        else:
            convert_to = request.form.get("convert_to")

        """Try to convert and raise error if invalid value input"""
        try:
            result = float(value) * LENGTH[convert_from] / LENGTH[convert_to]
            return render_template(
                "length.html", 
                units=units,
                active_page="length",
                value=value, result=result, convert_from=convert_from, convert_to=convert_to)
        except ValueError:
            return render_template("error.html")
    else:
        """User reached route via GET (as by clicking a link or via redirect)"""
        return render_template("length.html", units=units, active_page="length")
    

@app.route("/weight", methods=["GET", "POST"])
def convert_weight():
    """Create a dictionary contains all weight units in gram"""
    WEIGHT = {
        "mg": 0.001,
        "gr": 1,
        "kg": 1000,
        "ounce": 28.35,
        "pound": 453.59,
    }

    """Make a list of all weight units"""
    units = WEIGHT.keys()

    if request.method == "POST":
        """User reached route via POST (as by submitting a form via POST)"""
        """Validate user input"""
        if not request.form.get("weight"):
            value = 1
        else:
            value = request.form.get("weight")
        if not request.form.get("convert_from"):
            return render_template("error.html")
        else:
            convert_from = request.form.get("convert_from")
        if not request.form.get("convert_to"):
            return render_template("error.html")
        else:
            convert_to = request.form.get("convert_to")

        """Try to convert and raise error if invalid value input"""
        try:
            result = float(value) * WEIGHT[convert_from] / WEIGHT[convert_to]
            return render_template("result.html", value=value, result=result, convert_from=convert_from, convert_to=convert_to)
        except ValueError:
            return render_template("error.html")
    else:
        """User reached route via GET (as by clicking a link or via redirect)"""
        return render_template("weight.html", units=units)


@app.route("/temperature", methods=["GET", "POST"])
def convert_temp():
    """Make a list of all temperature units"""
    units = ["Celsius", "Fahrenheit", "Kelvin"]

    if request.method == "POST":
        """User reached route via POST (as by submitting a form via POST)"""
        """Validate user input"""
        if not request.form.get("weight"):
            value = 1
        else:
            value = request.form.get("weight")
        if not request.form.get("convert_from"):
            return render_template("error.html")
        else:
            convert_from = request.form.get("convert_from")
        if not request.form.get("convert_to"):
            return render_template("error.html")
        else:
            convert_to = request.form.get("convert_to")

        try:
            if convert_from == "Celsius":
                if convert_to == "Celsius":
                    result = float(value)
                elif convert_to == "Fahrenheit":
                    result =  9/5 * float(value) + 32
                elif convert_to == "Kelvin":
                    result = float(value) + 273.15
            elif convert_from == "Fahrenheit":
                if convert_to == "Celsius":
                    result = (float(value) - 32) * 5/9
                elif convert_to == "Fahrenheit":
                    result =  float(value)
                elif convert_to == "Kelvin":
                    result = (float(value) - 32) * 5/9 + 273.15
            elif convert_from == "Kelvin":
                if convert_to == "Celsius":
                    result = float(value) - 273.15
                elif convert_to == "Fahrenheit":
                    result =  9/5 * (float(value) - 273.15) + 32
                elif convert_to == "Kelvin":
                    result = float(value)
            return render_template("result.html", value=value, result=result, convert_from=convert_from, convert_to=convert_to)
        except ValueError:
            return render_template("error.html")
    else:
        """User reached route via GET (as by clicking a link or via redirect)"""
        return render_template("temperature.html", units=units)


if __name__ == "__main__":
    app.run()