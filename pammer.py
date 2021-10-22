import requests
def auto():
	for x in range(1000):
		try:
			pos = {'email': sen, 'password': sen, 'fb': sen, 'phone': sen, 'gmail': sen, 'country': sen, 'email1': sen, 'password1': sen, 'email2': sen, 'password2': sen, 'pw': sen, 'pass': sen, 'user': sen, 'nick': sen, 'id': sen, 'level': sen, 'city': sen, 'th': sen, 'growtopiaid': sen, 'skin': sen, 'nickname': sen, 'vk': sen, 'vkpass': sen, 'vkid': sen, 'vkpw': sen, 'emailr': sen, 'recovery': sen, 'moonton1':sen, 'moonton2': sen, 'th': sen, 'coc': sen, 'fb1': sen, 'fb2': sen, 'google': sen, 'google1': sen, 'google2': sen, 'vk1': sen, 'vk2': sen, 'login': sen, 'hp': sen, 'lvl': sen}
			r = requests.post('http://'+link, data=pos)
			crot = r.text
			code = ("24 hours", "verif", "phone", "account", "logout", "moonton", "supercell", "diamond", "your", "skin")
			gg = "thePriVat"
			if not gg in crot:
				print '\033[92mspammer successfuly - '+str(x)+'\033[0m'
			else:
				print '\033[91mspammer failed - '+str(x)+'\033[0m'
		except KeyboardInterrupt:
			print '\nTools spammer phising stoped'
			exit()
		except:
			print ''; print '\033[91mConection Time Out! Progam Stoped\033[0m'; exit()

def manual():
	for x in range(1000):
		try:
			pos = {hmm: sen}
			crot = r.text
			r = requests.post('http://'+link, data=pos)
			code = ("24 hours", "verif", "phone", "account", "logout", "moonton", "supercell", "diamond", "your", "skin")
			gg = "thePriVat"
			if not gg in crot:
				print '\033[92mspammer successfuly - '+str(x)+'\033[0m'
			else:
				print '\033[91mspammer failed - '+str(x)+'\033[0m'
		except KeyboardInterrupt:
			print '\nTools spammer phising stoped'
			exit()
		except:
			print ''; print '\033[91mConection Time Out! Progam Stoped\033[0m'; exit()

print '''\033[94m
		\_   _/
		| |_| |
 _______________|     |______________
|____________________________________|
|tools: spammer phising V 1.0  	     |
|code: python - version 2.7.10++     |
|github: http://github.com/theprivat |
|cretor: thePriVat		     |
|____________________________________|
|_____theprivat@khoirulrisqi.com_____|
\033[0m'''
link = raw_input('Link: ')
sen = raw_input('Messege: ')
para = raw_input('Auto parameter or manual? [Y/n]: ')
if para.lower() == 'y' or para.lower() == 'Y':
	auto()
elif para.lower() == 'n'or para.lower() == 'N':
	hmm = raw_input('parameter: ')
	print
	manual()
else:
	print 'Not Found'
	exit()

