import requests
import  bs4
links=[]
job_title_=[]
company_name_=[]
company_location_=[]
jop_posted_=[]
#page 1
page = requests.get(f"https://wuzzuf.net/search/jobs/?a=spbg&q=python&start=0")
bs = bs4.BeautifulSoup(page.content, 'html.parser')
page_limit=int(bs.find("strong").get_text())
page_num=int(page_limit/15)
for j in range(page_num+1):
    page = requests.get(f"https://wuzzuf.net/search/jobs/?a=spbg&q=python&start={j}")
    bs = bs4.BeautifulSoup(page.content, 'html.parser')
    job_title1 = (bs.find_all("h2", {"class": "css-m604qf"}))
    for i in job_title1:
        job_title_.append(i.get_text())
    company_name1 = bs.find_all("a", {"class": "css-17s97q8"})
    for i in company_name1:
        company_name_.append(i.get_text())
    company_location1 = bs.find_all("span", {"class": "css-5wys0k"})
    for i in company_location1:
        company_location_.append(i.get_text())
    jop_posted = bs.find_all("div", {"class": "css-do6t5g"})
    jop_posted1 = bs.find_all("div", {"class": "css-4c4ojb"})
    for i in jop_posted:
        jop_posted_.append(i.get_text())
    for i in jop_posted1:
        jop_posted_.append(i.get_text())
    jop_title=bs.find_all("h2",{"class":"css-m604qf"})
    for i in range(len(jop_title)) :
     links.append("https://wuzzuf.net"+jop_title[i].find('a').get("href"))
for i in range(len(job_title_)):
    print("jop title : "+job_title_[i],"company name : "+company_name_[i] ,"company location : "+company_location_[i] ,"jop psted : "+jop_posted_[i] ,"link : "+links[i])



