from flask import Flask, render_template, send_from_directory
import subprocess
import threading
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/streamlit')
def streamlit():
    return render_template('streamlit.html')

def run_streamlit():
    os.system('streamlit run dashboard.py')

if __name__ == '__main__':
    # Run the Streamlit app in a separate thread
    thread = threading.Thread(target=run_streamlit)
    thread.start()
    
    app.run(debug=True, use_reloader=False)
