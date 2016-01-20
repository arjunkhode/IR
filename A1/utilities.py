from __future__ import print_function
import re

class Utilities:
	words={}

	def tokenize(self,f1):
		content=f1.read()

		listoftokens=re.findall(r"[\w+]+",content)

		print("here are the tokens")
		for i in listoftokens:
			if i in self.words: 
				self.words[i.lower()]+=1
			else:
				self.words[i.lower()]=1
		for i in self.words:
			print("\'"+i+"\'"+" occured",self.words[i],"times")


def main():
	util=Utilities()
	f1=open("inputfile","r")
	util.tokenize(f1)

if __name__ == "__main__":
	main()

