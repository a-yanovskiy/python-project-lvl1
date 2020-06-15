# python-project-lvl1

Добрый день уважаемый ментор. Отправляю свой первый проект на проверку, зная, что в нем огромная куча ошибок, среди замеченных мною:
- неполная аксинема (не показывает неверное завершение ни одной из игр);
- неверные имена функций (их нужно именовать глаголами, а у меня существительные);
- не заполнены необходимые поля в pyproject.toml;

Причина этого безобразия заключается в том, что при после попытки переименования функций согласно рекомендациям стали возникать ошибки poetry:

[TypeError]
__init__() missing 1 required positional argument: 'char'

Причем, как при вызове любой из игр, так и при вызове команд типа poetry config.
Попытки решить проблему свелись к обсуждению в слаке "как заставить peotry вывести трейсбек".
Команда poetry -vvv run brain-calc (к примеру calc), вместо вывода трейсбека вывело список команд poetry.
Мне не у кого спросить совета по данному поводу и я решил отправить проект на проверку чтобы дело хоть немного сдвинулось с мертвой точки.
Фактически, я не выполнил последний шаг (Проверка) проекта. Версия моего проекта тут - недоработанная, но рабочая.
Прошу какую-нибудь наводку для решения проблемы. Готов исправлять все ошибки.
Благодарю за понимание.

[![Build Status](https://travis-ci.com/a-yanovskiy/python-project-lvl1.svg?branch=master)](https://travis-ci.com/a-yanovskiy/python-project-lvl1)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
<a href="https://codeclimate.com/github/codeclimate/codeclimate/maintainability"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" /></a>
<a href="https://codeclimate.com/github/codeclimate/codeclimate/test_coverage"><img src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/test_coverage" /></a>

## Brain-games
[![asciicast](https://asciinema.org/a/rlxZ1MjevLY0gSsuOQEiotwBs.svg)](https://asciinema.org/a/rlxZ1MjevLY0gSsuOQEiotwBs)
