# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
from datetime import date
import itertools

# TODO: Getting some duplicates in SQL database



H_list = []
S_list = []
U_list = []


class NoisenewsPipeline:

    def __init__(self):
        self.create_connection()


    def create_connection(self):
        self.conn = sqlite3.connect('articles.db')
        self.curr = self.conn.cursor()

    # def create_table(self):
    #     self.curr.execute("""create table articles_tb(
    #                     headline text,
    #                     subheading text,
    #                     url text,
    #                     date_detected real)""")

    def process_item(self, item, spider):

        global H_list, S_list, U_list

        def clean_list(list, item_key_values):
            if item_key_values not in list:
                list.append(item_key_values)
            elif item_key_values in list:
                pass

        clean_list(H_list, item["headline"])
        clean_list(S_list, item["subheading"])
        clean_list(U_list, item["url"])

        today = date.today()
        date_str = today.strftime("%d/%m/%Y")

        for (a, b, c) in itertools.zip_longest(H_list, S_list, U_list):
            self.curr.execute("""insert into articles_tb values (?,?,?,?)""",(
                a,
                b,
                c,
                date_str
            ))
            self.conn.commit()
            print("Hello, it's me you're looking for.")
            print(a)
