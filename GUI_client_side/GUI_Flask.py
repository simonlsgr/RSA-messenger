import os
import flask
import json

basedir = os.path.abspath(os.path.dirname(__file__))
datafile = os.path.join(basedir, 'fetched_messages.json')

app = flask.Flask(__name__)

@app.route('/index.html')
def index():
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="https://thenounproject.com/api/private/icons/1238399/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=16&flipX=false&flipY=false&foregroundColor=%23000000&foregroundOpacity=1&imageFormat=png&rotation=0&token=gAAAAABjsyejDaujQ4nYlgT1OD9UIzOlDLBFGj1M_Xm1oraaDDz4BdSK_o2yDS3l0vpmrNCmQV_Z0NKdZulxZhE1D8MkDjN1JA%3D%3D" type="image/x-icon">
    <link rel="stylesheet" href="static/css/messenger.css">
    <title>RSA Messenger</title>
</head>
<body>
    <main class="main-wrapper">
        <ul class="wrapper-contacts">
    """
    with open(os.path.join(basedir + "/fetched_messages.json"), "r") as f:
        data = json.load(f)
        name = data[0]["sender_name"]
        html += f"""<a href="{data[0]["sender_name"]}.html" class="contact selected-contact" id="contact_id_{data[0]["sender_name"]}">{data[0]["sender_name"]}</a>
        """
        for i in range(len(data)-1):
            j = data[i+1]["sender_name"]
            print(data[i+1]["sender_name"])
            html += f"""
            <a href="{j}.html" class="contact" id="contact_id_{j}">{j}</a>
            """
    html += f"""</ul>
    <section class="section-contact">
            <div class="contact-name-wrapper">
                <div class="placeholder-contact-name"></div>
                <h1 class="contact-name">{name}</h1>
            </div>
            <ul class="texts">
                 <li class="message sent">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vero et autem placeat fugiat beatae adipisci sit reiciendis sed? Sequi ullam assumenda accusantium saepe aperiam velit soluta temporibus, delectus dolorum nihil deleniti dolor laudantium sapiente ut consequatur minus sint! Porro, sit!</li>
                <li class="message received">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab commodi dolores asperiores qui beatae aut corrupti? Repellendus, quis. Facere natus vitae in molestias ut, aut quidem quaerat veniam modi alias commodi iste nobis itaque accusantium sapiente minima id consequatur. Eaque.</li>
            </ul>
            <form class="form-message-input">
                <input type="text" class="message-input" placeholder="Message…">
                <button class="send-button">↑</button>
            </form>
        </section>
            </main>
</body>
</html>
        """
    return html

@app.route('/<name>.html')
def contact(name):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="https://thenounproject.com/api/private/icons/1238399/edit/?backgroundShape=SQUARE&backgroundShapeColor=%23000000&backgroundShapeOpacity=0&exportSize=16&flipX=false&flipY=false&foregroundColor=%23000000&foregroundOpacity=1&imageFormat=png&rotation=0&token=gAAAAABjsyejDaujQ4nYlgT1OD9UIzOlDLBFGj1M_Xm1oraaDDz4BdSK_o2yDS3l0vpmrNCmQV_Z0NKdZulxZhE1D8MkDjN1JA%3D%3D" type="image/x-icon">
    <link rel="stylesheet" href="static/css/messenger.css">
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
    html += f"""</ul>
    <section class="section-contact">
            <div class="contact-name-wrapper">
                <div class="placeholder-contact-name"></div>
                <h1 class="contact-name">{name}</h1>
            </div>
            <ul class="texts">
                 <li class="message sent">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vero et autem placeat fugiat beatae adipisci sit reiciendis sed? Sequi ullam assumenda accusantium saepe aperiam velit soluta temporibus, delectus dolorum nihil deleniti dolor laudantium sapiente ut consequatur minus sint! Porro, sit!</li>
                <li class="message received">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ab commodi dolores asperiores qui beatae aut corrupti? Repellendus, quis. Facere natus vitae in molestias ut, aut quidem quaerat veniam modi alias commodi iste nobis itaque accusantium sapiente minima id consequatur. Eaque.</li>
            </ul>
            <form class="form-message-input">
                <input type="text" class="message-input" placeholder="Message…">
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
    