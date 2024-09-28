from langchain_core.prompts import ChatPromptTemplate
from ai.chat import chat

classes = """
УПРАВЛЕНИЕ АККАУНТОМ,Персонализация
УПРАВЛЕНИЕ АККАУНТОМ,Уведомления
УПРАВЛЕНИЕ АККАУНТОМ,Подписки
УПРАВЛЕНИЕ АККАУНТОМ,Удаление аккаунта
УПРАВЛЕНИЕ АККАУНТОМ,Платный контент
УПРАВЛЕНИЕ АККАУНТОМ,Верификация
УПРАВЛЕНИЕ АККАУНТОМ,Регистрация/Авторизация
УПРАВЛЕНИЕ АККАУНТОМ,Аналитика
ВИДЕО,Недоступность видео
ВИДЕО,Загрузка видео
ВИДЕО,Комментарии
ВИДЕО,Система рекомендаций
ВИДЕО,Воспроизведение видео
ВИДЕО,Управление плеером
ВИДЕО,Встраивание видео
ВИДЕО,Перенос видео с Youtube
ТРАНСЛЯЦИЯ,ТВ-эфиры
ТРАНСЛЯЦИЯ,Просмотр трансляции
ТРАНСЛЯЦИЯ,Чат/Комментарии
ТРАНСЛЯЦИЯ,Управление трансляцией
ПОИСК,Текстовый поиск
ПОИСК,Голосовой поиск
ПОИСК,История поиска
ПРЕДЛОЖЕНИЯ,Студия RUTUBE
ПРЕДЛОЖЕНИЯ,Навигация
ПРЕДЛОЖЕНИЯ,Персонализация 0
ПРЕДЛОЖЕНИЯ,Плеер
ПРЕДЛОЖЕНИЯ,Трансляция
ПРЕДЛОЖЕНИЯ,Монетизация
МОДЕРАЦИЯ,Долгая модерация
МОДЕРАЦИЯ,Отклонение/блокировка видео
МОДЕРАЦИЯ,Удаление/добавление комментариев
МОДЕРАЦИЯ,Блокировка канала
МОДЕРАЦИЯ,Смена категории/возрастные ограничения
МОДЕРАЦИЯ,Нарушение авторских прав
МОДЕРАЦИЯ,Запрещенный контент
МОНЕТИЗАЦИЯ,Отключение/подключение монетизации
МОНЕТИЗАЦИЯ,Подключение/отключение рекламы
МОНЕТИЗАЦИЯ,Статистика по монетизации
МОНЕТИЗАЦИЯ,Кошелек
МОНЕТИЗАЦИЯ,Выплаты
БЛАГОТВОРИТЕЛЬНОСТЬ ДОНАТЫ,Подключение/отключение донатов
БЛАГОТВОРИТЕЛЬНОСТЬ ДОНАТЫ,Подключение/отключение благотворительности
СОТРУДНИЧЕСТВО ПРОДВИЖЕНИЕ РЕКЛАМА,Реклама на RUTUBE
СОТРУДНИЧЕСТВО ПРОДВИЖЕНИЕ РЕКЛАМА,Партнерство с RUTUBE
СОТРУДНИЧЕСТВО ПРОДВИЖЕНИЕ РЕКЛАМА,Продвижение канала
СОТРУДНИЧЕСТВО ПРОДВИЖЕНИЕ РЕКЛАМА,Эксклюзивный контент на RUTUBE
СОТРУДНИЧЕСТВО ПРОДВИЖЕНИЕ РЕКЛАМА,Акции и конкурсы
МОШЕННИЧЕСТВО,RUTUBE.ru
МОШЕННИЧЕСТВО,Студия RUTUBE
МОШЕННИЧЕСТВО,Приложение
ДОСТУП К RUTUBE,RUTUBE.ru
ДОСТУП К RUTUBE,Студия RUTUBE
ДОСТУП К RUTUBE,Приложение
ДОСТУП К RUTUBE,Навигация 0
"""

SYSTEM_TEMPLATE = f"""
As an assistant, your task is to act as a question classification expert.
You need to classify the question into 2 classes at once. 
The classes are presented below in <сontext></context>.

- Response with this format: CLASS_1,CLASS_2
- **Do not generate information** that is not present in the <context></context> tags.
- If the question is not relevant to any classes, say "ОТСУТСВУЕТ,Отсутствует".
- Then carefully double-check your answer. Think about whether this is the right answer, would others agree with it? Improve your answer as needed.

<context>
CLASS_1,CLASS_2
{classes}
</context>
"""

classifier_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", 
            SYSTEM_TEMPLATE
        ),
        ("human", "{input}"),
    ]
)

classifier_chain = (
    # {"context": retriever | format_docs, "input": RunnablePassthrough() }
    classifier_prompt 
    | chat
#    | StrOutputParser()
)