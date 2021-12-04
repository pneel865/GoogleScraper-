from flask import render_template, url_for, flash, redirect, request, jsonify,send_file
from flasksite import webscrap, app


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		query = request.form.get('search')
		data = webscrap.get_data(query)
		return render_template('main.html', text=request.form.get('search'), data=data) 

	return render_template('main.html') 

@app.route('/downloader')
def download_file():
	path1 = "scrapdata.xlsx"
	return send_file(path1, as_attachment=True, cache_timeout=0)






