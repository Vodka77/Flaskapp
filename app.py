from flask import Flask, render_template, request, url_for, flash, redirect
lol
app = Flask(__name__)
app.config['SECRET_KEY'] = '03a789e8af223fc21a2896478b5cd84446c8eb595427b229'
messages = [{'title': ' ',
             'content': 'There Is No Conetnt'},
            {'title': ' ',
             'content': 'There Is No Conetnt'}
    
            ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            messages.append({'title': title, 'content': content})
            return redirect(url_for('index'))

    return render_template('create.html')
