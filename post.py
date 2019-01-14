import requests
import os
import datetime
# print('##########################')
# ch = input('Tracker[T] or Checker[C] => ')

# seri ="Bp0Fqh-Bfu4"
def post_l(seri):
	ig_t = 'ig/'+seri+'.txt'
	if os.path.exists(ig_t):
  		os.remove(ig_t)
	r = requests.get("https://www.instagram.com/p/"+seri+"/")
	f = open(ig_t,'x', encoding="utf-8")
	f.write(r.text)
	fx = open('data.txt', 'a')
	i = 0
	w = open(ig_t, 'r',encoding="utf-8")
	T = str(datetime.datetime.now().time())
	while i<33000:
		y = w.readline(i)
		i+=1
		# print(i,'===>',y)
		if "Likes" in y or "mentions J’aime" in y :
			i+=34000
			fls=y[19:40]
			print(fls)
			fx.write('\n'+fls+" At =>> "+T)
			print('##########################')
			f.close()
			w.close()
			os.remove(ig_t)
	post_l(seri)
# while 0<1:
# 	post_l(seri)

# if ch == "T":
# 	while 0<1:
# 		follow(seri)
# elif ch == "C":
# 	follow(seri)

