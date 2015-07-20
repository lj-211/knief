#!/usr/bin/python
#--coding:utf-8--
import common.com_utils

import sys
import getopt

if __name__ == "__main__":
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'g:')
	except Exception, e:
		common.com_utils.print_error("argument error: " + str(e))
		sys.exit(0)

	user_name = ""
	for o, a in opts:
		if o in ('-g'):
			user_name = a

	if user_name == "":
		common.com_utils.print_error("没有输入正确的用户名")
		sys.exit(0)

	common.com_utils.print_red("用户名为: " + user_name)
	pwd = ""
	for c in user_name:
		pwd += str(ord(c))
	common.com_utils.print_notice("生成密码为: " + pwd);
