##
health_data = [
    {'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96},
    {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85},
    {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77},
    {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62},
    {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70},
    {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82},
]
##
bmi_data = {range(0, 184): {"Category": "Underweight",
                            "Health risk": "Malnutrition risk"},
            range(185, 249): {"Category": "Normal weight",
                              "Health risk": "Low risk"},
            range(250, 299): {"Category": "Overweight",
                              "Health risk": "Enhanced risk"},
            range(300, 349): {"Category": "Moderately obese",
                              "Health risk": "Medium risk"},
            range(350, 399): {"Category": "Severely obese",
                              "Health risk": "High risk"},
            range(400, 999): {"Category": "Very severely obese",
                              "Health risk": "Very high risk"},
            }

