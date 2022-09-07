# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:11:34 2022

@author: FactsgeniX
"""

def implementDB():
    tell='Tell me, which toy you would like to know about?'
    alexaSpeak(tell)
    while True:
        # Exception handling to handle
        # exceptions at the runtime
        try:
         
            # use the microphone as source for input.
            with sr.Microphone() as input_source:
             
                # we are waiting for minimum time(only for a second) to let the recognizer
                # adjust the energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise(input_source, duration=0.2)
                 
                #listens for the user's input
                audio_captured = r.listen(input_source)
             
                # Using google to recognize audio
                invoking_Text = r.recognize_google(audio_captured, language="en-IN")
                invoking_Text = invoking_Text.lower()
                #print(invoking_Text)
 
                #checking if the story associated with the Indian toy is available in the DB and calling the alexSpeak function
                conn=mysql.connector.connect(user='userName',password='passwd',host='localhost', database ='Alexa')
                cur=conn.cursor()
                toy=invoking_text
                query=f'select * from toy_master_story where toy_name="toy"'
                cur.execute(query)
                result=cur.fetchall()
                if(len(result)>1):
                    alexaSpeak(result)
                    break
                else:
                    implemementWiki(invoking_text)
                    break
        
        except sr.RequestError as e:
            output="Sorry, an unknown error occured"
            alexaSpeak(output)
            break
         
        except sr.UnknownValueError:
            output="Sorry, an unknown error occured, try again"
            alexaSpeak(output)
            implementDB()

#In the below function an internal API call is made to the wikipedia to retrieve the story associated with the Indian toy            
def implementWiki(invoking_text):
    url = 'https://en.wikipedia.org/wiki/'+invoking_text
    index = requests.get(url).text
    soup = BeautifulSoup(index, 'html.parser')
    pp = pprint.PrettyPrinter(indent=4)
    metadata_info = {
        'description': description_retrieval(soup)}
    text_recived=metadata_info.get('description')
    text_recived=str(text_recived)
    soup_extr = BeautifulSoup(text_recived)
    out=soup_extr.get_text()
    alexaSpeak(out)

#below function is used to get the decription of the Indian toy from the wiki source    
def description_retrieval(html):
    #Scraping the description from the page
    description = None
    if html.find("meta", property="description"):
        description = html.find("meta", property="description").get('content')
    elif html.find("meta", property="og:description"):
        description = html.find("meta", property="og:description").get('content')
    elif html.find("meta", property="twitter:description"):
        description = html.find("meta", property="twitter:description").get('content')
    elif html.find("p"):
        description = html.find("p").contents
    return description