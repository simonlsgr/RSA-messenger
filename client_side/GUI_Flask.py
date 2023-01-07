import os
import flask
import json
import datetime
import sys

import backend_client_side.server_handling as server_handling



basedir = os.path.abspath(os.path.dirname(__file__))
datafile = os.path.join(basedir, 'fetched_messages.json')


STANDARD_HEADER = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><link rel="icon" href="https://thenounproject.com/api/private/icons/1238399/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=16&flipX=false&flipY=false&foregroundColor=%23000000&foregroundOpacity=1&imageFormat=png&rotation=0&token=gAAAAABjsyejDaujQ4nYlgT1OD9UIzOlDLBFGj1M_Xm1oraaDDz4BdSK_o2yDS3l0vpmrNCmQV_Z0NKdZulxZhE1D8MkDjN1JA%3D%3D" type="image/x-icon"><link rel="stylesheet" href="/static/css/messenger.css">"""

app = flask.Flask(__name__)

@app.route('/')
def login():
    html = STANDARD_HEADER
    html += """<link rel="stylesheet" href="static/css/login.css"><title>Login</title></head><body>"""
    html += """<div class="login-wrapper"><div class="login-form"><h1 class="login-title">Login</h1><form action="/index.html" method="POST"><input type="text" name="username-login" class="login-input" placeholder="Username" required><input type="password" name="password-login" class="login-input" placeholder="Password" required><button type="submit" class="login-button">Login</button></form></div></div>"""
    return html




@app.route('/index.html', methods = ["GET", "POST"])
def index():
    
    if flask.request.method == "POST":
        username_from_login = flask.request.form.getlist("username-login")
        password_from_login = flask.request.form.getlist("password-login")
        if server_handling.server_handling(username_from_login[0], password_from_login[0], "auth").login_status == "Login successful":
            global username
            global password
            username = username_from_login[0]
            password = password_from_login[0]
            server_handling.server_handling(username, password, "f")
            global login_successful
            login_successful = True
        else:
            login_successful = False
    else:
        login_successful = True
    
    html = STANDARD_HEADER
    html += """<title>RSA Messenger</title></head><body>
    <main class="main-wrapper">
        <ul class="wrapper-contacts">
    """
    with open(os.path.join(basedir + "/fetched_messages.json"), "r") as f:
        data = json.load(f)
        name = data[0]["sender_name"]
        html += f"""<a href="/messenger/{data[0]["sender_name"]}.html" class="contact selected-contact" id="contact_id_{data[0]["sender_name"]}">{data[0]["sender_name"]}</a>
        """
        for i in range(len(data)-1):
            j = data[i+1]["sender_name"]
            html += f"""
            <a href="/messenger/{j}.html" class="contact" id="contact_id_{j}">{j}</a>
            """
    html += f"""<form action="/messenger/{name}.html" class="form-new-contact"><input type="text" class="new-contact-input" name="new-contact" placeholder="Username…"><button class="add-contact"></button></form></ul>
    <section class="section-contact">
            <div class="contact-name-wrapper">
                <div class="placeholder-contact-name"></div>
                <h1 class="contact-name">{name}</h1>
            </div>
            <ul class="texts">"""
    with open(os.path.join(basedir + "/fetched_messages.json"), "r") as f:
        data = json.load(f)
        for i, j in enumerate(data[0]["message"]):
            if j["sender_name"] == name:
                html += f"""
                <li class="message received">{j["message"]}</li>
                """
            elif j["receiver_name"] == name:
                html += f"""
                <li class="message sent">{j["message"]}</li>
                """

    html += """</ul>
            <form class="form-message-input">
                <input type="text" class="message-input" placeholder="Message…">
                <button class="send-button">↑</button>
            </form>
        </section>
            </main>
</body>
</html>
        """
    if login_successful:
        return html
    else:
        return flask.redirect("/")



@app.route('/messenger/<name>.html', methods = ["GET", "POST"])
def contact(name):
    
    if login_successful == False:
        return flask.redirect("/")
    elif login_successful == True:
        server_handling.server_handling(username, password, "f")
    
    ### COMMUNICATE WITH BACKEND ###
    if flask.request.method == "POST":
        if flask.request.form.getlist("new-message") not in [[], [""]]:
            input_new_message = flask.request.form.getlist("new-message")[0]
            with open(basedir + "/fetched_messages.json", "r") as f:
                data = json.load(f)
                for i in data:
                    if i["sender_name"] == name:
                        server_handling.server_handling(username, password, "s", input_new_message, name)
                        i["message"].append({"message_id": 0, "sender_name": username, "receiver_name": name, "message": input_new_message, "date": datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")})
                with open(basedir + "/fetched_messages.json", "w") as f:
                    json.dump(data, f)
            
        elif flask.request.form.getlist("new-contact") not in [[], [""]]:
            input_new_contact = flask.request.form.getlist("new-contact")[0]
            with open(basedir + "/fetched_messages.json", "r") as f:
                data = json.load(f)
                counter = 0
                for i in data:
                    if i["sender_name"] == input_new_contact:
                        counter += 1
                        
            if counter == 0:            
                data.append({"sender_name": input_new_contact, "message": []})
                with open(basedir + "/fetched_messages.json", "w") as f:
                    json.dump(data, f)
    
    ### HTML START ###
    html = STANDARD_HEADER
    html += f"""<!DOCTYPE html>
    <title>{name}</title>
</head>
<body>
    <main class="main-wrapper">
        <ul class="wrapper-contacts">
    """
    with open(os.path.join(basedir + "/fetched_messages.json"), "r") as f:
        data = json.load(f)
        for i in range(len(data)):
            j = data[i]["sender_name"]
            if j == name:
                html += f"""
                <a href="{j}.html" class="contact selected-contact" id="contact_id_{j}">{j}</a>
                """
            else:
                html += f"""
                <a href="{j}.html" class="contact" id="contact_id_{j}">{j}</a>
                """
    html += f"""<form action="/messenger/{name}.html" class="form-new-contact" method="POST"><input type="text" class="new-contact-input" name="new-contact" placeholder="Username…"><button class="add-contact"></button></form></ul>
    <section class="section-contact">
            <div class="contact-name-wrapper">
                <div class="placeholder-contact-name"></div>
                <h1 class="contact-name">{name}</h1>
            </div>
            <ul class="texts">"""
    
    with open(os.path.join(basedir + "/fetched_messages.json"), "r") as f:
        data = json.load(f)
        for i, j in enumerate(data):
            if j["sender_name"] == name:
                for k in j["message"]:
                    if k["sender_name"] == name:
                        html += f"""
                        <li class="message received">{k["message"]}</li>
                        """
                    elif k["receiver_name"] == name:
                        html += f"""
                        <li class="message sent">{k["message"]}</li>
                        """
    html += f"""</ul>
            <form action="/messenger/{name}.html" class="form-message-input" method="POST">
                <input type="text" class="message-input" name="new-message" placeholder="Message…">
                <button class="send-button">↑</button>
            </form>
        </section>
            </main>
</body>
</html>
        """
    return html

        
        



if __name__ == '__main__':
    app.run(debug=True)
    