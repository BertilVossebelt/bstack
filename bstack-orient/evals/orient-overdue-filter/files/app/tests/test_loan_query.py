from services.loan_query import build_loan_query


def test_lent_after_adds_a_date_condition():
    sql, params = build_loan_query(1, {"lentAfter": "2026-01-01"})
    assert "lent_on > ?" in sql
    assert params[1].isoformat() == "2026-01-01"


def test_empty_filter_is_ignored():
    sql, params = build_loan_query(1, {"lentAfter": ""})
    assert "lent_on" not in sql.split("ORDER BY")[0]
