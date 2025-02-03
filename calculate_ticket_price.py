def calculate_ticket_price(age, is_student):

    base_price = 20.0

    if  age >= 65:
        return base_price * 0.5  # 50% Rabatt -> 10€
    elif is_student and age < 30:
        return base_price * 0.7  # 30% Rabatt -> 14€
    else:
        return base_price  # Standardpreis 20€


age = int(input("Geben Sie das Alter des Besuchers ein: "))
is_student = False
if not (age > 30): is_student = input("Ist der Besucher ein Student? (ja/nein): ").strip().lower() == "ja"

ticket_price = calculate_ticket_price(age, is_student)

print(f"Der Ticketpreis beträgt: {ticket_price:.2f} Euro")


