from flask import Flask, render_template, request, redirect
app = Flask(__name__)

  
@app.route('/clear', methods = ['POST'])
def clear():  
  # clear list
  del todo_list[:]
  return  redirect('/')
  
@app.route('/submit', methods=['GET', 'POST'])
def add_task():
  task =  request.form["task"]
  email = request.form["email"]
  priority = request.form["priority"]  
  # validate email
  if len(email.split('@')) != 2:
    return  redirect('/')
  # validate priority
  priorities = ['high','medium','low']
  if priority not in priorities:
    return  redirect('/')
  tup = ((task, email, priority))
  todo_list.append(tup)
  return  redirect('/')

@app.route('/')
def view_home(): 
    return render_template('index.html', todo_list=todo_list)

todo_list = []
if __name__ == "__main__":
    app.run()










