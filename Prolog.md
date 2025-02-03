## Prolog
### Basis

male(max). 
male(peter). 
female(anna). 
female(lisa). 

mother(anna,max).
father(peter,max).
mother(anna,lisa).
father(peter,lisa).

child (C,M,F) :- mother(M, K); father (F, C). 

sister(X, Y):-(mother (M,X) , mother(M,Y);    father (F,X), father (F,Y)).

child (C,M, F) :- mother(M, C), father (F, C). 

##### Q01: Alle Kinder zu einem bestimmten Elternteil.
     findall (X, mother(anna, X), L).
##### Q02 : Alle Geschwister zu einer bestimmten Person.
        findall( X,sister ( lisa,X) , L). 
##### Q03: Überprüfen, ob zwei Personen Geschwister sind
         geschwister (lisa, max).
## Rekursion


vehicle(4, ),  vehicle(7, ), vehicle(13,). 


check_vehicle_type(Size, VehicleType) :-
   Size =< 4, 
    VehicleType = kleinwagen.

check_vehicle_type(Size, VehicleType) :-
    Size > 4, Size =< 5,
     VehicleType = mittelwagen.

check_vehicle_type(Size, VehicleType) :-
    Size > 5, Size =< 12,
    VehicleType = lkw.

check_vehicle_type(Size, VehicleType) :-
    Size > 12,
    VehicleType = bus


isBigger(bus, lkw).
isBigger(bus, mittelwagen).
isBigger(mittelwagen,  kleinwagen).

recursiveIsBigger(X, Y) :- isBigger(X, Y).
recursiveIsBigger(X, Y) :- isBigger(X, Z), recursiveIsBigger(Z, Y).

.
same_vehicle_type([Size], VehicleType) :- vehicle_type(Size, VehicleType).

## Expertensystem 04
tier(elefant, 5000, savanne, pflanzenfresser).
tier(löwe, 190, savanne, fleischfresser).
tier(pinguin, 30, antarktis, fischfresser).
tier(krokodil, 600, flüsse, fleischfresser).
tier(hase, 5, wald, pflanzenfresser).

gewichtskategorie(Tier, leicht) :- tier(Tier, Gewicht, , ), Gewicht < 50.
gewichtskategorie(Tier, mittel) :- tier(Tier, Gewicht, , ), Gewicht >= 50, Gewicht < 1000.
gewichtskategorie(Tier, schwer) :- tier(Tier, Gewicht, , ), Gewicht >= 1000.


lebensraumkategorie(Tier, savanne) :- tier(Tier, , savanne, ).
lebensraumkategorie(Tier, wald) :- tier(Tier, , wald, ).
lebensraumkategorie(Tier, wasser) :- tier(Tier, , antarktis, ).
lebensraumkategorie(Tier, wasser) :- tier(Tier, , flüsse, ).

ehrungskategorie(Tier, fleischfresser) :- tier(Tier, , , fleischfresser).
ernaehrungskategorie(Tier, pflanzenfresser) :- tier(Tier, , , pflanzenfresser).
ernaehrungskategorie(Tier, fischfresser) :- tier(Tier, , , fischfresser).


abfragegewichtskategorie(Tier, Kategorie) :- tier(Tier, 600, , _), gewichtskategorie(Tier, Kategorie).


abfrage_lebensraumlöwe(Lebensraum) :- tier(löwe, , Lebensraum, _).

abfrage_ernaehrungpinguin(Ernaehrung) :- tier(pinguin, , _, Ernaehrung). (Bearbeitet)

## Komplexe Regel 06

hubschrauber(helicopter1, 150, 300, 1000).
hubschrauber(helicopter2, 120, 250, 800).
hubschrauber(helicopter3, 180, 350, 1200).

rettungsfluggeeignet(Hubschrauber) :-
    hubschrauber(Hubschrauber, Geschwindigkeit, Reichweite, Tragkraft),
    (Geschwindigkeit > 140; 
    (Geschwindigkeit =< 140, Geschwindigkeit >= 100, Reichweite > 280, Tragkraft > 900)).


% Q01: Ist Helicopter1 für Rettungsflüge geeignet?
abfrage_geeignet_1 :-
    rettungsfluggeeignet(helicopter1),
    write('Helicopter1 ist für Rettungsflüge geeignet.').
abfrage_geeignet_1 :-
    + rettungsfluggeeignet(helicopter1),
    write('Helicopter1 ist nicht für Rettungsflüge geeignet.').

% Q02: Ist Helicopter2 für Rettungsflüge geeignet?
abfrage_geeignet_2 :-
    rettungsfluggeeignet(helicopter2),
    write('Helicopter2 ist für Rettungsflüge geeignet.').
abfrage_geeignet_2 :-
    + rettungsfluggeeignet(helicopter2),
    write('Helicopter2 ist nicht für Rettungsflüge geeignet.').

% Q03: Welche Hubschrauber erfüllen nicht die Kriterien für Rettungsflüge?
nicht_geeignet(Hubschrauber) :-
    hubschrauber(Hubschrauber, Geschwindigkeit, Reichweite, Tragkraft),
    + rettungsfluggeeignet(Hubschrauber).

abfrage_nicht_geeignet :-
    nicht_geeignet(Hubschrauber),
    write(Hubschrauber), nl,
    fail.
abfrage_nicht_geeignet. 