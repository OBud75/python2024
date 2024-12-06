from sqlite3 import connect


class Model:
    con = connect("db.sqlite3")
    cur = con.cursor()


class Asset(Model):
    @classmethod
    def create_table(cls):
        cls.cur.execute(f"""
            DROP TABLE if exists {cls.__name__}
        """)

        cls.cur.execute(f"""
            CREATE table {cls.__name__}
            (url, name, title)
        """)

    @classmethod
    def create(cls, url, name, title):
        instance = cls()
        instance.url = url
        instance.name = name
        instance.title = title
        return instance

    @classmethod
    def get_by_name(cls, name):
        cls.cur.execute(f"""
            SELECT * from {cls.__name__}
            WHERE name='{name}'
        """)
        return cls.create(*cls.cur.fetchone())

    @classmethod
    def all(cls):
        cls.cur.execute(f"SELECT * from {cls.__name__}")
        return cls.cur.fetchall()

    def save(self):
        self.cur.execute(f"""
            INSERT INTO {self.__class__.__name__}
            VALUES (
                    '{self.url}',
                    '{self.name}',
                    '{self.title}'
                )
        """)
        self.con.commit()
