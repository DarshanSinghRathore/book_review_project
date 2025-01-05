import os
from flask import Flask, render_template, request, redirect, url_for
import yaml

app = Flask(__name__)

# Load reviews from a YAML file
def load_reviews():
    file_path = os.path.join(os.path.dirname(__file__), 'reviews.yaml')
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        return yaml.safe_load(file) or []

# Save reviews to the YAML file
def save_reviews(reviews):
    file_path = os.path.join(os.path.dirname(__file__), 'reviews.yaml')
    with open(file_path, 'w', encoding='utf-8-sig') as file:
        yaml.safe_dump(reviews, file, default_flow_style=False, allow_unicode=True)

@app.route('/')
def home():
    reviews = load_reviews()
    return render_template('index.html', reviews=reviews)

@app.route('/add_review', methods=['POST'])
def add_review():
    new_review = request.form['review']
    
    reviews = load_reviews()
    reviews.append({'Review': new_review})  # Adding new review to the list
    
    save_reviews(reviews)  # Save updated reviews back to the file
    
    return redirect(url_for('home'))  # Redirect back to the home page to show updated reviews

if __name__ == "__main__":
    app.run(debug=True)
