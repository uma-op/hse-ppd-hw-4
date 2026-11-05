# Домашняя работа №4

Для запуска сервера требуется настроить окружение. Для этого из папки проекта нужно выполнить следующие команды

```shell
$> python3 -m venv .venv
$> . .venv/bin/activate
(.venv) $> pip install -r requirements.txt
```

Теперь можно запустить сервер следующей командой

```shell
$> uv run fastapi dev
```

После выполнения всех команд на http://127.0.0.1:8000 должен поднятся сервер с требуемым в ДЗ API.

## API

На http://127.0.0.1:8000/report/ можно посылать POST запросы с телом следующей схемы:

```json
{
  "$defs": {
    "Reason": {
      "properties": {
        "reason_type": {
          "$ref": "#/$defs/ReasonType"
        },
        "detection_time": {
          "format": "date-time",
          "title": "Detection Time",
          "type": "string"
        }
      },
      "required": [
        "reason_type",
        "detection_time"
      ],
      "title": "Reason",
      "type": "object"
    },
    "ReasonType": {
      "enum": [
        "нет доступа к сети",
        "не работает телефон",
        "не приходят письма"
      ],
      "title": "ReasonType",
      "type": "string"
    }
  },
  "properties": {
    "first_name": {
      "pattern": "^[А-Я][а-я]*$",
      "title": "First Name",
      "type": "string"
    },
    "last_name": {
      "pattern": "^[А-Я][а-я]*$",
      "title": "Last Name",
      "type": "string"
    },
    "birth_date": {
      "format": "date",
      "title": "Birth Date",
      "type": "string"
    },
    "phone_number": {
      "pattern": "^\\+?[1-9]\\d{1,14}$",
      "title": "Phone Number",
      "type": "string"
    },
    "email": {
      "format": "email",
      "title": "Email",
      "type": "string"
    },
    "reasons": {
      "items": {
        "$ref": "#/$defs/Reason"
      },
      "minItems": 1,
      "title": "Reasons",
      "type": "array"
    }
  },
  "required": [
    "first_name",
    "last_name",
    "birth_date",
    "phone_number",
    "email",
    "reasons"
  ],
  "title": "Report",
  "type": "object"
}
```

В ответе будет возвращаться путь до файла, в котором сохраняются запросы

## Тестирование

В директории testdata в корне проекта находятся тестовые json файлы, который можно применить следующей командой

```shell
$> curl http://127.0.0.1:8000/report/ --json @testdata/valid_report.json
```

После этого в директории /tmp должны появиться файл с именем вида _uuidv7_.json