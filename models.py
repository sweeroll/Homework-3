from peewee import SqliteDatabase, Model, IntegerField, CharField, PrimaryKeyField, ForeignKeyField

# SET DataBase
db = SqliteDatabase('db.sqlite')


class BaseModel(Model):
    """Задаем бозовый класс."""

    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'
        null = True


class GoodsTable(BaseModel):
    """Класс для таблицы G."""

    name = CharField()
    package_height = IntegerField()
    package_width = IntegerField()

    class Meta:
        db_table = 'G'


class ShopsGoodsTable(BaseModel):
    """Класс для таблицы S."""

    good = ForeignKeyField(GoodsTable)
    location = CharField()
    amount = IntegerField()

    class Meta:
        db_table = 'S'
