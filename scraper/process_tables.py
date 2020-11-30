import pandas as pd
import numpy as np


df_list = []
skips = []

# Default coffee numbers (already known, but can be updated)
coffee_numbers = ['797340', '630917', '961547', '976095', '640499', '507718', '758571', '619167', '529406', '811504', '135582', '939387', '835570', '123896', '471216', '427875', '713155', '501173', '408751', '694807', '275081', '226926', '925989', '353708', '881745', '551955', '502806', '374364', '900224', '366737', '599249', '848100', '747694', '919897', '188057', '562525', '468749', '652231', '418612', '531749', '826052', '363072', '481969', '565015', '826681', '524961', '360769', '277424', '745862', '528189', '696793', '822911', '656051', '437143', '498918', '612046', '870843', '739227', '270107', '530305', '971417', '777532', '945126', '505661', '889380', '913558', '887829', '708727', '325206', '626072', '402577', '955100', '819209', '910258', '510686', '471378', '213200', '981880', '350487', '386512', '778342', '965326', '551160', '740624', '357799', '202360', '385795', '503643', '734614', '485415', '435010', '154271', '244253', '947026', '609705', '286122', '606938', '560979', '770298', '416481', '131629', '436849', '139380', '351180', '576176', '898272', '285178', '652875', '545835', '175658', '358005', '904659', '126880', '184562', '458487', '813284', '564165', '799551']

coffee_numbers = [int(coffee_number) for coffee_number in coffee_numbers]

for idx, i in enumerate(coffee_numbers): # 600
	# print(i)
	try:
		df1 = pd.read_csv('coffee_{}_table_0.csv'.format(i), header=None)
		df2 = pd.read_csv('coffee_{}_table_1.csv'.format(i))
		df3 = pd.read_csv('coffee_{}_table_2.csv'.format(i))
		df4 = pd.read_csv('coffee_{}_table_3.csv'.format(i))
		df5 = pd.read_csv('coffee_{}_table_4.csv'.format(i))
	except FileNotFoundError:
		# print('skipping {}'.format(i))
		continue


	# df1
	"""
			Unnamed: 0                                 0          1
	0           0                             90.58        NaN
	1           1        View Q Arabica Certificate        NaN
	2           2       Print Q Arabica Certificate        NaN
	3           3  Cupping Protocol and Descriptors        NaN
	4           4       View Green Analysis Details        NaN
	5           5                  Request a Sample        NaN
	6           6                           Species    Arabica
	7           7                             Owner  metad plc
	"""
	print("doing {}".format(i))
	df1.columns = ['one','two']
	# print(df1)
	colnames1 = df1['one'].tolist()
	# these names are inconistent, but the data doesn't look important 
	colnames1[1] = 'view_certificate_1'
	colnames1[2] = 'view_certificate_2'
	data1 = df1['two'].tolist()
	colnames1[0] = 'quality_score'

	df1_processed = pd.DataFrame([data1],columns=colnames1)
	df1_processed = df1_processed.drop(columns=['view_certificate_1', 'view_certificate_2'])
	df1_processed = df1_processed.loc[:, df1_processed.columns.notnull()]
	# df2
	"""
			Unnamed: 0                  0                                  1  \
	0           0  Country of Origin                           Ethiopia   
	1           1          Farm Name                          METAD PLC   
	2           2         Lot Number                                NaN   
	3           3               Mill                          METAD PLC   
	4           4         ICO Number                          2014/2015   
	5           5            Company  METAD Agricultural Developmet plc   
	6           6           Altitude                          1950-2200   
	7           7             Region                  GUJI-HAMBELA/GOYO   
	8           8           Producer                          METAD PLC   

											2                                   3  
	0      Number of Bags                                 300  
	1          Bag Weight                               60 kg  
	2  In-Country Partner  METAD Agricultural Development plc  
	3        Harvest Year                                2014  
	4        Grading Date                     April 4th, 2015  
	5               Owner                           metad plc  
	6             Variety                                 NaN  
	7              Status                           Completed  
	8   Processing Method                        Washed / Wet  
	"""
	df2.columns = ['one','two','three','four','five']
	colnames1 = df2['two'].tolist()
	colnames2 = df2['four'].tolist()
	data1 = df2['three'].tolist()
	data2 = df2['five'].tolist()

	df2_processed = pd.DataFrame([(data1+data2)],columns=(colnames1+colnames2))

	# df3
	"""
			Unnamed: 0           0       1                 2              3
	0           0         NaN  Sample               NaN         Sample
	1           1       Aroma    8.67        Uniformity          10.00
	2           2      Flavor    8.83         Clean Cup          10.00
	3           3  Aftertaste    8.67         Sweetness          10.00
	4           4     Acidity    8.75     Cupper Points           8.75
	5           5        Body    8.50  Total Cup Points  Sample  90.58
	6           6     Balance    8.42               NaN            NaN

	"""
	df3.columns = ['one','two','three','four','five']
	colnames1 = df3['two'].tolist()
	colnames2 = df3['four'].tolist()
	data1 = df3['three'].tolist()
	data2 = df3['five'].tolist()

	df3_processed = pd.DataFrame([(data1+data2)],columns=(colnames1+colnames2))

	# df4
	"""
			Unnamed: 0                     0               1                     2  \
	0           0              Moisture            12 %                 Color   
	1           1  Category One Defects  0 full defects  Category Two Defects   
	2           2               Quakers               0                   NaN   

									3  
	0           Green  
	1  0 full defects  
	2             NaN  
	"""

	df4.columns = ['one','two','three','four','five', 'six', 'seven']
	colnames1 = df4['two'].tolist()
	colnames2 = df4['four'].tolist()
	data1 = df4['three'].tolist()
	data2 = df4['five'].tolist()

	df4_processed = pd.DataFrame([(data1+data2)],columns=(colnames1+colnames2))

	# df5
	"""
			Unnamed: 0                      0  \
	0           0             Expiration   
	1           1     Certification Body   
	2           2  Certification Address   
	3           3  Certification Contact   

																											1  
	0                                    April 3rd, 2016  
	1                 METAD Agricultural Development plc  
	2  BAWA Center, 3rd Floor (Gerji), Addis Ababa, E...  
	3  Aman Adinew (Emebet Dinku) - +251-116-292534, ...  

	"""

	df5.columns = ['one','two','three']
	colnames1 = df5['two'].tolist()
	data1 = df5['three'].tolist()

	if idx > 1:
		prev_cols = df.columns # cols before repalcing df with next coffee 

	df5_processed = pd.DataFrame([data1],columns=colnames1)
	df = pd.concat([df1_processed,df2_processed,df3_processed,df4_processed,df5_processed],1)
	df = df.rename(columns = {np.nan : "NA"})
	df_list.append(df)

	these_cols = df.columns

	df['sample_number'] = i

	# are the columns matching across coffees? 
	if idx>1:
		# figuring out where the column mismatches are 
		#print(these_cols==prev_cols)
		#print(these_cols)
		#print(prev_cols)
		pass

j = 0
for i in df_list:
	print('{} shape: {}'.format(j,i.shape))
	j+=1

df_final = pd.concat(df_list, 0)
df_final = df_final.loc[:, df_final.columns.notnull()]

# print(df_final.columns)
# print(df_final.shape)
#print(df_final.head())
df_final.to_csv('df_1_600.csv')
