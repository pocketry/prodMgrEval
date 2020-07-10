from prodmgreval import db


class Evaluation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, default="Product Manager")
    criteria = db.relationship("Criterion", backref="evaluation", lazy=True)

    def getEval(self):
        return [
            {
                "name": "productKnowledge",
                "label": "Product Knowledge",
                "criteria": [
                    {
                        "label": "User and Customer Knowledge",
                        "name": "userAndCustomerKnowledge",
                        "category": "productKnowledge",
                        "value": "7",
                    },
                    {
                        "label": "Data Knowledge",
                        "name": "dataKnowledge",
                        "category": "productKnowledge",
                        "value": "7",
                    },
                    {
                        "label": "Industry and Domain Knowledge",
                        "name": "industeryAndDomainKnowledge",
                        "category": "productKnowledge",
                        "value": "7",
                    },
                    {
                        "label": "Business and Company Knowledge",
                        "name": "businessAndCompanyKnowledge",
                        "category": "productKnowledge",
                        "value": "7",
                    },
                    {
                        "label": "Product Operational Knowledge",
                        "name": "productOperationalKnowledge",
                        "category": "productKnowledge",
                        "value": "7",
                    },
                ],
            },
            {
                "name": "processSkillsandTechniques",
                "label": "Process Skills and Techniques",
                "criteria": [
                    {
                        "label": "Product Discovery Techniques",
                        "name": "productDiscoveryTechniques",
                        "category": "processSkillsandTechniques",
                        "value": "7",
                    },
                    {
                        "label": "Product Optimization Techniques",
                        "name": "productOptimizationTechniques",
                        "category": "processSkillsandTechniques",
                        "value": "7",
                    },
                    {
                        "label": "Product Delivery Techniques",
                        "name": "productDeliveryTechniques",
                        "category": "processSkillsandTechniques",
                        "value": "7",
                    },
                    {
                        "label": "Product Development Process",
                        "name": "productDevelopmentProcess",
                        "category": "processSkillsandTechniques",
                        "value": "7",
                    },
                ],
            },
            {
                "name": "peopleSkillsandResponsibilities",
                "label": "People Skills and Responsibilities",
                "criteria": [
                    {
                        "label": "Team Collaboration Skills",
                        "name": "teamCollaborationSkills",
                        "category": "peopleSkillsandResponsibilities",
                        "value": "7",
                    },
                    {
                        "label": "Stakeholder Management Skills",
                        "name": "stakeholderManagementSkills",
                        "category": "peopleSkillsandResponsibilities",
                        "value": "7",
                    },
                    {
                        "label": "Evangelism Skills",
                        "name": "evangilismSkills",
                        "category": "peopleSkillsandResponsibilities",
                        "value": "7",
                    },
                    {
                        "label": "Leadership Skills",
                        "name": "leadershipSkills",
                        "category": "peopleSkillsandResponsibilities",
                        "value": "7",
                    },
                ],
            },
        ]

    def toJSON(self):
        criteriaList = []
        for criterion in self.criteria:
            evalJSON.append()


class Criterion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    evaluationid = db.Column(db.Integer, db.ForeignKey("evaluation.id"), nullable=False)
    categoryname = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float)

    # def toDict(self):
    #     return {
    #         "label": self.name,
    #         "": self.name.replace(" ",""),
    #         "value"
    #     }
