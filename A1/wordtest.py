from nltk.corpus import wordnet as wn
import re

def main():
	primary={}
	f1=open("inputfile","r")
	content=f1.read()
	words=re.findall(r"[\w+]+['-]*[\w+]*",content)
    	for i in words:
		b=''.join(sorted(i.lower()))
		primary[i.lower()]=b		
	for w,y in sorted(primary.items()): #sorted keys alphabetically
	#	print(w,y)
		anagrams=[]
		if wn.synsets(w):
			for x,z in sorted(primary.items()):
				if len(x)==len(w):
					if x!=w and y==z and wn.synsets(x):
						anagrams.append(x)
						#print(anagrams)
			if anagrams:
			#	anagrams.append("stop")
				print(w+" has anagrams: "+(','.join(x for x in anagrams)))
if __name__=="__main__":
	main()
