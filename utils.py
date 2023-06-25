from datetime import timedelta

def to_timedelta(h):
    ho, mi, se = h.split(':')
    se, mili = se.split(".")
    return timedelta(hours=int(ho), minutes=int(mi), seconds=int(se), milliseconds=int(mili))

def separetate_time_tuple(h):
    try:
        ho, mi, se = h.split(':')
        se, mili = se.split(".")
        se = int(round(float(se)))
        return (int(ho), int(mi), se)
    except:
        print("falha ao aredondar: ", h)
        ho, mi, se = h.split(':')
        se = int(round(float(se)))
        return (int(ho), int(mi), se)