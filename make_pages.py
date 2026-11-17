import os
import markdown


with open('infrastructure/navbar.txt') as h:
    header = h.read()


for file in os.listdir('pages'):
    with open('pages/'+file) as f:
        content = f.read()
    content = markdown.markdown(content)
    html_content = header+'\n\n<div id="content">\n\n'+content+'\n\n<div>'
    with open(os.path.splitext(file)[0]+'.htm', 'w') as g:
        g.write(html_content)

