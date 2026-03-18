# Statki
Celem projektu było zaznajomienie się z funkcjonowaniem klas w pythonie i biblioteki tkinter. 

## Instrukcja gry

### Przebieg gry:
1. Wybranie statku oraz narodowości kapitana. Narodowość wpływa na umiejętności żeglarstwa(⎈) oraz dowodzenia (⚔).
2. Bitwa morska z przeciwnikiem. W grze jest 5 przeciwników. Gra kończy się, gdy gracz wygra wszystkie bitwy lub gdy jego statek zostanie zatopiony.
3. Naprawa statku gracza
4. Punkt 2.

### Przebieg bitwy:
1. Gracze deklarują swoje działania w przyszłej rundzie. Może to być ucieczka, ostrzał lub abordaż.
2. Gracze rzucają liczbą kości odpowiadającą ich umiejętności żeglarstwa (⎈). Zliczona jest ilość sukcesów (5 i 6), reprezentowanych przez czaszki.
3. Wygrana - Jeśli kapitan, który wygrał, wybrał ostrzał, strzela wszystkimi dostępnymi działami. Jeśli wybrał abordaż, rozpoczyna się starcie załogi. Jeśli wybrał ucieczkę, udaje mu się uciec.
  Remis - jeżeli kapitan wybrał ostrzał, strzela tyloma działami, ile wyrzucił sukcesów. Jeżeli kapitan wybrał abordaż lub ucieczkę, nic się nie dzieje.
  Porażka - Tak jak w przypadku remisu.

### Starcie załogi:
1. Gracze rzucają liczbą kości odpowiadającą ich umiejętności dowodzenia(⚔). Zliczona jest ilość sukcesów (5 i 6), reprezentowanych przez czaszki.
2. Załoga zadaje tyle obrażeń, ile wynosi liczba sukcesów, ale nie więcej, niż liczba załogantów.
3. Powtarza się do momentu, gdy jedna z załóg nie ma już żadnych załogantów.
4. Gdy gracz wygra starcie załogi ze statkiem o wyższym poziomie, przejmuje go.
