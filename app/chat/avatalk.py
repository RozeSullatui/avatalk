import openai
import json

openai.api_key = "OPENAPI_KEY"

def conversation(post_messages,history_message):
    result = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=post_messages
    )
    result_json = '{"result":{"current_emotion": "'+ result.choices[0].message.content + "}"
    print(result_json)
    result_json = json.loads(result_json)
    emotion_message = result_json['result']['current_emotion']
    response_message = result_json['result']['grandma_reply']

    return  emotion_message,response_message


def chatinit():
    try:
        with open("character/grandma.txt", mode = "r", encoding = "utf_8") as f:
            character_setting = f.read()
        with open("history_grandma.txt", mode = "r", encoding = "utf_8") as f:
            history_message = f.read()
        if len(history_message) != 0:
            system_prompt = {"role":"system", "content":character_setting}
        else:
            history_settings = "#History \n Also, please take into account the history of past conversations and output your responses as follows.\n" + history_message
            system_prompt = {"role":"system", "content":character_setting + history_settings}
        user_text = input("You:")
        user_prompt = {"role": "user", "content": user_text}
        emotion_prompt = {"role": "assistant", "content": '{"current_emotion": "'}

        

        full_prompt = []
        full_prompt.append(user_prompt)
        full_prompt.append(system_prompt)
        full_prompt.append(emotion_prompt)
        emotion,replaymessage= conversation(full_prompt,history_message)

        print("Emotion:", emotion)
        print("AI:", replaymessage)


        with open("history_grandma.txt", mode = "a", encoding = "utf_8") as f:
            f.write("User:" + user_text + "\n" + "grandma_replay:" +replaymessage + "\n")
        
        return emotion,replaymessage
    except:
        print("Error!もう一度！")