from __future__ import print_function
import re

class Utilities:
	words={}
	total=0
	threegrams={}
	def tokenize(self,f1):
		content=f1.read()
		listoftokens=re.findall(r"[\w+]+['-]*[\w+]*",content)
		print("Here are the tokens")
		for i in listoftokens:
			if i.lower() in self.words:
				self.words[i.lower()]+=1
				self.total+=1
			else:
				self.words[i.lower()]=1
				self.total+=1
		return

	def display(self):
		for i in self.words:
			print("\'"+i+"\'"+" occured",self.words[i],"times")
		print("Total tokens:",self.total)
		return

	def three(self,f1):
		print("Welcome to three grams")
		content=f1.read()
		listoftokens=re.findall(r"[\w+]+['-]*[\w+]*",content)
		total=len(listoftokens)
		i=0
		nogram=0
		while i<total-2: 
			grams=" ".join(listoftokens[i:i+3])
			print(grams)
			string=grams.lower()
			if string in self.threegrams:
				self.threegrams[string]+=1
			else:
				self.threegrams[string]=1
			nogram+=1
			i+=1
		i=0
		while i in self.threegrams:
			print("\'"+i+"\;"+" occured",self.threegrams[i],"times")
			i+=1
		print("Total three grams are:",nogram)
		return

	def anagrams(self,f1):
		print("Welcome to anagrams")
		return

def main():
	u=Utilities()
	f1=open("inputfile","r")
	ip=input("1234:")
	while 1:
		if ip==1:
			u.tokenize(f1)
			u.display()
			ip=input("1234:")
		elif ip==2:
			u.three(f1)
			ip=input("1234:")
		elif ip==3:
			u.anagrams(f1)
			ip=input("1234:")
		elif ip==4:
			break
		else:
			print("Oops! You pushed the wrong key")
			ip=input("1234:")


if __name__=="__main__":
	main()
