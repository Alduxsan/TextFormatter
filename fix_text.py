#!/usr/bin/env python3
import os
import sys
import re
import argparse
import datetime

		
def clean_and_format(bad_text):
	
	"""take a txt file from the first CLI argument, 
	normalize the format and return the result"""
	
	only_sentences = r"\w.*"
	raw_text = re.findall(only_sentences, bad_text)
	text = ' '.join(raw_text)
	text = text.split('. ')
		
	final = ''
	counter = 0
	
	for line in text:
			counter += 1
			if counter % sentences == 0:
				final = final + line + '.\n\n'
			else:
				final = final + line + "."
	
	return final
	
	 
def append_text(dest_file, final_text):
	
	"""Copy the formated text to the destination file
	with a separator and a title on the first lines"""
	
	separator = "_"*50
	
	try:
		with open(dest_file, "a+") as dest_file:
			dest_file.write(f"\n{separator}\n\n{title.upper()}\n\n{final_text}")
		print("\nThe text has been copied successfully","\n".center(30))
		print("{}{}".format(title + '\n', '\n' + final_text))
		

	except:
		print("""There was a problem opening or creating the
		destination file for the formatted text,
		please verify it has a valid name (eg file.txt)""".center(30))
		
		
#creando el parser
parser = argparse.ArgumentParser(prog='FixText', 
								description=
								"""It takes a text file as a source, normalizes 
								its format and saves it at the end of the target 
								text file, with a separator, a title entered by 
								the user, or the date (by default)""",
								usage='''%(prog)s 
								-src [source_file_path] 
								-dest [destination_file_path] 
								-title [title] -sen [sentences_number],
								epilog='You can use short parameters name too: 
								-src=-s, -dest=d,-title=-t, -sen=-st''')


#agregando los argumentos
parser.add_argument('-src', '-s',
					help="file text to format",
					required=True,
					type=str)

parser.add_argument('-dest', '-d',
					help=
					"""The text file where insert the formatted text,
					If it does not exist, it will be created""",
					required=True,
					type=str)

divisor = '='*10					
parser.add_argument('-title', '-t',
					help="An optional id title for the inserted text", 
					default=f"{divisor} text appended on the date: {datetime.date.today()} {divisor}")

parser.add_argument('-sen','-st',
					help="An optional value to take dots as reference to group sentences",
					default=5)

#ejecutando el metodo parse_arg()
args = parser.parse_args()

path_source_file = args.src
dest_file = args.dest
title = args.title
sentences = int(args.sen)

if os.path.isdir(path_source_file):
	print(os.path.isdir(path_source_file)) #debug
	print('''\n\n
_____________________________________________________________

THE SPECIFIED SOURCE PATH IS A DIRECTORY, NOT A FILE
_____________________________________________________________
\n\n''')
	sys.exit()

try:
  f = open(path_source_file)
  bad_text = f.read()
except:
  print("""\n\n
  _____________________________________________________________
  
  There was an error opening the source file, 
  check that it has been correctly written (eg file.txt)
  _____________________________________________________________
  \n\n""")
  
finally:
  f.close() 


final_text = clean_and_format(bad_text)
append_text(dest_file, final_text)

