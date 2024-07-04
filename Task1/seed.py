import sys
import codecs
import psycopg2
from faker import Faker # type: ignore
import random

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())


try:

    conn = psycopg2.connect(
        dbname="task1.1",
        user="postgres",
        password="Irinal371",
        host="localhost",
        port="5432"
    )
    print("Підключення до PostgreSQL успішно")

    cur = conn.cursor()

    fake = Faker()

    status_names = ['new', 'in progress', 'completed']
    for name in status_names:
        cur.execute("INSERT INTO status (name) VALUES (%s) ON CONFLICT DO NOTHING", (name,))

    for _ in range(10): 
        fullname = fake.name()
        email = fake.email()
        cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s) RETURNING id", (fullname, email))
        user_id = cur.fetchone()[0]

        for _ in range(random.randint(1, 5)): 
            title = fake.sentence(nb_words=6)
            description = fake.text()
            status_id = random.randint(1, len(status_names)) 
            cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                        (title, description, status_id, user_id))

    conn.commit()

except psycopg2.Error as e:
    print("Помилка при підключенні до PostgreSQL:", e)

finally:
    if 'conn' in locals() and conn is not None:
        cur.close()
        conn.close()
        print("Підключення до PostgreSQL закрито")