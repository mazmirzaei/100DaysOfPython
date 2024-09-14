# the styling and the structure, and then to replace the content,
# for example, the title or the subtitle or the body with dynamic content
# that's generated each time we load a specific page.
from flask import Flask, render_template
import requests
import random
import datetime 

app = Flask(__name__)

# create random number
random_number = random.randint(0,10)

#  current year 
today = datetime.datetime.now()
year = today.year


# name , gender , age
@app.route('/')
def home_page():
    return render_template("index.html", num=random_number, year=year)

@app.route('/guess/<name>')
def guess_age_gender(name):
    # agify API setting up
    agify_end_point = 'https://api.agify.io'
 
    agify_param = {
        'name': name,
    }
    response_age = requests.get(agify_end_point, params=agify_param)
    response_age.raise_for_status()
    age_data = response_age.json()['age']

    # genderize API setting
    genderize_end_point = 'https://api.genderize.io'
    genderize_param = {
        'name': name,
    }
    response_genderize = requests.get(genderize_end_point, params=genderize_param)
    response_genderize.raise_for_status()
    gender_data = response_genderize.json()['gender']
    return render_template("guess.html",age=age_data, gender=gender_data, name=name)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/5abcca6f4e39b4955965'
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)
    

if __name__ == '__main__':
    app.run(debug=True)
