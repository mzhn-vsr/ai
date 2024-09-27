import requests

from typing import Dict, List, Union
from langchain_core.documents import Document
from langchain_community.docstore.base import Docstore, AddableMixin

documents = [
    {
        "question": "Зачем нужна регистрация на RUTUBE?",
        "answer": """Зарегистрированный пользователь получает возможность: ·Завести собственный канал на RUTUBE: оформить его и начать загружать видеоролики и/или проводить стримы (прямые трансляции); ·Присоединиться к партнерской программе RUTUBE; ·Оформить платную подписку и получить доступ к тысячам единиц лицензионного контента и эфирам сотен телеканалов; ·Оставлять комментарии.""",
    },
    {
        "question": "Что нужно для регистрации на RUTUBE?",
        "answer": "Актуальный личный e-mail (корпоративный e-mail — для юридических лиц) или номер телефона – эти данные будут использоваться в качестве логина при последующей авторизации, а e-mail понадобится для восстановления пароля.",
    },
    {
        "question": "Как сменить пароль?",
        "answer": "Авторизуйтесь на RUTUBE, перейдите в свой профиль: https://rutube.ru/profile, нажмите «Изменить пароль» и следуйте подсказкам.",
    },
    {
        "question": "Как восстановить пароль?",
        "answer": "Нажмите на кнопку «Вход и регистрация» в правом верхнем углу страницы. В появившемся окне введите адрес электронной почты или номер телефона, по которому вы регистрировались, и нажмите «Продолжить». В окне ввода пароля нажмите внизу на сноску «Забыли пароль?», после чего на привязанный к профилю электронный адрес придет код для сброса пароля.",
    },
]


class RESTDocstore(Docstore, AddableMixin):
    def __init__(self):
        self.base_url = "http://localhost:3000"
        pass

    def search(self, search: str) -> Union[str, Document]:
        """
        doc_id = search
        response = requests.get(f"{self.base_url}/docs/{doc_id}")

        if response.status_code == 200:
            data = response.json()

            return Document(
                page_content=data["question"],
                metadata={
                    "answer": data["answer"],
                }
            )
        else:
            return f"ID {search} not found."
        """
        d = documents[int(search)]
        return Document(
            page_content=d["question"],
            metadata={
                "answer": d["answer"],
            },
        )

    def add(self, texts: Dict[str, Document]) -> None:
        """
        Не нужно, т.к. REST - база
        """
        pass

    def delete(self, ids: List) -> None:
        """
        Не нужно, т.к. REST - база
        """
        pass
