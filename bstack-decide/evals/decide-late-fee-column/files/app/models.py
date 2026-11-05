from dataclasses import dataclass
from datetime import date


@dataclass
class Member:
    id: int
    branch_id: int
    name: str


@dataclass
class Loan:
    id: int
    member_id: int
    branch_id: int
    book_title: str
    lent_on: date
    due_on: date
    returned_on: date | None
