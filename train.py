from chatterbot import ChatBot
from botapi import views
from chatterbot.trainers import ChatterBotCorpusTrainer
# chatbot = ChatBot('Chatterbot',trainer='chatterbot.trainers.CorpusTrainer' )
trainer = ChatterBotCorpusTrainer(views.ChatterBotApiView.chatterbot)
trainer.train( './ecell.yml' )