# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class AmazonpracticePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(host="127.0.0.1"
            ,port = 3307,
            user = "test",
            password = "12345678",
            database="quotesdb"   
        )

        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute(""" DROP TABLE IF EXISTS books""")
        self.cursor.execute(""" create table books (
                                name text,
                                author text,
                                price INT,
                                imageUrl text,
                                id INT NOT NULL AUTO_INCREMENT,

                                PRIMARY KEY ( id )
                            )""")

    def store_db(self, item):
        print("here")
        self.cursor.execute("""
            insert into books (name, author, price, imageUrl) 
                values (%s, %s, %s, %s)
        """, (
            item["prodcut_name"],
            item["prodcut_author"],
            item["prodcut_price"],
            item["prodcut_imageUrl"],
        ))

        self.conn.commit()

        
    def process_item(self, item, spider):
        self.store_db(item)
        return item



