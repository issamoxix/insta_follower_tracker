# from lxml import html
# import requests
# web_s=input('====>')
# page = requests.get(web_s)
# tree = html.fromstring(page.content)
# abn = tree.xpath('//span[@class="g47SY "]/text()')
# print(abn)
# #print(tree.xpath('//h1[@class="AC5d8 notranslate"]/text()'))
import requests
import os
# print('##########################')
# ch = input('Tracker[T] or Checker[C] => ')
# ig = input('Enter Your Ig Name => ')
def follow(ig):
	ig_t = 'ig/'+ig+'.txt'
	r = requests.get("https://www.instagram.com/"+ig+"/")
	f = open(ig_t,'x', encoding="utf-8")
	f.write(r.text)
	i = 0
	w = open(ig_t, 'r', encoding="utf-8")
	while i<4000:
		y = w.readline(i)
		i+=1
		if "Followers" in y:
			i+=4000
			fls=y[23:37]
		# print(y)
			print(fls)
			print('##########################')

# que= input('Do u wanna keep The file ? y/n => ')
# if que !='y':
	f.close()
	w.close()
	os.remove(ig_t)

def go(ch, ig):
	if ch == "T":
		while 0<1:
			print('##########################')
			follow(ig)
			
	elif ch == "C":
		print('##########################')
		follow(ig)


