{"filter":false,"title":"rock.py","tooltip":"/rock.py","undoManager":{"mark":24,"position":24,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":64},"action":"insert","lines":["cd: /thnkful/projects/prate_bartendar: No such file or directory"],"id":1}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":64},"action":"remove","lines":["cd: /thnkful/projects/prate_bartendar: No such file or directory"],"id":2},{"start":{"row":0,"column":0},"end":{"row":39,"column":19},"action":"insert","lines":["import random","","# globals","","questions = {","    \"strong\": \"Do ye like yer drinks strong?\",","    \"salty\": \"Do ye like it with a salty tang?\",","    \"bitter\": \"Are ye a lubber who likes it bitter?\",","    \"sweet\": \"Would ye like a bit of sweetness with yer poison?\",","    \"fruity\": \"Are ye one for a fruity finish?\"","}","","ingredients = {","    \"strong\": [\"glug of rum\", \"slug of whisky\", \"splash of gin\"],","    \"salty\": [\"olive on a stick\", \"salt-dusted rim\", \"rasher of bacon\"],","    \"bitter\": [\"shake of bitters\", \"splash of tonic\", \"twist of lemon peel\"],","    \"sweet\": [\"sugar cube\", \"spoonful of honey\", \"spash of cola\"],","    \"fruity\": [\"slice of orange\", \"dash of cassis\", \"cherry on top\"]","}","","","# functions","","def drink_pref():","    \"\"\"I collect the user's drink pref and put it into a new dictionary\"\"\"","    preferences = {}","    for key, value in questions.items():","        user_input = input(value + \" \")","        preferences[key] = (user_input == \"y\" or user_input == \"yes\")","    return preferences","","","def mix_the_drink(value):","    \"\"\"I now use the user preferences captured in the responses dict","    and make a delicious drink\"\"\"","    my_drink = []","    for key, value in value.items():","        if value is True:","            my_drink.append(random.choice(ingredients[key]))","    return my_drink"]}],[{"start":{"row":21,"column":0},"end":{"row":21,"column":11},"action":"remove","lines":["# functions"],"id":3}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":9},"action":"remove","lines":["","# globals"],"id":4}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":5}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":13},"action":"remove","lines":["import random"],"id":6}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"remove","lines":["",""],"id":7}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"remove","lines":["",""],"id":8}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":9}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["n"],"id":10}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"],"id":11}],[{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"],"id":12}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"],"id":13}],[{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"],"id":14}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":15}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["r"],"id":16}],[{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["a"],"id":17}],[{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["n"],"id":18}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["d"],"id":19}],[{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["o"],"id":20}],[{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["m"],"id":21}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":["n"],"id":22}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":[","],"id":23}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"remove","lines":[","],"id":24}],[{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"],"id":25}]]},"ace":{"folds":[],"scrolltop":401.5,"scrollleft":0,"selection":{"start":{"row":7,"column":47},"end":{"row":7,"column":47},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":20,"state":"start","mode":"ace/mode/python"}},"timestamp":1451941999921,"hash":"c2177d8d6a3fc71f2a2be982250fa2c514bdbeac"}