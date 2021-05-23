import requests, json, pprint, pathlib, array, os.path

libraryURL='https://api.mangadex.org/'
config = {
	"username": None,
	"password": None,
	"result": None,
	"token": None,
	"tl":"en"
}
tags = {
	"tag": {
		"Oneshot": "0234a31e-a729-4e28-9d6a-3f87c4966b9e",
		"Thriller": "07251805-a27e-4d59-b488-f0bfbec15168",
		"Award Winning": "0a39b5a1-b235-4886-a747-1d05d216532d",
		"Reincarnation": "0bc90acb-ccc1-44ca-a34a-b9f3a73259d0",
		"Sci-Fi": "256c8bd9-4904-4360-bf4f-508a76d67183",
		"Time Travel": "292e862b-2d17-4062-90a2-0356caa4ae27",
		"Genderswap": "2bd2e8d0-f146-434a-9b51-fc9ff2c5fe6a",
		"Loli": "2d1f5d56-a1e5-4d0d-a961-2193588b08ec",
		"Traditional Games": "31932a7e-5b8e-49a6-9f12-2afa39dc544c",
		"Official Colored": "320831a8-4026-470b-94f6-8353740e6f04",
		"Historical": "33771934-028e-4cb3-8744-691e866a923e",
		"Monsters": "36fd93ea-e8b8-445e-b836-358f02b3d33d",
		"Action": "391b0423-d847-456f-aff0-8b0cfc03066b",
		"Demons": "39730448-9a5f-48a2-85b0-a70db87b1233",
		"Psychological": "3b60b75c-a2d7-4860-ab56-05f391bb889c",
		"Ghosts": "3bb26d85-09d5-4d2e-880c-c34b974339e9",
		"Animals": "3de8c75d-8ee3-48ff-98ee-e20a65c86451",
		"Long Strip": "3e2b8dae-350e-4ab8-a8ce-016e844b9f0d",
		"Romance": "423e2eae-a7a2-4a8b-ac03-a8351462d71d",
		"Ninja": "489dd859-9b61-4c37-af75-5b18e88daafc",
		"Comedy": "4d32cc48-9f00-4cca-9b5a-a839f0764984",
		"Mecha": "50880a9d-5440-4732-9afb-8f457127e836",
		"Anthology": "51d83883-4103-437c-b4b1-731cb73d786c",
		"Boy's Love": "5920b825-4181-4a17-beeb-9918b0ff7a30",
		"Incest": "5bd0e105-4481-44ca-b6e7-7544da56b1a3",
		"Crime": "5ca48985-9a9d-4bd8-be29-80dc0303db72",
		"Survival": "5fff9cde-849c-4d78-aab0-0d52b2ee1d25",
		"Zombies": "631ef465-9aba-4afb-b0fc-ea10efe274a8",
		"Reverse Harem": "65761a2a-415e-47f3-bef2-a9dababba7a6",
		"Sports": "69964a64-2f90-4d33-beeb-f3ed2875eb4c",
		"Superhero": "7064a261-a137-4d3a-8848-2d385de3a99c",
		"Martial Arts": "799c202e-7daa-44eb-9cf7-8a3c0441531e",
		"Fan Colored": "7b2ce280-79ef-4c09-9b58-12b7c23a9b78",
		"Samurai": "81183756-1453-4c81-aa9e-f6e1b63be016",
		"Magical Girls": "81c836c9-914a-4eca-981a-560dad663e73",
		"Mafia": "85daba54-a71c-4554-8a28-9901a8b0afad",
		"Adventure": "87cc87cd-a395-47af-b27a-93258283bbc6",
		"User Created": "891cf039-b895-47f0-9229-bef4c96eccd4",
		"Virtual Reality": "8c86611e-fab7-4986-9dec-d1a2f44acdd5",
		"Office Workers": "92d6d951-ca5e-429c-ac78-451071cbf064",
		"Video Games": "9438db5a-7e2a-4ac0-b39e-e0d95a34b8a8",
		"Post-Apocalyptic": "9467335a-1b83-4497-9231-765337a00b96",
		"Sexual Violence": "97893a4c-12af-4dac-b6be-0dffb353568e",
		"Crossdressing": "9ab53f92-3eed-4e9b-903a-917c86035ee3",
		"Magic": "a1f53773-c69a-4ce5-8cab-fffcd90b1565",
		"Girl's Love": "a3c67850-4684-404e-9b7f-c69850ee5da6",
		"Harem": "aafb99c1-7f60-43fa-b75f-fc9502ce29c7",
		"Military": "ac72833b-c4e9-4878-b9db-6c8a4a99444a",
		"Wuxia": "acc803a4-c95a-4c22-86fc-eb6b582d82a2",
		"Isekai": "ace04997-f6bd-436e-b261-779182193d3d",
		"4-Koma": "b11fda93-8f1d-4bef-b2ed-8803d3733170",
		"Doujinshi": "b13b2a48-c720-44a9-9c77-39c9979373fb",
		"Philosophical": "b1e97889-25b4-4258-b28b-cd7f4d28ea9b",
		"Gore": "b29d6a3d-1569-4e7a-8caf-7557bc92cd5d",
		"Drama": "b9af3a63-f058-46de-a9a0-e0c13906197a",
		"Medical": "c8cbe35b-1b2b-4a3f-9c37-db84c4514856",
		"School Life": "caaa44eb-cd40-4177-b930-79d3ef2afe87",
		"Horror": "cdad7e68-1419-41dd-bdce-27753074a640",
		"Fantasy": "cdc58593-87dd-415e-bbc0-2ec27bf404cc",
		"Villainess": "d14322ac-4d6f-4e9b-afd9-629d5f4d8a41",
		"Vampires": "d7d1730f-6eb0-4ba6-9437-602cac38664c",
		"Delinquents": "da2d50ca-3018-4cc0-ac7a-6b7d472a29ea",
		"Monster Girls": "dd1f77c5-dea9-4e2b-97ae-224af09caf99",
		"Shota": "ddefd648-5140-4e5f-ba18-4eca4071d19b",
		"Police": "df33b754-73a3-4c54-80e6-1a74a8058539",
		"Web Comic": "e197df38-d0e7-43b5-9b09-2842d0c326dd",
		"Slice of Life": "e5301a23-ebd9-49dd-a0cb-2add944c7fe9",
		"Aliens": "e64f6742-c834-471d-8d72-dd51fc02b835",
		"Cooking": "ea2bc92d-1c26-4930-9b7c-d5c0dc1b6869",
		"Supernatural": "eabc5b4c-6aff-42f3-b657-3e90cbd00b75",
		"Mystery": "ee968100-4191-4968-93d3-f82d72be7e46",
		"Adaptation": "f4122d1c-3b44-44d0-9936-ff7502c39ad3",
		"Music": "f42fbf9e-188a-447b-9fdc-f19dc1e4d685",
		"Full Color": "f5ba408b-0e7a-484d-8d49-4e9125ac96de",
		"Tragedy": "f8f62932-27da-4fe4-8ee1-6779a8c5edba",
		"Gyaru":"fad12b5e-68ba-460e-b933-9ae8318f5b6"
	},
	"mode": "AND",
	"included": [],
	"excluded": [],
	# "ratings": ["safe","suggestive", "erotica", "pornographic"]
	"ratings": ["safe","suggestive", "erotica"]
}


def json_load(filename="mango.config", j_dict=config):
	try:
		f = open(filename, "r")
		j_file = f.read()
		f.close()
		j_dict.update(json.loads(j_file))
	except Exception as e:
		print("Error opening file:\n" + str(e))
	

def save_json(filename="mango.config", j_obj=config):
	try:
		f = open(filename, "w")
		f.write(json.dumps(j_obj))
		f.close()
	except Exception as e:
		print("Error when saving file:\n" + str(e))

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
	save_json()
	return response

def get_tags():
	tag_resp = requests.get("https://api.mangadex.org/manga/tag")
	print(str(tag_resp))
	for t in tag_resp.json():
		tags["tag"].update( {t["data"]["attributes"]["name"]["en"] : t["data"]["id"]} )
	return tags

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
		view_manga_chapters(manga)
	else:
		return None


def search(query="", offset=None, limit=10, fullsearch=False, tl_filter=False):
	bearer_header = None
	if config["tl"] != "" or config["tl"] is not None:
		pass
	if config["token"] is not None: bearer_header = {'Authorization': 'Bearer ' + config["token"]["session"]}
	
	query_params = {}
	if fullsearch:
		query_params = query
	else:
		if query != "":
			query_params.update({"title":query})

		print("Filtering query by saved tags...")

		for n, tag in enumerate(tags["included"]):
			query_params.update({"includedTags["+str(n)+"]": tags["tag"][tag]})

		for n, tag in enumerate(tags["excluded"]):
			query_params.update({"excludedTags["+str(n)+"]": tags["tag"][tag]})

		query_params.update({"includedTagsMode":tags["mode"]})

		for n, prf in enumerate(tags["ratings"]): 
			query_params.update({"contentRating["+str(n)+"]" : prf})
			
	print(query_params)
	query_params.update({"limit":limit, "offset":offset})
	param_items = query_params.items()
	search_response = requests.get("https://api.mangadex.org/manga", params=query_params, headers=bearer_header)
	# return search_response.json()
	# if search_response.status_code == 200: pprint.pprint(search_response.json())
	if search_response.status_code == 200: paginated_search(search_response.json(), query, tl_filter)
	elif search_response.status_code == 204: print("No results found.")
	else:
		print(str(search_response))
		print("Error: " + str(search_response.json()["errors"]))
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

def print_manga_short(manga=None):
	if manga is not None:
		tags = []
		print(manga["data"]["attributes"]["title"]["en"])
		for tag in manga["data"]["attributes"]["tags"]:
			tags.append(tag["attributes"]["name"]["en"])
		print(tags)
		print("---")
		if manga["data"]["attributes"]["description"]["en"] is not None:
			print(manga["data"]["attributes"]["description"]["en"][0:350])
		else: print("No description available.")
		print("\n")


def paginated_search(search_response, query, tl_filter=False):
	page_lim = search_response["limit"]
	offset = search_response["offset"]
	total_results = search_response["total"]

	print("Showing results " + str(offset+1) + " through " + str(limited_add(offset, page_lim, total_results)) + " of " + str(total_results) + ".")
	manga_list = []
	for i, manga in enumerate(search_response["results"]):
		manga_list.append(manga)
		print("Page result #" + str(i+1) + ", " + str(offset+i+1) + " of " + str(total_results))
		if get_one_chapter(manga).status_code == 200: print_manga_short(manga)
		else:
			print(manga["data"]["attributes"]["title"]["en"])
			print("No chapters in filtered language.")

	print("Showing results " + str(offset+1) + " through " + str(limited_add(offset, page_lim, total_results)) + " of " + str(total_results) + ".")
	userin = input("Press A, W, or ',' for back, S, D, or '.' for foward. 'Enter' or 'e' to exit. Enter result # to read manga.\n").lower()

	while(userin):
		if userin == "a" or userin == "w" or userin == ",":
			#get previous page of results or do nothing
			if offset < page_lim:
				print("Reached the beginning of the search results.")
				userin=input("")
			else:
				search(query, offset=offset-page_lim, limit=page_lim, tl_filter=tl_filter)
				userin=None
		elif userin == "s" or userin == "d" or userin == ".":
			#get next page of results
			if offset+page_lim <= total_results:
				search(query, offset=offset+page_lim, limit=page_lim, tl_filter=tl_filter)
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
				# try:
				# 	raise 
				# 	uuid = sorted(quiet_search(query, offset=index))[0]["data"]["id"]
				# except Exception as e:
				print("Index " + str(index+1) + " not yet retrieved from server.\n" + str(e))
			else:
				print("Viewing page result " + str(index+1))
				print_manga_styled(manga_list[index])
				view_manga_chapters(manga_list[index])
			userin=input("")
		elif userin == "e" or userin == "exit":
			userin == None
			break


def check_login():
	if config["result"] == "ok" and config["token"] is not None:
		# token = config["token"]
		bearer_header = {'Authorization': 'Bearer ' + config["token"]["session"]}
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
	view_manga_chapters(view_response.json())

def get_chap_no(chapter):
	return str(chapter["data"]["attributes"]["chapter"])

def get_one_chapter(manga=None):
	params = {"limit":100, "manga":manga["data"]["id"], "translatedLanguage[0]":config["tl"]}
	# print("GET " + str(params))
	# print("Checking for chapters with query: " + str(params))
	ch_response = requests.get("https://api.mangadex.org/chapter", params=params)
	# print(str(ch_response.json()))
	# print(str(ch_response))
	return ch_response

def view_manga_chapters(manga=None, title=None):
	params = {"limit":100, "manga":manga["data"]["id"], "translatedLanguage[0]":config["tl"]}
	ch_response = requests.get("https://api.mangadex.org/chapter", params=params)
	# print(str(ch_response.json()))
	try:
		ch_json = ch_response.json()
	except Exception as e:
		if ch_response.status_code == 204:
			print("There were no chapters with the selected parameters\n" + str(params))
			params.pop("translatedLanguage")
			print(str(params))
		else:
			print("Error retrieving chapters: " + str(e))
			# all_lang_res = requests.get("https://api.mangadex.org/chapter", params=params)
	#should have only returned 1 manga's chapters
	if ch_response.status_code == 200:
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
			chapter_list.extend(ch_json["results"])
			offset = offset + page_lim
			if(offset < total_results):
				ch_json = requests.get("https://api.mangadex.org/chapter", params=params)

		sorted_list = sorted(chapter_list, key=lambda c: c["data"]["attributes"]["publishAt"])
		# pprint.pprint(str(sorted_list))
		dl_menu = {}
		default_ch_no = 0
		ch_formatted_str = ""

		for chapter in sorted_list:
			title = str(chapter["data"]["attributes"]["title"])
			chap_no = chapter["data"]["attributes"]["chapter"]
			tl_lang = str(chapter["data"]["attributes"]["translatedLanguage"])
			pub_date = str(chapter["data"]["attributes"]["publishAt"])

			if chap_no is None or chap_no == "":
				if len(sorted_list) == 1:
					chap_no = "1"
				else:
					chap_no = "no_ch_" + str(default_ch_no)
				default_ch_no+=1

			ch_line = chapter["data"]["id"] + "	" + pub_date.split('T')[0] + "	Chapter " + chap_no + "		" + tl_lang + "	" + title
			ch_formatted_str+=ch_line.encode(errors="replace").decode(errors="replace") + "\n"
			print(ch_line)
			#might want to check for chapter version and pick highest
			dl_menu[chap_no]=chapter

		print("" + str(total_results) + " chapters found in the specified language.")
		userin = input("Download chapter by number or 'a'll: ").lower()
		# pprint.pprint("dl menu:" + str(dl_menu))
		manga_path = "./manga/" + str(manga["data"]["id"])+ "/"
		toc_path = os.path.normpath((manga_path + str(manga["data"]["attributes"]["title"]["en"]) + ".txt")[0:200])
		while(userin in dl_menu.keys()):
			try:
				#save table of contents and title file
				try:
					pathlib.Path(manga_path).mkdir(parents=True, exist_ok=True)
					f = open(toc_path, "x")
					f.write(str(ch_formatted_str))
					f.close()
				except FileExistsError:
					pass
				save_manga_chapter(manga, dl_menu[userin], ch_label=chap_no)

			except Exception as e:
				print("Could not save chapter " + userin)
				print("Exception: " + str(e))
			userin = input("Download chapter: ")
		if userin == 'all' or userin == 'a':
			try:
				pathlib.Path(manga_path).mkdir(parents=True, exist_ok=True)
				f = open(toc_path, "x")
				f.write(str(ch_formatted_str))
				f.close()
			except FileExistsError:
				pass
			for ci in dl_menu:
				try:
					save_manga_chapter(manga, dl_menu[ci], ch_label=chap_no)
				except Exception as e:
					print("Could not save chapter " + chid)
					print("Exception: " + str(e))
		print("End")

def save_manga_chapter(manga=None, chapter=None, chapter_id=None, ch_label="Oneshot"):
	manga_id = manga["data"]["id"]
	if chapter_id is not None:
		ch_id=chapter_id
	else:
		ch_id=chapter["data"]["id"]
	print("Retrieving chapter " + ch_id)
	try:
		ch_no = get_chap_no(chapter)
		if ch_no is None: ch_no = ch_label
		transfers = []
		save_path="./manga/" + str(manga_id) + "/" + str(ch_no)
		pathlib.Path(save_path).mkdir(parents=True, exist_ok=True)
		md_url=get_mdhome_url(ch_id)
		ch_hash=chapter["data"]["attributes"]["hash"]
		ch_data_array=chapter["data"]["attributes"]["data"]
		# print(str(md_url))
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
					print(".", end="", flush=True)
				except Exception as e:
					print("Error on file write:" + str(e))
					break

		except Exception as e:
			print("Error getting or saving page " + str(i) +  "\n" + str(e))
	print("\n" + ch_no + " saved to " + save_path + "/")

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

def tags_menu():
	print("Control tag content and search settings.  Enter a tag again to remove it from a list.")
	helpstr = "'g'et or 'l'ist all tags, a'dd or 'i'nclude to add tags to search, 'r'emove or e'x'clude to remove tags, 'c'ontent for content rating filter, 'm' for tag inclusion mode"
	print(helpstr)
	modified = False
	
	end = False
	while end == False:
		t_in = input("" ).lower()

		if t_in == "e" or t_in == "exit" or t_in == "": end=True
		elif t_in == "m" or t_in == "mode":
			tags["mode"] = validate_mode(input("Enter AND or OR\n"))
			modified = True
			print("Mode set: " + str(tags["mode"]))
		elif t_in == "a" or t_in == "i":
			print("Included tags: " + str(tags["included"]))
			print("Only manga with included tags will appear in search results, AND mode requires results to include all tags, OR mode allows manga that include ANY tag.  Entering an existing tag removes it.\n")
			for tag in validate_tags(list_from_input()):
				if not tag in tags["included"]: tags["included"].append(tag)
				else: 
					tags["included"].remove(tag)
			modified = True
			print("Updated: " + str(tags["included"]))
		elif t_in == "x" or t_in == "r": 
			print("Excluded tags: " + str(tags["excluded"]))
			print("Manga with excluded tags will not appear in search results.  Entering an existing tag removes it.\n")
			for tag in validate_tags(list_from_input()):
				if not tag in tags["excluded"]: tags["excluded"].append(tag)
				else: 
					tags["excluded"].remove(tag)
			modified = True
			print("New Excluded Tags: " + str(tags["excluded"]))
		elif t_in == "c" or t_in == "content": 
			print("Current Content Ratings: " + str(tags["ratings"]))
			print("Any content tag not included is excluded. Valid content tags: safe, suggestive, erotica, pornographic. Default: All but pornographic\n")
			for cf in validate_cf(list_from_input()):
				if not cf in tags["ratings"]: tags["ratings"].append(cf)
				else:
					tags["ratings"].remove(cf)
			modified = True
			print("Updated Content Ratings: " + str(tags["ratings"]))
		elif t_in == "g" or t_in == "l": pprint.pprint(get_tags())

	if modified:
		save_json("tags.conf", tags)
	print("Returned to main menu")

def list_from_input():
	end = False
	ret_list = []
	u_in = input("Enter input in sequence, or press enter with no input to exit listing mode.\n")
	while u_in != "" and u_in != "e" and u_in is not None:
		ret_list.append(u_in)
		u_in=input("")
	return ret_list

def validate_cf(cf_list):
	valid = ["safe","suggestive", "erotica", "pornographic"]
	vl = []
	for cf in cf_list:
		if cf.lower() in valid: vl.append(cf.lower())
	return vl

def validate_tags(t_list):
	vl = []
	for t in t_list:
		if t in tags["tag"]: vl.append(t)
		else: print("Tag " + str(t) + " was invalid.  Tags are case sensitive.")
	return vl

def validate_mode(m_in):
	if m_in.lower() == "all" or m_in.lower() == "and":
		return "AND"
	elif m_in.lower() == "or" or m_in.lower() == "any":
		return "OR"
	else:
		return "AND"

print("Mangospex version 0.0.3 - direpenguin@gmail.com")
print("Search for manga by title or parameter dictionary (https://api.mangadex.org/docs.html#operation/get-search-manga)")
print("Logging in is currently optional")
help_string = "Suggested Usage Manual:  Enter your username and password (or ignore the login error).  Search for a manga by title, or set up tag filtering and press enter with no search term to search by tags alone.  From the search menu, enter the list result number of a desired manga to view its description and chapters.  From the chapter view, enter 'a' to download all chapters or select a chapter number to download.  You can note the UUID of the manga and use the View command to see it directly without searching.  Saved files are in a UUID-named folder in the same directory as Main.py.  There is a table of contents file with the name of the manga in the saved directory.\nTLDR: search > enter result # > download all chapters with 'a'\n"
try:
	json_load()
	json_load("tags.conf", tags)
except Exception as e:
	print("Could not load preferences files, first time running?")
if not check_login():
	response = login()
	if not response:
		print("There was an error logging in.")
else:
	print(config["username"] + " is already logged in.")

menu_list=("'M'enu", "'H'elp", "'T'ags", "'C'heck", "'S'earch", "'R'andom", "'V'iew (by manga UUID entry)", "'D'ownload (by chapter UUID)", "Exit")
end=False

while end==False:

	menu = input("Enter a manga name to search or enter 'm'enu for a list of all commands, or 'H'elp for guidance\n" ).lower()
	if menu == "e" or menu == "exit": end=True
	elif menu == "m" or menu == "menu": print(str(menu_list))
	elif menu == "t" or menu == "tags": tags_menu()
	elif menu == "c" or menu == "check": print("Logged in? " + str(check_login()))
	elif menu == "r" or menu == "random": random_search()
	elif menu == "s" or menu == "search": search(input("Enter full or partial manga title:\n"), fullsearch=False)
	#c20350bb-0e53-493f-8c92-71198d57bf8a example string
	elif menu == "v" or menu == "view" or menu == "uuid": view_manga(input("Enter a manga's ID: "))
	elif menu == "h" or menu == "help": print(help_string)
	# elif menu == "d" or menu == "dl" or menu == "download": save_manga_chapter(input("Enter a chapter's ID: "))
	elif menu == "l" or menu == "lang" or menu == "language": config["tl"]=input("Enter a language code (ex: en=English, es-la=Latin American Spanish): ")
	else: search(menu)

