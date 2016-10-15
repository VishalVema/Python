import urllib
def main():

  webUrl=urllib.urlopen("http://kamalthakur.com")
  print ("result code: "+str(webUrl.getcode()))
  data=webUrl.read()
  print (data)

if __name__ == "__main__":
  main()
