import json
import requests
from bs4 import BeautifulSoup
from enum import Enum

# INGREDIENTS = "source,link.json"
INGREDIENTS = "api\\news\\source,link.json"

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


class NewsChannel:
    # def __init__(self, id, INGREDIENTS):
    def __init__(self, id):
        self.id = id
        # INGREDIENTS = "source,link.json"
        with open(INGREDIENTS) as ingredients:
            self.source = json.load(ingredients)["source"][id-1]
    
    # def getContent(self, numberOfContent=10):
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
        # if "{}" in each:
        #     each
        tag_ = each["tag"]
        class_ = each["class"]
        if tag_ and class_:
            if "<>" in class_:
                class_ = class_.replace("<>","")
                # print("\n----\n"+class_+"\n----\n")
                groupEachNews = groupNews.find_all(tag_, class_ = lambda c: c and c.startswith(class_))
            else:
                groupEachNews = groupNews.find_all(tag_, class_ = class_)
        elif tag_:
            groupEachNews = groupNews.find_all(tag_)
        elif class_:
            if "<>" in class_:
                class_ = class_.replace("<>","")
                # print("\n----\n"+class_+"\n----\n")
                groupEachNews = groupNews.find_all(class_ = lambda c: c and c.startswith(class_))
            else:
                groupEachNews = groupNews.find_all(class_ = class_)
        else:
            groupEachNews = None
        
        # return groupEachNews

        # if groupNews:
        if groupEachNews:
            # self.each = self.source["page"]["each"][0]
            # tag_ = self.each["tag"]
            # class_ = self.each["class"]
            # if tag_ and class_:
            #     each = self.soup.find(tag_, class_ = class_)
            # elif tag_:
            #     each = self.soup.find(tag_)
            # elif class_:
            #     each = self.soup.find(class_ = class_)
            # else:
            #     each = None

            # top 5 news (from top)
            # print(type(groupNews[0:11]))
            # return groupNews[0:11]
            # print(type(groupNews[0:11]))
            # print()
            # groupNews_ = json.dumps(groupNews[0:11])
            # print(type(groupNews_))
            # print()
            
            # return groupNews_
            # print(groupNews[0:11])
            # print(type(groupNews[0:11]))
            # return json.dumps({"news" : groupNews[0:11]})
            # return json.dumps(groupNews[0:11])
            # for news in groupNews[0:11]:
            #     news_data = {

            #     }
            # return None
            # return groupNews[0:11]
            # return str(groupNews[0:11])

            

            news_data = []

            if numberOfContent:
                groupNews = groupEachNews[1:1+numberOfContent]
            groupNews = groupEachNews

            # for news in groupEachNews[1:1+numberOfContent]:
            for news in groupNews:

                content = self.source["page"]["content"][0]
                # tag_ = content["tag"]
                # class_ = content["class"]
                # onEachValue_ = content["onEachValue"]
                # if tag_ and onEachValue_:
                #     contentNews = news.find(tag_, onEachValue_ = onEachValue_)
                # elif tag_:
                #     contentNews = news.find(tag_)
                # elif onEachValue_:
                #     contentNews = news.find(class_ = onEachValue_)
                # elif onEachValue_:
                #     contentNews = news
                # else:
                #     None
                

                # # a = news.find('a', class_='ga-Breaking1')
                # a = news.find('a')
                # title = a['title']
                # div = news.find(class_='right-img-headline')
                # scope = div['title']

                # # start_index = div.find("url(") + len("url(")
                # # start_index = div.find("url(")
                # style = div["style"]
                
                # # end_index = div.find(")", start_index)
                # # url_string = div[start_index:end_index]

                # # Find the start and end index of the URL within the parentheses
                # start_index = style.find("url(") + len("url(")
                # end_index = style.find(")", start_index)

                # # Extract the URL string
                # url_string = style[start_index:end_index]

                # tumbnail = url_string
                # # content = "a.get('href')"
                # content = a.get('href')

                # if onEachValue_:
                    # title = contentNews[content]

                # news = news.find('div')

                title_ = self.getDataContent(content["title"], news)
                tumbnail_link_ = self.getDataContent(content["tumbnail_link"], news)
                content_link_ = self.getDataContent(content["content_link"], news)
                channel_name_ = self.getDataContent(content["channel_name"], news)
                date_ = self.getDataContent(content["date"], news)
                id_ = self.getDataContent(content["id"], news)
                channel_ = self.getDataContent(content["channel"], news)

                # new_data = {
                #     "title" : title,
                #     "scope" : scope,
                #     "tumbnail" : tumbnail,
                #     "content" : content
                # }

                new_data = {
                    "title" : title_,
                    "tumbnail_link" : tumbnail_link_,
                    "content_link" : content_link_,
                    "channel_name" : channel_name_,
                    "date" : date_,
                    "id" : id_,
                    "channel" : channel_
                }

                # news_data.append(new_data)
                news_data.append(new_data)

                

                # self.each = self.source["page"]["each"][0]
                # tag_ = self.each["tag"]
                # class_ = self.each["class"]
                # if tag_ and class_:
                #     each = news.find(tag_, class_ = class_)
                # elif tag_:
                #     each = news.find(tag_)
                # elif class_:
                #     each = news.find(class_ = class_)
                # else:
                #     each = None
                # news_data.append(each)
                # pass
                # return news
            # return groupNews[0:11]
            # return news_data
            # return news_data
            return json.dumps({
                "news_source" : self.source["name"],
                "news_total" : len(news_data),
                "news_data" :news_data
                })
            # return groupEachNews
        # return groupNews
        # return groupEachNews
            # return (len(groupNews))
        
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

            # if onEachValue_:
            #     contentData = contentData.find(tag_)

            # if onEachValue_:
            #     contentData = contentData[onEachValue_]

            return contentData
        # else:
        #     raise("content.soup not found")

        return none
        
        
        
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