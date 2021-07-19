import requests    
 
def News():

    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    article = open_bbc_page["articles"]
 
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        print(i + 1, results[i])
 
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)                
 

    