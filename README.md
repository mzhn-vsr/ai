# AI

Сервис для генерации ответа на основе вопроса и базы знаний.

## Как развернуть?

Решение проверялось на Ubuntu 22.04 LTS Python 3.10. 

### Установка

Для работы потребуется [ollama](https://ollama.com/).

Устанавливаем зависимости:

```
$ pip install -r requirements.txt
```

Скачиваем используемую модель:

```
$ ollama pull krith/qwen2.5-14b-instruct:IQ4_XS
```

### Настройка

```
$ cp .env.example .env
```

Настройте env в соответствии с комментариями

### Запуск

> [!] Перед запуском необходимо запустить [managment](https://github.com/mzhn-vsr/management) сервис.

```
$ uvicorn main:app --host 0.0.0.0 --port 8080
```

## REST API

Документация доступна по `http://host:port/docs` и в качестве openai.json в корне репозитория

P.S.: `/chat/*` и `/classifier` - созданы автоматически с помощью [LangServe](https://github.com/langchain-ai/langserve).

### Краткий обзор полезных endpoint'ов

- `/faiss/add` и `/faiss/delete` - для добавления и удаления из FAISS документов (индексов). Необходимы для обновления базы FAISS без перезагрузки сервиса.

- `/chat/invoke` - простой вызов LLM для получения ответа на вопрос.

- `/chat/invoke` - простой вызов LLM для получения классов вопроса.