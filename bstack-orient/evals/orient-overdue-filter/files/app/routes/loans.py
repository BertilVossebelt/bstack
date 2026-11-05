import csv
import io
import logging

from flask import Blueprint, request, Response

from auth import require_branch_access
from db import query
from services.loan_query import build_loan_query

loans = Blueprint("loans", __name__)
log = logging.getLogger(__name__)


@loans.get("/branches/<int:branch_id>/loans/export")
def export_loans(branch_id):
    require_branch_access(branch_id)
    log.info("loan export for branch %s with %s", branch_id, dict(request.args))

    sql, params = build_loan_query(branch_id, request.args)
    rows = query(sql, params)

    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id", "member_id", "book_title", "lent_on", "due_on", "returned_on"])
    for row in rows:
        writer.writerow([row[0], row[1], row[3], row[4], row[5], row[6]])

    return Response(output.getvalue(), mimetype="text/csv")
