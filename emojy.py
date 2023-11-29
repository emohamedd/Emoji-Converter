# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    emojy.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: emohamed <emohamed@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/29 10:32:04 by emohamed          #+#    #+#              #
#    Updated: 2023/11/29 10:32:12 by emohamed         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def emojis_converter(message, custom_emojis=None):
    emoji_dict = {
        ";)": "😉",
        ":)": "😊",
        ":D": "😃",
        "<3": "❤️",
        ":(": "😞",
        ":O": "😲",
        ":P": "😛",
        ">:(": "😡",
        "XD": "😆",
        ":-(": "😔",
        ":-)": "🙂",
        ":-D": "😄",
        ":-P": "😜",
        ":-O": "😮",
        ";-)": "😜",
        "=)": "🙄",
    }
    if custom_emojis:
        emoji_dict.update(custom_emojis)

    words = message.split()
    converted_message = []
    emoji_count = 0

    for word in words:
        emoji = emoji_dict.get(word.lower())
        if emoji:
            converted_message.append(emoji)
            emoji_count += 1
        else:
            converted_message.append(word)

    result = " ".join(converted_message)
    if "<3" in message or "love" in message.lower():
        result = "\033[91m" + result + "\033[0m" 

    return result, emoji_count

custom_emojis = {
    "positive": "😊",
    "negative": "😞",
    "animals": "🐶🐱🐰🐼🦁🐘🐬",
    "dog": "🐶",
    "cat": "🐱",
    "horse": "🐴",
    "shapes": "⚪⚫🔴🔵",
    "circle": "⚪",
    "square": "⬛",
    "rectangle": "⬜",
    "triangle": "🔺",
    "foods": "🍔🍕🍣🍦🥗🍎🍓",
    "weather": "☀️🌦️❄️⚡",
    "transportation": "🚗🚲🚀🚢🚁🚂",
    "symbols": "✨💡🔗🔮",
    "random": "🤪👻🧸🎉🎈🎁",
    "ass": "🍑",
}

user_input = input("> ")
converted_text, emoji_count = emojis_converter(user_input, custom_emojis)
print("Converted Message:", converted_text)
print("Emoji Count:", emoji_count)
