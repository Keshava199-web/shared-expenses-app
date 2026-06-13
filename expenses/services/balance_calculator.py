from decimal import Decimal

from expenses.models import ExpenseParticipant


class BalanceCalculator:

    def calculate_group_balances(self, group):
        balances = {}

        participants = ExpenseParticipant.objects.filter(
            expense__group=group
        ).select_related(
            "expense",
            "user"
        )

        for participant in participants:
            expense = participant.expense
            user = participant.user

            paid_by = expense.paid_by

            if user.username not in balances:
                balances[user.username] = Decimal("0")

            if paid_by.username not in balances:
                balances[paid_by.username] = Decimal("0")

            share = participant.share_amount or Decimal("0")

            balances[user.username] -= share

            if paid_by != user:
                balances[paid_by.username] += share

        return balances
   
    def simplify_debts(self, balances):

        creditors = []
        debtors = []

        for person, amount in balances.items():

            if amount > 0:
                creditors.append(
                    [person, amount]
                )

            elif amount < 0:
                debtors.append(
                    [person, abs(amount)]
                )

        settlements = []

        i = 0
        j = 0

        while i < len(debtors) and j < len(creditors):

            debtor, debt = debtors[i]
            creditor, credit = creditors[j]

            amount = min(debt, credit)

            settlements.append({
                "from": debtor,
                "to": creditor,
                "amount": float(amount)
            })

            debtors[i][1] -= amount
            creditors[j][1] -= amount

            if debtors[i][1] == 0:
                i += 1

            if creditors[j][1] == 0:
                j += 1

        return settlements