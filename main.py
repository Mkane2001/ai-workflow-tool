from flask import Flask, render_template, request, redirect, url_for
from workflows import run_workflow

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    selected_workflow = ""
    user_input = ""

    if request.method == "POST":
        selected_workflow = request.form.get("workflow", "").strip()
        user_input = request.form.get("user_input", "").strip()

        if user_input and selected_workflow:
            result = run_workflow(selected_workflow, user_input)
        else:
            result = "Please choose a workflow and enter some text."

    return render_template(
        "index.html",
        result=result,
        selected_workflow=selected_workflow,
        user_input=user_input
    )


@app.route("/clear", methods=["POST"])
def clear():
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)