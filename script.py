import requests 
import os 
from sys import argv 


def main():
	if len(argv) == 1 :
		print('''
			Por favor, use o comando fornecido abaixo...
			python dirbust.py url wordlist
			exemplo:
			python dirbust.py http://example.com/ wordlist.txt /
			''')
	elif len(argv) == 2:
		if argv[1][len(argv[1])-4:len(argv[1])] == '.txt':
			print('\t\t\tPor favor, forneça o url de um site antes da lista de palavras.')
		else:
			print('\t\t\tPor favor, insira o link da lista de palavras após o url.')
	elif len(argv) == 3:
		dirb(str(argv[1]),"/"+str(argv[2]))
	else:
		print('''
			Você digitou o comando no formato errado.
			Por favor, use o comando fornecido abaixo...
			python dirbust.py url wordlist
			exemplo:
			python dirbust.py http://example.com/ wordlist.txt/
			''')


def dirb(urls,wordlist):
	arr=[]
	url=urls
	try:
		if url[:7] != 'http://':
			url="http://"+url
		r=requests.get(url)
		if r.status_code == 200:
			print('Host is up.')
		else:
			print('Host is down.')
			return
		if os.path.exists(os.getcwd()+wordlist):
			fs=open(os.getcwd()+wordlist,"r")
			for i in fs:
				print(url+"/"+i)
				rq=requests.get(url+"/"+i)
				if rq.status_code == 200:
					print(">OK".rjust(len(url+"/"+i)+5,'-'))
					arr.append(str(url+"/"+i))
				else:
					print(">404".rjust(len(url+"/"+i)+5,'-'))
			fs.close()
			print("output".center(100,'-'))
			l=1
			for i in arr:
				print(l, "> ", i)
				l+=1
		else:
			print(wordlist+" não existe no diretório.")
	except Exception as e:
		print(e)



if __name__ == '__main__':
	main()
