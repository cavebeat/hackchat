'''
Created on 19 Aug 2017

@author: cave
'''


#!/usr/bin/env python3
import hackchat
import web



def message_got(chat, message, sender):
    print message.lower()
    if "hello" in message.lower():
        chat.send_message("Hello there {}!".format(sender))
        

class hooks:
    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print
        chat.send_message(data)
        return 'OK'

if __name__ == '__main__':
    chat = hackchat.HackChat("1337Bot", "programming", 1)
    chat.on_message += [message_got]    
    urls = ('/.*', 'hooks')
    app = web.application(urls, globals())    
    app.run()