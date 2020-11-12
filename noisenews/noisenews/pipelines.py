# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

# TODO: Getting some unwanted line breaks between URLs and webpage sections



H_list = []
S_list = []
U_list = []


class NoisenewsPipeline:

    # def __init__(self):
    #     self.create_connection()


    # def create_connection(self):
    #     self.conn = sqlite3.connect('articles.db')
    #     self.curr = self.conn.cursor()

    # def create_table(self):
    #     self.curr.execute("""create table articles_tb(
    #                     headline text,
    #                     subheading text,
    #                     url text,
    #                     date_detected real)""")

    def process_item(self, item, spider):

        global H_list, S_list, U_list

        file1 = open("publish.txt", "a")

        def clean_list(list, item_key):
            if item_key not in list:
                list.append(item_key)
                file1.write(item_key)
                file1.write("\n")
            elif item_key in list:
                pass

        clean_list(H_list, item["headline"])
        clean_list(S_list, item["subheading"])
        clean_list(U_list, item["url"])
        file1.write("\n")
        file1.close()

        print("Pipeline: " + item["headline"])
        return item
