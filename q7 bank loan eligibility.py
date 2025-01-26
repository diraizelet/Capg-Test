
#check_loan_eligibility will check all the required conditions and ir rejected will show the reason as well
def check_loan_eligibility(salary, age, credit_score):
    if age < 18:
        return "Loan Rejected: Applicant must be at least 18 years old."
    if salary < 25000:
        return "Loan Rejected: Minimum salary requirement is $25,000."
    if credit_score < 650:
        return "Loan Rejected: Credit score must be at least 650."

    return "Loan Approved"

#main will take the input and call the validator fucntion 
#here the validator is the check_loan_eligibility
def main():
    try:
        salary = float(input("Enter your salary: "))
        age = int(input("Enter your age: "))
        credit_score = int(input("Enter your credit score: "))
        
        result = check_loan_eligibility(salary, age, credit_score)
        print(result)
    except ValueError:
        print("Invalid input. Please enter numeric values for salary, age, and credit score.")

if __name__ == "__main__":
    main()