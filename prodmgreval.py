from flask import Flask, render_template, url_for

# from forms import EvaluationForm
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ["flaskKey"]


def getEval():
    return [
        {
            "name": "productKnowledge",
            "label": "Product Knowledge",
            "criteria": [
                {
                    "label": "User and Customer Knowledge",
                    "category": "productKnowledge",
                    "value": None,
                },
                {
                    "label": "Data Knowledge",
                    "category": "productKnowledge",
                    "value": None,
                },
                {
                    "label": "Industry and Domain Knowledge",
                    "category": "productKnowledge",
                    "value": None,
                },
                {
                    "label": "Business and Company Knowledge",
                    "category": "productKnowledge",
                    "value": None,
                },
                {
                    "label": "Product Operational Knowledge",
                    "category": "productKnowledge",
                    "value": None,
                },
            ],
        },
        {
            "name": "processSkillsandTechniques",
            "label": "Process Skills and Techniques",
            "criteria": [
                {
                    "label": "Product Discovery Techniques",
                    "category": "processSkillsandTechniques",
                    "value": None,
                },
                {
                    "label": "Product Optimization Techniques",
                    "category": "processSkillsandTechniques",
                    "value": None,
                },
                {
                    "label": "Product Delivery Techniques",
                    "category": "processSkillsandTechniques",
                    "value": None,
                },
                {
                    "label": "Product Development Process",
                    "category": "processSkillsandTechniques",
                    "value": None,
                },
            ],
        },
        {
            "name": "peopleSkillsandResponsibilities",
            "label": "People Skills and Responsibilities",
            "criteria": [
                {
                    "label": "Team Collaboration Skills",
                    "category": "peopleSkillsandResponsibilities",
                    "value": None,
                },
                {
                    "label": "Stakeholder Management Skills",
                    "category": "peopleSkillsandResponsibilities",
                    "value": None,
                },
                {
                    "label": "Evangelism Skills",
                    "category": "peopleSkillsandResponsibilities",
                    "value": None,
                },
                {
                    "label": "Leadership Skills",
                    "category": "peopleSkillsandResponsibilities",
                    "value": None,
                },
            ],
        },
    ]


@app.route("/")
def index():
    eval = getEval()
    return render_template("eval.html", eval=eval)


if __name__ == "__main__":
    app.run(debug=True)
