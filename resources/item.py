#import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type = int,
        required = True,
        help = "Every item needs a store id!"
    )

    @jwt_required()
    def get(self, name): #read
        #for item in items:
            #if item['name'] == name:
                #return item
        #item = next(filter(lambda x: x['name'] == name, items), None)
        #return {'item':item}, 200 if item else 404 #404 - not found
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Item not found'}, 404

    def post(self, name): #CREATE
        #if next(filter(lambda x: x['name'] == name, items), None):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exist.".format(name)}, 400 #400 -bad request

        data = Item.parser.parse_args()
        #data = request.get_json()
        item = ItemModel(name, **data) #data['price'], data['store_id'])
        try:
            #items.append(item)
            item.save_to_db()
        except:
            return {"message":"An error occurred inserting the item."}, 500 #500 -internal server error

        return item.json(), 201 #201 -created

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message':"Item deleted."}
        #global items # this items is outer items variable
        #items = list(filter(lambda x: x['name'] != name, items))
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()

#        query = "DELETE FROM items WHERE name=?"
#        cursor.execute(query, (name,))

#        connection.commit()
#        connection.close()

#        return {'message':'Item deleted'}

    def put(self,name): #update
        data = Item.parser.parse_args()

        #data = request.get_json()
        #item = next(filter(lambda x: x['name'] == name, items), None)
        item = ItemModel.find_by_name(name)
#        update_item = ItemModel(name, data['price'])

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
#            try:
#                update_item.insert()
#            except:
#                return {"message": "An error occurred inserting the item"}, 500
        else:
            item.price = data['price']
#            try:
#                update_item.update()
#            except:
#                return {"message": "An error occurred updating the item"}, 500
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'item': list(map(lambda x: x.json(), ItemModel.query.all()))} #[item.json() for item in ItemModel.query.all()]}
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()

#        query = "SELECT * FROM items"
#        result = cursor.execute(query)
#        items = []
#        for row in result:
#            items.append({'name':row[0], 'price':row[1]})

#        connection.close()

#        return {'items':items}
