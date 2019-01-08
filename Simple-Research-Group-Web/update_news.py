###############7.17.2017 Lan Huang############
#   update news from news.txt                #
#   news.txt format:                         #
#        ID:int                              #
#        Title:string                        #
#        Time:string                         #
#        Data:string                         #
#  below is User Configuration Section       #
#number_of_latest_news_shown_in_homepage=int #
#website_foldername=string                   #
##############################################
number_of_latest_news_shown_in_homepage=2
website_foldername="public_html"
############################################
all_news_template="template/all_news.html"
latest_news_template="template/latest_news.html"
import os
all_news_location=os.path.join(os.getcwd(),website_foldername,all_news_template)
latest_news_location=os.path.join(os.getcwd(),website_foldername,latest_news_template)
news={}
newsfile=open("news.txt",'r')
firstline=newsfile.readline()
ID=firstline.split(":")[0]
if not ID=="ID":
    raise Exception("The format of news is not correct")
total_number_of_news=int(firstline.split(":")[1])
newsfile.seek(0)
for i in range(total_number_of_news):
    newsid=int(newsfile.readline().strip().split(":")[1])
    newstitle=newsfile.readline().strip().split(":")[1]
    newstime=newsfile.readline().strip().split(":")[1]
    newsdata=newsfile.readline().strip().split(":")[1]
    news[newsid]=(newstitle,newstime,newsdata)
newsfile.close()
all_news_file=open(all_news_location,'w')
for i in range(total_number_of_news):
    newsid=total_number_of_news-i
    newstitle,newstime,newsdata=news[newsid]
    all_news_file.write("<h4> %s </h4> \n" % (newstitle,) )
    all_news_file.write("<h5> %s </h5> \n" % (newstime,) )
    all_news_file.write("<p> %s </p> \n" % (newsdata,) )  
all_news_file.close()
latest_news_file=open(latest_news_location,'w')
for i in range(number_of_latest_news_shown_in_homepage):
    newsid=total_number_of_news-i
    newstitle,newstime,newsdata=news[newsid]
    latest_news_file.write("<h4> %s </h4> \n" % (newstitle,) )
    latest_news_file.write("<h5> %s </h5> \n" % (newstime,) )
    latest_news_file.write("<p> %s </p> \n" % (newsdata,) )
latest_news_file.close()
print("Done! Update News Successfully!!!")
input()
