'''
  Python version: 2.7
  Database source: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing

   Input variables:
   # bank client data:
   1 - age (numeric)
   2 - job : type of job (categorical: [
   		"admin." : 1,
   		"blue-collar" : 2,
   		"entrepreneur" : 3,
   		"housemaid" : 4,
   		"management" : 5,
   		"retired" : 6,
   		"self-employed" : 7,
   		"services" : 8,
   		"student" : 9,
   		"technician" : 10,
   		"unemployed" : 11,
   		"unknown" : 0.5
   	])
   3 - marital : marital status (categorical: [
   		"divorced" : 1,
   		"married" : 2,
   		"single" : 3,
   		"unknown" : 0.5
   	])
   4 - education (categorical: [
	   	"basic.4y" : 1,
	   	"basic.6y" : 2,
	   	"basic.9y" : 3,
	   	"high.school" : 4,
	   	"illiterate" : 5,
	   	"professional.course" : 6,
	   	"university.degree" : 7,
	   	"unknown" : 0.5
   	])
   5 - default: has credit in default? (categorical: [
   		"no" : 0,
   		"yes" : 1,
   		"unknown" : 0.5
   	])
   6 - housing: has housing loan? (categorical: [
   		"no" : 0,
   		"yes" : 1,
   		"unknown" : 0.5
   	])
   7 - loan: has personal loan? (categorical: [
   		"no" : 0,
   		"yes" : 1,
   		"unknown" : 0.5
   	])
   # related with the last contact of the current campaign:
   8 - contact: contact communication type (categorical: [
   		"cellular" : 1,
   		"telephone" : 2
   	]) 
   9 - month: last contact month of year (categorical: [
   		"jan" : 1,
   		  .
   		  .
   		"dec" : 12
   	])
  10 - day_of_week: last contact day of the week (categorical: [
  		"mon" : 1,
  		  .
  		  .
  		"fri" : 5
  	])
  11 - duration: last contact duration, in seconds (numeric). Important note:  this attribute highly affects the output target (e.g., if duration=0 then y="no"). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
   # other attributes:
  12 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
  13 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
  14 - previous: number of contacts performed before this campaign and for this client (numeric)
  15 - outcome: outcome of the previous marketing campaign (categorical: [
  		"failure" : 0,
  		"nonexistent" : 1,
  		"success" : 2
  	])
   # social and economic context attributes
  16 - emp.var.rate: employment variation rate - quarterly indicator (numeric)
  17 - cons.price.idx: consumer price index - monthly indicator (numeric)     
  18 - cons.conf.idx: consumer confidence index - monthly indicator (numeric)     
  19 - euribor3m: euribor 3 month rate - daily indicator (numeric)
  20 - nr.employed: number of employees - quarterly indicator (numeric)
'''

def quantify_array(line_data):
	opt = {
		# miscellaneous
   		"no" : 0,
   		"yes" : 1,
   		"unknown" : 0.5,
   		# job
   		"admin." : 1,
   		"blue-collar" : 2,
   		"entrepreneur" : 3,
   		"housemaid" : 4,
   		"management" : 5,
   		"retired" : 6,
   		"self-employed" : 7,
   		"services" : 8,
   		"student" : 9,
   		"technician" : 10,
   		"unemployed" : 11,
   		# marital
   		"divorced" : 1,
   		"married" : 2,
   		"single" : 3,
   		# education
   		"basic.4y" : 1,
	   	"basic.6y" : 2,
	   	"basic.9y" : 3,
	   	"high.school" : 4,
	   	"illiterate" : 5,
	   	"professional.course" : 6,
	   	"university.degree" : 7,
	   	"unknown" : 0.5,
	   	# contact
	   	"cellular" : 1,
   		"telephone" : 2,
   		# month
   		"jan" : 1,
   		"feb" : 2,
   		"mar" : 3,
   		"apr" : 4,
   		"may" : 5,
   		"jun" : 6,
   		"jul" : 7,
   		"aug" : 8,
   		"sep" : 9,
   		"oct" : 10,
   		"nov" : 11,
   		"dec" : 12,
   		# day_of_week
   		"mon" : 1,
   		"tue" : 2,
   		"wed" : 3,
   		"thu" : 4,
   		"fri" : 5,
   		# outcome
   		"failure" : 0,
  		"nonexistent" : 1,
  		"success" : 2,
   	}
   	a = []
   	for data in line_data:
   		try:
   			a.append(opt[data] if data in opt else float(data))
   		except:
   			a.append(data)
   	return a

def line2array(csv_line, delimiter = ';'):
	return csv_line.replace('"','').replace('\n','').split(delimiter)

def csv2matrix(csv_path):
	m = []
	csv = open(csv_path,'r')
	for line in csv.readlines()[1:]:
		m.append(line2array(line))
	csv.close()
	return m

def matrix2data(matrix, data_filename):
	d = open(data_filename + '.data','w')
	for line in matrix:
		d.write(line.join(','))
	d.close()

sample_matrix = csv2matrix('original-bank-sample.csv')
matrix2data(sample_matrix,'bank-sample')