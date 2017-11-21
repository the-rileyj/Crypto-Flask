#https://api.coinmarketcap.com/v1/ticker/
from flask import Flask
app = Flask(__name__)

"""def setIOTA():
    r = requests.get("https://api.coinmarketcap.com/v1/ticker/iota/")
    if r.status_code == 200:
        #global obj = json.loads(r.text)[0]
        obj.update(json.loads(r.text)[0])
        if "error" in obj.keys():
            print("Initial Data Grab Failed")
            print(obj["error"])
    else:
        print("Initial Data Grab Failed")"""

def getIOTA():
    return """
        <!DOCTYPE html>
            <html lang="en">
                <head>
                        <meta charset="utf-8" />
                        <title>Crypto-Watcher</title>      
                        <link rel="shortcut icon" href="favicon.ico">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no, user-scalable=no">
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js"></script>
                        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
                        <script src="https://code.jquery.com/jquery-3.1.0.js"></script>
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
                        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
                        <link href="https://fonts.googleapis.com/css?family=Oswald" type="text/css" rel="stylesheet">
                        <link href="https://unpkg.com/vuetify/dist/vuetify.min.css" rel="stylesheet">
                        <script src="https://cdnjs.cloudflare.com/ajax/libs/axios/0.17.1/axios.min.js"></script>
                        <link href="static/cf.css" rel="stylesheet">
                        <script src="static/cf.js"></script>
                </head>
                <body>
                    <div class="container-fluid">
                        <div class="row no-gutters">
                            <div class="col">
                                <p>
                                    Name: <span id="name"></span>
                                </p>
                                <p>
                                    USD: $<span id="price_usd"></span>
                                </p>
                                <p>
                                    BTC: <span id="price_btc"></span>
                                </p>
                                <p class="pchange">
                                    Percent Change (1hour)  : <span id="percent_change_1h"></span>%
                                </p>
                                <p class="pchange">
                                    Percent Change (24hours): <span id="percent_change_24h"></span>%
                                </p>
                                <p class="pchange">
                                    Percent Change (7days)  : <span id="percent_change_7d"></span>%
                                </p>
                            </div>
                        </div>
                    </div>
                    <script>
                           
                    </script>
                </body>
            </html>"""

@app.route('/static/<path:path>')
def send_js(path):
        return send_from_directory('static', path)

@app.route("/")
def show_page():
    return getIOTA()


if __name__ == "__main__":
    app.run(port="4500")
