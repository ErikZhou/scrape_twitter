import sys
import os
import twint
import datetime
from datetime import timedelta

def get_tw(user):
    c = twint.Config()
    c.Username = user
    c.Limit = 10

    #c.Since = '2020-01-01'
    d = timedelta(days=2)
    today = datetime.date.today()
    #print(today)
    before_yesterday = today - d
    date = before_yesterday.strftime("%Y-%m-%d")
    print(date)
    c.Since = date 

    c.Store_object = True
    c.Output = "data/tweets_" + user + "_.csv"
    if os.path.exists(c.Output):
        os.remove(c.Output)

    twint.run.Search(c)
    tweets = twint.output.tweets_list


def main():
    for arg in sys.argv[1:]:
        print(arg)
    user = sys.argv[1]
    get_tw(user)


if __name__ == "__main__":
    #usage()
    main()

