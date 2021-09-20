<h3 align='center'>Password complexity</h3>

---

<p align='center'> Сервис для предсказания популярности паролей</p>


# Источники
- Курс DMIA ProductionML : https://github.com/data-mining-in-action/DMIA_ProductionML_2021_Spring
- Соревнование : kaggle.com/c/dmia-production-ml-2021-1-passwords

# Полезные ресурсы
- Установка pyenv - https://realpython.com/intro-to-pyenv/
- Архитектура проекта - https://drivendata.github.io/cookiecutter-data-science/ 
- Гайд по написанию кода от Google - https://github.com/google/styleguide/blob/gh-pages/pyguide.md
- Гайд по Docker - https://www.amazon.com/Docker-Deep-Dive-Nigel-Poulton-ebook/dp/B01LXWQUFF/
- DVC - https://dvc.org
- Основы инструментов ml с углублённым описанием - https://drive.google.com/file/d/1p_soJ1fA03rpfqow7N2H2bXQLWBK6OeS/view

--- 

# Описание проекта
Данный репозиторий представляет собой: Ml архитектура + базовый flask софт   
Главная задача проекта - сделать ml архитектуру, которая будет: 
-  [x] Автоматизированной - модель должна самостоятельно принимать на вход данные и автоматически выдавать ответ.
-  [x] Гибкой - модель можно менять, дополнять без каких-то проблем.
-  [x] Надёжной - модель должна устанавливаться и работать без каких-нибудь ошибок. В процессе....
-  [ ] Стабильной - модель должна выдавать периодически одинаковый результат на тестовых данных. Обновлённая модель не должна сильно отличаться от предыдущей. Данные должны иметь одинаковыве распределения и не менятся со временем.  В проессе..

## Реализация:
В качестве реализации я использовал Pipeline архитектуру. Главный плюс данного выбора - он проще в реализации и гораздо удобнее в его изменении, так как каждый метод пайплайна изолирован и никак не связан с остальными.
Каждый отдельный скрипт я писал в отдельном python файле и импортировал эти методы как кастомные библиотеки с помощью setuptools. Всю методы я обернул в один Pipeline из библиотеки sklearn в отдельный файл [pipeline_structure.py](https://github.com/Lisstrange/password_complexity/blob/main/password_complexity/utils/pipeline_structure.py). В pipeline_structure.py написана готовая архитектура, которую мы можем изменять независимо от других методов. 
На данный момент в стрктуре пайплайна реализовано 2 первых конечных процессов из 3;
<img width=800 align='center'> src="https://github.com/Lisstrange/benchmark/blob/main/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202021-09-21%20%D0%B2%2000.25.36.png" alt="bench">
