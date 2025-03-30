def calculate_total_budget(school_project):
    total_budget = 0

    # Assume each item in the list represents an expense category
    expense_categories = ["cost of supplies", "equipment rent", "teacher salaries", "classroom materials"]
    for category in expense_categories:
        if school_project.get(category, None) is not None:
            current_total = school_project[category]
            total_budget += current_total

    return total_budget
