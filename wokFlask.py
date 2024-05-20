import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template('wokofasia.html')

@app.route('/uploaded', methods = ['GET', 'POST'])
def uploaded():
    if request.method == 'POST':
        cuisine = request.form['cuisine']
        name = request.form['name']
        time = request.form['time']
        servingsize = request.form['servingsize']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        
        #for chinese recipes
        if cuisine == 'chinese':
            #insert into chinese table
        
        #for malay recipes
        elif cuisine == 'malay':
            #insert into malay table
        
        #for indian recipes
        elif cuisine == 'indian':
            #insert into indian table
        
        #for other recipes
        elif cuisine == 'others':
            #insert into others table
        
        else:
            return 'Form is filled incorrectly. Data not saved. Please ensure your entries follow the format suggested, and try again!'
    
    return render_template('wokUploaded.html')

if __name__ == '__main__':
    app.run()
