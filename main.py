from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def contact_form():
    if request.method == "POST":
        # Get form data
        email = request.form["email"]
        phone = request.form["phone"]
        address = request.form["address"]
        message = request.form["message"]
        # Render the 'information' template with the form data
        return render_template(
            "information.html",
            email=email,
            phone=phone,
            address=address,
            message=message,
        )
    # Render the 'contact_form' template for GET requests
    return render_template("contact_form.html")


@app.route("/information")
def information():
    # Render the 'information' template for displaying submitted data
    return render_template("information.html")


if __name__ == "__main__":
    app.run(debug=True)
