# from datetime import datetime, tzinfo, timedelta
# # class TZ(tzinfo):
# #     def utcoffset(self, __dt: datetime | None) -> timedelta | None:
# #         return timedelta(hours=6, minutes=30)
# td = datetime.now()
# # print(td)
# # print(datetime.now().isoformat(sep='T', timespec='YYYY-MM-DD'))
# d = datetime.strftime(td, "%Y-%m-%d")
# # print(d)
#
# # print("YYYY-MM-DD".format(td.now().year, td.now().month, td.now().day))
#
# m = int(d[5:7])
# if m%3 == 0:
#     print('you can get interest')
# # print(int(d[5:7]))
#
# password = 'helloworld'
#
# def salt_hashing(password):
#     salt = str(uuid.uuid4()).encode()
#     plaintext = password.encode()
#     ha = hashlib.pbkdf2_hmac('sha512', plaintext, salt, 100)
#     hashed_password = ha.hex()
#     return hashed_password
#
#
# # a = datetime(2022, 5, 30)
# # b = datetime(2023, 9, 22)
# # c = (b.year - a.year) * 12 + (b.month - a.month)
# # print('The months are- ', c)
#
# ls = ['hello', 'world', '1', '2', '3']
# print(', '.join(ls))
#


from bank import Bank
from conf import get_rtc


class Base:
    def __init__(self):
        self.hello = "Hello World"
        self.__fuck = "Fuck You"
        self._did_you_see = "Yes"


class Devi(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling private member for Base class: ")
        print(self._Base__fuck)


Devi()
