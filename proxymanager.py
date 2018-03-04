from utils import*
import random
formattedProxies =  []

def getProxy(tasknum,formattedProxies):
	if tasknum + 1 <= len(formattedProxies):
		a= tasknum
	elif tasknum + 1 > len(formattedProxies):
		if len(formattedProxies) > 1:
			a = tasknum%len(formattedProxies)
		elif len(formattedProxies) == 1:
			a = 0
		else:
			a = int(random.randrange(0, len(formattedProxies) - 1))
			log('Couldnt get proxy... choosing random proxy')
	else:
		a=int(random.randrange(0,len(formattedProxies)-1))
		log('Couldnt get proxy... choosing random proxy')
	proxy = formattedProxies[a]
	# print(proxy)
	return proxy


def chooseProxy(tasknum):
	if tasknum + 1 <= len(proxieslines):
		proxy = proxieslines[tasknum].rstrip()
	if tasknum + 1 > len(proxieslines):
		if len(proxieslines) > 1:
			a = random.randint(1, len(proxieslines) - 1)
		if len(proxieslines) == 1:
			a = 0
		proxy = proxieslines[a].rstrip()
	try:
		proxytest = proxy.split(":")[2]
		userpass = True
	except IndexError:
		userpass = False
	if userpass == False:
		proxyedit = proxy
	if userpass == True:
		ip = proxy.split(":")[0]
		port = proxy.split(":")[1]
		userpassproxy = ip + ':' + port
		proxyedit = userpassproxy
		proxyuser = proxy.split(":")[2]
		proxyuser = proxyuser.rstrip()
		proxypass = proxy.split(":")[3]
		proxyuser = proxyuser.rstrip()
	if userpass == True:
		proxies = {'http': 'http://' + proxyuser + ':' + proxypass + '@' + userpassproxy,
				   'https': 'https://' + proxyuser + ':' + proxypass + '@' + userpassproxy}
	if userpass == False:
		proxies = {'http': 'http://' + proxy,
				   'https': 'https://' + proxy}
	global formattedProxies
	formattedProxies.append(proxies)

def importProxies(proxyfile):
	p = open('{}.txt'.format(proxyfile))
	global proxieslines
	proxieslines = p.readlines()
	numproxies = len(proxieslines)
	global formattedProxies
	if numproxies > 0:
		formattedProxies = []
		for i in range (0,len(proxieslines)):
			chooseProxy(i)
	if numproxies == 0:
		formattedProxies = [None]
	# print(formattedProxies[0])
	log('%s proxies loaded' % numproxies)
	return formattedProxies

