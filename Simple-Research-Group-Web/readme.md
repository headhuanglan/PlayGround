README
===========================
# Simple Research Group website template by L 

* HTML + CSS + JS
* Modified from https://www.html5webtemplates.co.uk/templates/black_white/index.html
* Add two python script for Group News and Publication update

# Files structure

* index.html news.html people.html publication.html research.html galleries.html
are the frames for the web.
* The actual contents are loaded by jQuery of template files from template folder.
* The <head> </head> parts need to be modifed for your needs.
XXX_content.html is the corresponding files for website content.
The footer.html and header.html need to be modified for your needs.

# For template forlder 

* Files in this forlder contains the actual contents for the web. 
You can also modify the content by MS-WORD and save the file of html format.

* latest_news.html all_news.html publication_content.html 
can be generated from python scripts with news.txt and publication.txt
 
# Config Steps


## 1>Config the py files first
```
update_news.py
set website_foldername
set number_of_latest_news_shown_in_homepage
update_publication.py
set website_foldername
```

## 2>customize your news.txt and publication.txt

```
   news.txt format:                         
        ID:int                              
        Title:string                        
        Time:string                         
        Data:string                         
  publication.txt format:                  
        Year:int                            
        ID:int                              
        Author:string                       
        Title:string                        
        Journal:string                      
```

## 3>run these py for website update

```
folder style contains all the css pics and js files.
forder template contains the files for each page's content update them as your needs.
forder galleries contains the pics for the page galleries.
 
For style/location.js
Your need define your own location on google map
Change the following two variable
lat=30.6208435;  
lon=-96.3420207;
```  
 
