import berserk
session = berserk.TokenSession(token)
client = berserk.Client(session=session)
client.account.get()