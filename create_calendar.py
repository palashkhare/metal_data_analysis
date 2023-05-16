from datetime import datetime, timedelta
import pandas as pd
from date_to_epoch import *


start_date = "01-01-1980"
end_date = "01-01-2035"

start_date = datetime.strptime(start_date, "%d-%m-%Y")
end_date = datetime.strptime(end_date, "%d-%m-%Y")

date_range = [(start_date+timedelta(days=date), (start_date+timedelta(days=date)).strftime("%s")) for date in range((end_date-start_date).days)]
d = list(zip(*date_range))
df = pd.DataFrame({"date": d[0], "epoch": d[1]})
df["day"] = df["date"].apply(lambda x: x.day)
df["month"] = df["date"].apply(lambda x: x.month)
df["year"] = df["date"].apply(lambda x: x.year)
df["day_name"] = df["date"].apply(lambda x: x.day_name())
df["day_of_week"] = df["date"].apply(lambda x: x.day_of_week)
df["day_of_year"] = df["date"].apply(lambda x: x.day_of_year)
df["dayofweek"] = df["date"].apply(lambda x: x.dayofweek)
df["dayofyear"] = df["date"].apply(lambda x: x.dayofyear)
df["days_in_month"] = df["date"].apply(lambda x: x.days_in_month)
df["daysinmonth"] = df["date"].apply(lambda x: x.daysinmonth)
df["is_leap_year"] = df["date"].apply(lambda x: x.is_leap_year)
df["is_month_end"] = df["date"].apply(lambda x: x.is_month_end)
df["is_month_start"] = df["date"].apply(lambda x: x.is_month_start)
df["is_quarter_end"] = df["date"].apply(lambda x: x.is_quarter_end)
df["is_quarter_start"] = df["date"].apply(lambda x: x.is_quarter_start)
df["is_year_end"] = df["date"].apply(lambda x: x.is_year_end)
df["is_year_start"] = df["date"].apply(lambda x: x.is_year_start)
df["month_name"] = df["date"].apply(lambda x: x.month_name())
df["quarter"] = df["date"].apply(lambda x: x.quarter)
df["week"] = df["date"].apply(lambda x: x.week)
df["weekday"] = df["date"].apply(lambda x: x.weekday())
df["weekofyear"] = df["date"].apply(lambda x: x.weekofyear)

holiday_calendar_df = pd.read_csv("data/calendar.csv")
holiday_calendar_df["full_dt"] = holiday_calendar_df["Date"] + "-" + holiday_calendar_df["Year"].astype("str")
holiday_calendar_df["epoch"] = holiday_calendar_df["full_dt"].apply(str_to_epoch)
holiday_calendar_df = holiday_calendar_df[["epoch", "Name", "Type"]]
calendar = df.merge(holiday_calendar_df, how="left", left_on="epoch", right_on="epoch")

calendar.to_parquet("output/calendar.parquet", partition_cols=["year", "month"])
calendar.to_excel("output/calendar.xlsx")