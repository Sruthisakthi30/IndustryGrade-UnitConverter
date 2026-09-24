from flask import Flask, request, jsonify

app = Flask(__name__)


# Unit conversion logic
def convert_unit(value, from_unit, to_unit):

    # Distance conversions
    distance_conversions = {
        ("km", "miles"): lambda x: x * 0.621371,
        ("miles", "km"): lambda x: x * 1.60934,
        ("m", "ft"): lambda x: x * 3.28084,
        ("ft", "m"): lambda x: x * 0.3048
    }

    # Temperature conversions
    temperature_conversions = {
        ("celsius", "fahrenheit"): lambda x: (x * 9 / 5) + 32,
        ("fahrenheit", "celsius"): lambda x: (x - 32) * 5 / 9
    }

    # Weight conversions
    weight_conversions = {
        ("kg", "pounds"): lambda x: x * 2.20462,
        ("pounds", "kg"): lambda x: x * 0.453592
    }

    conversions = {
        **distance_conversions,
        **temperature_conversions,
        **weight_conversions
    }

    conversion = conversions.get((from_unit, to_unit))

    if conversion is None:
        return None

    return conversion(value)


@app.route("/api/convert", methods=["GET"])
def convert():

    # Get query parameters
    value = request.args.get("value")
    from_unit = request.args.get("from")
    to_unit = request.args.get("to")

    # Check whether all parameters are provided
    if value is None or from_unit is None or to_unit is None:
        return jsonify({
            "success": False,
            "error": "Missing required parameters: value, from, to"
        }), 400

    # Validate numeric value
    try:
        value = float(value)
    except ValueError:
        return jsonify({
            "success": False,
            "error": "Value must be a valid number"
        }), 400

    # Normalize units
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Perform conversion
    result = convert_unit(value, from_unit, to_unit)

    # Check unsupported conversion
    if result is None:
        return jsonify({
            "success": False,
            "error": f"Unsupported conversion from {from_unit} to {to_unit}"
        }), 400

    return jsonify({
        "success": True,
        "value": value,
        "from": from_unit,
        "to": to_unit,
        "result": round(result, 5)
    }), 200


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "service": "Smart Unit Converter Microservice",
        "status": "running",
        "endpoint": "/api/convert"
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)