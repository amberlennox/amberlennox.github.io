function getReminder() {
  console.log('Water the plants.');
}
 
 function get_combo() {
   random_preposition = Math.floor(Math.random() * prepositions.length)
   random_pronoun = 1+ Math.floor(Math.random() * 7)
   preposition = prepositions[random_preposition][0]
   //console.log(preposition)
   pronoun = pronouns[random_pronoun]
   //console.log(pronoun)
   prep_pronoun = prepositions[random_preposition][random_pronoun]
   //console.log(prep_pronoun)
   url = ('pronouns/'+(preposition)+'/'+prep_pronoun+'.mp3')
   //console.log(url)
   return [preposition, pronoun, prep_pronoun, url]
 }

 aig = ['aig', 'agam', 'agad', 'aige', 'aice', 'againn', 'agaibh', 'aca']
    air = ['air', 'orm', 'ort', 'air', 'oirre', 'oirnn', 'oirbh', 'orra']
    ann = ['ann', 'annam', 'annad', 'ann', 'innte', 'annainn', 'annaibh', 'annta']
    as1 = ['às', 'asam', 'asad', 'às', 'aiste', 'asainn', 'asaibh', 'asta']
    bho = ['bho', 'bhuam', 'bhuat', 'bhuaithe', 'bhuaipe', 'bhuainn', 'bhuaibh', 'bhuapa']
    de = ['de', 'dhìom', 'dhìot', 'dheth', 'dhith', 'dhinn', 'dhibh', 'dhiubh']
    do1 = ['do', 'dhomh', 'dhut', 'dha', 'dhi', 'dhuinn', 'dhuibh', 'dhaibh']
    fo = ['fo','fodham', 'fodhad', 'fodha', 'foidhpe', 'fodhainn', 'fodhaibh', 'fodhpa']
    gu = ['gu', 'thugam', 'thugad', 'thuige', 'thuice', 'thugainn', 'thugaibh', 'thuca']
    le = ['le', 'leam', 'leat', 'leis', 'leatha', 'leinn', 'leibh', 'leotha']
    mu = ['mu', 'umam', 'umad', 'uime', 'uimpe', 'umainn', 'umaibh', 'umpa']
    o = ['o', 'uam', 'uat', 'uaithe', 'uaipe', 'uainn', 'uaibh', 'uapa']
    ri = ['ri', 'rium', 'riut', 'ris', 'rithe', 'rinn', 'ribh', 'riutha']
    ro = ['ro', 'romham', 'romhad', 'roimhe', 'roimhpe', 'romhainn', 'romhaibh', 'romhpa']
    thar = ['thar','tharam', 'tharad', 'thairis', 'thairte', 'tharainn', 'tharaibh', 'tharta']
    tro = ['tro', 'tromham', 'tromhad', 'troimhe', 'troimhpe', 'tromhainn', 'tromhaibh', 'tromhpa']



prepositions = [as1]
pronouns = ['pronoun', 'mi', 'thu', 'e', 'i', 'sinn', 'sibh', 'iad']

console.log(prepositions.length)
console.log(get_combo())

const preposition = document.querySelector('preposition');
preposition.textContent = 'air';
const pronoun = document.querySelector('pronoun');
pronoun.textContent = 'mi';
//var name = window.prompt("Enter your name: ");
//alert("Your name is " + name);
