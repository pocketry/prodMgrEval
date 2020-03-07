from flask_wtf import FlaskForm
from wtforms.fields.html5 import IntegerRangeField


def getEval():
    return [
        {
            "category": "productKnowledge",
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
            "category": "processSkillsandTechniques",
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
            "category": "peopleSkillsandResponsibilities",
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


class EvaluationForm(FlaskForm):
    criteria = getCriteria()

    product = {}
    process = {}
    people = {}
    for criterion in criteria:
        if criterion["category"] == "product":
            product[criterion["label"]] = IntegerRangeField(
                criterion["label"].replace(" ", "")
            )
        if criterion["category"] == "process":
            process[criterion["label"]] = IntegerRangeField(
                criterion["label"].replace(" ", "")
            )
        if criterion["category"] == "people":
            people[criterion["label"]] = IntegerRangeField(
                criterion["label"].replace(" ", "")
            )

    print(product)
    # for criterion in criteria:
    #     criterion["label"] = IntegerRangeField(criterion["label"].replace(" ", ""))

    # discovery = IntegerRangeField("Discovery")

