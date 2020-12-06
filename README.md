# TEXTFORMATTER

Created to format the downloadable texts of the courses given on educational platforms (such as Cursera, Edx, etc), which are usually very uncomfortable to read.

This script is originally intended to use it in Linux, but you can adapt it as you wish for your OS. 

Bear in mind that this script is intended to normalize text with abnormal spaces and line breaks. Don't check other details like capital letters, hyphens, symbols, etc.

### HOW TO USE IT

In the most practical way, you would use the script in the folder where you save the file with the plain text downloaded from the platform.

I recommend always using the same file name when downloading, as it allows you to reuse the values ​​entered in the terminal.

#### Detailed guide:
- Download the file from the platform, or copy and paste the text in a file to take it as a source.
- Put the fix_text.py script in the folder with the previous file.
- Open a terminal and navigate to the directory where both files are.
- Execute the script passing it the corresponding arguments: the source file or the path to it, the destination file (if it doesn't exist it will create it), an optional title, an optional number indicating how many sentences you want to group the text together in pargraphs.

Example:

#### ./fix_text.py -src source_file_name -dst destination_file_name -title 'Title for text' -st 10

When done, you can simply download again the next text selecting the first file on the browser download prompt. If you need, change the destination file, title or line numbers and run script again. 
