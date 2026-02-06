# filepath: c:\Users\Judah\Desktop\CS-School\PythonFunda\library.py
TodayDate = "2026-01-24"
TodayLabel = "Jan 24, 2026"


def ParseDate(DateString):
    YearString, MonthString, DayString = DateString.split("-")
    return int(YearString), int(MonthString), int(DayString)


def ToOrdinal(Year, Month, Day):
    DaysInMonth = [31, 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    Days = Year * 365
    for MonthIndex in range(1, Month):
        Days += DaysInMonth[MonthIndex - 1]
    Days += Day
    return Days


def days_overdue(due_date, today):
    YearDue, MonthDue, DayDue = ParseDate(due_date)
    YearToday, MonthToday, DayToday = ParseDate(today)
    DueOrdinal = ToOrdinal(YearDue, MonthDue, DayDue)
    TodayOrdinal = ToOrdinal(YearToday, MonthToday, DayToday)
    return TodayOrdinal - DueOrdinal


def format_status(book):
    Title = book["title"]
    Status = book["status"]
    if Status == "available":
        return f"\"{Title}\" (available)"
    if Status == "checked_out":
        Due = book.get("due_date")
        if not Due:
            return f"\"{Title}\" (checked out)"
        OverdueDays = days_overdue(Due, TodayDate)
        if OverdueDays > 0:
            return f"\"{Title}\" (checked out, due {Due}: {OverdueDays} days overdue)"
        else:
            return f"\"{Title}\" (checked out, due {Due})"
    return f"\"{Title}\" ({Status})"


def print_inventory(inventory):
    print(f"Library Inventory ({TodayLabel}):")
    for Book in inventory:
        Line = format_status(Book)
        print(Line)