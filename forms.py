from flask_wtf import FlaskForm
from wtforms.fields.html5 import IntegerRangeField

def getCriteria():
    return [
        {
            "label": "User and Customer Knowledge",
            "category": "productKnowledge",
            "value": null
        },
        {
            "label": "Data Knowledge",
            "category": "productKnowledge",
            "value": null
        },
        {
            "label": "Industry and Domain Knowledge",
            "category": "productKnowledge",
            "value": null
        },
        {
            "label": "Business and Company Knowledge",
            "category": "productKnowledge",
            "value": null
        },
        {
            "label": "Product Operational Knowledge",
            "category": "productKnowledge",
            "value": null
        },
        {
            "label": "Product Discovery Techniques",
            "category": "processSkillsandTechniques",
            "value": null
        },
        {
            "label": "Product Optimization Techniques",
            "category": "processSkillsandTechniques",
            "value": null
        },
        {
            "label": "Product Delivery Techniques",
            "category": "processSkillsandTechniques",
            "value": null
        },
        {
            "label": "Product Development Process",
            "category": "processSkillsandTechniques",
            "value": null
        },
        {
            "label": "Team Collaboration Skills",
            "category": "peopleSkillsandResponsibilities",
            "value": null
        },
        {
            "label": "Stakeholder Management Skills",
            "category": "peopleSkillsandResponsibilities",
            "value": null
        },
        {
            "label": "Evangelism Skills",
            "category": "peopleSkillsandResponsibilities",
            "value": null
        },
        {
            "label": "Leadership Skills",
            "category": "peopleSkillsandResponsibilities",
            "value": null
        },
    ]

class EvaluationForm(FlaskForm):
    criteria = getCriteria()

    for criterion in criteria:
        
