# Звіт до першої лабораторної
## Тема: перша програма на мові *Python*

### Виконання роботи
- Результати виконання завдання:
    1. Виконали першу програму, результат виконання: ![alt](img1.png);
    1. Модифікували програму та використали [Python Notebook для її виконання](lab1.ipynb);
    
    
    
    1. Програма вивела значення
    1. Отримано наступні результати Олег started learning Python on 2024-11-05 22:32:57. Kyiv is a wonderful place!
    1. Навчились прості програми на мові Python



___


```Python
from datetime import datetime

name = "Олег"
location = "Kyiv"
activity = "learning Python"

print(f"{name} started {activity} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}. {location} is a wonderful place!")

```
