function getCriteria() {
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
    ];
}

function getCriteriaElement(label) {
    criteriaDiv = document.createElement('div');
    criteriaDiv.setAttribute("class", "criteria");

    criteriaHeader = document.createElement('h4');
    criteriaHeader.textContent = label;

    criteriaInput = document.createElement('input');
    criteriaInput.setAttribute("type", "range");
    criteriaInput.setAttribute("class", "slider");
    criteriaInput.setAttribute("id", label.replace(/ /g, ""));
    criteriaInput.setAttribute("name", label.replace(/ /g, ""));
    criteriaInput.setAttribute("onclick", "updateEval");
    criteriaInput.setAttribute("min", "0");
    criteriaInput.setAttribute("max", "10");
    criteriaInput.setAttribute("step", ".5");
    criteriaInput["value"] = "0";

    criteriaDiv.appendChild(criteriaHeader);
    criteriaDiv.appendChild(criteriaInput);

    return criteriaDiv;
}

// function updateEval(

// )

productSection = document.querySelector("#productKnowledge");
processSection = document.querySelector("#processSkillsandTechniques");
peopleSection = document.querySelector("#peopleSkillsandResponsibilities");

criteria = getCriteria();

for (c in criteria) {
    // console.log(criteria[c].category);
    if (criteria[c].category == 'productKnowledge') {
        productSection.appendChild(getCriteriaElement(criteria[c].label));
    }
    if (criteria[c].category == 'processSkillsandTechniques') {
        processSection.appendChild(getCriteriaElement(criteria[c].label));
    }
    if (criteria[c].category == 'peopleSkillsandResponsibilities') {
        peopleSection.appendChild(getCriteriaElement(criteria[c].label));
    }
}

inputs = document.querySelectorAll("input");
// console.log(inputs.length);
evaluation = [];

inputs.forEach(i => evaluation.push({ [i["id"]]: i["value"] }));

// console.log(evaluation);

