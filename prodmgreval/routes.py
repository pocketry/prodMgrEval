from flask import render_template, url_for, request, redirect
from flask_wtf import FlaskForm
from prodmgreval import app, db
from prodmgreval.models import Evaluation, Criterion


@app.route("/eval", methods=["GET", "POST"])
def eval():
    if request.method == "POST":
        # print(request)
        # print(request.data)
        print(request.form)
        newEval = Evaluation()
        db.session.add(newEval)
        db.session.commit()
        # print(newEval.id)
        for c in request.form:
            if c == "csrf_token":
                continue
            print(c)
            cat = c.split("-")[0]
            crit = c.split("-")[1]

            db.session.add(
                Criterion(
                    name=crit,
                    evaluationid=newEval.id,
                    categoryname=cat,
                    value=request.form[c],
                )
            )
        db.session.commit()
        return redirect(url_for("evalList"))
    eval = Evaluation()
    form = FlaskForm()
    return render_template("eval.html", eval=eval.getEval(), form=form)


@app.route("/eval/<int:evalID>")
def showEval(evalID):
    selectedEval = Evaluation.query.id(evalID)
    print(selectedEval.id + selectedEval.name)


@app.route("/list", methods=["GET", "POST"])
def evalList():
    if request.method == "POST":
        return redirect(url_for("eval"))
    evals = Evaluation.query.all()
    return render_template("list.html", list=evals)
