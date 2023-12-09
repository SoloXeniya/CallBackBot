from aiogram import Bot, Dispatcher, executor
from aiogram.types import *
import random
from os import system
from core.config import TOKEN, ADMIN_ID, ADMIN_PUSH_ID
from core.inline import menu, other, admin_b, admin_push
from core.database import create_table, insert_users, find_user, pull_user, admin_get_users
from core.keyboard import regictration, profile
system("clear")


bot= Bot(token =TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message:Message):
    create_table()
    username = message.from_user.username
    first_name = message.from_user.first_name

    name = "Пользователь"
    if username != None:
        name = username
    elif first_name != None:
        name= first_name 

    await message.answer(f"Добро пожаловать {name}!", reply_markup=menu)

    if message.from_user.id in ADMIN_ID:
        await message.answer("Вы администратор", reply_markup=admin_b)

        await message.answer("Можете добавить или удалить администротора", reply_markup=admin_push)        

    if find_user(message.from_user.id) is not None:
        await message.answer("Вы зашли на ваш профиль", reply_markup=profile)

    else:
        await message.answer("Зарегистрируйтесь", reply_markup=regictration)

@dp.callback_query_handler()   
async def menu_1(call: CallbackQuery):
    if call.data == "menu_1":
        await call.message.edit_text("https://www.youtube.com/", reply_markup=menu)

    elif call.data == "menu_2":
        await call.message.edit_text("https://www.instagram.com/",reply_markup=menu)

    elif call.data == "menu_3":
        await call.message.edit_reply_markup(reply_markup=other)

    elif call.data == "menu_4":
        await call.message.edit_reply_markup(reply_markup=menu)

    elif call.data == "other_1":
        await call.message.edit_text("https://web.telegram.org/k/",reply_markup=menu)



    elif call.data == "other_2":
        c = 0
        l =[]
        lange = ""
        for i in range(1,10):
            lange += random.choice(l)
            c += 10
            await call.message.edit_text(f"Загружено{l} на {c}")
        await call.message.edit_text("https://web.whatsapp.com/", reply_markup=other)

    elif call.data == "del":
        await call.message.delete_reply_markup()
        
    elif call.data == "users":
        if call.message.chat.id in ADMIN_ID:
            text = admin_get_users()
            await call.message.edit_text(text, reply_markup=admin_b)
        else:
            await call.message.answer("У вас больше не доступа к этой функции", reply_markup=profile)
    


@dp.message_handler(content_types=ContentTypes.CONTACT)
async def contact(message:Message):
    user_id = message.from_user.id
    username= message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    phone = message.contact.phone_number 

    insert_users(user_id, username, first_name, last_name, phone)

    await message.answer(f"Вы зарегистрированы", reply_markup = profile)


# @dp.message_handler(content_types=ContentTypes.TEXT)
# async def contact(message:Message):
#     if find_user(message.from_user.id) is not None:
#         if message.text.lower() == "профиль":
#             user_id = message.from_user.id
            
#             t = pull_user(user_id)
#             await message.answer(f"Данные о пользователе {t}")
#         else:
#             await message.answer("Ваш профиль не найден")
#     else:
#         await message.answer("Ваш пользователь не найден")




saved_id = [] 
@dp.message_handler(commands=['add_p'])
async def add_p_handler(message:Message):
    user_id = message.from_user.id
    iuser_id = [user_id]
    if iuser_id == ADMIN_ID:
        text_id = message.text.split('/add_p', 1)[1] 
        saved_id = ADMIN_PUSH_ID
        saved_id.append(text_id)
        print(text_id)
        print(saved_id)
        await message.answer("Сохранение сообещния")
    else:
        await message.answer("ваши права ограничены") 




del_id = []
@dp.message_handler(commands=['del_p'])
async def add_p_handler(message:Message):
    user_id = message.from_user.id
    iuser_id = [user_id]
    if iuser_id == ADMIN_ID:
        global del_id
        text_id = message.text.split('/del_p', 1)[1] 
        del_id.append(text_id)
        print(text_id)
        print(del_id)
        await message.answer("Данный администратор удален")
    else:
        await message.answer("ваши права ограничены") 

# <class 'int'> 5122138718
# <class 'list'> [5122138718]

    # print(type(user_id),user_id)
    # print(type(ADMIN_ID), ADMIN_ID)










if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        pass





# # Обработчик для сохранения следующего сообщения пользователя
# @dp.message_handler(lambda message: message.chat.id in ADMIN_ID and saved_id)
# async def save_id_handler(message: Message):
#     global saved_id
#     saved_id.append(message.text)  # Сохранить текст сообщения
#     await message.answer("Сообщение сохранено. Используйте /save_id для завершения.")

# # Обработчик команды для завершения сохранения и передачи в ADMIN_PUSH_ID
# @dp.message_handler(commands=['save_id'])
# async def save_id_command_handler(message:Message):
#     global saved_id
#     global ADMIN_PUSH_ID






# @dp.callback_query_handler()   
# async def menu_1(call: CallbackQuery):
#     if call.data == "add_p":
#         await call.message.
#     elif call.data == "delete_p":
        #await call.message.edit_text("https://www.youtube.com/", reply_markup=menu)



# from aiogram.dispatcher import FSMContext


# save_id = [] 

# async def message_handler(message: Message, state: FSMContext):
#     if message.text == 'add_p':
#         await state.set_state("waiting_for_id")
#         await message.answer("Ваше следующее сообщение будет сохранено как ID нового администратора.")
#     else:
#          await message.answer("Произошла ошибка") 
    

# @dp.message_handler(commands=['text']) 
# async def start(message:Message): 
#     param = message.text.split(' ', 1)[1] 
#     print(param)
#     await message.answer('ваше сообщение сохранено')



# dp.message_handler(eaquals= 'add_p')
# save_id = []
# async def save_id(message:Message):
#     save_id.append(message.text)
#     ADMIN_PUSH_ID = save_id.copy()
#     await message.answer(f"id нового администратора успешно сохранен")


# dp.message_handler(eaquals= 'delete_p')
# save_id = []
# ADMIN_PUSH_ID = save_id.copy()
# async def save_id(message:Message):
#     save_id.append(message.text)
# #    ADMIN_PUSH_ID = save_id.copy()
#     await message.answer(f"id нового администратора успешно сохранен")


#     if message.from_user.id in ADMIN_ID:
#         await message.answer("Вы администратор, удалите или добавьте нового администратора", reply_markup=admin_push)

#     else:
#         await message.answer("У вас недостаточно прав")

# dp.message_handler(commands="add_p")
# async def start(message:Message):




    








# append/ кнопка добавления и удаления алминистратора.
