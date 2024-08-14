def emoji_convertor(message) : 
    words = message.split(" ")
    emoji = {
        ":)" : "😊",
        ":(" : "😒"
    }
    output = ""
    for word in words :
        output += emoji.get(word,word) + " "
    return output


message = input("> ")
result = emoji_convertor(message)
print(result)

