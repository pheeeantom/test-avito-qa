0) Если не установлен питон 3 версии - устанавливаем, переходим в папку с проектом
1) Устанавливаем playwright: python3 -m venv venv
    pip install pytest-playwright
2) Затем обновляем: playwright install
3) Запускаем тесты: pytest