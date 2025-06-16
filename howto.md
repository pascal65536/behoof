Пошаговая инструкция по обновлению и публикации Python-пакета на TestPyPI и PyPI с учётом создания токенов и настройки `.pypirc`:

---

## Шаг 1. Обновите версию пакета и подготовьте исходники

- В файле `setup.py` или `pyproject.toml` увеличьте версию пакета (`version`).
- Проверьте, что все необходимые файлы (код, README, LICENSE) на месте.
- Удалите старые сборки, чтобы избежать конфликтов:

```bash
rm -rf build dist *.egg-info
```

- Соберите пакет заново:

```bash
python3 -m build
```

---

## Шаг 2. Создайте API-токены для TestPyPI и PyPI

- Войдите в аккаунт на https://test.pypi.org и https://pypi.org (аккаунты разные).
- Перейдите в **Account settings → API tokens**.
- Нажмите **Add API token**.
- Для теста создайте токен с областью действия «Entire account» или ограниченный вашим пакетом.
- Скопируйте токен сразу после создания — он показывается один раз.
- Повторите для PyPI.

---

## Шаг 3. Создайте и настройте файл `~/.pypirc`

Создайте файл `.pypirc` в домашней директории (`~/.pypirc`) со следующим содержимым:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-ваш_токен_от_TestPyPI

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-ваш_токен_от_PyPI
```

- Замените `pypi-ваш_токен_от_TestPyPI` и `pypi-ваш_токен_от_PyPI` на реальные токены.
- Установите права доступа к файлу для безопасности:

```bash
chmod 600 ~/.pypirc
```

---

## Шаг 4. Загрузите пакет на TestPyPI

- Проверьте пакет командой:

```bash
twine check dist/*
```

- Загрузите пакет:

```bash
twine upload --repository testpypi dist/*
```

- Убедитесь, что загрузка прошла успешно и пакет доступен по ссылке https://test.pypi.org/project/ваш_пакет/

---

## Шаг 5. Проверьте установку из TestPyPI

- Создайте виртуальное окружение и активируйте его.
- Установите пакет из TestPyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ ваш_пакет==версия
```

- Проверьте импорт и работу пакета.

---

## Шаг 6. Загрузите пакет на PyPI

- После успешной проверки загрузите пакет на основной PyPI:

```bash
twine upload dist/*
```

- Пакет станет доступен по адресу https://pypi.org/project/ваш_пакет/

---

## Итог

| Шаг           | Команда/Действие                                   |
|---------------|---------------------------------------------------|
| Обновить версию и собрать пакет | `rm -rf build dist *.egg-info``python3 -m build` |
| Создать API-токены | Через настройки аккаунта на PyPI и TestPyPI |
| Настроить `.pypirc` | Создать файл с токенами и правами доступа 600 |
| Проверить пакет | `twine check dist/*`                              |
| Загрузить на TestPyPI | `twine upload --repository testpypi dist/*`  |
| Проверить установку | `pip install --index-url https://test.pypi.org/simple/ пакет` |
| Загрузить на PyPI | `twine upload dist/*`                            |

---

[1] https://test.pypi.org/manage/account/

[2] https://guidebook.devops.uis.cam.ac.uk/howtos/python/pypi/

[3] https://packaging.python.org/guides/using-testpypi/

[4] https://pypi.org/help/

[5] https://www.pyopensci.org/python-package-guide/tutorials/publish-pypi.html

[6] https://kynan.github.io/blog/2020/05/23/how-to-upload-your-package-to-the-python-package-index-pypi-test-server

[7] https://stackoverflow.com/questions/62532237/how-can-i-create-an-api-token-on-pypi-for-a-new-project

[8] https://pydevtools.com/handbook/tutorial/publishing-your-first-python-package-to-pypi/
