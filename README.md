# 📚 Aplikacja Biblioteka Szkolna

Projekt umożliwia zarządzanie biblioteką szkolną w terminalu: logowanie, wypożyczanie książek, zarządzanie użytkownikami oraz historię operacji.

---

## 📦 Struktura projektu

```
library/
├── app.py               # Główna aplikacja
├── book.py              # Klasa Book
├── library.py           # Główna logika biblioteki
├── logs.py              # System logowania działań
├── user.py              # Użytkownicy i ich zarządzanie
├── utils.py             # Funkcje pomocnicze
└── storage/
    ├── books.json       # Dane książek
    ├── users.json       # Dane użytkowników
    └── logs.json        # Logi
```

---

## 🔐 Logowanie

- 3 próby logowania.
- Hasła mogą być hashowane za pomocą `hashlib` (do wdrożenia).
- Rola admina (`is_admin`) umożliwia dostęp do rozszerzonych opcji.

---

## 👤 Role użytkowników

| Rola          | Możliwości                                    |
| ------------- | --------------------------------------------- |
| Użytkownik    | Przeglądanie książek, wypożyczanie, zwracanie |
| Administrator | Zarządzanie książkami, użytkownikami, logami  |

---

## 📘 Funkcje

- Dodawanie/edycja/usuwanie książek
- Filtrowanie wg autora, roku, gatunku, dostępności
- Obsługa logów (kto co zrobił i kiedy)
- Statystyki biblioteki (np. najczęstszy autor)
- Możliwość dodania użytkowników przez admina

---

## ✅ Przykładowy przebieg

1. Uruchom `app.py`
2. Zaloguj się jako istniejący użytkownik (admin lub zwykły)
3. Wybierz odpowiednie menu
4. Wykonuj operacje (np. wypożycz, edytuj, dodaj książkę)

---

## ⚠️ TODO

- [ ] Hashowanie haseł
- [ ] Możliwość zmiany hasła
- [ ] Logi filtrowane po akcji
- [ ] Testy jednostkowe (`pytest`)
- [ ] Refaktoryzacja `logs_filter()` do `logs.py`

---

## 🧪 Testowanie

Zalecane testy jednostkowe dla klas:

- `User`
- `Book`
- `LogsManager`
- `Library`

---

## 📄 Licencja

Projekt edukacyjny – możesz modyfikować i używać dowolnie w celach niekomercyjnych.
