{"changed":true,"filter":false,"title":"run.py","tooltip":"/run.py","value":"#!flask/bin/python\nfrom app import app\nimport os\napp.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))\n","undoManager":{"mark":9,"position":9,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":19},"action":"insert","lines":["#!flask/bin/python","from app import app","app.run(debug=True)"],"id":1}],[{"start":{"row":2,"column":19},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"insert","lines":["app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))",""],"id":3}],[{"start":{"row":2,"column":8},"end":{"row":2,"column":18},"action":"remove","lines":["debug=True"],"id":4}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":18},"action":"insert","lines":["debug=True"],"id":5}],[{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":[","],"id":6}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["app.run()",""],"id":7}],[{"start":{"row":1,"column":19},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":["i"],"id":9}],[{"start":{"row":2,"column":1},"end":{"row":2,"column":9},"action":"insert","lines":["mport os"],"id":10}],[{"start":{"row":3,"column":0},"end":{"row":4,"column":0},"action":"remove","lines":["app.run(debug=True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))",""],"id":15}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":4,"column":0},"end":{"row":4,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1528505353049}