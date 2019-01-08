###############7.17.2017 Lan Huang############
#   update publication from publication.txt  #
#   publication.txt format:                  #
#        Year:int                            #
#        ID:int                              #
#        Author:string                       #
#        Title:string                        #
#        Journal:string                      #
#    below is User Configuration Section     #
##############################################
website_foldername="public_html"
##############################################
publication_template="template/publication_content.html"
import os
publication_template_location=os.path.join(os.getcwd(),website_foldername,publication_template)
publication={}
publication_template_file=open(publication_template_location,'w')
publicationfile=open("publication.txt",'r')
for line in publicationfile:
    if line.strip().split(":")[0]=="Year":
        publication_template_file.write("<h2> %s </h2> \n" % (line.strip().split(":")[1],))
    elif line.strip().split(":")[0]=="ID":
        publication_template_file.write("<p>[%2i ] "  %  (int(line.strip().split(":")[1]),))
    elif line.strip().split(":")[0]=="Title":
        publication_template_file.write("%s <br>" % (line.strip().split(":")[1],))
    elif line.strip().split(":")[0]=="Author":
        publication_template_file.write("<i> %s </i><br>" % (line.strip().split(":")[1],))
    elif line.strip().split(":")[0]=="Journal":
        publication_template_file.write("<strong> %s</strong></p> \n" % (line.strip().split(":")[1],))
    else:
        raise Exception("The format of publication list is not correct")
                
publication_template_file.close()
publicationfile.close()
print("Done! Update publication list Successfully!!!")
input()
