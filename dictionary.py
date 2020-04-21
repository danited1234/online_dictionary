import requests
from bs4 import BeautifulSoup
import bs4
import os
import sys
def dictionary(word):
	website=requests.get("https://www.vocabulary.com/dictionary/"+word)
	website_two=requests.get("https://www.thesaurus.com/browse/"+word)
	source_code_two=website_two.content
	source_code=website.content
	soup=BeautifulSoup(source_code,'lxml')
	soup_two=BeautifulSoup(source_code_two,"lxml")
	default_color='\033[m'
	word_color='\033[1;32;40m'
	text_color='\033[1;31;40m'
	try:
		to_be_found=soup.find("h3",{"class":"definition"}).getText()
		string=""
		string=str(to_be_found)
		res=" ".join(string.split())
		if "adj" in res:
			os.system("cls" if os.name == "nt" else "clear")
			print(f"{word_color}{word}{default_color} is an adjective and it means\n{text_color}{res.replace('adj','')}\nSynonyms Include:")
			for a_tags in soup_two.find_all(class_="css-7854fb etbu2a31"):
				print(f"{word_color}{a_tags.text}{default_color}")
		elif "n" in res:
			os.system("cls" if os.name == "nt" else "clear")
			print(f"{word_color}{word}{default_color} is a noun and it means\n{text_color}{res[1:]}\nSynonyms Include")
			for a_tags in soup_two.find_all(class_="css-7854fb etbu2a31"):
				print(f"{word_color}{a_tags.text}{default_color}")
		elif "v" in res:
			os.system("cls" if os.name == "nt" else "clear")
			print(f"{word_color}{word}{default_color} is a verb and it means\n{text+color}{res[1:]}\nSynonyms Include")
			for a_tags in soup_two.find_all(class_="css-7854fb etbu2a31"):
				print(f"{word_color}{a_tags.text}{default_color}")
		else:
			os.system("cls" if os.name == "nt" else "clear")
			print(res)
	except AttributeError:
		print("We did not find the word that you were looking for")
if __name__=="__main__":
	cmd=sys.argv[1:]
	if len(cmd)>=1:
		list_to_dir=''.join(map(str, cmd))
		dictionary(list_to_dir)
	else:
		print("type any word\ne.g dictionary.py word")
