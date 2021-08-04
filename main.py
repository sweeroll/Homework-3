import json
from validate import validate_json
from models import GoodsTable, ShopsGoodsTable, db

with open('my_data.json', 'r', encoding='utf-8') as f:
    text: dict = json.load(f)
    validate_json(text)

with db:
    db.create_tables([GoodsTable, ShopsGoodsTable])
    if GoodsTable.get_or_none(GoodsTable.id == text['id']):
        (GoodsTable.update(name=text['name'], package_width=text['package_params']['width'],
                           package_height=text['package_params']['height']).where(
            GoodsTable.id == text['id']).execute())
    else:
        GoodsTable.create(id=text['id'], name=text['name'], package_width=text['package_params']['width'],
                          package_height=text['package_params']['height'])

    if ShopsGoodsTable.get_or_none(ShopsGoodsTable.good == text['id']):
        ShopsGoodsTable.delete().where(ShopsGoodsTable.good_id == text['id']).execute()
        for i in text['location_and_quantity']:
            ShopsGoodsTable.create(good=text['id'], location=i['location'],
                                   amount=i['amount'])
    else:
        for i in text['location_and_quantity']:
            ShopsGoodsTable.create(good=text['id'], location=i['location'],
                                   amount=i['amount'])
