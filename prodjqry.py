from threading import Thread,Condition
import time
import random
from Queue import Queue
import cherrypy
import urllib2,cookielib
import ast
import redis
import os, os.path

conn = redis.Redis('localhost')
condition = Condition()




class ProducerThread(Thread):
    def run(self):
        site= "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"
        hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        req = urllib2.Request(site, headers=hdr)
        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

        c = page.read()
        global conn
        b= ast.literal_eval(c)
        a=b["data"]


        while True:
            condition.acquire()
            ltn=conn.llen("test")
            if ltn == 10:
                print "Queue full, producer is waiting"
                condition.wait()
                print "Space in queue, Consumer notified the producer"

            num = conn.rpush("test", *a)

            print "produced"
            condition.notify()
            condition.release()
            time.sleep(4)


class ConThread(Thread,object):
    def test(self):
        global conn
        while True:
            condition.acquire()
            ltn=conn.llen("test")
            num = conn.lrange("test",0,9)
            t = conn.lrange("test",0,0)
            a = str(t)
            a= a.replace(", ","\n")
            a= a.replace("'","")
            a= a.replace("{","")
            a= a.replace("}","")
            a= a.replace("\\\\","")
            an = ast.literal_eval(t[0])
            an = an["symbol"]
            t = conn.lrange("test",1,1)
            b = str(t)
            b= b.replace(", ","\n")
            b= b.replace("'","")
            b= b.replace("{","")
            b= b.replace("}","")
            b= b.replace("\\\\","")
            bn = ast.literal_eval(t[0])
            bn = bn["symbol"]
            t = conn.lrange("test",2,2)
            c = str(t)
            c= c.replace(", ","\n")
            c= c.replace("'","")
            c= c.replace("{","")
            c= c.replace("}","")
            c= c.replace("\\\\","")
            cn = ast.literal_eval(t[0])
            cn = cn["symbol"]
            t = conn.lrange("test",3,3)
            d = str(t)
            d= d.replace(", ","\n")
            d= d.replace("'","")
            d= d.replace("{","")
            d= d.replace("}","")
            d= d.replace("\\\\","")
            dn = ast.literal_eval(t[0])
            dn = dn["symbol"]
            t = conn.lrange("test",4,4)
            e = str(t)
            e= e.replace(", ","\n")
            e= e.replace("'","")
            e= e.replace("{","")
            e= e.replace("}","")
            e= e.replace("\\\\","")
            en = ast.literal_eval(t[0])
            en = en["symbol"]
            t = conn.lrange("test",5,5)
            f = str(t)
            f= f.replace(", ","\n")
            f= f.replace("'","")
            f= f.replace("{","")
            f= f.replace("}","")
            f= f.replace("\\\\","")
            fn = ast.literal_eval(t[0])
            fn = fn["symbol"]
            t = conn.lrange("test",6,6)
            g = str(t)
            g= g.replace(", ","\n")
            g= g.replace("'","")
            g= g.replace("{","")
            g= g.replace("}","")
            g= g.replace("\\\\","")
            gn = ast.literal_eval(t[0])
            gn = gn["symbol"]
            t = conn.lrange("test",7,7)
            h = str(t)
            h= h.replace(", ","\n")
            h= h.replace("'","")
            h= h.replace("{","")
            h= h.replace("}","")
            h= h.replace("\\\\","")
            hn = ast.literal_eval(t[0])
            hn = hn["symbol"]
            t = conn.lrange("test",8,8)
            i = str(t)
            i= i.replace(", ","\n")
            i= i.replace("'","")
            i= i.replace("{","")
            i= i.replace("}","")
            i= i.replace("\\\\","")
            it = ast.literal_eval(t[0])
            it = it["symbol"]
            t = conn.lrange("test",9,9)
            j = str(t)
            j= j.replace(", ","\n")
            j= j.replace("'","")
            j= j.replace("{","")
            j= j.replace("}","")
            j= j.replace("\\\\","")
            jn = ast.literal_eval(t[0])
            jn = jn["symbol"]
            if not num:
                print "Nothing in queue, consumer is waiting"
                condition.wait()
                print "Producer added something to queue and notified the consumer"
            #print "consumed",num
            print ltn
            print "consumed"
            conn.ltrim("test",-1,0)
            condition.notify()
            condition.release()
            time.sleep(2)
            return '''<html>
            <head>
            <meta http-equiv="refresh" content="300" >
            <link href="/static/css/style2.css" rel="stylesheet">
            </head>
            <body>
            <div id="mainDiv">
            <div id= "subDiv">
            <div id="the-string0" class="card"><div class= "title">{10}</div>{0}</div>
            <div id="the-string1" class="card"><div class= "title">{11}</div>{1}</div>
            <div id="the-string2" class="card"><div class= "title">{12}</div>{2}</div>
            <div id="the-string3" class="card"><div class= "title">{13}</div>{3}</div>
            <div id="the-string4" class="card"><div class= "title">{14}</div>{4}</div>
            <div id="the-string5" class="card"><div class= "title">{15}</div>{5}</div>
            <div id="the-string6" class="card"><div class= "title">{16}</div>{6}</div>
            <div id="the-string7" class="card"><div class= "title">{17}</div>{7}</div>
            <div id="the-string8" class="card"><div class= "title">{18}</div>{8}</div>
            <div id="the-string9" class="card"><div class= "title">{19}</div>{9}</div>
            </div>
            </div>
            </body>
            </html>'''.format(a,b,c,d,e,f,g,h,i,j,an,bn,cn,dn,en,fn,gn,hn,it,jn)


class ConsumerThread(object):


    @cherrypy.expose
    def index(self):
        ProducerThread().start()
        ConThread().start()
        return ConThread().test()

@cherrypy.expose
class Display(object):
    @cherrypy.tools.accept(media='text/plain')
    def POST(self):
        return ConThread().test()

#ConThread().test()
#open('main.html')



if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
       '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        },
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': int(os.environ.get('PORT', 5000)),
        }
    }
    webapp = ConsumerThread()
    webapp.generator = Display()
    cherrypy.quickstart(webapp, '/', conf)
    #cherrypy.quickstart(ConsumerThread())
