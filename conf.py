from datetime import datetime
from dateutil import relativedelta

def get_rtc():
    today = datetime.now()
    return datetime.strftime(today, "%Y-%m-%d")

def deta_time_by_months(ref_time="2022-08-12"):
    start_time = datetime.strptime(ref_time, "%Y-%m-%d")
    current_time = datetime.strptime(get_rtc(), "%Y-%m-%d")
    deta = relativedelta.relativedelta(current_time, start_time)
    return int(deta.months + (deta.years * 12))

def case_change1(name: str):  # It changes camelCase to snake_case
    result = [name[0].lower()]
    for c in name[1:]:
        if c.isupper():
            result.append('_')
            result.append(c.lower())
        else:
            result.append(c)
    return ''.join(result)


def case_change2(name: str):  # It will change snake_case to camelCase
    result = name.split('_')[0]
    result += ''.join(s.title() for s in name.split('_')[1:])
    return result

case_change2('hello_world')