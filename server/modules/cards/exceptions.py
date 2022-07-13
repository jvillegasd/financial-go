class CardNotFound(Exception):
    """ Raise when a card is not found """
    pass


class InvalidCardOwner(Exception):
    """
      Raise when a provided user uuid does not
      match with card owner uuid.
    """
    pass
