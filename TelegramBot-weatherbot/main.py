from pyowm import OWM
from aiogram import Bot, Dispatcher, executor, types

# Инициализация бота и диспетчера
bot = Bot(token="5802287517:AAHhjctK2pN74XRRvIQs1gYI0hgeAI-60RI")
dp = Dispatcher(bot)

# Инициализация сервиса для получения погоды
owm = OWM("d620b424e319156697049cc599466d1c")

# Обработка сообщений с текстом
@dp.message_handler(text=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот, который сообщит тебе текущую погоду в заданном городе. Просто напиши название города.")

# Обработка сообщений с городами
@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        # Поиск города
        observation = owm.weather_manager().weather_at_place(message.text)
        w = observation.weather

        # Составление ответа
        weather_status = w.detailed_status
        temperature = round(w.temperature('celsius')['temp'])
        humidity = w.humidity

        response = f"Текущая погода в городе {message.text}: {weather_status}, температура - {temperature}°C, влажность - {humidity}%."

    except Exception as e:
        print(e)
        response = "Не удалось получить погоду для города {message.text}. Попробуйте еще раз."

    await message.reply(response)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)




