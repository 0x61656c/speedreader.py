import math
from termcolor import colored
import os
import time

def parse(text):
	text_array = str.split(str(text))
	return text_array

def highlight(word):
	word_length = len(str(word))
	bit1_length = math.floor((word_length/2))
	if bit1_length % 2 != 0:
		bit1_length -= 1

	fh = word[0:bit1_length]
	md = word[bit1_length]
	end = word[bit1_length + 1:]

	return (colored(fh,"white") + colored(md,"red")+ colored(end,"white"))

def speedRead(text):
	start = time.time()
	text_array = parse(text)
	count = 0
	for word in text_array:
		count += 1
		print(highlight(word))
		time.sleep(.05)
		os.system("clear")

	end = time.time()
	timer = end - start
	print(colored("Done. ", "white") + colored("%i"%count, "red") + colored(" words read in ", "white") + colored("%f"%timer,"red") + colored(" seconds", "white"))


def test_parse():
	print(parse("It's the end of the world as we know it."))

def test_highlight():
	print()
	os.system("clear")
	print(highlight("hello,"))
	time.sleep(.1)
	os.system("clear")
	print(highlight("WORLD!"))
	time.sleep(.1)
	os.system("clear")	
	print(highlight("12345"))
	time.sleep(.1)
	os.system("clear")

def test_speedRead():	
	text = """Romeo and Juliet is a tragedy written by William Shakespeare early in his career about two young star-crossed lovers whose deaths ultimately reconcile their feuding families. It was among Shakespeare's most popular plays during his lifetime and along with Hamlet, is one of his most frequently performed plays. Today, the title characters are regarded as archetypal young lovers.

Romeo and Juliet belongs to a tradition of tragic romances stretching back to antiquity. The plot is based on an Italian tale translated into verse as The Tragical History of Romeus and Juliet by Arthur Brooke in 1562 and retold in prose in Palace of Pleasure by William Painter in 1567. Shakespeare borrowed heavily from both but expanded the plot by developing a number of supporting characters, particularly Mercutio and Paris. Believed to have been written between 1591 and 1595, the play was first published in a quarto version in 1597. The text of the first quarto version was of poor quality, however, and later editions corrected the text to conform more closely with Shakespeare's original.

Shakespeare's use of his poetic dramatic structure (especially effects such as switching between comedy and tragedy to heighten tension, his expansion of minor characters, and his use of sub-plots to embellish the story) has been praised as an early sign of his dramatic skill. The play ascribes different poetic forms to different characters, sometimes changing the form as the character develops. Romeo, for example, grows more adept at the sonnet over the course of the play.

Romeo and Juliet has been adapted numerous times for stage, film, musical, and opera venues. During the English Restoration, it was revived and heavily revised by William Davenant. David Garrick's 18th-century version also modified several scenes, removing material then considered indecent, and Georg Benda's Romeo und Julie omitted much of the action and added a happy ending. Performances in the 19th century, including Charlotte Cushman's, restored the original text and focused on greater realism. John Gielgud's 1935 version kept very close to Shakespeare's text and used Elizabethan costumes and staging to enhance the drama. In the 20th and into the 21st century, the play has been adapted in versions as diverse as George Cukor's 1936 film Romeo and Juliet, Franco Zeffirelli's 1968 version Romeo and Juliet, and Baz Luhrmann's 1996 MTV-inspired Romeo + Juliet. """
	speedRead(text)

def main():
	#test_parse()
	#test_highlight()
	test_speedRead()
	pass

if __name__ == "__main__":
	main()