#Amber Lennox

from PIL import Image
import os
from os import path
import numpy as np
import datetime

#This code presumes your photographs are all held in a folder titled 'Photos'  
#With subfolders organised by month with the title 'YYYYMM'
#But can be easily modified for other purposes

#If you want a specific photo to be the thumbnail for that folder
#Put 'thumbnail' in the title of that file

make_thumbnails = 'yes' #THIS SHOULD BE 'YES' IF ADDING OR CHANGING PHOTOS

#The dictionaries that are used to translate the month of each folder
english = {
  "01": "January",
  "02": "Febuary",
  "03": "March",
  "04": "April",
  "05": "May",
  "06": "June",
  "07": "July",
  "08": "August",
  "09": "September",
  "10": "October",
  "11": "November",
  "12": "December"
}

#Open a html file in the English page location
f = open('photos_test.html', 'w')



#Print general CSS information
f.write("""<!DOCTYPE html>\n""")

f.write("""<style>\n""")
f.write("""@import "main.css"\n""")

f.write("""</style>\n""")


f.write("""<script\n""")
f.write("""    src="https://code.jquery.com/jquery-3.3.1.js" \n""")
f.write("""    integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=" \n""")
f.write("""    crossorigin="anonymous"> \n""")
f.write("""</script> \n""")



f.write("""<script>\n""")
f.write("""$(function(){\n""")
f.write("""  $("#header").load("header.htm"); \n""")
f.write("""  $("#footer").load("footer.htm"); \n""")
f.write("""}); \n""")
f.write("""</script> \n""")

f.write("""<title>Amber Leamhnachd's Webpage</title>\n""")
f.write("""<html>\n""")
f.write("""<body>\n""")

#My header that I use
f.write("""<div id="header"></div>\n""")
f.write("""<title>Amber Leamhnachd's Webpage</title>\n""")
f.write("""<br>\n""")

#Open main div
f.write("""<div class="main">\n""")
f.write("""<br>\n""")
f.write("""<center>\n""")

#Open text div
f.write("""<div class="mytext">\n""")
f.write("""<center>\n""")

#Generate table
f.write(""" <table width=100%> """)
f.write(""" <td align ="left"> << </td>""")
f.write(""" <td align = "right"> >> </td>""")
f.write(""" </table> \n \n""")

f.write(""" <div id="myphotomenu" style="overflow-x:scroll; overfloy-y:hidden;overflow-style:none;">\n """)
f.write(""" <table style= "overflow:auto;" border=0>\n """)
f.write(""" <tr> \n""")





#Location of my intro blurb
target = 'Photos/photos_english.html'

#Pick a fake year that will be immediately changed
now = datetime.datetime.now()
myyear = '1999'

#This loads up all the subfolders in the 'Photos' folder
#If they are labeled 'YYYYMM' this will go in reverse chronological order
no_of_months = dict()
list_of_years = []

for i in reversed(os.walk('Photos').next()[1]):

    #Create a seperate page (that we will use as an iframe) for each subfolder
    page = open('Photos/%s/page.html' %i, 'w')
    page.write("""<style>\n""")
    page.write(""".album{height:150px;border:solid 1px #999;margin:5px;\n -webkit-filter: grayscale(0) !important; filter: grayscale(0) !important; height:140px;border:solid 1px #999;margin:3px;}\n""")
    page.write(""".album:hover{height:150px;border:solid 1px #999;margin:5px;\n -webkit-filter: grayscale(50%) !important;filter: grayscale(50%) !important; height:140px;border:solid 1px #999;margin:3px;}\n""")
    page.write("""</style>\n<center>""")
		
    #Load up the year and month from the subfolder's name
    year = i[0:4] ; month = i[4:6]	
    #If we get onto a new year, print a header
    if year != myyear:
        myyear = year
        list_of_years.append(year)
        no_of_months[year] = 1
    else:
        no_of_months[year] += 1

    #Use the first photo as the thumbnail for the album(default)
    thumb = os.listdir('Photos/%s' %i)[0]

    #Cycle through each photo in the directory
    for j in os.listdir('Photos/%s' %i):
        #Ignore the page file we already created or any stray thumbnails
        if 'page' in j or 'small' in j:
            break

        im_resize = Image.open('Photos/%s/%s' %(i, j))
        imwidth, imheight = im_resize.size


        if imwidth > 1790 or imheight > 1790:
            max_size = 1780.0
            new_size = np.round(min(max_size/imwidth, max_size/imheight)*np.array((imwidth, imheight)))
            im_resize.thumbnail(new_size)


        im_resize.save('Photos/%s/%s' %(i, j))



        if make_thumbnails == 'yes':

            #Check if a thumbnail has already been generated for this photo
            if not path.exists("Photos/%s/thumbnails/small_%s" %(i, j)):
					
                """ Generate the thumbnail if it doesn't exist """
					
                #Open image
                im = Image.open('Photos/%s/%s' %(i, j))


                #Load up image size
                imwidth, imheight = im.size

                #If the photo is portrait, we still want the thumbnail to be landscape
                if imwidth > imheight:
                    mybox = (0,0,imwidth, int(imwidth/1.7))
                else:
                    mybox = (0,int(imheight/5),imwidth,int(imwidth/1.7)+int(imheight/5))
                
                #Crop photo
                im = im.crop(box=mybox)

                #Rescale
                im.thumbnail((400,200))

                #im = im.convert(mode="L")
					
                #Create a 'thumbnails' folder if necessary
                if not os.path.exists('Photos/%s/thumbnails/' %(i)):
                    os.mkdir('Photos/%s/thumbnails/' %(i))
					
                #Save thumbnail
                im.save('Photos/%s/thumbnails/small_%s' %(i, j))
			
        #Add each photo to the subfolder's page
        page.write("""<a href="%s" target="_blank"><img src="thumbnails/small_%s" class="album"></a>""" %(j,j))	
			
        #If a photo has been designated as the album thumbnail, replace the default thumbnail
        if 'thumbnail' in j:
            thumb = j

    #Close the subfolder's page
    page.close()


for year in list_of_years:
    f.write(""" \n <td colspan=%s style="background-color:#fff; border-left: solid 8px #897A93; padding-left:5px;"> <h2>%s</h2> </td> """ %(no_of_months[year], year))
f.write("""</tr> """)
f.write(""" \n \n <tr style="background-color:#897A93;"> \n \n""")

for i in reversed(os.walk('Photos').next()[1]):

    f.write("""<td> \n """)
    f.write("""<div class="monthlinks"> \n""")

    thumb = os.listdir('Photos/%s' %i)[0]
    for j in os.listdir('Photos/%s' %i):
        if 'page' in j or 'small' in j:
            break
        if 'thumbnail' in j:
            thumb=j

    f.write(""" <a href="Photos/%s/page.html" target="pictureframe" class="photolinks"> \n """ %i)
    f.write(""" <img src="Photos/%s/thumbnails/small_%s" style="width:180px;border: solid 1px black;" class="myphotos"><br>\n """ %(i, thumb))
    month = i[4:6]
    f.write(""" %s</a></div></td> \n""" %english[month])

f.write(""" </tr></table></div>""")
#Load up iframe
f.write("""<iframe name="pictureframe" src='%s' frameBorder="0" width="100%%" style="overflow:visible;height:4000px;"></iframe><br><br></td></tr></table> \n """ %(target))

f.write("""</ul></div>""")

f.write("<br><font size=4>All photos are free for personal use, but please give credit back to this site and consider a donation to <a href='https://www.refuweegee.co.uk/'>Refuweegee</a> if you use them.</font>")


f.write("""</center>""")
f.write("""</div>""")
f.write("""<br><br>""")
f.write("""<br><br>""")
f.write("""<br><br>""")
f.write("""<div id="footerdiv">""")
f.write("""<iframe id="footer" src="footer.htm" frameBorder="0" scrolling="no"></iframe>""")
f.write("""</div>""")
f.write("""</body>""")
f.write("""</html>""")

#Close pages
f.close()


#Write my intro bio
f_2 = open('Photos/photos_english.html', 'w')

f_2.write("""<style>\n""")
f_2.write("""body{font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif; font-size:15px;}\n""")
f_2.write("""</style>\n""")
f_2.write(""" <center> """)
#k.write(""" <img src="P1010006.jpg" style="width:300px; border: solid 1px black; float:right; margin:10px;"><br><br> """)

f_2.write(""" <b><br><br> 
Pictures will appear here.</b><br><br>
The script I use to generate this album can be found <a href="https://github.com/amberlennox/websitescripts/blob/master/photographypage.py" target="_blank">here</a>.<br><br>""")
f_2.close()


