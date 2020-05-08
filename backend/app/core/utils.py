def attribute_mapper(l, atr='id'):
    """ Retrieves attribute value for each element in list or tuple """
    return [getattr(atr_l, atr) for atr_l in l]
