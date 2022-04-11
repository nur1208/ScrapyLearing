# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class PostscrapePipeline:

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
        self.cursor.execute(""" DROP TABLE IF EXISTS quotes""")
        self.cursor.execute(""" create table quotes (
                                title text,
                                author text,
                                tag text
                            )""")

    def store_db(self, item):
        print("here")
        self.cursor.execute("""
            insert into quotes values (%s, %s, %s)
        """, (
            item["title"],
            item["author"],
            item["tag"][0]
        ))

        self.conn.commit()

        
    def process_item(self, item, spider):
        print("pipline:", item["title"])
        self.store_db(item)
        return item
