import re

from .enumerations import DISTANCE_STOP_WORDS, NUMBERS_AS_WORDS, UNITS_MATRIX


def parse(magnitude_text, source, dest=None):

    if magnitude_text is None:
        raise Exception("magnitude_text missing")

    if not isinstance(magnitude_text, basestring):
        raise Exception("magnitude_text is not a string")

    if source is not None and not isinstance(source, basestring):
        raise Exception("source units is not a string")

    if dest is not None and not isinstance(dest, basestring):
        raise Exception("destination units is not a string")

    # trim string if needed
    magnitude_text = magnitude_text.strip()

    value = None
    if magnitude_text in DISTANCE_STOP_WORDS:
        raise Exception("georel hit stop word "+magnitude_text+".")
    elif magnitude_text in NUMBERS_AS_WORDS:
        value = NUMBERS_AS_WORDS.index(magnitude_text)
    elif re.match("^\d+$", magnitude_text) is not None:
        value = int(magnitude_text)
    elif re.match("^\d+[.]\d+$", magnitude_text) is not None:
        value = float(magnitude_text)
    else:
        m = re.match("^(?P<thousand>\d{1,3})[,](?P<one>\d{3})$", magnitude_text)
        if m is not None:
            value = (
                (1000 * int(m.group("thousand"))) +
                int(m.group("one"))
            )
        else:
            m = re.match("^(?P<million>\d{1,3})[,](?P<thousand>\d{1,3})[,](?P<one>\d{3})$", magnitude_text)
            if m is not None:
                value = (
                    (1000000 * int(m.group("million"))) +
                    (1000 * int(m.group("thousand"))) +
                    int(m.group("one"))
                )
            else:
                m = re.match("^(?P<thousand>\d{1,3})[,]?(?P<one>\d{3})[.](?P<decimals>\d+)$", magnitude_text)
                if m is not None:
                    value = (
                        (1000 * int(m.group("thousand"))) +
                        int(m.group("one")) +
                        float("0."+m.group("decimals"))
                    )
                else:
                    m = re.match("^(?P<million>\d{1,3})[,](?P<thousand>\d{1,3})[,]?(?P<one>\d{3})[.](?P<decimals>\d+)$", magnitude_text)
                    if m is not None:
                        value = (
                            (1000000 * int(m.group("million"))) +
                            (1000 * int(m.group("thousand"))) +
                            int(m.group("one")) +
                            float("0."+m.group("decimals"))
                        )

    if source is not None and len(source) > 0:
        source = source.strip()
        source_lc = source.lower()
        source_units = None
        if dest is not None and len(dest) > 0:
            destination_lc = dest.lower()
            for name, unit in UNITS_MATRIX.iteritems():
                if source_lc in unit["words"]:
                    source_units = name
                    break
            if source_units is None:
                raise Exception("could not recognize source units")
            destination_units = None
            for name, unit in UNITS_MATRIX.iteritems():
                if destination_lc in unit["words"]:
                    destination_units = name
                    break
            if destination_units is None:
                raise Exception("could not recognize destination units")
            return {"value": value * UNITS_MATRIX[source_units]["multiplier"][destination_units], "units": destination_units}
        else:
            for name, unit in UNITS_MATRIX.iteritems():
                if source_lc in unit["words"]:
                    source_units = name
                    break
            if source_units is None:
                raise Exception("could not recognize source units")
            return {"value": value, "units": source_units}
    else:
        if dest is not None and len(dest) > 0:
            raise("cannot transform to destination units without knowing source units")

    return {"value": value, "units": None}
