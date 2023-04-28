from bale import Bot, CallbackQuery, Message, Components, InlineKeyboard, EventType, Photo
import requests
import json

bot = Bot(token="1250946986:N7gQYReP6qrlqqflT2mygS6WL3lVS8UuJ6kVotBv")

TextWelcome = "سلام خوش آمدی به ربات بله پدیا \n " \
              "اینجا میتونی مقاله های ویکی پدیا را به صورت شانسی دریافت کنی\n "


@bot.listen(EventType.MESSAGE)
async def when_receive_message(message: Message):
    if message.content == "/start":
        riding = "خوب شما با کلیک بر رویه دکمه زیر میتونی مقاله بخونی"
        await message.reply(
            TextWelcome,
            components=Components(inline_keyboards=[[
                InlineKeyboard("شروع", callback_data="STAR")
            ]])
        )


@bot.listen(EventType.CALLBACK)
async def rond_two(callback: CallbackQuery):
    if callback.data == "STAR":
        await callback.message.reply(
            "یکی از موضوعات زیر را انتخاب کنید",
            components=Components(inline_keyboards=[[
                InlineKeyboard("general", callback_data="general"),
                InlineKeyboard("sports_and_outdoors", callback_data="sports"),
                InlineKeyboard("education", callback_data="education"),
                InlineKeyboard("collection", callback_data="collection"),
                InlineKeyboard("competition", callback_data="competition"),
                InlineKeyboard("observation", callback_data="observation"),
            ]])
        )


@bot.listen(EventType.CALLBACK)
async def select(call: CallbackQuery):
    if call.data == "general":
        category = 'general'
        api_url = 'https://api.api-ninjas.com/v1/hobbies?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': '/HNShFyE8nwxLWhB5M8oSw==wPoSUezPUpf4wscF'})
        if response.status_code == requests.codes.ok:
            # print(response.text)
            response_dict = json.loads(response.text)
            url = response_dict["link"]
            await call.message.reply(
                "خوب شما با کلیک بر رویه دکمه زیر میتونی مقاله بخونی",
                components=Components(inline_keyboards=[[
                    InlineKeyboard("خواندن مقاله", url=url)

                ]])
            )
        else:
            print("Error:", response.status_code, response.text)
    #         /////////////////////////////
    elif call.data == "sports_and_outdoors":
        category = 'sports'
        api_url = 'https://api.api-ninjas.com/v1/hobbies?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': '/HNShFyE8nwxLWhB5M8oSw==wPoSUezPUpf4wscF'})
        if response.status_code == requests.codes.ok:
            # print(response.text)
            response_dict = json.loads(response.text)
            url = response_dict["link"]
            await call.message.reply(
                "خوب شما با کلیک بر رویه دکمه زیر میتونی مقاله بخونی",
                components=Components(inline_keyboards=[[
                    InlineKeyboard("خواندن مقاله", url=url)

                ]])
            )
        else:
            print("Error:", response.status_code, response.text)
    #         /////////////////////////////
    elif call.data == "education":
        category = 'education'
        api_url = 'https://api.api-ninjas.com/v1/hobbies?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': '/HNShFyE8nwxLWhB5M8oSw==wPoSUezPUpf4wscF'})
        if response.status_code == requests.codes.ok:
            # print(response.text)
            response_dict = json.loads(response.text)
            url = response_dict["link"]
            await call.message.reply(
                "خوب شما با کلیک بر رویه دکمه زیر میتونی مقاله بخونی",
                components=Components(inline_keyboards=[[
                    InlineKeyboard("خواندن مقاله", url=url)

                ]])
            )
        else:
            print("Error:", response.status_code, response.text)

    #         /////////////////////////////
    elif call.data == "collection":
        category = 'collection'
        api_url = 'https://api.api-ninjas.com/v1/hobbies?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': '/HNShFyE8nwxLWhB5M8oSw==wPoSUezPUpf4wscF'})
        if response.status_code == requests.codes.ok:
            # print(response.text)
            response_dict = json.loads(response.text)
            url = response_dict["link"]
            await call.message.reply(
                "خوب شما با کلیک بر رویه دکمه زیر میتونی مقاله بخونی",
                components=Components(inline_keyboards=[[
                    InlineKeyboard("خواندن مقاله", url=url)

                ]])
            )
        else:
            print("Error:", response.status_code, response.text)

    #         /////////////////////////////
    elif call.data == "competition":
        category = 'competition'
        api_url = 'https://api.api-ninjas.com/v1/hobbies?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': '/HNShFyE8nwxLWhB5M8oSw==wPoSUezPUpf4wscF'})
        if response.status_code == requests.codes.ok:
            # print(response.text)
            response_dict = json.loads(response.text)
            url = response_dict["link"]
            await call.message.reply(
                "خوب شما با کلیک بر رویه دکمه زیر میتونی مقاله بخونی",
                components=Components(inline_keyboards=[[
                    InlineKeyboard("خواندن مقاله", url=url)

                ]])
            )
        else:
            print("Error:", response.status_code, response.text)

        #         /////////////////////////////
    elif call.data == "observation":
        category = 'observation'
        api_url = 'https://api.api-ninjas.com/v1/hobbies?category={}'.format(category)
        response = requests.get(api_url, headers={'X-Api-Key': '/HNShFyE8nwxLWhB5M8oSw==wPoSUezPUpf4wscF'})
        if response.status_code == requests.codes.ok:
            # print(response.text)
            response_dict = json.loads(response.text)
            url = response_dict["link"]
            await call.message.reply(
                "خوب شما با کلیک بر رویه دکمه زیر میتونی مقاله بخونی",
                components=Components(inline_keyboards=[[
                    InlineKeyboard("خواندن مقاله", url=url)

                ]])
            )
        else:
            print("Error:", response.status_code, response.text)


bot.run()
