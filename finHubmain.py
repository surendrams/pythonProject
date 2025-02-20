from datetime import datetime, timedelta
import finnhub
from myclass import SQLTemplate, MongoTemplate


def get_upcoming_earnings(weekStart, weekEnd):
    finnhub_client = finnhub.Client(api_key="ctghdb9r01qn78n3v6o0ctghdb9r01qn78n3v6og")
    response = finnhub_client.earnings_calendar(_from=weekStart, to=weekEnd, symbol="", international=False)
    earnings_list = response["earningsCalendar"]
    return earnings_list

def printClassDetails(c1, c2):
    print(f'c1 - {c1.__class__.__name__} - {c1}')
    print(f'c2 - {c2.__class__.__name__} - {c2}')

if __name__ == "__main__":
    sql = SQLTemplate("scott", "tiger")
    mon = MongoTemplate("cnd", "verizon")

    printClassDetails(sql, mon)

    # today = datetime.today()
    # weekStart = (today - timedelta(days = today.weekday())).date()
    # weekEnd   = (weekStart + timedelta(days=20))
    # earnings = get_upcoming_earnings(weekStart, weekEnd)
    # sorted_earnings = sorted(earnings, key=lambda x: x['date'])
    # for item in sorted_earnings:
    #     if item['hour'] != '':
    #         print(f"{item['date']}|{item['symbol']:4}|{item['hour']}|{item['epsEstimate']}")

# Sample
# {
#     "date": "2020-01-28",
#     "epsActual": 4.99,
#     "epsEstimate": 4.5474,
#     "hour": "amc",
#     "quarter": 1,
#     "revenueActual": 91819000000,
#     "revenueEstimate": 88496400810,
#     "symbol": "AAPL",
#     "year": 2020
# }
