import requests, json, pprint, pathlib

libraryURL='https://api.mangadex.org/'
config = {
	"username": None,
	"password": None,
	"result": None,
	"token": None,
	"tl":"en"
}


def config_load(config_file=None):
	if config_file is None:
		try:
			f = open("mango.config", "r")
			config_file = f.read()
			f.close()
		except Exception as e:
			print("Error opening mango.config: \n" + str(e))
	config.update(json.loads(config_file))


def config_save():
	try:
		f = open("mango.config", "w")
		f.write(json.dumps(config))
		f.close()
	except Exception as e:
		print("Error when saving config file:\n" + str(e))

def login_attempt(username=None, password=None):
	if username or password is not None:
		print("Logging in as " + username)
		login_response = requests.post("https://api.mangadex.org/auth/login", data=json.dumps({'username': str(username),'password': str(password)}))
		print(str(login_response))
		# print(login_response.headers)
		try:
			# print(login_response.json())
			token = login_response.json()
			config.update(token)
		except Exception as e:
			print("Error handling response JSON in login_attempt\n" + str(e))
		
		return login_response
		
		# print(login_response.token)
		return None
	else:
		print("Username or password was empty")

# login
def login():
	username = None
	password = None
	response = None
	username = input("Please enter username, or press Enter to use the saved credentials.\n")
	if username == "":
		username=config["username"]
		password=config["password"]
		if username is None:
			username = input("No saved username found, please provide a new one.\n")
		if password is None:
			password = input("No saved password found, please provide a new one.\n")
		else:
			print("User: " + username)
	if username is not None:
		config["username"]=username

	if password is None:
		password = input("Please enter password:\n")
	if username and password is not None:
		config["password"]=password
		response = login_attempt(username, password)
	config_save()
	return response

def tags():
	tag_resp = requests.get("https://api.mangadex.org/manga/tag")
	print(str(tag_resp))
	return tag_resp.json()

def limited_add(a, b, c):
	if (a + b) > c:
		return c
	else:
		return a + b

def random_search():
	ran_response = requests.get("https://api.mangadex.org/manga/random")
	if ran_response.status_code == 200:
		manga = ran_response.json()
		print_manga_styled(manga)
	userin = input("Show Chapters? Input any key to show and 'e' or just 'enter' to ignore.").lower()
	if userin is not None or userin != "" or userin != "e":
		view_manga_chapters(manga["data"]["id"])
	else:
		return None


def search(query="", offset=None, limit=10, fullsearch=False):
	if fullsearch:
		query_params = query
	else:
		query_params = {"title":query, "limit":limit, "offset":offset}
	search_response = requests.get("https://api.mangadex.org/manga", params=query_params)
	print(str(search_response))
	# return search_response.json()
	# if search_response.status_code == 200: pprint.pprint(search_response.json())
	if search_response.status_code == 200: paginated_search(search_response.json(), query)
	try:
		s_results = search_response.json()
		return s_results
	except Exception as e:
		print("No results returned by query \"" + str(query) + "\".\n")
	return None

def quiet_search(query="", offset=None, limit=10, fullsearch=False):
	if fullsearch:
		query_params = query
	else:
		query_params = {"title":query, "limit":limit, "offset":offset}
	search_response = requests.get("https://api.mangadex.org/manga", params=query_params)
	if search_response.status_code == 200:
		try:
			s_results = search_response.json()
			return s_results
		except Exception as e:
			print("No results returned by query \"" + str(query) + "\".\n")
	return None

def print_manga_styled(manga=None):
	if manga is not None:
		tags = []
		print(str(manga["data"]["id"]))
		print(manga["data"]["attributes"]["title"]["en"])
		print("---")	
		for alttitle in manga["data"]["attributes"]["altTitles"]:
			print(alttitle["en"])
		for tag in manga["data"]["attributes"]["tags"]:
			tags.append(tag["attributes"]["name"]["en"])
		print(tags)
		print("---")
		if manga["data"]["attributes"]["description"]["en"] is not None:
			print(manga["data"]["attributes"]["description"]["en"])
		else: print("No description available.")
		print("\n")


def paginated_search(search_response, query):
	page_lim = search_response["limit"]
	offset = search_response["offset"]
	total_results = search_response["total"]

	print("Showing results " + str(offset+1) + " through " + str(limited_add(offset, page_lim, total_results)) + " of " + str(total_results) + ".")
	page_uuid_list = []
	for i, manga in enumerate(search_response["results"]):
		page_uuid_list.append(manga["data"]["id"])
		print("Page result #" + str(i+1) + ", " + str(offset+i+1) + " of " + str(total_results))
		print_manga_styled(manga)
		

	print("Showing results " + str(offset+1) + " through " + str(limited_add(offset, page_lim, total_results)) + " of " + str(total_results) + ".")
	userin = input("Press A, W, or ',' for back, S, D, or '.' for foward. 'Enter' or 'e' to exit. Enter result # to read manga.\n").lower()

	while(userin):
		if userin == "a" or userin == "w" or userin == ",":
			#get previous page of results or do nothing
			if offset < page_lim:
				print("Reached the beginning of the search results.")
				userin=input("")
			else:
				search(query, offset=offset-page_lim, limit=page_lim)
				userin=None
		elif userin == "s" or userin == "d" or userin == ".":
			#get next page of results
			if offset+page_lim <= total_results:
				search(query, offset=offset+page_lim, limit=page_lim)
				userin=None
			else:
				print("Reached the end of the search results.")
				userin=input("")
		elif userin.isdecimal():
			index = int(userin)-1
			if index < 0: index = 0
			if index > total_results: index = total_results-1
			if index > offset and index < offset+page_lim:
				index = index - offset
			if index > offset+page_lim:
				#item is not loaded in UUID list, so must be searched up
				try:
					raise 
					uuid = sorted(quiet_search(query, offset=index))[0]["data"]["id"]
				except Exception as e:
					print("Index " + str(index+1) + " not yet retrieved from server.\n" + str(e))
			else:
				print("Viewing page result " + str(index+1))
				view_manga(page_uuid_list[index])
			userin=input("")
		elif userin == "e" or userin == "exit":
			userin == None
			break


def check_login():
	if config["result"] == "ok" and config["token"] is not None:
		token = config["token"]
		bearer_header = {'Authorization': 'Bearer ' + token["session"]}
		check_response = requests.get("https://api.mangadex.org/auth/check", headers=bearer_header)
		print("Session check:" + str(check_response.status_code))
		try:
			check = check_response.json()
			if check["isAuthenticated"] is not None: return check["isAuthenticated"]
		except Exception as e:
			print("Error handling response JSON in check_login\n" + str(e))
	return False

def view_manga(uuid=None):
	URL = "https://api.mangadex.org/manga/" + str(uuid)
	view_response = requests.get(URL)
	print(str(view_response.status_code))
	if view_response.status_code == 200 and view_response.json() is not None: print_manga_styled(view_response.json())
	#also display the chapter list
	view_manga_chapters(uuid)

def get_chap_no(chapter):
	print(str(chapter["data"]["attributes"]["chapter"]))
	return float(chapter["data"]["attributes"]["chapter"])

def view_manga_chapters(uuid=None):
	params = {"limit":100, "manga":uuid, "translatedLanguage":config["tl"]}
	ch_response = requests.get("https://api.mangadex.org/chapter", params=params)
	try:
		ch_json = ch_response.json()
	except Exception as e:
		if ch_response.status_code == 204:
			print("There were no chapters with the selected parameters\n" + str(params))
		print(str(ch_response))
		print(str(ch_response.headers))
		print("There was an error reading the JSON response, likely no chapters exist.\n" + str(e))
	#should have only returned 1 manga's chapters
	ch_results = ch_json["results"]
	print("Results list length: " + str(len(ch_results)))

	page_lim = ch_json["limit"]
	offset = ch_json["offset"]
	total_results = ch_json["total"]

	print("Chapters:  " + str(offset+1) + " through " + str(limited_add(offset, page_lim, total_results)) + " of " + str(total_results) + ".")
	chapter_list = []
	while(offset < total_results):
		print("Chapter request made:\n")
		print("GET, https://api.mangadex.org/chapter, " + str(params))
		chapter_list.append(ch_json["results"])
		offset = offset + page_lim
		if(offset < total_results):
			ch_json = requests.get("https://api.mangadex.org/chapter", params=params)

	sorted_list = sorted(ch_results, key=lambda c: get_chap_no(c))
	# pprint.pprint(str(sorted_list))
	dl_menu = {}
	for chapter in sorted_list:
		title = str(chapter["data"]["attributes"]["title"])
		chap_no = chapter["data"]["attributes"]["chapter"]
		tl_lang = str(chapter["data"]["attributes"]["translatedLanguage"])
		last_update = str(chapter["data"]["attributes"]["updatedAt"])
		print("Chapter " + chap_no + "		" + tl_lang + "	" + title + "  			" + str(chapter["data"]["id"]))
		#might want to check for chapter version and pick highest
		dl_menu[chap_no]=chapter

	print("" + str(total_results) + " chapters found in the specified language.")
	userin = input("Enter chapter number or range (X-Y) to begin download: ").lower()
	try:
		save_manga_chapter(uuid, dl_menu[userin])
	except:
		print("Could not save chapter " + userin)
	print("End")

def save_manga_chapter(manga_id=None, chapter=None, chapter_id=None):
	if chapter_id is not None:
		ch_id=chapter_id
	else:
		ch_id=chapter["data"]["id"]
	print("Retrieving chapter " + ch_id)
	try:
		ch_no = get_chap_no(chapter)
		transfers = []
		save_path="./manga/" + str(manga_id) + "/" + str(ch_no)
		pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)
		md_url=get_mdhome_url(ch_id)
		ch_hash=chapter["data"]["attributes"]["hash"]
		ch_data_array=chapter["data"]["attributes"]["data"]
		print(str(md_url))
		n = 1
		for ch_page_data in ch_data_array:
			web_url = md_url + "/data/" + ch_hash + "/" + ch_page_data
			file_path = save_path + "/" + str(n) + "_" + ch_page_data
			transfers.append({"src":web_url, "dest":file_path, "pg_no":str(n)})
			n+=1
	except Exception as e:
		print("Error when retrieving chapter/page URL with ID " + str(chapter["data"]["id"]) + ".\n" + str(e))
		return None
	page = None
	for xfer in transfers:
		try:
			url = xfer["src"]
			local = xfer["dest"]
			i = xfer["pg_no"]
			# print("From " + url + " to " + local)
			try:
				page = requests.get(url, params={"ssl":True})
			except Exception as e:
				print("Error on page request:\n" + str(e))
				print("Target URL:\n" + url)
				break
			if page is not None:
				try:
					f = open(local, 'wb')
					f.write(page.content)
					f.close()
					print("Page " + i + "saved to " + local)
				except Exception as e:
					print("Error on file write:" + str(e))
					break

		except Exception as e:
			print("Error getting or saving page " + str(i) +  "\n" + str(e))
	

#23eaf433-44dd-4740-839f-df31b8b13e81
def get_mdhome_url(ch_id):
	try:
		md_home_url_resp = requests.get("https://api.mangadex.org/at-home/server/" + str(ch_id))
		md_home = md_home_url_resp.json()
		if md_home_url_resp.status_code != 200:
			print("Response not 200, request failed")
			print("JSON Error section: " + str(md_home["errors"]))
		else:
			return md_home['baseUrl']
	except Exception as e:
		print("Exception when getting MD@Home URL: " + str(e))
		print("Response contents: " + str(md_home))
	return None

print("Mangospex version 0.0.0 - direpenguin@gmail.com")
print("Search for manga by title or parameter dictionary (https://api.mangadex.org/docs.html#operation/get-search-manga)")
config_load()
if not check_login():
	response = login()
	if not response:
		print("There was an error logging in.")
else:
	print(config["username"] + " is already logged in.")

menu_list=("Menu", "Tags", "Check", "Search (for direct API param entry)", "Random", "View (by manga UUID entry)", "Download (by chapter UUID)", "Exit")
end=False

while end==False:

	menu = input("Enter a manga name to search, or enter a menu command/key, or enter 'm'enu for a list of all commnds\n" ).lower()
	if menu == "e" or menu == "exit": end=True
	elif menu == "m" or menu == "menu": print(str(menu_list))
	elif menu == "t" or menu == "tags": pprint.pprint(tags())
	elif menu == "c" or menu == "check": print("Logged in? " + str(check_login()))
	elif menu == "r" or menu == "random": random_search()
	elif menu == "s" or menu == "search": search(input("Enter API param dictionary:\n"), fullsearch=True)
	#c20350bb-0e53-493f-8c92-71198d57bf8a example string
	elif menu == "v" or menu == "view" or menu == "uuid": view_manga(input("Enter a manga's ID: "))
	# elif menu == "d" or menu == "dl" or menu == "download": save_manga_chapter(input("Enter a chpater's ID: "))
	elif menu == "l" or menu == "lang" or menu == "language": config["tl"]=input("Enter a language code (ex: en=English, es-la=Latin American Spanish): ")
	else: search(menu)

