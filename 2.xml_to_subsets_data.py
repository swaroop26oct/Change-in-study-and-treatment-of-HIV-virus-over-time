from lxml import etree
import glob
import csv
import os
import zipfile


def xml_text(file_name):
	file=file_name
	#parse the xml file to find all the root tags with "Pubmedarticle" as the string to find
	tree = etree.parse(file)
	root = tree.getroot().findall('pubmedarticle')

	dt= open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/date_plus_abstract_hiv.csv','a+', encoding='utf-8')
	f = open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/date_plus_abstract_hiv.txt','a+',encoding='utf-8')

	csvwriter=csv.writer(dt)

	for med in root:
		ln=[]
		#find the subtags in the root tag with "medlinecitation/pmid" as the string to find
		pid= med.find('medlinecitation/pmid').text
		ln.append(pid)
		try:
			#Find the date of the publication completed, if publication completion date is not present search for issue date
			date_year= med.find('medlinecitation/datecompleted/year').text
			date_year=med.find('medlinecitation/article/journal/journalissue/pubdate/year').text
			ln.append(date_year)
		except:
			#If both date not found store daterevised in date_year variable
			date_year= med.find('medlinecitation/daterevised/year').text
			ln.append(date_year)
		try:
			#Check for the presence of abstracts, if no abstract found leave it blank and continue
			abstract=med.find('medlinecitation/article/abstract/abstracttext').text
			ln.append(abstract)
			f.write(abstract+'\n')
			#Write the abstracts from publications in a text file based on the different time periods they were found
			if(date_year>'1800' and date_year<='1900'):
				date1900= open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/1800_1900.txt','a+', encoding='utf-8')
				print(date_year)
				print("abs1 done")
				date1900.write(abstract+'\n')
				date1900.close()
			elif(date_year>='1901' and date_year<='1920'):
				date1920=open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/1901_1920.txt','a+', encoding='utf-8')
				date1920.write(abstract+'\n')
				print(date_year)
				print("abs2 done")
				date1920.close()
			elif(date_year>='1921' and date_year<='1940'):
				date1940=open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/1921_1940.txt','a+', encoding='utf-8')
				date1940.write(abstract+'\n')
				print(date_year)
				print("abs3 done")
				date1940.close()
			elif(date_year>='1941' and date_year<='1960'):
				date1960=open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/1941_1960.txt','a+', encoding='utf-8')
				date1960.write(abstract+'\n')
				print(date_year)
				print("abs4 done")
				date1960.close()
			elif(date_year>='1961' and date_year<='1980'):
				date1980=open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/1961_1980.txt','a+', encoding='utf-8') 
				date1980.write(abstract+'\n')
				print(date_year)
				print("abs5 done")
				date1980.close()
			elif(date_year>='1981' and date_year<='2000'):
				date2000=open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/1981_2000.txt','a+', encoding='utf-8')
				date2000.write(abstract+'\n')
				print(date_year)
				print("abs6 done")
				date2000.close()
			elif(date_year>='2001' and date_year<='2005'):
				date2005=open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/2001_2005.txt','a+', encoding='utf-8')
				date2005.write(abstract+'\n')
				print(date_year)
				print("abs7 done")
				date2005.close()
			elif(date_year>='2006' and date_year<='2010'):
				date2010=open('C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs/2006_2010.txt','a+', encoding='utf-8')
				date2010.write(abstract+'\n')
				print(date_year)
				print("abs8 done")
				date2010.close()
			else:
				date2011=open('C:/Users/Suraj/Desktop/CS584/Scripts/2011/final_Programs_plus.txt','a+', encoding='utf-8') 
				date2011.write(abstract+'\n')
				print(date_year)
				print("abs9 done")
				date2011.close()

		except:
			abstract=""
			continue
	
		#Write the date and abstracts in a csv file format as well
		csvwriter.writerow(ln)

	dt.close()
	f.close()
	print("job is completed")


#Change the working directory to the directory where the PubMed xml files were downloaded
os.chdir("C:/Users/Suraj/Desktop/CS584/Scripts/final_Programs")
for file in glob.glob("*.xml"):
	print("I am in file:"+file)
	xml_text(file)
