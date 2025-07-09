# SpisaLoveO

## Локальная установка
Создать файл .env в корне проекта: скопировать содержимое из .env-example и настроить под себя, если надо
```sh
cat .env.example > .env
```
Установить зависимости
```sh
poetry install

```
Запустить приложение
```sh
uvicorn src.spisa_love_o.main:app --host 0.0.0.0 --port 8000

```