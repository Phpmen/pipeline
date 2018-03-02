import telebot
import const
import math
from telebot import types
bot = telebot.TeleBot(const.API_TOKEN)
markup = types.ReplyKeyboardMarkup(row_width=1)
itembtn1 = types.KeyboardButton('Решить квадратное уравнение')
markup.add(itembtn1)



def square(message):
	a=[]
	a=message.text.split()
	#bot.send_message(message.chat.id,a,reply_markup=markup)
	D = int(a[1])**2-4*int(a[0])*int(a[2])
	msd = print('1.D = {}^2-4*{}*{}={}'.format(a[0],a[1],a[2],D))
	file = open('D.txt','w')
	file.write('1.D = '+str(a[0])+'^2-4*'+str(a[1])+'*'+str(a[2])+'='+str(D)+'\n')
	file.close()
	if D>=0:
		D = math.sqrt(D)
		print('Корень из дискриминанта = ',D)
		x1 = (-int(a[1])-D)/2
		x2 = (-int(a[1])+D)/2
		print('X1=(-{}-{})/2={}'.format(a[1],D,x1))
		print('X2=(-{}+{})/2={}'.format(a[1],D,x2))
		file = open('D.txt','a')
		file.write('2.Корень из дискриминанта = '+str(D)+'\n')
		file.write('3.X1=(-'+str(a[1])+'-'+str(D)+')/2='+str(x1)+'\n')
		file.write('  X2=(-'+str(a[1])+''+str(D)+')/2='+str(x2)+'\n')
		file.close()
		file = open('D.txt','r')
		msg = file.read()
		bot.send_message(message.chat.id,msg,reply_markup=markup)
	else:
		print('Дискриминант меньше 0')
		bot.send_message(message.chat.id,'Дискриминант меньше 0',reply_markup=markup)




@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет!",reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def start(message):
	if message.text == 'Решить квадратное уравнение':
		sent = bot.send_message(message.chat.id, 'Напиши через пробел значения a,b,c!',reply_markup=markup)
		bot.register_next_step_handler(sent, square)
bot.polling()