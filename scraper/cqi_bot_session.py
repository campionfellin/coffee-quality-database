from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('/Users/campionfellin/Downloads/chromedriver')
time.sleep(2)

driver.get('https://database.coffeeinstitute.org/coffees/arabica')
time.sleep(2)

# these values can be changed if this breaks midway through collecting data to pick up close to where you left off
page = 0
coffeenum = 0

# Hardcoding to start cause these are at least "known"
coffee_numbers = ['797340', '630917', '961547', '976095', '640499', '507718', '758571', '619167', '529406', '811504', '135582', '939387', '835570', '123896', '471216', '427875', '713155', '501173', '408751', '694807', '275081', '226926', '925989', '353708', '881745', '551955', '502806', '374364', '900224', '366737', '599249', '848100', '747694', '919897', '188057', '562525', '468749', '652231', '418612', '531749', '826052', '363072', '481969', '565015', '826681', '524961', '360769', '277424', '745862', '528189', '696793', '822911', '656051', '437143', '498918', '612046', '870843', '739227', '270107', '530305', '971417', '777532', '945126', '505661', '889380', '913558', '887829', '708727', '325206', '626072', '402577', '955100', '819209', '910258', '510686', '471378', '213200', '981880', '350487', '386512', '778342', '965326', '551160', '740624', '357799', '202360', '385795', '503643', '734614', '485415', '435010', '154271', '244253', '947026', '609705', '286122', '606938', '560979', '770298', '416481', '131629', '436849', '139380', '351180', '576176', '898272', '285178', '652875', '545835', '175658', '358005', '904659', '126880', '184562', '458487', '813284', '564165', '799551']

while True:
	print('page {}'.format(page))

	for p_num in range(page):
		time.sleep(10)


		page_buttons = driver.find_element_by_id('DataTables_Table_0_next')
		print(page_buttons)
		actions = webdriver.common.action_chains.ActionChains(driver);

		actions.move_to_element(page_buttons).click().perform()
		time.sleep(10)

	time.sleep(10)
	for i in range(1,401,8):

		try:
			test_page_initial=driver.find_elements_by_xpath('//td')[i] #.find_elements_by_tag_name('a')[0].click()
			link_text = test_page_initial.get_attribute("innerText")[1:]
			coffee_numbers.append(link_text)
		except IndexError:
			print('oh no')

	print(coffee_numbers)
	page += 1
	if page == 3:
		break

coffee_numbers = list(dict.fromkeys(coffee_numbers))
print(coffee_numbers)
print(len(coffee_numbers))

for coffee_num in coffee_numbers:
	print('Coffee Rating #{}'.format(coffee_num))
	test_page=driver.get('https://database.coffeeinstitute.org/coffee/' + coffee_num)
	time.sleep(5)
	tables = driver.find_elements(By.TAG_NAME, "table")

	j = 0
	for tab in tables:
		try:
			t = BeautifulSoup(tab.get_attribute('outerHTML'), "html.parser")
			#print(t)
			df = pd.read_html(str(t))
			name = 'coffee_{}_table_{}.csv'.format(coffee_num,j)
			df[0].to_csv(name)
			print(name)
		except:
			# only one's needed but I want this to be onoxious since it's the only way I'm logging this currently
			print('ERROR: {} failed'.format(name))
			print('ERROR: {} failed'.format(name))
			print('ERROR: {} failed'.format(name))
			print('ERROR: {} failed'.format(name))
		j += 1

# close the driver
driver.close()



