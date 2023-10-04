from flask import Flask, render_template
import requests
from requests.structures import CaseInsensitiveDict
app = Flask(__name__)

def get_cur():
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_QUv4jHtgokP22VThdSjaB50OcdOCfVRbCR08zvU0&currencies=TRY"
    resp = requests.get(url)
    if resp.status_code == 200:
        cur = resp.json()
        val = cur['data']['TRY']
        print(val)
        return val
    else:
        notfound = "This website is not currently functioning due to the exceeded limit in API."
        print(notfound)
        return notfound

@app.route("/")
def get_tl():
    currency = get_cur()
    return render_template("index.html", tl = currency)
    
if __name__ == "__main__":
  app.run()
