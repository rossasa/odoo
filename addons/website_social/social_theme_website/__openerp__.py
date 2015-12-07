{
'name': 'Tema Website Social',
'author': 'Rossa S.A.',
'category': 'Hidden',
'version': '8.0.1.0',
'description':
"""
Tema para el sitioweb del Sistema Social.
========================
This module apply the Social theme for the website
""",
'depends': [
	'website',
	'social_theme',
],

'installable': True,
'auto_install': False,
'data' : [
		  'views/website_view.xml',
],
'test': [],
}
