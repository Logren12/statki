# Statki
Celem projektu było zaznajomienie się z funkcjonowaniem klas w pythonie i biblioteki tkinter. 

## Instrukcja gry

### Przebieg gry:
1. Wybranie statku oraz narodowości kapitana. Narodowość wpływa na umiejętności żeglarstwa(⎈) oraz dowodzenia (⚔).
2. Bitwa morska z przeciwnikiem. W grze jest 5 przeciwników. Gra kończy się, gdy gracz wygra wszystkie bitwy lub gdy jego statek zostanie zatopiony.
3. Naprawa statku gracza
4. Punkt 2.

### Przebieg rundy:
Każda runda dzieli się na trzy fazy: fazę deklaracji, fazę manewrów i fazę rozliczeń.

1. Faza deklaracji: Gracze deklarują swoje działania w przyszłej rundzie. Może to być ucieczka, ostrzał lub abordaż.

2.Faza manewrowania: Obaj Kapitanowie rzucają na żeglarstwo (⎈). Wygrywa ten, który wyrzucił większą ilość sukcesów (5 i 6) reprezentowanych przez czaszki. Dodatkowo, jeśli jakiś kapitan ma zniszczone żagle, rzuca maksymalnie jedną kostką.

3. Faza rozliczeń: Determinowany jest typ starcia. Jeśli wygrany gracz chciał abordażu, zaczyna się bitwa załogi. Jeśli wygrany gracz chce uciekać, udaje mu się uciec. Jeśli wygrany gracz chciał strzelać z dział dzieje się jedno z poniższych:
a) przegrany chciał uciekać lub dokonać abordażu: wygrany strzela do przegranego ze wszystkich dział i runda się kończy
b) przegrany chciał strzelać: wygrany strzela do przegranego ze wszystkich dział, a przegrany strzela do wygranego z tylu dział, ile wyrzucił sukcesów.

Gracze strzelają do siebie równocześnie. W takim wypadku naliczanie obrażeń dzieje się po strzelaniu. W przypadku remisu, jeśli któryś z Kapitanów chciał strzelać, strzela z tylu dział, ile wyrzucił sukcesów. W pozostałych przypadkach nic się nie dzieje.

### Starcie załogi:
1. Gracze rzucają liczbą kości odpowiadającą ich umiejętności dowodzenia(⚔). Zliczona jest ilość sukcesów (5 i 6), reprezentowanych przez czaszki.
2. Załoga zadaje tyle obrażeń, ile wynosi liczba sukcesów, ale nie więcej, niż liczba załogantów.
3. Powtarza się do momentu, gdy jedna z załóg nie ma już żadnych załogantów.
4. Gdy gracz wygra starcie załogi ze statkiem o wyższym poziomie, przejmuje go.
