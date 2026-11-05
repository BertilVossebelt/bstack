from flask import g, abort


def require_branch_access(branch_id):
    """Stops the request when the signed-in librarian does not work at this branch."""
    if branch_id not in g.librarian.branch_ids:
        abort(403)
