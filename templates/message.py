from db.crud import StationType

STATION_QUESTIONS = {
    StationType.START: 'Введи название СТАРТОВОЙ станции (города/жд станции/автобусной станции)',
    StationType.END: 'Введи название КОНЕЧНОЙ станции (города/жд станции/автобусной станции)',
    StationType.NODE: 'Введи название ПРОМЕЖУТОЧНОЙ станции (города/жд станции/автобусной станции)'
}

NOT_FOUND = 'Ничего не найдено. Попробуй снова'

DESTINATION_TIME_QUESTION = 'Требуется ли время для достижения этой станции?'

DESTINATION_TIME_ANSWERS = ['Да, указать время', 'Нет, не требуется']

DESTINATION_TIME_INPUT = 'Укажи время в минутах'