import random

from swagger_server.models import Quote


def calculate(quote: Quote) -> float:
    """
    TODO: Calculate against risk-factors determined in profile
    :param quote:
    :return:
    """
    return float(random.randint(1, 1000)) + float(0.99)
