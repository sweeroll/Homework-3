# публичные тестовые случаи из текста условия задачи
PUBLIC_TEST_CASES = [
    {"test_input": {
        "id": 3,
        "name": "правильно",
        "package_params": {
            "width": 14,
            "height": 24
        },
        "location_and_quantity": [
            {
                "location": "мой дом",
                "amount": 1
            },
            {
                "location": "не мой дом",
                "amount": 17
            }
        ]
    }, "expected": True},
    {"test_input": {
        "name": "не правильно",
        "package_params": {
            "width": 14,
            "height": 24
        },
        "location_and_quantity": [
            {
                "location": "мой дом",
                "amount": 1
            },
            {
                "location": "не мой дом",
                "amount": 17
            }
        ]
    }, "expected": False}
]
