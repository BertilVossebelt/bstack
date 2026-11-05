from db import query
from models import Loan
from services.fees import FeeCalculator


def member_balance_cents(member_id):
    rows = query("SELECT id, member_id, branch_id, book_title, lent_on, due_on, returned_on FROM loans WHERE member_id = ?", (member_id,))
    loans = [Loan(*row) for row in rows]
    return FeeCalculator().total_owed_cents(loans)
