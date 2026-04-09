class DomainException(Exception):
    """Базовое доменное исключение"""
    pass


class InvariantViolation(DomainException):
    """Нарушение бизнес-инварианта"""
    pass