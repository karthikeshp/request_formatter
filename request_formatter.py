import json

from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route("/format_xmls/", methods=['GET', 'POST'])
def json_formatter():
    if request.method == 'POST':
        tuxml = request.form.get('tuxml', '')
        dlxml = request.form.get('dlxml', '')
        clxml = request.form.get('clxml', '')
        idaxml = request.form.get('idaxml', '')
        tm_qs = request.form.get('tm_qs', '')
        return json.dumps({
            'tuxml': tuxml, 'dlxml': dlxml, 'clxml': clxml,
            'idaxml': idaxml, 'tm_qs': tm_qs})
    return render_template('get_xmls.html')

