import requests
import json
import os

#searching for all the hiv records from dates 1800/01/01 to 2017/12/31
url_search = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=HIV&mindate=1800/01/01&maxdate=2017/12/31&usehistory=y&retmode=json"
results_search = requests.post(url_search)
data_search_results = results_search.json()
#setting webenvironment
webenv = data_search_results["esearchresult"]['webenv']
total = int(data_search_results["esearchresult"]['count'])

#Urls to fetch the data in batches of 10000 abstracts at a time, based on the search query criteria 
url_fetch = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmax=10000&retmode=xml&rettype=abstract&query_key=1&webenv="+webenv

for i in range(0,total , 10000):
	#Session number set
	fetch = url_fetch+"&retstart="+str(i)		
	print("Getting this URL: "+fetch)
	try:
		#Fetching data
		results_fetch = requests.post(fetch,data={"retmdoe":"text","rettype":"abstract"}) 
	except:
		print("Error!"+"Retstart value:"+"&retstart")
	f= open('HIV_batch_'+str(i)+'_to_'+str(i+9999)+".xml", 'wb')
	#Write data obtained to files and lowercase the data.
	f.write(results_fetch.text.encode("utf-8").lower())					
	f.close()

print("Number of records found :"+str(total))
