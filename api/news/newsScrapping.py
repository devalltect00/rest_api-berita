import json
import requests
from bs4 import BeautifulSoup
from enum import Enum
from werkzeug.exceptions import InternalServerError
import os

project_root = os.path.dirname(os.path.abspath(__file__))

# INGREDIENTS = "source,link.json"
# INGREDIENTS = os.path.join(project_root, 'api', 'news', 'source,link.json')
INGREDIENTS = os.path.join(project_root, 'source,link.json')
# INGREDIENTS = "api\\news\\source,link.json"

# class AvailableNewsId(Enum):
class AvailableNews(Enum):
    CNN_INDONESIA = 1
    MERDEKA = 5
    SUARA = 6
    DETIK = 11
    KOMPAS = 12
    PIKIRAN_RAKYAT = 14
    OKEZONE = 15

availableNews = {
    "cnn-indonesia" : 1,
    "merdeka" : 5,
    "suara" : 6,
    "detik" : 11,
    "kompas" : 12,
    "pikiran-rakyat" : 14,
    "okezone" : 15
}

class SourceNews:
    def __init__(self):
        with open(INGREDIENTS) as ingredients:
            self.source = json.load(ingredients)["source"]

    def getAvailableNewsSource(self):
        try:
            listNews = []
            for sourceNews, id in availableNews.items():
                name = self.source[id-1]["name"]
                link = self.source[id-1]["link"][0]
                listNews.append({
                    "name":name,
                    "link":link
                })

            return listNews
        except:
            raise InternalServerError("Conflit when trying get avalibale news source")

class NewsChannel(SourceNews):
    def __init__(self, id):
        # super.__init__(self)
        super().__init__()
        self.id = id
        self.source = self.source[id-1]
        self.name = self.source["name"]

    def getContent(self, numberOfContent=None):
        #setup
        self.page = requests.get(self.source["link"][0])
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

        groupEach = self.source["page"]["groupEach"][0]
        tag_ = groupEach["tag"]
        class_ = groupEach["class"]
        if tag_ and class_:
            groupNews = self.soup.find(tag_, class_ = class_)
        elif tag_:
            groupNews = self.soup.find(tag_)
        elif class_:
            groupNews = self.soup.find(class_ = class_)
        else:
            groupNews = None

        # return groupNews

        each = self.source["page"]["each"][1]
        tag_ = each["tag"]
        class_ = each["class"]
        if tag_ and class_:
            if "<>" in class_:
                class_ = class_.replace("<>","")
                groupEachNews = groupNews.find_all(tag_, class_ = lambda c: c and c.startswith(class_))
            else:
                groupEachNews = groupNews.find_all(tag_, class_ = class_)
        elif tag_:
            groupEachNews = groupNews.find_all(tag_)
        elif class_:
            if "<>" in class_:
                class_ = class_.replace("<>","")
                groupEachNews = groupNews.find_all(class_ = lambda c: c and c.startswith(class_))
            else:
                groupEachNews = groupNews.find_all(class_ = class_)
        else:
            groupEachNews = None

        if groupEachNews:
            news_data = []
            if numberOfContent:
                groupNews = groupEachNews[1:1+numberOfContent]
            groupNews = groupEachNews

            for news in groupNews:

                content = self.source["page"]["content"][0]

                title_ = self.getDataContent(content["title"], news)
                tumbnail_link_ = self.getDataContent(content["tumbnail_link"], news)
                content_link_ = self.getDataContent(content["content_link"], news)
                channel_name_ = self.getDataContent(content["channel_name"], news)
                date_ = self.getDataContent(content["date"], news)
                id_ = self.getDataContent(content["id"], news)
                channel_ = self.getDataContent(content["channel"], news)

                new_data = {
                    "title" : title_,
                    "tumbnail_link" : tumbnail_link_,
                    "content_link" : content_link_,
                    "channel_name" : channel_name_,
                    "date" : date_,
                    "id" : id_,
                    "channel" : channel_
                }

                news_data.append(new_data)

            return {
                "news_source" : self.name,
                "news_total" : len(news_data),
                "news_data" :news_data
                }
        return None
    
    def findTag_content(self, type="content"):
        if self.source:
            if type == "content":
                contentSource = self.source["page"]["groupEach"][0]
                tag_ = contentSource["tag"]
                class_ = contentSource["class"]
                if self.soup:
                    if tag_ and class_:
                        contentData = self.soup.find(tag_, class_ = class_)
                    elif tag_:
                        contentData = self.soup.find(tag_)
                    elif class_:
                        contentData = self.soup.find(class_ = class_)
                    elif onEachValue_:
                            contentNews = news
                    else:
                        None
                else:
                    raise("content.soup not found")
            if type == "content":
                contentSource = self.source["page"]["content"][0]
                title_ = contentSource["title"]
        else:
            raise("content.source not found")
        
    def getDataContent(self, contentSource, content):
        tag_ = contentSource["tag"]
        class_ = contentSource["class"]
        onEachValue_ = contentSource["onEachValue"]
        if self.soup:
            if tag_ and class_:
                contentData = content.find(tag_, class_ = class_)
            elif tag_:
                contentData = content.find(tag_)
            elif class_:
                contentData = content.find(class_ = class_)
            elif onEachValue_:
                # contentData = content
                try:
                    contentData = content[onEachValue_]
                except:
                    raise("onEachValue_ =>" + onEachValue_)
                # contentData = content
            else:
                None
            return contentData

        return None
        
        
        
class News():
    def __init__(self, id, title, typeNews):
        self.id = id
        self.title = title
        self.typeNews = typeNews

if __name__ == '__main__':
    # INGREDIENTS = "source,link.json"
    cnn = NewsChannel(15)
    # cnn = NewsChannel(15, INGREDIENTS)
    # print(cnn.ingredients)
    print(cnn.source)
    print()
    # cnn.getContent()
    content = cnn.getContent()
    # content = cnn.getContent(numberOfContent=2)
    # content = cnn.getContent(numberOfContent=2)
    # content = cnn.getContent(numberOfContent=5)
    # content = cnn.getContent(numberOfContent=1)
    print(content)
    print()
    print("\nlen\n")
    if content:
        print(len(content))

    # print(type(cnn.getContent()))

    # output = NewsChannel(availableNews[newsSource_id])
    # output = NewsChannel(availableNews[cnn-indonesia])
    # output = NewsChannel(availableNews["cnn-indonesia"])
    # print("\n--------------\n")
    # print(output)
    # print()
    # print(type(output))
    # print()
    # print(output.getContent())
    # print()
    # print(type(output.getContent()))

    source = SourceNews()
    print(source.getAvailableNewsSource())