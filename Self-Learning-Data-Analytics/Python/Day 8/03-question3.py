# ------------------------------------------------------------
# QUESTION:
# Write a Python program to check loan eligibility.
# Eligibility depends on age, income, and credit score.
# ------------------------------------------------------------

class LoanApplicant:
    def __init__(self, name, age, income, credit_score):
        self.name = name
        self.age = age
        self.income = income
        self.credit_score = credit_score


class LoanChecker:
    @staticmethod
    def is_eligible(applicant):
        return (
            applicant.age >= 21 and
            applicant.income >= 30000 and
            applicant.credit_score >= 650
        )


def main():
    applicant = LoanApplicant("Rahul", 25, 45000, 700)

    if LoanChecker.is_eligible(applicant):
        print("Loan Approved")
    else:
        print("Loan Rejected")


if __name__ == "__main__":
    main()


# OUTPUT DISPLAYED:
# Loan Approved
