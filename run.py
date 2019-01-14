import insta
import post
o = input("Do you wanna check an Account [A] or a Post [P] : ")
if o == 'A' or o == 'a':
	ch = input('Tracker[T] or Checker[C] => ')
	ig = input('Enter Your Ig Name => ')
	insta.go(ch, ig)
elif o == 'P' or o == 'p':
	seri = input('Enter The post id => ')
	post.post_l(seri)
else:
	leave = input("Press ENTER TO LEAVE .....")

