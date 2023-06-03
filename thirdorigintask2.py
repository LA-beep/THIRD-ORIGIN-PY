import datetime

class DateUtility:
    def convert_dt(self, from_date, from_date_TZ, to_date_TZ):
        """
        Converts a datetime object from one timezone to another.

        :param from_date: The datetime object to convert.
        :type from_date: datetime.datetime
        :param from_date_TZ: The timezone of the from_date.
        :type from_date_TZ: str
        :param to_date_TZ: The timezone to convert to.
        :type to_date_TZ: str
        :return: The converted datetime object.
        :rtype: datetime.datetime
        """
        from_date = from_date.replace(tzinfo=datetime.timezone(datetime.timedelta(hours=0), from_date_TZ))
        to_date = from_date.astimezone(datetime.timezone(datetime.timedelta(hours=0), to_date_TZ))
        return to_date

    def add_dt(self, from_date, number_of_days):
        """
        Adds the specified number of days to a given date.

        :param from_date: The base date.
        :type from_date: datetime.datetime
        :param number_of_days: The number of days to add.
        :type number_of_days: int
        :return: The resulting date after adding the specified number of days.
        :rtype: datetime.datetime
        """
        to_date = from_date + datetime.timedelta(days=number_of_days)
        return to_date

    def sub_dt(self, from_date, number_of_days):
        """
        Subtracts the specified number of days from a given date.

        :param from_date: The base date.
        :type from_date: datetime.datetime
        :param number_of_days: The number of days to subtract.
        :type number_of_days: int
        :return: The resulting date after subtracting the specified number of days.
        :rtype: datetime.datetime
        """
        to_date = from_date - datetime.timedelta(days=number_of_days)
        return to_date

    def get_days(self, from_date, to_date):
        """
        Returns the number of days between two dates.

        :param from_date: The starting date.
        :type from_date: datetime.datetime
        :param to_date: The ending date.
        :type to_date: datetime.datetime
        :return: The number of days between the two dates.
        :rtype: int
        """
        delta = to_date - from_date
        return delta.days

    def get_days_exclude_we(self, from_date, to_date):
        """
        Returns the number of days between two dates excluding weekends (Saturday and Sunday).

        :param from_date: The starting date.
        :type from_date: datetime.datetime
        :param to_date: The ending date.
        :type to_date: datetime.datetime
        :return: The number of days between the two dates excluding weekends.
        :rtype: int
        """
        delta = to_date - from_date
        count = 0
        for i in range(delta.days + 1):
            day = from_date + datetime.timedelta(days=i)
            if day.weekday() < 5:  # Monday to Friday (0 to 4)
                count += 1
        return count

    def get_days_since_epoch(self, from_date):
        """
        Returns the number of days since the epoch (January 1, 1970) to a given date.

        :param from_date: The date.
        :type from_date: datetime.datetime
        :return: The number of days since the epoch.
        :rtype: int
        """
        epoch = datetime.datetime(1970, 1, 1)
        delta = from_date - epoch
        return delta.days

    def get_business_days(self, from_date, to_date):
        """
        Returns the number of business days (excluding weekends and holidays) between two dates.

        :param from_date: The starting date.
        :type from_date: datetime.datetime
        :param to_date: The ending date.
        :type to_date: datetime.datetime
        :return: The number of business days between the two dates.
        :rtype: int
        """
        delta = to_date - from_date
        count = 0
        holidays = self.load_holidays()
        for i in range(delta.days + 1):
            day = from_date + datetime.timedelta(days=i)
            if day.weekday() < 5 and day not in holidays:  # Monday to Friday (0 to 4) and not a holiday
                count += 1
        return count

    def load_holidays(self):
        """
        Loads holidays from the 'holidays.dat' file and returns a list of datetime objects.
        The 'holidays.dat' file should be in the format: TIMEZONE,DATE,HOLIDAY

        :return: A list of datetime objects representing holidays.
        :rtype: list
        """
        holidays = []
        with open('holidays.dat', 'r') as file:
            for line in file:
                timezone, date_str, _ = line.strip().split(',')
                date = datetime.datetime.strptime(date_str, '%Y%m%d').date()
                holidays.append(date)
        return holidays
