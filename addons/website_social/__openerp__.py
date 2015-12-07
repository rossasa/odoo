# -*- encoding: utf-8 -*-
{
	'name': 'Website Sistema Social',
	'description': """

	Website de acuerdo a los patrones del Sistema Social

    """,
	'category': 'purchase',
	'author': 'Rossa S.A.',
	'website': 'http://www.sistema.social',
	'version': '0.1',
	'depends': [
		'website',
	],
	'data': [
		#'security/groups.xml',
		#'security/ir.model.access.csv',
		'views/website_menu.xml',
	],
	'installable': True,
	'application': False,
	'auto_install': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
