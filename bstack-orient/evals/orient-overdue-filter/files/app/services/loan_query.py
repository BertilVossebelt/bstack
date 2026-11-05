from datetime import date

KNOWN_FILTERS = ["lentAfter", "memberId"]


def build_loan_query(branch_id, filters):
    sql = "SELECT id, member_id, branch_id, book_title, lent_on, due_on, returned_on FROM loans WHERE branch_id = ?"
    params = [branch_id]

    lent_after = filters.get("lentAfter")
    if lent_after:
        sql += " AND lent_on > ?"
        params.append(date.fromisoformat(lent_after))

    member_id = filters.get("memberId")
    if member_id:
        sql += " AND member_id = ?"
        params.append(int(member_id))

    sql += " ORDER BY lent_on DESC LIMIT 5000"
    return sql, params
