from datetime import datetime

time_format = '%d.%m.%Y %H:%M'


def is_input_valid(input_time: str) -> bool:
    try:
        datetime.strptime(input_time, time_format)
        return True
    except:
        return False


def get_datetime_from_str(input_time: str) -> datetime:
    return datetime.strptime(input_time, time_format)


def get_str_from_datetime(time: datetime) -> str:
    return time.strftime(time_format)


def get_now_datetime() -> datetime:
    return datetime.now()