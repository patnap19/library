# 📚 Szkolna Biblioteka – Konsolowa aplikacja w Pythonie

Konsolowa aplikacja do zarządzania biblioteką szkolną. Pozwala na przeglądanie, filtrowanie, edytowanie oraz wypożyczanie książek, które są przechowywane w pliku JSON.

---

## ✅ Funkcje

- 📖 Wyświetlanie wszystkich książek w bibliotece w formie tabeli
- 🔍 Filtrowanie książek po wielu kryteriach:
  - tytuł
  - autor
  - rok wydania
  - gatunek
  - status wypożyczenia
- ➕ Dodawanie nowej książki (z walidacją danych)
- ✍ Edycja danych książki (tytuł, autor, rok, gatunek)
- 🔀 Wypożyczanie i zwracanie książek
- 📊 Statystyki biblioteki (liczba książek, dostępnych, najczęściej występujący autor)
- 📂 Dane zapisywane i wczytywane z pliku `books.json`

---

## 🛠 Wymagania

- Python 3.8+
- Biblioteka `prettytable` do wyświetlania książek w formie tabeli:

```bash
pip install prettytable
```

---

## 📂 Przykład zawartości `books.json`

Aplikacja sama tworzy plik `books.json`, jeśli go nie ma. Przykładowa struktura:

```json
[
  {
    "id": "1234-uuid",
    "title": "Wiedźmin",
    "author": "Andrzej Sapkowski",
    "year": 1993,
    "genre": "Fantasy",
    "borrowed": false
  }
]
```

---

## 🚀 Uruchomienie aplikacji

1. Upewnij się, że plik `books.json` (jeśli istnieje) znajduje się w tym samym folderze co plik `.py`
2. Uruchom aplikację:

```bash
python biblioteka.py
```

---

## 🧪 Przykładowe opcje w menu

```
1. Pokaż książki
2. Dodaj książkę
3. Filtruj książki
4. Statystyki
5. Wypożycz książkę
6. Zwróć książkę
7. Edytuj książkę
0. Wyjście
```

---

## 🧹 Planowane funkcje

- 📅 Import i eksport danych (CSV lub JSON)
- 👥 Obsługa wielu użytkowników
- 🕒 Historia wypożyczeń
- 🔍 Sortowanie wyników filtrowania
- 🗑 Usuwanie książek
- 📌 Ulubione książki / oznaczenia

---

## 🧠 Struktura projektu (OOP)

- `Book` – reprezentuje pojedynczą książkę
- `Library` – zarządza książkami, plikiem JSON oraz operacjami (dodawanie, filtrowanie, wypożyczanie itp.)
- `LibraryApp` – główna aplikacja sterująca menu i przepływem programu

---

## 📌 Licencja

Projekt stworzony do celów edukacyjnych. Można dowolnie modyfikować i rozwijać 🚀
