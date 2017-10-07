from flask import Flask

@app.route("/api/v1/info")
def home_index():
	conn = sqlite3.connect('app.db')
	print ("Opened database successfully");
	api_list=[]
	cursor = conn.execute("SELECT buildtime, version, methods, links from apirelease")

	for row in cursor:
		api = {}
		api['version'] = row[0]
		api['buildtime'] = row[1]
		api['methods'] = row[2]
		api['links'] = row[3]
		api_list.append(api)
	conn.close()

	return jsonify({'api_version': api_list}), 200 






app = Flask(__name__) 

if __name__ == "__main__": 
	app.run(host='0.0.0.0', port=5000, debug=True) 
