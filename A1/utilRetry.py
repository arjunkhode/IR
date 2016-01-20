from __future__ import print_function
import re

class Utilities:
	words={}
	def tokenize(self,f1):
		content=f1.read()



	        #self.tokens=content.split()
		#for i in self.tokens:
		#--------mechanism to strip punctuation marks from words-------
		'''	length=len(i)
			word=list(i)   #make a list of chars of each token string
			if word[length-1] in "!?,.;":	#checks if last letter is punctuation
				word[length-1]=''
				"".join(word)
		'''





		listoftokens=re.split('\W+',content)
		print("Here are the tokens")
		for i in listoftokens:
			if i in self.words: 
				self.words[i.lower()]+=1
			else:
				self.words[i.lower()]=1
		for i in self.words:
			print("\'"+i+"\'"+" occured",self.words[i],"times")





		#--------can not use word as a key in token_dict because it's a list----
		#--------so appending all letters except punctuation to a blank string--
		'''	string=""
			for letter in word:
				string+=letter.lower() #
		#----------------------Add the stripped word to --------------------------
			if string in self.token_dict : 
				self.token_dict[string]+=1
			
			else:
				self.token_dict[string]=1
	def display(self):
		
		print("Here are the tokens:")
		for i in self.token_dict:
			print("\'"+i+"\'"+" occured",self.token_dict[i],"times")
'''			
			

def main():
	util=Utilities()
	f1=open("inputfile","r")
	util.tokenize(f1)
#	util.display()
	
if __name__ == "__main__":
	main()

