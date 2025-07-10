# Define a list of rules, where each rule is a dictionary.
# Each rule maps a set of symptoms ('if') to a diagnosis ('then').
rules = [
    {"if": {"fever", "cough"}, "then": "flu"},
    {"if": {"fever", "rash"}, "then": "measles"},
    {"if": {"headache", "nausea"}, "then": "migraine"},
    {"if": {"sneezing", "runny nose"}, "then": "cold"},
    {"if": {"fever", "cough", "difficulty breathing"}, "then": "COVID-19"},
    {"if": {"sore throat", "fever"}, "then": "strep throat"},
    {"if": {"fatigue", "muscle pain"}, "then": "influenza"},
    {"if": {"itchy eyes", "sneezing"}, "then": "allergy"},
]

# Inference Engine: Checks which rules match the user's symptoms.
def diagnose(symptoms):
    matched_diseases = []     # List to store possible diagnoses
    explanations = []         # List to store matched rule explanations

    # Loop through all predefined rules
    for rule in rules:
        # Check if all symptoms in the rule are present in user input
        if rule["if"].issubset(symptoms):
            # Add corresponding disease to the matched list
            matched_diseases.append(rule["then"])
            # Save explanation for this match
            explanations.append(f"Rule matched: IF {', '.join(rule['if'])} THEN {rule['then']}")

    # Return the list of matched diseases and explanations
    return matched_diseases, explanations

# Function to collect user symptoms interactively
def get_user_symptoms():
    print("Enter your symptoms one by one. Type 'done' when finished:")
    symptoms = set()  # Use a set to avoid duplicate symptoms

    while True:
        symptom = input("Symptom: ").strip().lower()  # Clean and standardize input
        if symptom == "done":
            break  # Stop input collection
        if symptom:  # Only add non-empty input
            symptoms.add(symptom)

    return symptoms  # Return the set of entered symptoms

# Main function: Coordinates the interaction and diagnosis process
def main():
    print("\n Welcome to the Medical Expert System \n")
    user_symptoms = get_user_symptoms()  # Collect symptoms from user
    
    if not user_symptoms:
        print("\n️ No symptoms entered. Exiting.")  # Exit if no input
        return

    diagnoses, explanations = diagnose(user_symptoms)  # Perform diagnosis

    print("\n Diagnosis Result:")
    if diagnoses:
        # Display each matched disease
        for i, disease in enumerate(diagnoses):
            print(f" - {disease}")
        print("\n🧾 Explanation:")
        # Display each matched rule that led to a diagnosis
        for explanation in explanations:
            print(f" * {explanation}")
    else:
        # Inform user if no matching rules were found
        print("No diagnosis could be made based on the given symptoms.")

# Entry point: Starts the program when run as a script
if __name__ == "__main__":
    main()
