{
'name': 'Web Sistema Social',
'author': 'Rossa S.A.',
'category': 'Hidden',
'version': '8.0.1.0',
'description':
"""
Web Del Sistema Social.
========================
Este modulo aplica el tema del sistema social
""",
'depends': [
	'web',
],
'data' : [
	'theme.xml',
	'views/webclient_templates.xml'],
'qweb' : [
    "static/src/xml/*.xml",
],
'test': [],
'installable': True,
'auto_install': True,
}
