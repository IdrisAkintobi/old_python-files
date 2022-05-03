import requests
from bs4 import BeautifulSoup
import random
home = "http://quotes.toscrape.com"
Quotes = []
Authors = []
links = []
Author_info = {}
def gather_data(site):
	response = requests.get(site)
	data = BeautifulSoup(response.text, "html.parser")
	quote_list = data.find_all(class_="quote")
	for quote in quote_list:
		Quote = quote.find(class_="text").get_text()
		Author = quote.find("small").get_text()
		href = quote.find("a")["href"]
		Quotes.append(Quote)
		Authors.append(Author)
		links.append(href)
def gather_alldata(url=home):
	for i in range(1,10):
		url = home+f"/page/{i}"
		gather_data(url)
def play_guess():
	n = list(range(len(Quotes)))
	guess = 1
	random.shuffle(n)
	nth = n.pop()
	while guess <= 4:
		ans = input(f"{Quotes[nth]}\nWhat is the name of the Author: ")
		if ans == Authors[nth]:
			print("You Won!!!")
			break
		elif guess==1:
			guess += 1
			print(f"HINT: The Author firstname starts with {Authors[nth][0]}")
		elif guess==2:
			guess +=1
			print(f"HINT: The Author firstname starts with {Authors[nth].split()[1][0]}")
		elif guess==3:
			guess +=1
			print("Getting Author info....")
			hint_response = requests.get(home+links[nth])
			hint_data = BeautifulSoup(hint_response.text, "html.parser")
			hint_dob = hint_data.find(class_="author-born-date").get_text()
			hint_pob = hint_data.find(class_="author-born-location").get_text()
			print(f"HINT: The Author was born on {hint_dob} at {hint_pob}")
		elif guess==4:
			print("You Lose!", f"The name of the Author is {Authors[nth]}")
			guess+=1
def play_game():
	play_guess()
	ask = input("Will you like to play the game again? (Y/N): ")
	if ask.upper() == "Y":
		play_game()
	else:
		print ("Goodbye! Thanks for playing my game")
gather_alldata()
play_game()