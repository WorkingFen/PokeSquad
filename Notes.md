-Oryginalny plik .csv ma błędy odnośnie "Mega ewolucji", a także brakuje mu kilku pokemonów

Różnice
-typy (współczynniki obrażeń)
-umiejętności (z prawdopodobieństwem 100%)

Uproszczenia
-poksy są zawsze na poziomie 1
-pogoda z rozkładem normalnym (anomalie na krańcach)
-wyrzucenie ruchów statusowych

Założenia
-wybierany jest zawsze najkorzystniejszy ruch
-typ walki to 6v1

Pytanie
Czy próbować symulacji walk z różnymi poksami i na tej podstawie wyłonić najlepszą drużynę?
Czy szukać takiej drużyny żeby była jak najbardziej wszechstronna i przy tym jak najmocniejsza?

Podejście 1
Próba przetestowania drużyny versus duża ilość przeciwników i na tej podstawie
jej ocena.

Podejście 2
Założenie, że drużyna ma być mocna i jednocześnie możliwie wszechstronna,
na tej podstawie dobieranie kolejnych poksów.

Wtedy poksa charakteryzowałaby macierz wpółczynników atak/obrona z uwzględnieniem szybkości i hp.


-------------------------------------------------------------------------------------------------------
Pogoda:
Jeśli umiejętności pokemonów powodują zmianę pogody, to wywołany efekt będzie zależeć od tego, który z pokemonów jest wolniejszy (jego efekt zostanie wywołany jako ostatni, nadpisując poprzedni efekt)
