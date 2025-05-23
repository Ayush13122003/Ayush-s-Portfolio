# 🔹 Import the Flask class and important functions from the flask package
from flask import Flask, render_template, request, redirect, url_for, flash

# 🔹 Create a Flask application instance
app = Flask(__name__)

# 🔹 Set a secret key (required for flashing messages to users)
app.secret_key = 'secret123'

# 🔹 Define the route for the Home Page
@app.route("/")
def home():
    # Render the home.html template from the templates folder
    return render_template("home.html")

# 🔹 Route for the About Page
@app.route("/about")
def about():
    # Render the about.html page
    return render_template("about.html")

# 🔹 Route for the Projects Page
@app.route("/projects")
def projects():
    # Render the projects.html page
    return render_template("projects.html")

# 🔹 Route for the Contact Page (GET: show form, POST: process form)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Read data from the form using request.form
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Flash a thank-you message to user (displayed after form submission)
        flash(f"Thank you, {name}. Your message has been received!")

        # Redirect user back to the contact page after submission
        return redirect(url_for("contact"))

    # For GET request (normal page load), just show the form
    return render_template("contact.html")

# 🔹 Main section to run the app
if __name__ == "__main__":
    # Start the development server in debug mode
    app.run(debug=True)
