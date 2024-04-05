# Проверка параметра запроса через Query
#
# fastapi.Query — это класс, который используется для работы с параметрами запроса
# и проверки строк. Он позволяет определять параметры запроса, которые будут
# передаваться в URL, а также задавать для них ограничения на тип данных и значения.
#
# При использовании Query мы можем определять параметры запроса, задавать для них ограничения
# на тип данных и значения, а также указывать значения по умолчанию.

from fastapi import FastAPI, Query
app = FastAPI()
@app.get("/items/")
async def read_items(q: str = Query(None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Spam"}, {"item_id": "Eggs"}]}
    if q:
        results.update({"q": q})
    return results

# В этом примере мы создаем маршрут "/items/" с параметром запроса "q". Параметр
# "q" имеет тип str и может быть длиной от 3 до 50 символов. Если параметр "q" не
# передан в запросе, то ему будет присвоено значение None. Если же параметр "q"
# передан, то его значение будет добавлено к результатам запроса.