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

gaelic = {
  "01": "Am Faoilteach",
  "02": "An Gearran",
  "03": "Am M&agrave;rt",
  "04": "An Giblean",
  "05": "An C&egrave;itean",
  "06": "An t-&Ograve;gmhios",
  "07": "An t-Iuchar",
  "08": "L&ugrave;nasdal",
  "09": "An t-Sultain",
  "10": "An D&agrave;mhair",
  "11": "An t-Samhain ",
  "12": "An D&ugrave;bhlachd"
}

#Open a html file in the English page location
h = open('photos.html', 'w')
#Print general CSS information
h.write("""<!DOCTYPE html>\n""")

h.write("""<style>\n""")
h.write("""@import "main.css"\n""")
h.write("""</style>\n""")

h.write("""<script\n""")
h.write("""    src="https://code.jquery.com/jquery-3.3.1.js" \n""")
h.write("""    integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60=" \n""")
h.write("""    crossorigin="anonymous"> \n""")
h.write("""</script> \n""")

h.write("""<script>\n""")
h.write("""$(function(){\n""")
h.write("""  $("#header").load("header.htm"); \n""")
h.write("""  $("#footer").load("footer.htm"); \n""")
h.write("""}); \n""")
h.write("""</script> \n""")

h.write("""<title>Amber Leamhnachd's Webpage</title>\n""")
h.write("""<html>\n""")
h.write("""<body>\n""")
	
#My header that I use
h.write("""<div id="header"></div>\n""")


h.write("""<br>\n""")

#Open main div
h.write("""<div class="main">\n""")
h.write("""<br>\n""")
h.write("""<center>\n""")
	
#Open text div
h.write("""<div class="mytext">\n""")
h.write("""<center>\n""")

# Write the arrows at the top
h.write(""" <table width=100%><td align="left"><<</td><td align="right"> >> </td> </table> """)

#Generate table
h.write(""" <div style="overflow-x:scroll; overflow-y:hidden;scrollbar-width: none;-ms-overflow-style: none;">""")
h.write(""" <table style=" overflow:auto;" border=0><tr> """)
h.write(""" <td colspan=5 style="background-color:#fff; border-left: solid 8px #897A93; padding-left:5px;">  """)

#Location of my intro blurb
target = 'Photos/photos_english.html'

#Current year
now = datetime.datetime.now()
myyear = str(now.year)


#------------------------------CHANGE THIS SECTION TO MY DIV
#------------------------------I NEED TO WORK OUT HOW TO PRINT YEARS CAUSE I'M DOING IT SLIGHTLY DIFFERENTLY NOW
		

#Print Current Year
h.write(""" <h2>%s</h2> </td> """ %myyear)

	#This loads up all the subfolders in the 'Photos' folder
	#If they are labeled 'YYYYMM' this will go in reverse chronological order
	for i in reversed(os.walk('Photos').next()[1]):
		
		#Create a seperate page (that we will use as an iframe) for each subfolder
		page = open('Photos/%s/page.html' %i, 'w')
		page.write("""<style>\n""")
		page.write(""".album{height:150px;border:solid 1px #999;margin:5px;\n -webkit-filter: grayscale(0) !important;
	filter: grayscale(0) !important; height:140px;border:solid 1px #999;margin:3px;}\n""")
		page.write(""".album:hover{height:150px;border:solid 1px #999;margin:5px;\n -webkit-filter: grayscale(50%) !important;
	filter: grayscale(50%) !important; height:140px;border:solid 1px #999;margin:3px;}\n""")
		page.write("""</style>\n<center>""")
		
		#Load up the year and month from the subfolder's name
		year = i[0:4] ; month = i[4:6]	
		
		#If we get onto a new year, print a header
		if year != myyear:
			myyear = year
			h.write("""</ul>\n <center><h2>%s</h2></center>\n \n <ul class="monthul">\n """ %myyear)

		#Use the first photo as the thumbnail for the album(default)
		thumb = os.listdir('Photos/%s' %i)[0]

		#Cycle through each photo in the directory
		for j in os.listdir('Photos/%s' %i):
			#Ignore the page file we already created or any stray thumbnails
			if 'page' in j or 'small' in j:
				break

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

		#Write the navigational list of albums
		h.write("""<li class="monthlinks"><a href="Photos/%s/page.html" target="pictureframe" class="photolinks"> """ %(i))
		h.write("""<img src="Photos/%s/thumbnails/small_%s" style="width:180px;border: solid 1px black;" class="myphotos"><br>\n""" %(i,thumb)) 
		h.write("""%s</a></li>\n""" %(english[month]))

		#Close the subfolder's page
		page.close()

	#Insert my footer
	h.write("""</ul>""")
	h.write("""</td><td class="photo_background">""")

	#Load up iframe
	h.write("""<iframe name="pictureframe" src='%s' frameBorder="0" width="100%%" style="overflow:auto;height:500px;"></iframe><br><br></td></tr></table> \n """ %(target))
	
	h.write("""</ul></div>""")

	if h == f:
		f.write("<br><font size=4>All photos are free for personal use, but please give credit back to this site and consider a donation to <a href='https://www.refuweegee.co.uk/'>Refuweegee</a> if you use them.</font>")
	if h == g:
		g.write("<br><font size=4>Tha a h-uile dealbhan saor, ach cuir mo ainm orra, agus thoir airgead gu <a href='https://www.refuweegee.co.uk/'>Refuweegee</a> ma 's toil leat.</font>")

	h.write("""</center>""")
	h.write("""</div>""")
	h.write("""<br><br>""")
	h.write("""<br><br>""")
	h.write("""<br><br>""")
	h.write("""<div id="footerdiv">""")
	h.write("""<iframe id="footer" src="footer.htm" frameBorder="0" scrolling="no"></iframe>""")
	h.write("""</div>""")
	h.write("""</body>""")
	h.write("""</html>""")

#Close pages
f.close()
g.close()


#Write my intro bio
f_2 = open('Photos/photos_english.html', 'w')
g_2 = open('Photos/photos_gaelic.html', 'w')
for k in f_2, g_2:
	k.write("""<style>\n""")
	k.write("""body{font-family: "Palatino Linotype", "Book Antiqua", Palatino, serif; font-size:15px;}\n""")
	k.write("""</style>\n""")
	k.write(""" <center> """)
	#k.write(""" <img src="P1010006.jpg" style="width:300px; border: solid 1px black; float:right; margin:10px;"><br><br> """)
	if k == f_2:
		f_2.write(""" <b><br><br> 
Pictures will appear here.</b><br><br>
The script I use to generate this album can be found <a href="https://github.com/amberlennox/websitescripts/blob/master/photographypage.py" target="_blank">here</a>.<br><br>""")
	if k == g_2:
		g_2.write(""" <b><br><br> Bidh dealbhan an-seo.  """)
f_2.close()
g_2.close()

