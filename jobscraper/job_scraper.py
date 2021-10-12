# import module
import requests
from bs4 import BeautifulSoup
# loading in all the essentials for data manipulation
import pandas as pd
import numpy as np
#load inthe NTLK stopwords to remove articles, preposition and other words that are not actionable
from nltk.corpus import stopwords
# This allows to create individual objects from a bog of words
from nltk.tokenize import word_tokenize
# Lemmatizer helps to reduce words to the base form
from nltk.stem import WordNetLemmatizer
# Ngrams allows to group words in common pairs or trigrams..etc
from nltk import ngrams
# We can use counter to count the objects
from collections import Counter
# This is our visual library
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.collocations import *



use_white_list = False
job = "software+developer" # Data for URL
location = "remote"
indeed_url="https://in.indeed.com/jobs?q=" + job + "&l=" + location 
# indeed_url = "https://in.indeed.com/jobs?q="+job+"&l="+Location
numberOfPages = 2
stop_words = set(stopwords.words('english'))
blacklist = []


whitelist = [
            #Basics
            "Git",
            "Terminal",
            "Data Structure",
            "Algorithm",
            "SSH",
            "FTP",
            "API",

            #Front End
            "Front End"
            "DNS",
            "HTML",
            "CSS",
            "SEO",
            "JavaScript",
            "HTTP",
            "HTTPS", 
            "npm",
            "yarn",
            #Frameworks
                "framework",
                "React",
                "Angular",
                "Vue.js",
                "Redux",
                "NgRx",
                "Vuex",
                "Mobx",

                "Bootstrap",
            "Progressive Web Apps",
            "TypeScript",
            "GraphQL",
            "Mobile",
            "Web Assembly",

            #Backend
            "Back-End",
            "Back End",

            "Rust",
            "Go",
            "Java",
            "C#",
            "PHP",
            "Javascript",
            "Python",
            "Ruby",
            "Version Control",
            #Database stuff
                "Database",
                "PostgreSQL",
                "MySQL",
                "MariaDB",
                "MS SQL",
                "MS SQL",
                "Oracle",
                "ORMs",
                "ACID",
                "Transaction",
                "N+1",
            "REST",
            "JSON",
            "SOAP",
            "gRCP",

                #Authentication
                "Authentication",
                "Cookie",
                "OAuth",
                "JWT",
                "OpenID",
                "SAML",

            "CDN",
            "Server Side",
            "Client Side",
            "Redis,"

                "Testing",
                "Integration Testing",
                "Unit Testing",
                "Functional Testing",

            "CI",
            "CD",
            "Security",
            "SHA",
            "bcrypt",
            "scrypt",
            "SSL",
            "TLS",

            "Docker",
            "Nginx",
            "Apache",
            "Caddy",
            "Sockets",

            "DevOps",

            #Still going to add

                ]

for i in range(len(whitelist)):
    whitelist[i] = whitelist[i].lower()

def word_frequency(sentence):

    return

# user define function
# Scrape the data
# and get in string
def getdata(url):

    #spoof user agent
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
    headers = {'User-Agent': user_agent}
    r = requests.get(url, headers=headers)
    print("url request return: " + r.text)

    return r.text

# Get Html code using parse
def html_code(url):

    # pass the url
    # into getdata function
    htmldata = getdata(url)
    soup = BeautifulSoup(htmldata, 'html.parser')

    # return html code
    return(soup)

# filter job data using
# find_all function
def get_text(soup):
    

    print("getting text")

    
    



    data_str = ""
    for item in soup.find_all("div", class_="jobsearch-jobDescriptionText"):
        data_str = data_str + item.get_text()

    

    word_tokens = word_tokenize(data_str) #Takes words out of a sentence and puts them into a list 

    filtered_sentence = []


    for word in word_tokens:
        #if not word.isalpha():
        #    continue;
        if word not in whitelist:
            continue;
        if word in blacklist:
            continue;
        filtered_sentence.append(word)
    
    return filtered_sentence


def get_links(soup):

    print("Getting Links...")
    links = []
    for link in soup.find_all('a', class_="tapItem"):
        links.append("https://in.indeed.com" + link.get('href'))

    return links

def count_words(text):
    freq = nltk.FreqDist(text)

    #print(freq.most_common())

    #for key,val in freq.items():
    #    print (str(key) + ':' + str(val))

    freq.plot(50,cumulative=False)


    #--------------------------------------------------
    #Bigram stuff 
    bigram_measures = nltk.collocations.BigramAssocMeasures()
    trigram_measures = nltk.collocations.TrigramAssocMeasures()

    # change this to read in your data
    finder = BigramCollocationFinder.from_words(text)
    # only bigrams that appear 3+ times
    finder.apply_freq_filter(3)

    # return the 10 n-grams with the highest PMI
    finder.nbest(bigram_measures.pmi, 10)
    #print(finder.nbest(bigram_measures.pmi, 10))
    #--------------------------------------------------



# driver nodes/main function
if __name__ == "__main__":
    links = []
    #Loop through pages and get links to each job page
    #for i in range(numberOfPages):
    for i in range(numberOfPages):
        temp= indeed_url + "&sort=date&start=" + str(i)
        soup = html_code(temp)
        links = links + get_links(soup)    
        #print(links)


    text = []

    for link in links:
        print(link)
        soup = html_code(link)
        text = text + get_text(soup)

    count_words(text)


