

def classify_earthquake(magnitude):
    category = (
        "Micro" if magnitude < 2.0 else
        "Minor" if 2.0 <= magnitude < 4.0 else
        "Light" if 4.0 <= magnitude < 5.0 else
        "Moderate" if 5.0 <= magnitude < 6.0 else
        "Strong" if 6.0 <= magnitude < 7.0 else
        "Major" if 7.0 <= magnitude < 8.0 else
        "Great" if magnitude >= 8.0 else
        "Geh sterben!!!"
    )
    advice = {
        "Micro": "Bleib Tapfer",
        "Minor": "weil_halt",
        "Light": "Licht",
        "Moderate": "Bleib Tapfer",
        "Strong": "Du packst das",
        "Major": "Klasse",
        "Great": "Großartig",
        "Geh sterben": "Opfer"

    }.get(category)

    return category,advice

magnitude = float(input("Enter magnitude: "))
print(classify_earthquake(magnitude))