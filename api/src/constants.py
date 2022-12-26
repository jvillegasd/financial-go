# Query params filtering parser
QUERY_PARAMS_BRACKET_OPERATORS: tuple = (
    '[lt]',
    '[le]',
    '[gt]',
    '[ge]',
    '[eq]'
)


# Cards
MAX_NUMBER_OF_CARDS: int = 4


# Transactions
TRANSACTION_TYPES: tuple[str] = ('Unique', 'Recurrent')
TRANSACTION_CATEGORIES: tuple[str] = (
    'Transport',
    'Shopping',
    'Others',
    'Outcome',
    'Income',
    'Money',
    'Savings',
    'Rent',
    'Property',
    'Loan',
    'Invoice',
    'Gift',
    'Gadget',
    'Entertainment',
    'Credit card',
    'Company',
    'Child care',
    'Charithy',
    'Automobile',
    'Traveling',
    'Medical',
    'Fitness',
    'Eating',
    'Bank'
)


# Repository filtering
# http://docs.mongoengine.org/guide/querying.html
ALLOWED_QUERY_OPERATORS: tuple[str] = (
    'eq',
    'ne',
    'lt',
    'lte',
    'gt',
    'gte',
    'in',
    'nin',
    'mod',
    'all',
    'size',
    'exists',
    'contains'
)
