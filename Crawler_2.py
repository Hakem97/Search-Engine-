#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Required Libraries
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# In[2]:


# leed Univerty link
response=requests.get('https://eps.leeds.ac.uk/computing/stafflist')
soup = BeautifulSoup(response.text, 'html.parser')


# In[3]:


#get the link and clean it
for link in soup:
    urls = [item.get("href") for item in soup.find_all("a")]
    url_final = [x for x in urls if not x.startswith('//')]
    url_final1 = [x for x in url_final if not x.startswith('#')]
    url_final = [x for x in url_final1 if not x.startswith('mailto')]


# In[ ]:


url_final


# In[535]:


#All the staff links in leeds uni
urls = ['https://eps.leeds.ac.uk/staff/115/dr-andy-bulpitt',
 'https://eps.leeds.ac.uk/staff/76/professor-anthony-g-cohn-freng-ceng-citp',
 'https://eps.leeds.ac.uk/staff/189/dr-mark-walkley',
 'https://eps.leeds.ac.uk/staff/446/mrs-gaynor-butterwick',
 'https://eps.leeds.ac.uk/computing/staff/810/dr-isolde-adler',
 'https://eps.leeds.ac.uk/computing/staff/8077/dr-kareem-al-ammari',
 'https://eps.leeds.ac.uk/computing/staff/8245/mark-allen',
 'https://eps.leeds.ac.uk/computing/staff/635/dr-mohammad-ammar-alsalka',
 'https://eps.leeds.ac.uk/computing/staff/33/professor-eric-atwell',
 'https://eps.leeds.ac.uk/computing/staff/121/dr-brandon-bennett',
 'https://eps.leeds.ac.uk/computing/staff/523/dr-peter-bollada',
 'https://eps.leeds.ac.uk/computing/staff/686/ruksana-bukhari-bibi',
 'https://eps.leeds.ac.uk/computing/staff/115/dr-andy-bulpitt',
 'https://eps.leeds.ac.uk/computing/staff/446/mrs-gaynor-butterwick',
 'https://eps.leeds.ac.uk/computing/staff/499/dr-hamish-carr',
 'https://eps.leeds.ac.uk/computing/staff/285/dr-natasha-shakhlevich',
 'https://eps.leeds.ac.uk/computing/staff/301/professor-netta-cohen',
 'https://eps.leeds.ac.uk/computing/staff/76/professor-anthony-g-cohn-freng-ceng-citp',
 'https://eps.leeds.ac.uk/faculty-engineering-physical-sciences/staff/1272/dr-robert-j-cooper',
 'https://eps.leeds.ac.uk/computing/staff/390/dr-marc-de-kamps',
 'https://eps.leeds.ac.uk/computing/staff/8419/sara',
 'https://eps.leeds.ac.uk/computing/staff/184/professor-vania-dimitrova',
 'https://eps.leeds.ac.uk/computing/staff/187/professor-karim-djemame',
 'https://eps.leeds.ac.uk/computing/staff/743/dr-mehmet-dogar',
 'https://eps.leeds.ac.uk/computing/staff/182/jill-duggleby',
 'https://eps.leeds.ac.uk/computing/staff/334/professor-david-duke',
 'https://eps.leeds.ac.uk/computing/staff/52/professor-martin-dyer',
 'https://eps.leeds.ac.uk/computing/staff/92/dr-nick-efford',
 'https://eps.leeds.ac.uk/computing/staff/1379/dr-mai-elshehaly',
 'https://eps.leeds.ac.uk/computing/staff/1337/dr-luis-figueredo',
 'https://eps.leeds.ac.uk/computing/staff/321/charlotte-francis',
 'https://eps.leeds.ac.uk/computing/staff/1535/professor-alejandro-f-frangi',
 'https://eps.leeds.ac.uk/computing/staff/1837/shokoufeh-golshani',
 'https://eps.leeds.ac.uk/computing/staff/6739/mrs-ellen-goodison',
 'https://eps.leeds.ac.uk/computing/staff/1670/dr-ali-gooya',
 'https://eps.leeds.ac.uk/computing/staff/332/anne-hayler',
 'https://eps.leeds.ac.uk/computing/staff/542/dr-david-head',
 'https://eps.leeds.ac.uk/faculty-engineering-physical-sciences/staff/8274/pd-dr-marc-hellmuth',
 'https://eps.leeds.ac.uk/computing/staff/283/beth-hilditch',
 'https://eps.leeds.ac.uk/computing/staff/84/professor-david-hogg',
 'https://eps.leeds.ac.uk/computing/staff/8178/dr-yanlong-huang',
 'https://eps.leeds.ac.uk/computing/staff/82/professor-peter-jimack',
 'https://eps.leeds.ac.uk/computing/staff/259/owen-johnson',
 'https://eps.leeds.ac.uk/computing/staff/1545/dr-tom-kelly',
 'https://eps.leeds.ac.uk/computing/staff/37/professor-raymond-kwan',
 'https://eps.leeds.ac.uk/computing/staff/1542/dr-toni-lassila',
 'https://eps.leeds.ac.uk/computing/staff/44/dr-lydia-lau',
 'https://eps.leeds.ac.uk/computing/staff/1509/joanna-leng',
 'https://eps.leeds.ac.uk/computing/staff/771/dr-matteo-leonetti',
 'https://eps.leeds.ac.uk/computing/staff/172/derek-magee',
 'https://eps.leeds.ac.uk/computing/staff/1736/ciaran-mcinerney',
 'https://eps.leeds.ac.uk/computing/staff/241/dr-haiko-muller',
 'https://eps.leeds.ac.uk/computing/staff/6446/dr-evangelos-pournaras',
 'https://eps.leeds.ac.uk/computing/staff/643/dr-thomas-ranner',
 'https://eps.leeds.ac.uk/computing/staff/1846/dr-nishant-ravikumar',
 'https://eps.leeds.ac.uk/computing/staff/257/professor-roy-ruddle',
 'https://eps.leeds.ac.uk/computing/staff/6780/dr-ali-sarrami-foroushani',
 'https://eps.leeds.ac.uk/computing/staff/621/claire-savy',
 'https://eps.leeds.ac.uk/computing/staff/8314/dr-shuang-song',
 'https://eps.leeds.ac.uk/computing/staff/258/dr-john-stell',
 'https://eps.leeds.ac.uk/computing/staff/249/professor-kristina-vuskovic',
 'https://eps.leeds.ac.uk/computing/staff/189/dr-mark-walkley',
 'https://eps.leeds.ac.uk/computing/staff/868/dr-he-wang',
 'https://eps.leeds.ac.uk/faculty-engineering-physical-sciences/staff/1600/dr-yongxing-wang',
 'https://eps.leeds.ac.uk/computing/staff/6452/dr-zheng-wang',
 'https://eps.leeds.ac.uk/computing/staff/760/dr-lijun-wei',
 'https://eps.leeds.ac.uk/computing/staff/573/dr-samuel-wilson',
 'https://eps.leeds.ac.uk/computing/staff/8269/dr-xia',
 'https://eps.leeds.ac.uk/computing/staff/331/professor-jie-xu',
 'https://eps.leeds.ac.uk/computing/staff/8199/dr-arezoo-zakeri']
#scrape elements


# In[ ]:


#Get the requuired information of from the crawled urls:
for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        name= soup.find("h1", class_= "heading-underline").get_text()
        try:
            research = soup.find(string=re.compile("Position")).findNext().get_text().replace('\n', '')
        except:
            pass
        try:
            school=soup.find(class_="local-header-title").get_text().replace('\n', '')
        except:
            pass
        data={'name': name,
         'research': research,
         'school':school,
         'url':url}  
        print(data)
        raw_data=print(data)
        df=pd.DataFrame(raw_data, columns = ['name', 'research', 'school'])
        df.to_csv('Dataset.csv', index = False)


# In[537]:


# Durham Univerty link
response=requests.get('https://www.dur.ac.uk/research/directory/view/?mode=department&id=4')


# In[538]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[539]:


#get the link and clean it
for link in soup:
    urls = [item.get("href") for item in soup.find_all("a")]


# In[ ]:


urls


# In[565]:


#All the staff links in Durham uni
durham_urls=['https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=246',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18445',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=14675',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17774',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=3328',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=106',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=11955',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=2826',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17167',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=12236',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=2378',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=1163',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=10305',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18580',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=4507',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=2387',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17133',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=2381',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=4509',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18350',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=15258',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=9703',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17243',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=115',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=10591',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=2380',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=8278',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18349',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=1151',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18474',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18378',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=12329',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=13966',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17022',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17157',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16066',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16471',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19395',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18003',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19162',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19394',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16722',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18307',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18604',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19131',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19139',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=2463',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=1968',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=6327',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=12792',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=4426',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=1159',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19199',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=1397',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=1620',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18231',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17804',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16845',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18276',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=14677',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17805',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18277',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=15991',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16918',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17823',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17806',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=14756',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17807',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=15773',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17808',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=14938',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17809',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17810',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18951',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=12702',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19054',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=15775',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19050',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17824',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17544',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16542',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17811',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19053',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17813',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19055',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18628',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18222',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=13969',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19056',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19405',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=15303',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=15427',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19057',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16662',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=14478',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17814',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16355',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19058',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17815',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17816',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19061',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19052',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19059',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17817',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=17818',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=6326',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18275',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=18278',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=16544',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19060',
 'https://www.dur.ac.uk/research/directory/staff/?mode=staff&id=19406',]


# In[ ]:


for url in durham_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        name= soup.find("h2").get_text()
        try:
            research = soup.find(string=re.compile("Research Interests")).findNext().get_text().replace('\n', '')
        except:
            pass
        school="Department of Computer Science"
        data={'name': name,
         'research': research,
         'school':school,
        'url':url}  
        raw_data=print(data)
        df=pd.DataFrame(raw_data, columns = ['name', 'research', 'school'])
        df.to_csv('Dataset.csv', index = False)


# In[446]:


# Durham Univerty link
response=requests.get('https://www.lboro.ac.uk/departments/compsci/staff/')


# In[447]:


soup = BeautifulSoup(response.text, 'html.parser')


# In[448]:


#get the link and clean it
for link in soup:
    urls = [item.get("href") for item in soup.find_all("a")]


# In[ ]:


urls


# In[1264]:


lob_urls=['https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/daniel-reidenbach/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/asma-adnane/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/james-l-alty/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/firat-batmaz/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/bellpaul/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/helmut-bez/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/caihaibin/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/tao-chen/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/paul-chung/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/john-connolly/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/john-cooke/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/georgina-cosma/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/christian-dawson/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/ray-dawson/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/joel-day/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/parisa-derakhshan/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/eran-edirisinghe/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/hui-fang/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/shaheen-fatima/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/dominik-freydenberger/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/alastair-gale/',
 'https://www.lboro.ac.uk/departments/compsci/staff/research-support/charlotte-greasley/',
 'https://www.lboro.ac.uk/departments/compsci/staff/research-support/yualin-gu/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/lin-guan/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/lianghao-han/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/chris-hinde/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/hussakwalter/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/roger-knott/',
 'https://www.lboro.ac.uk/departments/compsci/staff/research-support/pawel-ladosz/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/baihua-li/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/russell-lock/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/colin-machin/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/qinggang-meng/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/robert-mercas/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/lars-nagel/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/hossein-nevisi/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/iain-phillips/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/tsoposco/',
 'https://www.lboro.ac.uk/departments/compsci/staff/research-support/shreedhar-rangappa/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/daniel-reidenbach/',
 'https://www.lboro.ac.uk/departments/compsci/staff/research-support/mohamad-saada/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/gerald-schaefer/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/andré-schappo/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/andrea-soltoggio/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/roger-stone/',
 'https://www.lboro.ac.uk/departments/compsci/staff/research-support/gary-storey/',
 'https://www.lboro.ac.uk/departments/compsci/staff/research-support/diana-streeton/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/ana-salagean/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/amitabh-trehan/',
 'https://www.lboro.ac.uk/departments/compsci/staff/emeriti-visitors/shuang-hua-yang/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/yanning-yang/',
 'https://www.lboro.ac.uk/departments/compsci/staff/academic-teaching/waad-yousif/',]


# In[ ]:


for url in lob_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        name= soup.find("h3",class_="fcbg2").get_text()
        try:
            research = soup.find('div',id="tab2",class_="tab_content").get_text().replace('\r\n', '').replace('\n', '').replace('\xa0','')
        except:
            pass
        school="Department of Computer Science"
        data={'name': name,
         'research': research,
         'school':school,
        'url':url}  
        raw_data=print(data)
        df=pd.DataFrame(raw_data, columns = ['name', 'research', 'school'])
        df.to_csv('Dataset.csv', index = False)


# In[545]:


df=pd.read_csv('workspace/SE_Database.csv', encoding='latin-1')
def make_clickable(val):
    return '<a href="{}">{}</a>'.format(val, val)

df.style.format({'Link': make_clickable})


# In[546]:


df = df.drop_duplicates(subset='Name', keep='first')
df=df[~df.Research.str.contains("Email", na=True)]
df=df[~df.Research.str.contains("nan", na=True)]


# In[547]:


from nltk.corpus import stopwords
# clean the Research column for easy retrieval.
df.Research = df.Research.str.lower()
df.Research = df.Research.str.replace('[^A-z ]','').str.replace(' +',' ')
df.Research = df.Research.str.replace(';','')
df.Research = df.Research.str.replace(':','')
df.Research = [w for w in df.Research if not w in stopwords.words('english')]
print(df.Research)


# In[548]:


print(df[:2].T)


# In[549]:


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

porter=PorterStemmer()

def stemSentence(sentence):
    token_words=word_tokenize(str(df.Research))
    token_words
    stem_sentence=[]
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

print(str(df.Research))
print("Stemmed sentence")
x=stemSentence(str(df.Research))
x


# In[550]:


class InvertedIndex(dict):
    def __init__(self, docs):
        self.docs = docs

        for doc_index,doc in enumerate(docs):
            for term in doc.split(" "):
                self[term].append(doc_index)

    def __missing__(self, term):
        # operate like defaultdict(list)
        self[term] = []
        return self[term]

    def search(self, term):
        return self.get(term) or 'No results'


docs=df.Research+x

ix = InvertedIndex(docs)
print ('learning:',ix.search("learning"))
print ('decision:', ix.search('decision'))
print ('\nTEST OF KEY SETTING')
print (ix['medic'])
print (('systems' in ix))
print (ix.search('systems'))


# In[ ]:


ix = InvertedIndex(docs)
ix 


# In[552]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# In[553]:


vectorizer = TfidfVectorizer()


# In[554]:


X = vectorizer.fit_transform(docs)


# In[555]:


X


# In[560]:


query = "machine learning"


# In[561]:


get_ipython().run_cell_magic('time', '', 'query_vec = vectorizer.transform([query]) # Ip -- (n_docs,x), Op -- (n_docs,n_Feats)\nresults = cosine_similarity(X,query_vec).reshape((-1,)) # Op -- (n_docs,1) -- Cosine Sim with each doc')


# In[562]:


results


# In[563]:


# Print Top 5 results
for i in results.argsort()[-5:][::-1]:
    print(df.iloc[i,0],"--",df.iloc[i,:5])


# In[504]:


import pandas as pd
import numpy as np
import sklearn
from nltk.corpus import stopwords


# In[209]:


stop=stopwords.words("english")


# In[ ]:


stop


# In[228]:


tc_df=pd.read_csv(r'BBC_News .csv')
tc_df


# In[6]:


x,y=tc_df.Text, tc_df.Category


# In[233]:


x


# In[38]:


y


# In[166]:


# Remove all the special characters
x1 = x.str.replace(r'\W', ' ')

# remove all single characters
x2 =x1.str.replace(r'\s+[a-zA-Z]\s+', ' ')

# Remove single characters from the start
x3 = x2.str.replace(r'\^[a-zA-Z]\s+', ' ')

# Substituting multiple spaces with single space
x4 = x3.str.replace(r'\s+', ' ')

# Removing prefixed 'b'
x5 = x4.str.replace(r'^b\s+', '')

# Converting to Lowercase
x6 = x5.str.lower()


# In[167]:


x6


# In[150]:


from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=1500, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))


# In[240]:


X = vectorizer.fit_transform(x6).toarray()


# In[241]:


X


# In[153]:


from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
Tfidfconverter= TfidfVectorizer(max_features=2000, min_df=5, max_df=0.7, stop_words=stopwords.words('english'))
Tfidfconverter = TfidfTransformer()
X = Tfidfconverter.fit_transform(X).toarray()


# In[154]:


X


# In[155]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


# In[156]:


from sklearn.cluster import KMeans
k=5
model=KMeans(n_clusters=k)
model.fit(X)
print("cluster number of documents in order")
print(model.labels_)


# In[157]:


from sklearn.naive_bayes import MultinomialNB
model=  MultinomialNB()
model.fit(X_train, y_train)


# In[158]:


prediction=model.predict(X_test)


# In[161]:


from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,prediction))
print(classification_report(y_test,prediction))
print(accuracy_score(y_test, prediction))


# In[224]:


#taking random sentencec for the documents and predcit their class:
y=vectorizer.transform(["stalemate in pension strike talks talks aimed at averting national strikes over pension reforms have ended without agreement after 90 minutes.  five public sector unions met deputy prime minister john prescott at the labour spring conference in gateshead. they want the government to withdraw regulations - due to be introduced in weeks - which would raise the pension age for council workers from 60 to 65. up to 1.4 million workers could take part in strikes earmarked for 23 march. discussions will resume next week.  a spokesman for unison  britain s biggest union  said after saturday s meeting:  at least we are still talking.  all sides are anxious to avoid a major confrontation in the run up to the general election  said bbc labour affairs correspondent stephen cape. in four days  unison will start balloting 800 000 local government workers on strikes. other public sector unions have pledged to follow. the five unions which met mr prescott want the government to withdraw these regulations. this would allow months of tough negotiations to follow  said our correspondent. but a spokesman for mr prescott warned that the changes to the local government pension scheme would have to go ahead in april.  privately ministers believe this will be the  less painful  option  our correspondent added. the public and commercial services union (pcs) will co-ordinate any industrial action with up to six other public sector unions. pcs leader mark serwotka warned last week that there could be further walkouts unless there was a government rethink.  for a government that lectures everyone on choice - choice on public service  choice on this and choice on that - isn t it ironic that they re saying to public sector workers there is no choice   he said.  if you want the pension you were promised when you started you must work for an extra five years - that is working until people drop.  in the 20th century  it s completely unacceptable.   unison s 800 000 workers  the transport and general workers  union s 70 000 and amicus  20 000 are among those being balloted about a 23 march walkout. mr prescott held a private meeting with senior union figures last week. it is understood no deal was offered in that meeting but there was room for further negotiations."])
prediction=model.predict(y)
print(prediction)

y=vectorizer.transform(["ferguson urges henry punishment sir alex ferguson has called on the football association to punish arsenal s thierry henry for an incident involving gabriel heinze.  ferguson believes henry deliberately caught heinze on the head with his knee during united s controversial win. the united boss said it was worse than ruud van nistelrooy s foul on ashley cole for which he got a three-game ban.  we shall present it to the fa and see what they do. the tackle on heinze was terrible   he said. clubs are permitted to ask the fa to examine specific incidents but information is expected to be provided within 48 hours of the game. the clash occurred moments before half-time when a freddie ljungberg challenge left heinze on the ground on the left touchline. henry  following the ball  attempted to hurdle the argentine but his knee collided with the back of heinze s head.  the striker protested his innocence - and referee mike riley deemed the collision accidental. ferguson was also upset by arsenal s overall discipline during the heated encounter between the two arch-rivals and praised his own side s behaviour.  edu produced a terrible tackle on scholes that was a potential leg-breaker   he said.  there were 24 fouls in the game by arsenal  seven on heinze  five on ronaldo  six by vieira - and it was only his sixth foul that got him booked. phil neville got booked for his first challenge.  i am proud of my players for the way they handled that pressure.  we have always been good at being gracious in defeat. what happened on sunday overshadowed our achievement  but then they do it all the time  don t they"])
prediction=model.predict(y)
print(prediction)

y=vectorizer.transform(["text messages aid disaster recovery text messaging technology was a valuable communication tool in the aftermath of the tsunami disaster in asia.  the messages can get through even when the cell phone signal is too weak to sustain a spoken conversation. now some are studying how the technology behind sms could be better used during an emergency. sanjaya senanayake works for sri lankan television. the blogging world  though  might know him better by his online name  morquendi. he was one of the first on the scene after the tsunami destroyed much of the sri lankan coast. cell phone signals were weak. land lines were unreliable. so mr senanayake started sending out text messages. the messages were not just the latest news they were also an on-the-ground assessment of  who needs what and where . blogging friends in india took mr senanayake s text messages and posted them on a weblog called dogs without borders. thousands around the world followed the story that unfolded in the text messages that he sent.  and that s when mr senanayake started to wonder if sms might be put to more practical use.  sms networks can handle so much more traffic than the standard mobile phone call or the land line call   he says.   in every rural community  there s at least one person who has access to a mobile phone  or has a mobile phone  and can receive messages.  half a world away  in the caribbean nation of trinidad and tobago  taran rampersad read morquendi s messages. mr rampersad  who used to work in the military  knew how important on the ground communication can be in times of disaster. he wondered if there might be a way to automatically centralise text messages  and then redistribute them to agencies and people who might be able to help. mr rampersad said:  imagine if an aid worker in the field spotted a need for water purification tablets  and had a central place to send a text message to that effect.  he can message the server  so the server can send out an e-mail message and human or machine moderators can e-mail aid agencies and get it out in the field.  he added:  or  send it at the same time to other people who are using sms in the region  and they might have an excess of it  and be able to shift supplies to the right places.   mr rampersad and others had actually been thinking about such a system since hurricane ivan ravaged the caribbean and the southern united states last september. last week  he sent out e-mail messages asking for help in creating such a system for asia.  in only 72 hours  he found dan lane  a text message guru living in britain. the pair  along with a group of dedicated techies  are creating what they call the alert retrieval cache. the idea is to use open-source software - software can be used by anyone without commercial restraint - and a far-flung network of talent to create a system that links those in need with those who can help.  this is a classic smart mobs situation where you have people self-organizing into a larger enterprise to do things that benefit other people   says paul saffo  a director at the california-based institute for the future.  you may be halfway around the world from someone  but in cyberspace you re just one click or one e-mail away   he said   that s put a whole new dimension on disaster relief and recovery  where often people halfway around the world can be more effective in making something happen precisely because they re not right on top of the tragedy.  it is still very early days for the project  though. in an e-mail  dan lane calls it  an early proof of concept.  right now  the alert retrieval cache can only take a text message and automatically upload it to a web-page  or distribute it to an e-mail list. in the near future  the group says it hopes to take in messages from people in affected areas  and use human moderators to take actions based on the content of those messages. but there s still another challenge. you have to get people to know that the system is there for them to use.  it s amazing how difficult it is to find someone to pass it along to  and say  look this is what we re trying to do and everything like that   says mr rampersad.  so the big problem right now is the same problem we re trying to solve - human communication.  he is optimistic  however. he thinks that the alert retrieval cache is an idea whose time has come and he hopes governments  too  will sit up and take notice. and he stands by his motto  courtesy of michelangelo: criticise by creating.  clark boyd is technology correspondent for the world  a bbc world service and wgbh-boston co-production."])
prediction=model.predict(y)
print(prediction)

y=vectorizer.transform(["musical treatment for capra film the classic film it s a wonderful life is to be turned into a musical by the producer of the controversial hit show jerry springer - the opera.  frank capra s 1946 movie starring james stewart  is being turned into a ¬£7m musical by producer jon thoday. he is working with steve brown  who wrote the award-winning musical spend spend spend. a spokeswoman said the plans were in the  very early stages   with no cast  opening date or theatre announced.  a series of workshops have been held in london  and on wednesday a cast of singers unveiled the musical to a select group of potential investors. mr thoday said the idea of turning the film into a musical had been an ambition of his for almost 20 years. it s a wonderful life was based on a short story  the greatest gift  by philip van doren stern. mr thoday managed to buy the rights to the story from van doren stern s family in 1999  following mr brown s success with spend spend spend. he later secured the film rights from paramount  enabling them to use the title it s a wonderful life."])
prediction=model.predict(y)
print(prediction)

y=vectorizer.transform(["ukraine strikes turkmen gas deal ukraine has agreed to pay 30% more for natural gas supplied by turkmenistan.  the deal was sealed three days after turkmenistan cut off gas supplies in a price dispute that threatened the ukrainian economy. supplies from turkmenistan account for 45% of all natural gas imported by ukraine  which has large coal deposits but no gas fields. turkmenistan is also trying to strike a similar deal with russia  which is not so dependent on its gas. turkmen president saparmurat niyazov  who signed the contract  said the turkmen side agreed to lower the price demanded by $2 per 1 000 cubic metres  bringing it down to $58. but the new price is still $14 higher than the price fixed in the contract for 2004. the head of the ukrainian state-owned naftohaz company  yury boyko  said he was  fully happy  with the deal. on friday  turkmenistan acted on a threat and shut off gas supplies to ukraine in attempt to bring the price dispute to a head. mr niyazov said that his government would insist on the same price for supplies to russia. analysts say thay may not happen as russia  the world s leading gas producer  needs the cheap turkmen gas only to relieve is state-owned gazprom from costly investment in the exploration of oil fields in siberia. turkmenistan is the second-largest gas producer in the world."])
prediction=model.predict(y)
print(prediction)

#Make our own sentences and see how well it classifiy them:
y=vectorizer.transform(["my name is hakem and i enjoy playing football"])
prediction=model.predict(y)
print(prediction)

y=vectorizer.transform(["the united states is facing budget deficits in the short term"])
prediction=model.predict(y)
print(prediction)
                      
y=vectorizer.transform(["manchester united will win the upcoming league according to analysts"])
prediction=model.predict(y)
print(prediction)                
print("All sentences were correclty classified")


# In[ ]:




