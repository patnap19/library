# 📚 Library Management CLI App (Python)

Aplikacja konsolowa do zarządzania biblioteką, pozwalająca na:

- dodawanie i edytowanie książek,
- wypożyczanie i zwracanie,
- filtrowanie i przeszukiwanie katalogu,
- rejestrowanie logów aktywności,
- analizę statystyk bibliotecznych.

## 🧠 Struktura projektu

```
library/
├── app.py               # Główna pętla programu (interfejs CLI)
├── library.py           # Klasa Library – zarządza książkami i logami
├── book.py              # Klasa Book – reprezentuje książkę
├── logs.py              # Klasa LogsManager – rejestruje historię działań
├── utils.py             # Funkcje pomocnicze (walidacja, czyszczenie ekranu)
└── storage/
    ├── books.json       # Dane książek
    └── logs.json        # Historia logów aktywności
```

## 🛠️ Wymagania

- Python 3.8 lub nowszy
- Pakiety: `prettytable`

Można zainstalować wymagany pakiet komendą:

```bash
pip install prettytable
```

## 🚀 Jak uruchomić?

1. Upewnij się, że masz strukturę katalogów zgodną z powyższą.
2. W terminalu (z katalogu projektu) uruchom:

```bash
python app.py
```

## 🧩 Funkcje

### 📖 Zarządzanie książkami:

- Dodawanie, edytowanie i usuwanie książek
- Przechowywanie danych w pliku `storage/books.json`

### 🔍 Filtrowanie:

- Po tytule, autorze, roku, gatunku lub stanie wypożyczenia

### 📕 Wypożyczanie i zwroty:

- Status `borrowed` zmieniany automatycznie
- Rejestrowanie akcji w logach

### 📊 Statystyki:

- Całkowita liczba książek
- Ilość wypożyczonych i dostępnych
- Autorzy z największą liczbą książek

### 📜 Historia logów:

- Logi akcji: dodanie, edycja, wypożyczenie, zwrot, usunięcie
- Możliwość przeszukiwania logów wg książki lub daty

## 📝 Dane logów

Log zawiera:

- unikalny identyfikator
- `book_id` powiązany z książką
- typ akcji (`Dodano`, `Zwrócono`, `Usunięto` itd.)
- datę i czas zdarzenia

Zapisane są w `storage/logs.json`.

## 📂 Przykład rekordu książki

```json
{
  "id": "e8a9b1f4-1234-4bde-a321-c0ac132d5001",
  "title": "Wiedźmin",
  "author": "Andrzej Sapkowski",
  "year": 1990,
  "genre": "Fantasy",
  "borrowed": false
}
```

## ✍️ Autor

Projekt utworzony i rozwijany przez patnap19.

## 📃 Licencja

MIT – możesz używać, kopiować i modyfikować wedle uznania.
