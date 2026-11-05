from datetime import date

DAILY_LATE_FEE_CENTS = 25
MAX_LATE_FEE_CENTS = 1000


class FeeCalculator:
    """Works out what a member owes for a loan: the late fee, capped per loan."""

    def late_fee_cents(self, loan, today=None):
        today = today or date.today()
        end = loan.returned_on or today
        days_late = (end - loan.due_on).days
        if days_late <= 0:
            return 0
        return min(days_late * DAILY_LATE_FEE_CENTS, MAX_LATE_FEE_CENTS)

    def total_owed_cents(self, loans, today=None):
        return sum(self.late_fee_cents(loan, today) for loan in loans)
