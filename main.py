import os
import ptbot
from dotenv import load_dotenv
from pytimeparse import parse


def reply(chat_id, time):
    secs_left = parse(time)
    start_timer = "Запускаю таймер"
    message_id = bot.send_message(chat_id, start_timer)
    bot.update_message(chat_id, message_id, secs_left)
    bot.create_countdown(parse(time), notify, message_id=message_id, time=time)
    bot.create_timer(parse(time), answer_to_message, chat_id=chat_id)


def notify(secs_left, message_id, time):
    time = parse(time)
    progressbar = f'Осталось {secs_left} секунд из {time}\n' \
                  f'{render_progressbar(time, secs_left)}'
    bot.update_message(tg_chat_id, message_id, progressbar)


def render_progressbar(total, iteration, prefix='', suffix='', length=13, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def answer_to_message (chat_id):
    answer = "Время вышло!"
    bot.send_message(chat_id, answer)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    tg_chat_id = os.getenv("TG_CHAT_ID")
    bot = ptbot.Bot(tg_token)

    bot.reply_on_message(reply)
    bot.run_bot()
