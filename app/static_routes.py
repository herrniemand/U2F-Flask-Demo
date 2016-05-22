from app import app

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/<path:path>')
def send_js(path):
    return app.send_static_file(path)