![Tests](https://github.com/MisterEblan/mtuci_private_api/actions/workflows/tests.yaml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12+-blue.svg)
![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

# Langchain + MTUCI

Данная библиотека содержит обёртки над функционалом [MTUCI Private API](https://github.com/MisterEblan/mtuci_private_api) для AI-агентов.

> [!IMPORTANT]
> Данные инструменты **только асинхронные**. У них нет синхронной реализации.

# Возможности

- **Информация о пользователе**. Агент может получить информацию о текущем пользователе.
- **Посещаемость**. Агент может получить информацию о посещаемости студента.
- **Расписание**. Агент может получить информацию о расписании на определённую дату.

# Быстрый старт

Чтобы получить инструмент достаточно данного кода:
```Python
from langchain_mtuci import MtuciToolFactory

# Создание фабрики инструментов
factory = MtuciToolFactory(
    login="ваш_логин",
    password="ваш_пароль"
)

# Получение всех инструментов
tools = factory.create_tools()
```

Сами по себе инструменты не создаются - только через фабрику, т.к. требуют доступа к её сессии.
