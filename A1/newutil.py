from __future__ import print_function
from nltk.corpus import wordnet as wn
import re,operator

class Utilities:
	words={}  #dictionary stores key as word and value as its frequency
	total=0
	totaltokens=0
	threegrams={}
	content=[]

	def init(self,f1):
		self.content=f1.read()

	def tokenize(self):
		listoftokens=re.findall(r"[\w+]+['-]*[\w+]*",self.content)
		print("Here are the tokens")
		for i in listoftokens:
			if i.lower() in self.words:
				self.words[i.lower()]+=1
				self.total+=1
			else:
				self.words[i.lower()]=1
				self.total+=1
				self.totaltokens+=1
				print(i)
			
		return

	def display(self):
		print("Here are the tokens with their frequencies")
		for i in self.words:
			print("\'"+i+"\'"+" occured",self.words[i],"times")
		print("Total words:",self.total)
		print("Total tokens:",self.totaltokens)
		return

	def qsort(self,dict):
		sortdict=sorted(dict,key,reverse=True)
		return sortdict
		

	def three(self):
		print("Welcome to three grams")
		listoftokens=re.findall(r"[\w+]+['-]*[\w+]*",self.content)
		total=len(listoftokens)
		i=0
		nogram=0
		while i<total-2: 
			grams=" ".join(listoftokens[i:i+3])
			string=(grams.lower()).rstrip()
		       #print(string)
			if string in self.threegrams:
				self.threegrams[string]+=1
			else:
				self.threegrams[string]=1
			nogram+=1
			i+=1
		sortdict=sorted(self.threegrams,reverse=True, key=self.threegrams.get)
		for w in sorted(self.threegrams, reverse=True, key=self.threegrams.get):
			print(w, self.threegrams[w])
		print('----------')
		#for i in sortdict:
		#	print(i,"occured",sortdict[i],"times")
	  	print("Total three grams are:",nogram)
		return

	def anagrams(self):
		primary={} #stores original word (Key) and sorted alphabets (Value)
		print("Welcome to anagrams")
	 	words=re.findall(r"[\w+]+['-]*[\w+]*",self.content)
		for i in words:
			b=''.join(sorted(i.lower()))
			primary[i.lower()]=b
		for w,y in sorted(primary.items()): #Sorted keys alphabetically
			anagrams=[]
			if wn.synsets(w):  
				for x,z in sorted(primary.items()):
					if len(x)==len(w): 	    #Compare lengths
						if x!=w and y==z and wn.synsets(x):
							anagrams.append(x)
				if anagrams:
					print(w+" has anagrams:"+(','.join(anagrams)))
		return

def main():
	u=Utilities()
	f1=open("inputfile","r")
	u.init(f1)
	ip=input("12345:")
	while 1:
		if ip==1:
			u.tokenize()
			ip=input("12345:")
		elif ip==2:
			u.display()
			ip=input("12345:")
		elif ip==3:
			u.three()
			ip=input("12345:")
		elif ip==4:
			u.anagrams()
			ip=input("12345:")
		elif ip==5:
			break
		else:
			print("Oops! You pushed the wrong key")
			ip=input("12345:")


if __name__=="__main__":
	main()
