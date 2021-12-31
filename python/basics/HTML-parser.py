"""You are given an HTML code snippet of  lines.
Your task is to detect and print all the HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]


The -> symbol indicates that the tag contains an attribute. It is immediately followed by the name of the attribute and the attribute value.
The > symbol acts as a separator of attributes and attribute values.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute or attribute value inside the HTML comment tags (<!-- Comments -->). Comments can be multiline.
All attributes have an attribute value.

Input Format

The first line contains an integer , the number of lines in the HTML code snippet.
The next  lines contain HTML code.

Constraints


Output Format

Print the HTML tags, attributes and attribute values in order of their occurrence from top to bottom in the snippet."""


from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        print(attrs)
                
    def handle_endtag(self, tag):
        
        print(tag)
            
#html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
#parser.feed(html)

parser.feed('<head>'
'<title>HTML</title>'
'</head>'
'<object type="application/x-flash" '
  'data="your-file.swf" '
  'width="0" height="0">'
  '<!-- <param name="movie" value="your-file.swf" /> -->'
  '<param name="quality" value="high"/>'
'</object>'
            '<body><h1>Parse me!</h1></body></html>')

parser.close()



from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, values  in attrs:
            print('-> ', attr, ' > ',values )
                 
N = int(input())
raw = ""
for i in range(N):
  raw += input()
new = MyHTMLParser()
new.feed(raw)
parser.close()
