#MODULE 10 OF 30 Days of python programming 
# Exercises: Level 1
class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return self.max() - self.min()

    def mean(self):
        return self.sum() / self.count()

    def median(self):
        sorted_data = sorted(self.data)
        n = self.count()
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def mode(self):
        from collections import Counter
        data_count = Counter(self.data)
        mode_data = data_count.most_common(1)[0]
        return {'mode': mode_data[0], 'count': mode_data[1]}

    def std(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / self.count()
        return variance ** 0.5

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / self.count()

    def freq_dist(self):
        from collections import Counter
        data_count = Counter(self.data)
        total_count = self.count()
        return [(count / total_count * 100, value) for value, count in data_count.items()]

# Example usage
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Variance: ', data.var()) # 17.5
print('Standard Deviation: ', data.std()) # 4.2
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# Exercises: Level 2
class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return f"Account holder: {self.firstname} {self.lastname}\nTotal Income: {self.total_income()}\nTotal Expense: {self.total_expense()}\nAccount Balance: {self.account_balance()}"
    
