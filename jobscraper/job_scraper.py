# import module
import requests
from bs4 import BeautifulSoup
# loading in all the essentials for data manipulation
#load inthe NTLK stopwords to remove articles, preposition and other words that are not actionable
from nltk.corpus import stopwords
# This allows to create individual objects from a bog of words
from nltk.tokenize import word_tokenize
# Lemmatizer helps to reduce words to the base form
# Ngrams allows to group words in common pairs or trigrams..etc
# We can use counter to count the objects
# This is our visual library
import pandas as pd 
import nltk
import random
from urllib.request import Request, urlopen



def scrape_jobs(
        job_search="software+developer", 
        whitelist="",blacklist="",
        search_size=1,
        location="remote",):
    
    indeed_url="https://in.indeed.com/jobs?q=" + job_search + "&l=" + location
    print("Scraping here: " + indeed_url) 
    stop_words = set(stopwords.words('english'))
    whitelist = word_tokenize(whitelist.lower())
    blacklist = word_tokenize(blacklist.lower()) + list(stop_words)

    text = []
    page_number = 0
    links = 0
    
    #Keep finding links until we've matched the search size
    while links < search_size:
        page_number = page_number + 1
        page_url = indeed_url + "&sort=date&start=" + str(page_number)
        proxy = generate_proxy() #generate new proxy for each page
        page_html = get_html_code(page_url, proxy)
        print("Getting page: " +  page_url)
            
        if len(page_html.find_all('a', class_="tapItem")) == 0:
            print("We got captcha blocked :(")
            break;
            
        #Loop through each job link on the page and add its text
        for link in page_html.find_all('a', class_="tapItem"):
            link_url = "https://in.indeed.com" + link.get('href')
            link_html = get_html_code(link_url, proxy)
            print("Adding text from link: " + link_url)
            text = text + get_text(link_html, whitelist, blacklist)
            links = links + 1
            if links >= search_size:
                break;

    return count_words(text)


def generate_proxy():
    # Here I provide some proxies for not getting caught while scraping
    print("Generating proxy")
    ua = generate_user_agent() # From here we generate a random user agent
    proxies = [] # Will contain proxies [ip, port]

    # Retrieve latest proxies
    proxies_req = Request('https://www.sslproxies.org/')
    proxies_req.add_header('User-Agent', ua)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')

    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='list')

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append({
      'ip':   row.find_all('td')[0].string,
      'port': row.find_all('td')[1].string
    })

    # Choose a random proxy
    proxy_index = random.randint(0, len(proxies) - 1)
    proxy = proxies[proxy_index]
    
    for n in range(1, 20):
        req = Request('http://icanhazip.com')
        req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')

    # Every 10 requests, generate a new proxy
    if n % 10 == 0:
        proxy_index = random.randint(0, len(proxies) - 1)
        proxy = proxies[proxy_index]

    # Make the call
    try:
        my_ip = urlopen(req).read().decode('utf8')
        print('#' + str(n) + ': ' + my_ip)
    except: # If error, delete this proxy and find another one
        del proxies[proxy_index]
        print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
        proxy_index = random.randint(0, len(proxies) - 1)
        proxy = proxies[proxy_index]
    return proxy

# Scrape the data
# and get in string

def generate_user_agent():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
    ]
    
    return random.choice(user_agent_list)


def getdata(url, proxy):
    user_agent = generate_user_agent()
    #spoof user agent
    headers= {'User-Agent': user_agent, "Accept-Language": "en-US, en;q=0.5"}
    r = requests.get(url, headers=headers, proxies=proxy)
    #print("url request return: " + r.text)

    return r.text

# Get Html code using parse
def get_html_code(url, proxy):

    # pass the url
    # into getdata function
    htmldata = getdata(url, proxy)
    soup = BeautifulSoup(htmldata, 'html.parser')

    # return html code
    return(soup)

# filter job data using
# find_all function
def get_text(soup, whitelist, blacklist):
    data_str = ""
    for item in soup.find_all("div", class_="jobsearch-jobDescriptionText"):
        data_str = data_str + item.get_text()

    word_tokens = word_tokenize(data_str.lower()) #Takes words out of a sentence and puts them into a list 

    filtered_sentence = []

    for word in word_tokens:
        if not word.isalpha():
            continue;
        if whitelist and word not in whitelist:
            continue;
        if blacklist and word in blacklist:
            continue;
        filtered_sentence.append(word)
    
    return filtered_sentence


def count_words(text):
    freq = nltk.FreqDist(text)
    #print(freq.most_common(50))
    
    return freq.most_common(50)

    #print(freq.most_common())

    #for key,val in freq.items():
    #    print (str(key) + ':' + str(val))

    #freq.plot(50,cumulative=False)


    #--------------------------------------------------
    #Bigram stuff 
    #bigram_measures = nltk.collocations.BigramAssocMeasures()
    #trigram_measures = nltk.collocations.TrigramAssocMeasures()

    # change this to read in your data
    #finder = BigramCollocationFinder.from_words(text)
    # only bigrams that appear 3+ times
    #finder.apply_freq_filter(3)

    # return the 10 n-grams with the highest PMI
    #finder.nbest(bigram_measures.pmi, 10)
    #print(finder.nbest(bigram_measures.pmi, 10))
    #--------------------------------------------------

old_whitelist = [
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