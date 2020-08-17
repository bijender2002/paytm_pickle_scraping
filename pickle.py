from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint
import time
import json
chrome_path = "/home/umesh/Desktop/chrome/chromedriver"
driver = webdriver.Chrome(chrome_path)
url ="https://paytm.com/shop/search?q=pickles&from=autosuggest&child_site_id=1&site_id=1&category=101471"
data=driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML;")
driver.close()
page=BeautifulSoup(html,"html.parser")
all_div=page.find("div",class_="_3RA-")
small_div=all_div.find_all("div",class_="_1fje")
# pprint(small_div)
pickles_dict={}
pickles_details=[]
for i in small_div:
	
	all_data=i.find_all("div",class_="_2i1r")
	for j in all_data:
		all_span=j.find("span",class_="qXdv")
		discount=all_span.find("span",class_="c-ax")
		if discount:
			discount=discount.text
			pickles_dict["Discount"]=discount
		else:
			pickles_dict["Discount"]="0%"
		
		names=j.find("div",class_="_2apC").get_text()
		# print(names)
		pickles_dict["Names"]=names
		prices=j.find("span",class_="_1kMS").get_text()
		# print(prices)
		pickles_dict["Prices"]=prices
		# pprint(pickles_dict)
		pickles_details.append(pickles_dict.copy())
	# pprint(pickles_details)

	op=open('pickle_data.json','w+')
	du=json.dump(pickles_details,op)
	op.close()
	po=open('pickle_data.json','r+')
	lo=json.load(po)
	time.sleep(2)



pickles_detail=open("pickles.html","w+")
pickles_detail.write("<html>\n")
pickles_detail.write("<head>\n")
pickles_detail.write("<title>Pickles</title>\n")
pickles_detail.write("</head>\n")
pickles_detail.write("<body>\n")
pickles_detail.write("<table border=1 style=text-align: center;>")
pickles_detail.write("<tr>\n<td>S.No.</td>\n<td>Names</td>\n<td>Prices</td>\n<td>Discount</td></tr>\n")
c=1

# Here it will pickup all value of key from phone_details 

for pickle in pickles_details:
	name1 = pickle["Names"]
	price1=pickle["Prices"]
	discount1=pickle["Discount"]

	pickles_detail.write("<tr>")
	pickles_detail.write("<td>"+str(c)+"."+"</td>"+"<td>"+name1+"</td>"+"<td>"+price1+"</td>"+"<td>"+discount1+"</td>")
	pickles_detail.write("/<tr>")
	c+=1
pickles_detail.write("</table>\n</body>\n</html>")

