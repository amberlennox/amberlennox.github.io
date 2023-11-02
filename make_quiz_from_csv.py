import csv
import numpy as np
import sys

input_file = 'sampleworkbook.csv'


def detect_entry(list_in, input_string, row):
    input_string = input_string.upper()
    if input_string in (name.upper() for name in row):
        for entry in np.arange(0, len(row), 1):
            if input_string in row[entry].upper():
                list_in.append(row[entry+1])
    return list_in

def test_entry(entry, name):
    if len(entry) == 0:
        print('ERROR: No %s detected' %name)
        sys.exit()
    if len(entry) > 1:
        print('ERROR: Multiple instances of %s detected' %name)
        sys.exit()
    return

title=[]
html_name = []
quiz_type = []
language = []

rows = dict()

array_detected = False
column_headers = []
with open('sampleworkbook.csv', newline='', encoding='utf-8-sig') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:

        title = detect_entry(title, 'title', row)
        html_name = detect_entry(html_name, 'output', row)
        quiz_type = detect_entry(quiz_type, 'type', row)
        language = detect_entry(language, 'language', row)

        if 'TABLE' in row:
            array_detected = not array_detected
            if len(column_headers) == 0:
                for entry in np.arange(0, len(row), 1):
                    if row[entry] != '' and 'TABLE' not in row[entry] and row[entry] != '':
                        column_headers.append(row[entry])
        if array_detected == True and row[0] != 'TABLE' and row[0] != '':
            rows[row[0]] = dict()
            for entry in np.arange(1, len(row), 1):
                rows[row[0]][column_headers[entry-1]] = row[entry] 
 


            
    test_entry(title, 'title')
    test_entry(html_name, 'output')
    test_entry(quiz_type, 'type')
    test_entry(language, 'language')




    print("Title of quiz: %s" %title[0])
    print("Output file: %s.htm" %html_name[0])
    print("Type of quiz: %s.htm" %quiz_type[0])
    print("Language of quiz: %s" %language[0])


    list_of_columns = column_headers[0]
    for column in column_headers[1:]:
        list_of_columns = list_of_columns + ', ' + column

    list_of_rows = ''
    for row in rows.keys():
        if list_of_rows == '':
            list_of_rows = row
        else:
            list_of_rows = list_of_rows + ', ' + row

    print("\n Table detected with the following:")
    print("Columns: ", list_of_columns)
    print("Rows: ", list_of_rows)

    meta_dict = dict()

    for column in np.arange(0, len(column_headers), 1):
        if '_' in column_headers[column]:
            meta_categories = []
            meta_nicknames = []
            i = 1
            print('\n Meta type detected: %s' %column_headers[column])
            for key in rows.keys():
                if (rows[key][str(column_headers[column])]) not in meta_categories:
                    meta_categories.append(rows[key][str(column_headers[column])])
                    meta_nicknames.append('meta%s' %i)
                    meta_dict[rows[key][str(column_headers[column])]] = 'meta%s' %i
                    i += 1
                    
    print('Detected meta categories: %s' %meta_categories)
    print('Assigning meta nicknames: %s' %meta_nicknames)

    print('\n Finished accessing csv file')
    print('Proceeding to HTML/Javascript generation')

f = open('quizzes/gaelic_quizzes/%s.htm' %html_name[0], 'wb')

f.write(u'''
<!DOCTYPE html> 
<style>
    @import "../../main.css";

    .table_title{border: solid 1px black; padding:5px; background-color:#fff;font-size:20px;width:150px; text-align:center;}
    .pronoun_cell{padding:5px}

    .explanation{background-color:rgba(255, 255, 255, 0.5); padding-left:10px;font-size:17px;}
    .accentbutton{background-color: #6b244a; color: #FFFFFF; padding: 10px;border-radius: 10px;margin:10px; font-size:20px;}

    input[type=checkbox] {width:20px; height:20px;}

    .submitandhint{background-color: #8a4168;color: #FFFFFF;padding: 10px;border-radius: 10px;-moz-border-radius: 10px;-webkit-border-radius: 10px;margin:10px; font-size:20px;}

    #app{background-color:rgba(255, 255, 255, 0.5);padding: 10px;border-radius: 10px;-moz-border-radius: 10px;-webkit-border-radius: 10px;margin:10px; font-size:20px;}
    #answer{ font-size:20px;}
</style>

<script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="crossorigin="anonymous"></script>

<script> 
    $(function(){
        $("#header").load("../../header.htm"); 
        $("#footer").load("../../footer.htm"); 
    });
</script> '''.encode('utf8'))

f.write((u'''
        
<title>%s</title> 

''' %title[0]).encode('utf8'))
f.write(u''' 
<html>

<body onload="new_saveddata()">
<div id="header"></div>

<br>

<meta charset="utf-8">

<div class="main">
<br>

<center>
<div class="mytext">
<center>

<!-- BLURB GOES HERE --!>

'''.encode('utf8'))

f.write((u'''<h1> %s </h1>''' %title[0]).encode('utf8'))

f.write(u''' 
        
<div>

<form name="theQuiz" onsubmit="return validateAnswer()" action="">
<br>

<br>
<font size="6"><noun></noun> @ <pronoun></pronoun> = ?</font>
<br><br>
<input type="text" name="answer" id="answer" autofocus="autofocus"> <br><result></result>
<br>
<button type="submit" class="submitandhint">Submit</button> <button type="button" onclick="giveHint()" class="submitandhint">Hint</button> 
<font size="3"><br><hint></hint> </font>
</form><br>
'''.encode('utf8'))


if language[0].lower() == 'gaelic':
    f.write(u'''  
    <button type="button" onclick="return add_a()" class="accentbutton">à</button>
    <button type="button" onclick="return add_e()" class="accentbutton">è</button>
    <button type="button" onclick="return add_i()" class="accentbutton">ì</button>
    <button type="button" onclick="return add_o()" class="accentbutton">ò</button>
    <button type="button" onclick="return add_u()" class="accentbutton">ù</button>
    '''.encode('utf8'))

if language[0].lower() == 'welsh':
    f.write(u'''  
    <button type="button" onclick="return add_a()" class="accentbutton">â</button>
    <button type="button" onclick="return add_e()" class="accentbutton">ê</button>
    <button type="button" onclick="return add_i()" class="accentbutton">î</button>
    <button type="button" onclick="return add_o()" class="accentbutton">ô</button>
    <button type="button" onclick="return add_u()" class="accentbutton">û</button>
    <button type="button" onclick="return add_w()" class="accentbutton">ŵ</button>
    <button type="button" onclick="return add_y()" class="accentbutton">ŷ</button>
    '''.encode('utf8'))

if language[0].lower() == 'finnish':
    f.write(u'''  
    <button type="button" onclick="return add_a()" class="accentbutton">ä</button>
    <button type="button" onclick="return add_o()" class="accentbutton">ö</button>
    '''.encode('utf8'))

f.write(u''' 
        <br><br>
        <font size=5>Test me on: </font>  
        <br><br>
        '''.encode('utf8'))

for i in np.arange(0, len(meta_categories), 1):
    f.write((u''' 
    <label for="%s"><b>%s: </b></label> <input type="checkbox" id="%s" onclick="checkBox('%s')"><br>  
    ''' %(meta_nicknames[i], meta_categories[i], meta_nicknames[i], meta_nicknames[i])).encode('utf8'))
    f.write((u''' 
 ''').encode('utf8'))
f.write((u''' 
<br>
<button onClick="window.location.reload();">Update</button>  ''').encode('utf8'))

f.write(u''' 
    <br><br>
    <table>
        <tr>
        '''.encode('utf8'))

f.write((u''' <td></td>''' ).encode('utf8'))
for column in column_headers:
    f.write((u''' <td class="table_title"><b>%s</b></td>''' %column).encode('utf8'))

f.write(u''' 
    </tr>
    '''.encode('utf8'))

for key in rows.keys():

    f.write((u''' <tr>
        <td class="table_title"><b>%s</b></td>''' %key).encode('utf8'))
    for entry in rows[key]:
        f.write((u''' <td class="table_entry"><b>%s</b></td>''' %rows[key][entry]).encode('utf8')) 
    f.write(u''' 
        </tr>
        '''.encode('utf8'))

f.write(u''' 
    </table>
        '''.encode('utf8'))


f.write(u''' 
    If you find this useful fire me an e-mail at arelennox@gmail.com and let me know! I want to make more similar programs for Gaelic (or other languages) - but only if it's a thing people actually use. If you have any issues or requests for other quizes, let me know that too. <br><br>
    The game is completely free, but consider a donation to <a href="https://www.refuweegee.co.uk/">Refuweegee</a> or <a href="https://scotland.shelter.org.uk/">Shelter Scotland</a> if you use it often.</b> </div>
        '''.encode('utf8'))


f.write(u''' 
    <script>
        '''.encode('utf8'))



if language[0].lower() == 'gaelic':
    f.write(u''' 
        function add_a() {
            insertAtCursor(document.getElementById("answer"), 'à')
                document.getElementById("answer").focus();
                }
function add_e() {
            insertAtCursor(document.getElementById("answer"), 'è')
                document.getElementById("answer").focus();
                }
function add_i() {
            insertAtCursor(document.getElementById("answer"), 'ì')
                document.getElementById("answer").focus();
                }
function add_o() {
            insertAtCursor(document.getElementById("answer"), 'ò')
                document.getElementById("answer").focus();
                }
function add_u() {
            insertAtCursor(document.getElementById("answer"), 'ù')
                document.getElementById("answer").focus();
                }
        '''.encode('utf8'))


if language[0].lower() == 'welsh':
    f.write(u''' 
        function add_a() {
	        insertAtCursor(document.getElementById("answer"), 'â')
	            document.getElementById("answer").focus();
                }
        function add_e() {
	        insertAtCursor(document.getElementById("answer"), 'ê')
	            document.getElementById("answer").focus();
                }
        function add_i() {
	        insertAtCursor(document.getElementById("answer"), 'î')
	            document.getElementById("answer").focus();
                }
        function add_o() {
	        insertAtCursor(document.getElementById("answer"), 'ô')
	            document.getElementById("answer").focus();
                }
        function add_u() {
	        insertAtCursor(document.getElementById("answer"), 'û')
	            document.getElementById("answer").focus();
                }
        function add_w() {
	        insertAtCursor(document.getElementById("answer"), 'ŵ')
	            document.getElementById("answer").focus();
                }
        function add_y() {
	        insertAtCursor(document.getElementById("answer"), 'ŷ')
	            document.getElementById("answer").focus();
                }
        '''.encode('utf8'))
    

if language[0].lower() == 'finnish':
    f.write(u''' 
        function add_a() {
	        insertAtCursor(document.getElementById("answer"), 'ä')
	            document.getElementById("answer").focus();
                }
        function add_o() {
	        insertAtCursor(document.getElementById("answer"), 'ö')
	            document.getElementById("answer").focus();
                }
        '''.encode('utf8'))


# PUT OTHER LANGUAGES HERE


f.write(u''' 

    function insertAtCursor(myField, myValue) {
        //IE support
        if (document.selection) {
            myField.focus();
            sel = document.selection.createRange();
            sel.text = myValue;
        }
        //MOZILLA and others
        else if (myField.selectionStart || myField.selectionStart == '0') {
            var startPos = myField.selectionStart;
            var endPos = myField.selectionEnd;
            myField.value = myField.value.substring(0, startPos)
                + myValue
                + myField.value.substring(endPos, myField.value.length);
            myField.selectionEnd = startPos + myValue.length;
        } else {
            myField.value += myValue;
        }
    }
        
        '''.encode('utf8'))


f.write(u'''
function new_saveddata() {        
'''.encode('utf8'))

for nickname in meta_nicknames:
    f.write((u'''
    for (i=0; i <%s.length; i++) {
        var data = window.localStorage.getItem('%s');
        if (data == 'true') {
            document.getElementById('%s').checked = true;
            if (! nouns.includes(%s[i])) {
                nouns.push(%s[i]);
                }
        } else {
            document.getElementById('%s').checked = false;
            if (nouns.includes(%s[i])) {
                var index = nouns.indexOf(%s[i]);
                nouns.splice(index, 1);
                }
        }
    }
    ''' %(nickname, nickname, nickname, nickname, nickname, nickname, nickname, nickname)).encode('utf8'))



f.write(u'''
    window.localStorage.setItem('nouns', nouns);
	newQuestion();
	return [nouns]; 
}
'''.encode('utf8'))

f.write(u''' 
function checkBox(mystring) {
    mybox = document.getElementById(mystring);
    if(mybox.checked === true){
        window.localStorage.setItem(mystring, true);
    } else {
        window.localStorage.setItem(mystring, false);
    }
}
function checkSelection(mystring) {
    mybox = document.getElementById(mystring);
    if(mybox.checked === true){
        window.localStorage.setItem(mystring, true);
    } else {
        window.localStorage.setItem(mystring, false);
    }
}



function validateAnswer() {
    var x = document.forms["theQuiz"]["answer"].value;
    x = x.toLowerCase();
    x = x.trim();
    const result = document.querySelector('result');
    if (x == a[2]) {
        result.style.color = "green";
        result.textContent = "Correct!";
        return true;    
    } else {    
        result.style.color = "red";
        result.textContent = "Not quite!";
        return false;
    }      
}


function newQuestion() {
    a = getCombo();
    noun1 = a[0];
    pronoun1 = a[1];
    const noun = document.querySelector('noun');
    noun.textContent = noun1;
    const pronoun = document.querySelector('pronoun');
    pronoun.textContent = pronoun1;
}

function giveHint() {
    hintno ++;
    const hint = document.querySelector('hint');
    hint.textContent = a[2].substr(0,hintno);
}


function getCombo() {
    var random_noun = Math.floor(Math.random() * nouns.length);
    var random_pronoun = (1 + Math.floor(Math.random() * 7));
    var noun = nouns[random_noun][0];
    var pronoun = pronouns[random_pronoun];
    var prep_pronoun = nouns[random_noun][random_pronoun]
    var url = '/pronouns/'+(noun)+'/'+prep_pronoun+'.mp3';
    return [noun, pronoun, prep_pronoun, url];
}

'''.encode('utf8'))

category_entries = dict()
for category in meta_nicknames:
    category_entries[category] = []

nickname  = dict()
i = 1
for key in rows.keys():
    nickname[key] = 'row%s' %(i)
    f.write((u'''
var %s''' %nickname[key]).encode('utf8'))
    i += 1
    f.write((u''' = [''' ).encode('utf8'))
    f.write((u'''"%s"''' %key).encode('utf8'))
    for entry in rows[key].keys():
        if '_' not in entry:
            f.write((u''', "%s"''' %rows[key][entry]).encode('utf8'))
        else:
            category_entries[meta_dict[(rows[key][entry])]].append(nickname[key])
    f.write((u'''];''' ).encode('utf8'))


f.write(u''' 

        '''.encode('utf8'))

for category in meta_categories:
    f.write((u'''
var %s = [''' %meta_dict[category]).encode('utf8'))
    first = True
    for entry in category_entries[meta_dict[category]]:
        if first==True:
            f.write((u'''%s''' %entry).encode('utf8'))
            first=False
        else:
            f.write((u''', %s''' %entry).encode('utf8'))
    f.write((u''']''').encode('utf8'))

f.write(u''' 

'''.encode('utf8'))

f.write(u'''var all_nouns = ['''.encode('utf8'))
first = True
for key in nickname.keys():
    if first==True:
        f.write((u'''%s''' %nickname[key]).encode('utf8'))
        first = False
    else:
        f.write((u''', %s''' %nickname[key]).encode('utf8'))

f.write((u''']
''' ).encode('utf8'))

f.write(u'''var all_strings = ['''.encode('utf8'))
first = True
for key in nickname.keys():
    if first==True:
        f.write((u'''"%s"''' %nickname[key]).encode('utf8'))
        first = False
    else:
        f.write((u''', "%s"''' %nickname[key]).encode('utf8'))

f.write((u''']
         
''' ).encode('utf8'))


f.write((u'''var hintno = 0;
var nouns = [];
   
''' ).encode('utf8'))


f.write((u'''var pronouns = ["pronoun"''' ).encode('utf8'))
for column in column_headers:
    if '_' not in column:
        f.write((u''', "%s"''' %column).encode('utf8'))
f.write((u''']''' ).encode('utf8'))


f.write(u''' 
    </script>
        '''.encode('utf8'))



f.close()

