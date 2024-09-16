from bs4 import BeautifulSoup
import os 
import pandas as pd


d = {'title':[],'price' :[], 'link':[]}

for file in os.listdir("data"):

    if 'py' not in str(file):
        with open(f"data/{file}") as f:
            try:
                html_doc = f.read(None)
                soup = BeautifulSoup(html_doc, 'html.parser')
                t = soup.find("h2", recursive= True)
                if t:
                    title = t.get_text()
            
                else:
                    continue




                l = t.find("a")
                if l:
                    link = l.get_text()
            
                else:
                    continue

        
                link = "https://amazon.in/" + l['href']
            except:
                print('Except ran')
                continue




            #PRICE
    
            p = soup.find("span",attrs={"class": 'a-price-whole'},recursive=True)
            if p:
                print('PRICE FOUND')
                price = p.get_text()
                print('LAPTOP NAME and specs: ',title )
                print('PRICE: ',price,'₹',)
                print('LINK: ',link)

                d['title'].append(title)
                d['link'].append(link)
                d['price'].append(price)
                print(d)

            

df = pd.DataFrame(data=d)

df.to_csv('data.csv')