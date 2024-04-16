from flask import Flask, render_template,request
import zipfile
import os
import chromadb
from chromadb.config import Settings

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/out',methods=['POST'])
def out():
    if request.method == 'POST':
        dialog = request.form['dialog']
        client = chromadb.PersistentClient(path="C:\\Users\\Win10\\Downloads\\archive (3)\\db")
        collection = client.get_collection(name="Students")
        results = collection.query(
        query_texts=[dialog],
        n_results=5
        )
        mov=[]
        ver=[]
        for movie in results['metadatas'][0]:
            mov.append(movie['chapter'])
            ver.append(movie['verse'])
        return render_template('out.html',movie=mov,verse=ver)
if __name__ == '__main__':
    app.run(debug=True)
