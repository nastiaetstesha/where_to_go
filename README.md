# Куда пойти — Москва глазами Артёма

Сайт с интерактивной картой, где собраны интересные места Москвы. Можно посмотреть описание, фото, координаты и детали каждого объекта.

## 🔗 Демо

Сайт доступен по адресу:  
[https://steshaet0steshaet.pythonanywhere.com/](https://steshaet0steshaet.pythonanywhere.com/)

## ⚙️ Переменные окружения

Проект использует следующие переменные окружения (например, через `.env`):

```env
SECRET_KEY=your_secret_key_django
DEBUG=False
ALLOWED_HOSTS=steshaet0steshaet.pythonanywhere.com,127.0.0.1,localhost

## Пример JSON-файла с локацией

```
{
  "title": "Арт-пространство «Бункер 703»",
  "imgs": [
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/35cbdddf2799337d8b571d141edec616.JPG",
    "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/9fec510ebb52aaa4667c4b9fa2b6222.JPG"
  ],
  "description_short": "«Бункер 703» — музей современной фортификации...",
  "description_long": "<p>Туристы и жители столицы, случайные прохожие и зеваки...</p>",
  "coordinates": {
    "lng": "37.6303209999998",
    "lat": "55.7343690000001"
  }
}
```

## 🚀 Загрузка локаций
Для загрузки данных в базу используется команда:

```bash
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/file_name.json