from flask import Flask, render_template, request, redirect, session
import sqlite3
app = Flask(__name__)

app.secret_key = 'necocchi'

@app.route('/') 
def hello_world():
    return 'Hello, World!'

@app.route('/add')
def add_get():
    if 'user_id' in session:
        return render_template('add.html')
    else:
        return redirect('/login')

@app.route('/add', methods=["POST"])
def add_post():
    # name="task" インプットタグに打ち込まれた内容を取得
    if 'user_id'in session:
        user_id=session['user_id']
        py_task = request.form.get("task")
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("INSERT INTO task VALUES(null, ?, ?)",(py_task,user_id))
        # DBの保存
        conn.commit()
        conn.close()
        return redirect('/list')

@app.route('/list')
def list():
    if 'user_id' in session:
        user_id = session['user_id']
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("SELECT name from users where id = ?",(user_id,))
        user_name = c.fetchone()[0]
        c.execute("SELECT id, task FROM task where user_id = ?", (user_id,))
        tasklist = []
        for row in c.fetchall():
            tasklist.append({"id":row[0], "task":row[1]})
        c.close
        print(tasklist)
        return render_template('list.html', html_tasklist=tasklist, user_name = user_name)
    else:
        return redirect('/login')

@app.route("/edit/<int:id>")
def edit(id):
    if 'user_id' in session:
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("SELECT task FROM task WHERE id = ?", (id,))
        task = c.fetchone()
        conn.close
        if task is None:
            return "タスクがありません"
        else:
            py_item = {"id":id, "task":task[0]}
            return render_template("edit.html", task = py_item)
    else:
        return redirect("/login")

@app.route('/edit', methods=["POST"])
def post_edit():
    if 'user_id' in session : 
        item_id = request.form.get("task_id")
        item_id = int(item_id)
        # 入力フォームからとってくると文字列型になるのでInt型に整形
        task = request.form.get("task")
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("UPDATE task SET task = ? WHERE id = ?", (task, item_id))
        conn.commit()
        c.close
        return redirect('/list')
    else:
        return redirect('/login')

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' in session:
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("DELETE FROM task WHERE id = ?", (id,))
        conn.commit()
        c.close
        return redirect('/list')
    else:
        return render_template("login.html")


@app.route('/regist/')
def regist_get():
    # print("HELLO")
    if 'user_id' in session:
        return render_template('list.html')
    else:
        return render_template('regist.html')

@app.route('/regist', methods=['POST'])
def regist_post():
    name = request.form.get("user_name")
    password = request.form.get("user_pass")
    email = request.form.get("user_address")
    conn = sqlite3.connect('necocchi.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(null, ?, ?, ?)",(name, password, email))
    conn.commit()
    c.close
    return redirect('/login')

@app.route('/login', methods =["GET"])
def login_get():
    if 'user_id' in session:
        return redirect("/list")
    else:
        return render_template("login.html")

@app.route('/login', methods=["POST"])
def login_post():

    name = request.form.get("user_name")
    password = request.form.get("user_pass")
    conn = sqlite3.connect('necocchi.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE name = ? AND password = ?", (name, password))
    user_id = c.fetchone()
    conn.close()
    if user_id is None:
        return render_template('login.html')
    else:
        session['user_id'] = user_id[0]
        return redirect('/list')

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect('/login')

@app.errorhandler(404)
def notfound(error):
    return "404ページです。URL違いです"

if __name__ == '__main__':
    app.run(debug=True)