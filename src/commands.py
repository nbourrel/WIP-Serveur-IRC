from src.user import User
from src.channel import Channel

def handle_nick(client, args):
    if len(args) > 0:
        nickname = args[0]
        if not client.user:
            client.user = User(nickname)
        else:
            client.user.nickname = nickname
        client.send_message(f":{client.user.nickname}!{client.user.nickname}@localhost NICK {nickname}\n")
    else:
        client.send_message(":No nickname provided\n")

def handle_join(client, args):
    if len(args) > 0:
        channel_name = args[0]
        if channel_name not in client.server.channels:
            client.server.channels[channel_name] = Channel(channel_name)
        channel = client.server.channels[channel_name]
        channel.add_user(client.user)
        client.user.channels.append(channel_name)
        join_message = f":{client.user.nickname}!{client.user.nickname}@localhost JOIN {channel_name}\n"
        client.send_message(join_message)
        send_names(client, channel)
        broadcast_message(client.server, channel_name, join_message, client.user.nickname)
    else:
        client.send_message(":No channel name provided\n")

def send_names(client, channel):
    names_list = ' '.join(channel.list_users())
    names_message = f":localhost 353 {client.user.nickname} = {channel.name} :{names_list}\n"
    end_of_names = f":localhost 366 {client.user.nickname} {channel.name} :End of /NAMES list.\n"
    client.send_message(names_message)
    client.send_message(end_of_names)

def handle_unknown(client, command):
    client.send_message(f":Unknown command: {command}\n")

def broadcast_message(server, channel_name, message, sender_nickname):
    channel = server.channels.get(channel_name)
    if channel:
        for nickname, user in channel.users.items():
            if nickname != sender_nickname:
                client = next((c for c in server.clients if c.user == user), None)
                if client:
                    client.send_message(message)

# Dictionary to map commands to their handler functions
COMMAND_HANDLERS = {
    'NICK': handle_nick,
    'JOIN': handle_join,
    # Add more commands here
    # 'PART': handle_part,
    # 'PRIVMSG': handle_privmsg,
}

def handle_command(client, message):
    parts = message.split()
    command = parts[0].upper()
    args = parts[1:]
    
    handler = COMMAND_HANDLERS.get(command, handle_unknown)
    handler(client, args)