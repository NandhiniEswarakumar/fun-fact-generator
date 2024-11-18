from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session management and flash messages
  
# Fun facts categorized
fun_facts = {
    "funny": [
        "In Switzerland, it’s illegal to own just one guinea pig.",
        "A shrimp's heart is located in its head.",
        "Cows have best friends and get stressed when they are separated.",
        "Apples float because they are 25% air.",
        "A shrimp's heart is located in its head."
    ],
    "animal_facts": [
        "Axolotls can regenerate their limbs.",
        "Octopuses have blue blood and three hearts.",
        "The heart of a blue whale is so big that a human can swim through its arteries.",
        "It is physically impossible for pigs to look up into the sky.",
        "An ostrich's eye is bigger than its brain.",
        "Ants take rest for around 8 minutes in a 12-hour period.",
        "Humans are the only animals that blush.",
        "Dolphins have names for each other and can call each other by name.",
        "Starfish have no brain."
    ],
    "pop_culture": [
        "The first film ever to be made was 'Roundhay Garden Scene' in 1888.",
        "The longest-running TV show is 'The Simpsons'.",
        "The first iPhone was released in 2007.",
        "Mickey Mouse was originally named Morty."
    ],
    "food": [
        "Honey never spoils; archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
        "Ketchup was sold in the 1830s as medicine.",
        "Chocolate was once used as currency by the Aztecs."
    ],
    "science": [
        "A day on Venus is longer than a year on Venus.",
        "One million Earths could fit inside the sun.",
        "The strongest muscle in the body is the tongue."
    ],
    "historical_facts": [
        "The Mona Lisa has no eyebrows.",
        "Competitive art used to be an Olympic sport.",
        "The Eiffel Tower can be 15 cm taller during the summer."
    ]
}

@app.route('/')
def index():
    return render_template('index.html', categories=fun_facts.keys())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically validate the username and password
        flash('Login successful!')  # Replace with actual login logic
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would typically save the new user to a database
        flash('Signup successful! Please log in.')  # Replace with actual signup logic
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/api/fact/<category>', methods=['GET'])
def get_fact(category):
    category = category.lower().replace(' ', '_')
    if category in fun_facts:
        fact = random.choice(fun_facts[category])
        return jsonify(fact=fact)
    else:
        return jsonify(error="Category not found"), 404

if __name__ == '__main__':
    app.run(debug=True)