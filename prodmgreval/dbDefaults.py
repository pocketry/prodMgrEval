from prodmgreval import Evaluation, Criterion, db

# db.session.add(Evaluation(name = "Product Manager"))

criteria = []

criteria.append(
    Criterion(
        name="User and Customer Knowledge",
        evaluationid=1,
        categoryname="Product Knowledge",
    )
)
criteria.append(
    Criterion(name="Data Knowledge", evaluationid=1, categoryname="Product Knowledge")
)
criteria.append(
    Criterion(
        name="Industry and Domain Knowledge",
        evaluationid=1,
        categoryname="Product Knowledge",
    )
)
criteria.append(
    Criterion(
        name="Business and Company Knowledge",
        evaluationid=1,
        categoryname="Product Knowledge",
    )
)
criteria.append(
    Criterion(
        name="Product Operational", evaluationid=1, categoryname="Product Knowledge"
    )
)
criteria.append(
    Criterion(
        name="Product Discovery Techniques",
        evaluationid=1,
        categoryname="Process Skills and Techniques",
    )
)
criteria.append(
    Criterion(
        name="Product Optimization Techniques",
        evaluationid=1,
        categoryname="Process Skills and Techniques",
    )
)
criteria.append(
    Criterion(
        name="Product Delivery Techniques",
        evaluationid=1,
        categoryname="Process Skills and Techniques",
    )
)
criteria.append(
    Criterion(
        name="Product Development Process",
        evaluationid=1,
        categoryname="Process Skills and Techniques",
    )
)
criteria.append(
    Criterion(
        name="Team Collaboration Skills",
        evaluationid=1,
        categoryname="People Skills and Responsibilities",
    )
)
criteria.append(
    Criterion(
        name="Stakeholder Management Skills",
        evaluationid=1,
        categoryname="People Skills and Responsibilities",
    )
)
criteria.append(
    Criterion(
        name="Evangelism Skills",
        evaluationid=1,
        categoryname="People Skills and Responsibilities",
    )
)
criteria.append(
    Criterion(
        name="Leadership Skills",
        evaluationid=1,
        categoryname="People Skills and Responsibilities",
    )
)

for c in criteria:
    db.session.add(c)

db.session.commit()
