class BookNotFoundError(Exception):
    pass


class MemberNotFoundError(Exception):
    pass


class BookUnavailableError(Exception):
    pass


class LoanNotFoundError(Exception):
    pass


class LoanAlreadyClosedError(Exception):
    pass