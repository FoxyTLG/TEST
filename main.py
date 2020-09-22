import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token ='409c55694b48e91a85ab5ea0061564263c119d93cff12f4771253c10db0926e42210c1e50b0e94d2957ab')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    vk_session.method('messeges.send', {'user_id': id, 'messege' :text, 'random_id' :0})
    
for event in longpoll.listen(): 
    if event.type ==VkEventType.MESSAGE_NEW:
        if event.to_me:
            
            msg = event.text.lower()
            id = event.user_id
            
            if msg == '!р Понедельник':
                sender(id, 'привет')
