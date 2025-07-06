# 📚 Szkolna Biblioteka – Konsolowa aplikacja Python

Aplikacja umożliwia przeglądanie, wyszukiwanie oraz dodawanie książek do biblioteki szkolnej, która jest przechowywana w pliku JSON.

---

## ✅ Funkcje

- 📖 Wyświetlanie wszystkich książek w bibliotece
- 🔍 Wyszukiwanie książek według:
  - autora
  - tytułu
  - gatunku
  - roku wydania
- ➕ Dodawanie nowej książki (z walidacją roku wydania)
- 🚫 Sprawdzanie, czy książka już istnieje przed dodaniem
- 🧾 Dane przechowywane w pliku `books.json` w formacie JSON

---

## 🛠 Wymagania

- Python 3.x
- Plik `books.json` z przykładową strukturą (jeśli nie istnieje, należy go utworzyć ręcznie)

Przykład zawartości `books.json`:

```json
[
  {
    "tytuł": "Wiedźmin",
    "autor": "Andrzej Sapkowski",
    "rok": 1993,
    "gatunek": "Fantasy"
  },
  {
    "tytuł": "Pan Tadeusz",
    "autor": "Adam Mickiewicz",
    "rok": 1834,
    "gatunek": "Epopeja"
  }
]
```

---

## 🚀 Uruchomienie aplikacji

1. Upewnij się, że masz plik `books.json` w tym samym folderze co plik `.py`.
2. Uruchom aplikację:

```bash
python biblioteka.py
```

---

## 💡 Przykład działania

```
Witaj w naszej szkolnej bibliotece! Co chciałbyś zrobić?

1. Wyświetl wszystkie książki.
2. Wyszukaj książki.
3. Dodaj książkę.
0. Zakończ pracę.

Twój wybór: 1
```

---

## 🧹 Planowane funkcje

- Rejestracja wypożyczeń książek
- Historia operacji użytkownika
- Usuwanie książek z biblioteki
- Edycja informacji o książkach
- Dodanie obsługi wielu użytkowników
- Eksport do CSV
- Sortowanie wyników wyszukiwania
