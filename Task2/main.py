import sys
import codecs
from pymongo import MongoClient
from bson.objectid import ObjectId
import pymongo

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

try:
    client = MongoClient('mongodb+srv://imamchur56:Irinal371@irynam.2ck4sxx.mongodb.net/test?retryWrites=true&w=majority')
    db = client['cat_database']
    collection = db['cats']

    # Функції CRUD

    # Створення (Create)
    def create_cat(name, age, features):
        cat = {
            "name": name,
            "age": age,
            "features": features
        }
        result = collection.insert_one(cat)
        print(f"Кота створено з id: {result.inserted_id}")

    # Читання (Read)
    def read_all_cats():
        cats = collection.find()
        for cat in cats:
            print(cat)

    def read_cat_by_name(name):
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print(f"Кота з ім'ям {name} не знайдено.")

    # Оновлення (Update)
    def update_cat_age(name, new_age):
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.matched_count > 0:
            print(f"Вік кота з ім'ям {name} оновлено до {new_age}.")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")

    def add_feature_to_cat(name, new_feature):
        result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
        if result.matched_count > 0:
            print(f"Коту з ім'ям {name} додано характеристику: {new_feature}.")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")

    # Видалення (Delete)
    def delete_cat_by_name(name):
        result = collection.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Кота з ім'ям {name} видалено.")
        else:
            print(f"Кота з ім'ям {name} не знайдено.")

    def delete_all_cats():
        result = collection.delete_many({})
        print(f"Видалено {result.deleted_count} котів.")

    # Приклад використання функцій
    if __name__ == "__main__":
        create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
        read_all_cats()
        read_cat_by_name("Barsik")
        update_cat_age("Barsik", 5)
        add_feature_to_cat("Barsik", "любить гратися з м'ячиком")
        delete_cat_by_name("Barsik")
        delete_all_cats()

except pymongo.errors.ConnectionError as e:
    print(f"Помилка підключення до MongoDB: {e}")



# Приклад використання функцій
if __name__ == "__main__":
    create_cat("Barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    read_all_cats()
    read_cat_by_name("Barsik")
    update_cat_age("Barsik", 5)
    add_feature_to_cat("Barsik", "любит гратися з м'ячиком")
    delete_cat_by_name("Barsik")
    delete_all_cats()
    pass