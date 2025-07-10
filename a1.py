# Simple Rule-Based Expert System for Medical Diagnosis

# Define the knowledge base: rules as functions that check symptoms and return diagnosis
def rule_flu(facts):
    # Rule: If fever and cough and body ache -> Flu
    if facts.get('fever') and facts.get('cough') and facts.get('body_ache'):
        return "You may have the flu."
    return None

def rule_cold(facts):
    # Rule: If cough and sneezing and no fever -> Common Cold
    if facts.get('cough') and facts.get('sneezing') and not facts.get('fever'):
        return "You may have a common cold."
    return None

def rule_allergy(facts):
    # Rule: If sneezing and itchy_eyes and no fever -> Allergy
    if facts.get('sneezing') and facts.get('itchy_eyes') and not facts.get('fever'):
        return "You may have an allergy."
    return None

def rule_malaria(facts):
    # Rule: If fever and chills and sweating -> Malaria
    if facts.get('fever') and facts.get('chills') and facts.get('sweating'):
        return "You may have malaria."
    return None

# List of all rules in the expert system
rules = [rule_flu, rule_cold, rule_allergy, rule_malaria]

def get_user_input():
    """
    Ask the user about symptoms and return facts as a dictionary.
    """
    facts = {}
    print("Please answer the following questions with yes or no:")
    facts['fever'] = input("Do you have a fever? ").lower() == 'yes'
    facts['cough'] = input("Do you have a cough? ").lower() == 'yes'
    facts['body_ache'] = input("Do you have body aches? ").lower() == 'yes'
    facts['sneezing'] = input("Are you sneezing? ").lower() == 'yes'
    facts['itchy_eyes'] = input("Do you have itchy eyes? ").lower() == 'yes'
    facts['chills'] = input("Do you have chills? ").lower() == 'yes'
    facts['sweating'] = input("Are you sweating a lot? ").lower() == 'yes'
    return facts

def infer(facts):
    """
    Apply each rule on the facts.
    Return the first matching diagnosis or a default message.
    """
    for rule in rules:
        result = rule(facts)
        if result is not None:
            return result
    return "Sorry, no diagnosis could be made based on the symptoms."

def main():
    print("Welcome to the simple Medical Diagnosis Expert System!")
    facts = get_user_input()
    diagnosis = infer(facts)
    print("\nDiagnosis:")
    print(diagnosis)

if __name__ == "__main__":
    main()
