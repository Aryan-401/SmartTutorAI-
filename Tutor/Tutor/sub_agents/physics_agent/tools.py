import logging
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")

def get_constants(constant_name: str) -> str:
    """Returns the value of a constant based on its name."""
    constants = {
        "PI": 3.14159,
        "E": 2.71828,
        "GOLDEN_RATIO": 1.61803,
        "SPEED_OF_LIGHT": 299792458,  # in m/s
        "GRAVITATIONAL_CONSTANT": 6.67430e-11,  # in m^3 kg^-1 s^-2
    }
    return str(constants.get(constant_name.upper(), "Constant not found."))
