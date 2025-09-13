from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("home.html")


@main.route("/category/<int:cat_id>")
def category_view(cat_id):
    category = category.query.get_or_404(cat_id)
    return render_template("category.html", category=category)