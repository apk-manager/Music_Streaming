
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template,request,session,Response,redirect,url_for

from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup
import requests


app=Flask(__name__,template_folder='Templates')

sample = False

app.secret_key="dljsaklqk24e21cjn!Ew@@dsa5"

def connect(host = 'https://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def check_links(links,vals):
    mp3s = [l for l in links if l['href'].endswith('.mp3')]
    for song in mp3s:
        vals+=str(song['href']).replace("//","\/\/")+','
    return vals

@app.route("/getsongs",methods=['POST'])
def names():
    name=request.form['name']
    print(name)
    name += " song mp3 free download"
    if connect():
        str=''
        query = name  # com
        for url in search(query, tld='co.in', lang='en', start=0, pause=1.0):
            try:
                URL = url
                content = requests.get(URL)
                soup = BeautifulSoup(content.text, 'html.parser')

                link = soup.find_all('a', href=True)

                str = check_links(link, str)

                if len(str.split(',')) > 10:
                    print(str)
                    return render_template('songlist.html',final=str)

            except Exception as ex:
                continue
    else:
        return render_template('songlist.html', final="fail to connect")

@app.route("/song")
def song():
    return render_template('index.html')
