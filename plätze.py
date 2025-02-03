k = ["Matthias Schmitt", "Felix Holzmann", "Sabrina Eggers", "Sebastian Wolf", "Niklas Eisenbaum", "Florian Kuster", "Jan Ackerman", "Erika Ebersbacher"]

eingabe = input("Welchen Platz möchten sie Wissen? ")
if eingabe == "eins" :
    print(k[0])
elif eingabe == "zwei" :
    print(k[1])
elif eingabe == "drei" :
    print(k[2])
elif eingabe == "vier" :
    print(k[3])
elif eingabe == "fünf" :
    print(k[4])
elif eingabe == "sechs" :
    print(k[5])
elif eingabe == "sieben" :
    print(k[6])
elif eingabe == "acht" :
    print(k[7])


else :
    from turtle import *
    color("black")
    begin_fill()
    pensize(17)
    left(50)
    forward(133)
    circle(50,200)
    right(140)
    circle(50,200)
    forward(133)
    end_fill()
