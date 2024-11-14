# zadanie-rekrutacyjne-Oxido

## Wymagania
Program wymaga Pythona w wersji >= 3.8 oraz zainstalowania poniższych zależności:
```
pip install openai
pip install python-dotenv
```
## Użucie
```
py main.py path_to_txt_file.txt 'your_api_key'
```
Alternatywnie klucz API można ustawić w os.environ, lub w pliku .env
```
OPENAI_API_KEY='your_api_key'
```
Plik .env powinien znajdować się w tym samym katalogu co skrypt main.py.
### Przykład użycia
```
py main.py "Zadanie dla JJunior AI Developera - tresc artykulu.txt"
```
## Działanie
Aplikacja zczytuje tekst z podanego pliku .txt, następnie wysyła go do API OpenAI, otrzymaną odpowiedz zapisuje jako `artykul.html`.
