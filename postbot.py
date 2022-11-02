#!/usr/bin/env python
_Z='User %s started the post.'
_Y='User %s canceled the conversation.'
_X='below is the post number for your post\n\nuse below  command to send post to ur group \n\ntime is in seconds'
_W='skiping link as u entered incorrect link'
_V='Please enter link name for second button\n\n or press /done'
_U='send the photo 📸\n\n/skip the Photo'
_T='but bot👇\u200c\u200c'
_S='Send Link'
_R='linkname'
_Q='✅Done'
_P='working'
_O='setting'
_N='type the text and send! ✍️\n\n/skip the Text'
_M='t.me/r5pro'
_L='Click Here To Buy'
_K='text'
_J='postid'
_I='video_id'
_H='photo_id'
_G='Setting'
_F='🤖 Buy bot'
_E='📝 edit post'
_D='📌 make new post'
_C='link'
_B=False
_A=True
import logging,toml
from pathlib import Path
from random import randint
from html import escape
import json
from telegram.constants import ParseMode
from asyncio import sleep
from telegram import InlineKeyboardMarkup,ReplyKeyboardRemove,PassportElementErrorTranslationFile,__version__ as TG_VER
try:from telegram import __version_info__
except ImportError:__version_info__=0,0,0,0,0
if __version_info__<(20,0,0,'alpha',1):raise RuntimeError(f"install python-telegram-bot --pre")
import base64
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove,Update,InlineKeyboardButton,InlineQueryResultArticle,InputTextMessageContent,Bot
from telegram.ext import Application,CommandHandler,ContextTypes,ConversationHandler,MessageHandler,filters,InlineQueryHandler
def random_id(n):A=10**(n-1);B=10**n-1;return randint(A,B)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)
current_path=Path.cwd()
EDIT,PHOTO,MESS,NAME,LINK=range(5)
RTPT,SETPOST,SETTIME=range(3)
waitpost=1
post_count=200000
with open('config.toml','r')as config:
	confd=toml.load(config)
	try:BOT_TOKEN=confd['bot_token'];owner=str(confd['owner'])
	except BaseException:print('fill the config.toml');exit()
DATALIST={}
bytename='dGhpcyBpcyB0aGUgZnJlZSB2ZXJzaW9uIG9mICBib3QgbWFkZSBieSBAcjVwcm8='
bytename=base64.b64decode(bytename)
nonono=str(bytename.decode())
async def start(update,context):
	'Starts the post bot.';A=update
	if str(A.effective_user.id)==str(owner):B=[[_D,_E],[_F,_G]];await A.message.reply_text('✨! this is free version of bot contact @r5pro',reply_markup=ReplyKeyboardMarkup(B,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder='welcome'))
	else:B=[[InlineKeyboardButton(_L,_M)]];C=InlineKeyboardMarkup(B);await A.message.reply_text('To Buy BOT Contact : @r5pro\u200c\u200c',reply_markup=C)
async def buy(update,context):'Starts the post bot.';A=[[InlineKeyboardButton(_L,_M)]];B=InlineKeyboardMarkup(A);await update.message.reply_text('contact @r5pro\u200c\u200c',reply_markup=B)
async def newpost(update,context):
	A=update
	if str(A.effective_user.id)==str(owner):context.user_data[_C]=[];await A.message.reply_text(_U);return PHOTO
	else:await A.message.reply_text(f"enter coreect user id in config.toml\n your ID is  : {str(A.effective_user.id)}")
async def editpost(update,context):
	A=update
	if str(A.effective_user.id)==str(owner):await A.message.reply_text('send the post number.\n you want to edit');return EDIT
async def photo(update,context):'Stores the photo and asks for a location.';A=update;context.user_data[_H]=A.message.photo[-1].file_id;await A.message.reply_text(_N);return MESS
async def video(update,context):
	'Stores the photo and asks for a location.';A=update;B=f"video file size should be less then 20mb";C=23000000
	if A.message.video.file_size>C:await A.message.reply_text(B)
	else:context.user_data[_I]=A.message.video.file_id;await A.message.reply_text(_N);return MESS
async def edit_video(update,context):
	'Stores the photo and asks for a location.';A=update;B=f"video file size should be less then 20mb";C=23000000
	if A.message.video.file_size>C:await A.message.reply_text(B)
	else:DATALIST[context.user_data[_J]][_I]=A.message.video.file_id;await A.message.reply_text(_N);return MESS
async def edit_photo(update,context):
	'Stores the photo and asks for a location.';A=update
	if A.message.text:await A.message.reply_text('send photo')
	else:DATALIST[context.user_data[_J]][_H]=A.message.photo[-1].file_id;await A.message.reply_text(_N);return MESS
async def save_post(update,context):
	'Stores the photo and asks for a location.';A=update;B=A.message.text
	if B in DATALIST:context.user_data[_J]=B;await A.message.reply_text(_U);return PHOTO
	else:await A.message.reply_text('This post ID not avilable.\n Enter correct ID or press /cancel to cancel')
async def skip_photo(update,context):'Skips the photo and asks for a message.';await update.message.reply_text(_N);return MESS
async def save_mess(update,context):
	'Stores the location and asks for some info about the user.';A=update
	try:B=A.message.text;context.user_data[_K]=B;await A.message.reply_text(B);await A.message.reply_text('Pease enter the name of link button : \n\n/done')
	except BaseException:await A.message.reply_text('it should be text send again ');return MESS
	return NAME
async def edit_mess(update,context):
	'Stores the location and asks for some info about the user.';A=update
	try:B=A.message.text;C=context.user_data[_J];DATALIST[C][_K]=B;await A.message.reply_text(A.message.text);D=[[_D,_E],[_F,_Q]];await A.message.reply_text('Pease enter the name of link button :  \n\n/done',reply_markup=ReplyKeyboardMarkup(D,resize_keyboard=_A,one_time_keyboard=_A))
	except BaseException:await A.message.reply_text('it should be text send again');return MESS
	return NAME
async def skip_mess(update,context):'Skips the location and asks for info about the user.';await update.message.reply_text('Pease enter the name of link button : /done');return NAME
async def link_name(update,context):'Stores the links';A=update;B=A.message.text;context.user_data[_R]=B;await A.message.reply_text('Please enter the link \n\nlink should be valid');return LINK
async def link(update,context):
	'Stores the links';C=update;A=context;D=C.message.text;E=A.user_data[_R]
	try:G=A.user_data[_C];B=InlineKeyboardButton(E,D);G.append(B)
	except BaseException:F=[];B=InlineKeyboardButton(E,D);F.append(B);A.user_data[_C]=F
	H=[[_D,_E],[_F,_Q]];await C.message.reply_text(_V,reply_markup=ReplyKeyboardMarkup(H,resize_keyboard=_A,one_time_keyboard=_A));return NAME
async def edit_link(update,context):
	'Stores the links';C=update;A=context;I=A.user_data[_J];D=C.message.text;E=A.user_data[_R]
	try:G=A.user_data[_C];B=InlineKeyboardButton(E,D);G.append(B)
	except BaseException:F=[];B=InlineKeyboardButton(E,D);F.append(B);A.user_data[_C]=F
	H=[[_D,_E],[_F,_Q]];await C.message.reply_text(_V,reply_markup=ReplyKeyboardMarkup(H,resize_keyboard=_A,one_time_keyboard=_A));return NAME
async def skip_link(update,context):
	'Skips the link.';D=context;A=update;B=str(random_id(2));H=[];K=D.user_data[_C]
	try:
		for L in K:I=[];I.append(L);H.append(I)
		J=InlineKeyboardMarkup(H);J;D.user_data[_C]=J
	except BaseException:await A.message.reply_text(_W)
	DATALIST[B]=D.user_data.copy();D.user_data.clear()
	try:E=DATALIST[B][_I]
	except BaseException:
		try:F=DATALIST[B][_H]
		except BaseException:pass
	try:C=DATALIST[B][_K]
	except BaseException:pass
	try:G=DATALIST[B][_C]
	except BaseException:pass
	try:await A.message.reply_video(video=E,caption=C,reply_markup=G)
	except BaseException:
		try:await A.message.reply_video(video=E,caption=C)
		except BaseException:
			try:await A.message.reply_video(video=E)
			except BaseException:
				try:await A.message.reply_photo(photo=F,caption=C,reply_markup=G)
				except BaseException:
					try:await A.message.reply_photo(photo=F,caption=C)
					except BaseException:
						try:await A.message.reply_photo(photo=F)
						except BaseException:
							try:await A.message.reply_text(C,reply_markup=G)
							except BaseException:await A.message.reply_text(C)
	M=[[_D,_E],[_F,_G]];await A.message.reply_markdown_v2(_X,reply_markup=ReplyKeyboardMarkup(M,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_S));await A.message.reply_text(f"/send {B} (time in seconds)\n/time {B} (time in minutes) send single post");return ConversationHandler.END
async def hidekey(update,context):await update.message.reply_text('Keyboard Removed',reply_markup=ReplyKeyboardRemove())
async def edit_skip_link(update,context):
	'Skips the link.';A=update;B=context.user_data[_J];G=[]
	try:
		for H in ontext.user_data[_C]:I=[];I.append(H);G.append(I)
		J=InlineKeyboardMarkup(G);DATALIST[B][_C]=J
	except BaseException:await A.message.reply_text(_W)
	H=DATALIST[B]
	try:D=DATALIST[B][_I]
	except BaseException:
		try:E=DATALIST[B][_H]
		except BaseException:pass
	try:C=DATALIST[B][_K]
	except BaseException:pass
	try:F=DATALIST[B][_C]
	except BaseException:pass
	try:await A.message.reply_video(video=D,caption=C,reply_markup=F)
	except BaseException:
		try:await A.message.reply_video(video=D,caption=C)
		except BaseException:
			try:await A.message.reply_video(video=D)
			except BaseException:
				try:await A.message.reply_photo(photo=E,caption=C,reply_markup=F)
				except BaseException:
					try:await A.message.reply_photo(photo=E,caption=C)
					except BaseException:
						try:await A.message.reply_photo(photo=E)
						except BaseException:
							try:await A.message.reply_text(C,reply_markup=F)
							except BaseException:await A.message.reply_text(C)
	K=[[_D,_E],[_F,_G]];await A.message.reply_markdown_v2(_X,reply_markup=ReplyKeyboardMarkup(K,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_S));await A.message.reply_text(f"/send {B} (time in seconds)\n/time {B} (time in minutes) send single post");return ConversationHandler.END
async def cancel(update,context):'Cancels and ends the conversation.';A=update;B=A.message.from_user;C=[[_D,_E],[_F,_G]];logger.info(_Y,B.first_name);await A.message.reply_text('Bye!.',reply_markup=ReplyKeyboardMarkup(C,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_S));return ConversationHandler.END
async def leftinmiddle(update,context):'Cancels and ends the conversation.';A=update;B=A.message.from_user;logger.info(_Y,B.first_name);await A.message.reply_text('U HAVE LEFT in middle of post press /cancel')
async def send(update,context):
	'start the send';K='True';E=context;A=update;N=A.message.from_user;L=None;O=int(A.message.chat_id);logger.info(_Z,N.first_name);await A.message.reply_text(nonono)
	if str(A.effective_user.id)==str(owner):
		B=E.args[0];P=float(E.args[1])
		try:F=DATALIST[B][_I]
		except BaseException:
			try:G=DATALIST[B][_H]
			except BaseException:pass
		try:D=DATALIST[B][_K]
		except BaseException:pass
		try:H=DATALIST[B][_C]
		except BaseException:pass
		DATALIST[B][_P]=K;M=post_count;await A.message.reply_text(f"stop by /stop {B}")
		while DATALIST[B][_P]==K and M>0:
			if str(A.effective_user.id)==str(owner):
				try:C=await A.message.reply_video(video=F,caption=D,reply_markup=H,quote=_B)
				except BaseException:
					try:C=await A.message.reply_video(video=F,caption=D,quote=_B)
					except BaseException:
						try:C=await A.message.reply_video(video=F,quote=_B)
						except BaseException:
							try:C=await A.message.reply_photo(photo=G,caption=D,reply_markup=H,quote=_B)
							except BaseException:
								try:C=await A.message.reply_photo(photo=G,caption=D,quote=_B)
								except BaseException:
									try:C=await A.message.reply_photo(photo=G,quote=_B)
									except BaseException:
										try:C=await A.message.reply_text(D,reply_markup=H,quote=_B)
										except BaseException:C=await A.message.reply_text(D,quote=_B)
				M-=1;await sleep(P*waitpost);L=C.message_id
				try:await E.bot.delete_message(O,L)
				except:pass
			else:break
		if DATALIST[B][_P]==K:await A.message.reply_text(f"{post_count} : message has been send");I=[[InlineKeyboardButton(_L,_M)]];J=InlineKeyboardMarkup(I);await A.message.reply_text(_T,reply_markup=J)
	else:I=[[InlineKeyboardButton(_L,_M)]];J=InlineKeyboardMarkup(I);await A.message.reply_text(_T,reply_markup=J)
async def sendonce(update,context):
	'start the send';H=context;A=update;I=A.message.from_user;logger.info(_Z,I.first_name);await A.message.reply_text(nonono)
	if str(A.effective_user.id)==str(owner):
		C=H.args[0];D=str(H.args[1])
		try:D=int(D)*60
		except BaseException:await A.message.reply_text('enter time un minutes 60 90 120')
		try:E=DATALIST[C][_I]
		except BaseException:
			try:F=DATALIST[C][_H]
			except BaseException:pass
		try:B=DATALIST[C][_K]
		except BaseException:pass
		try:G=DATALIST[C][_C]
		except BaseException:pass
		await A.message.reply_text(f"post will be send ater {D/60} minutes");await sleep(D)
		if str(A.effective_user.id)==str(owner):
			try:await A.message.reply_video(video=E,caption=B,reply_markup=G,quote=_B)
			except BaseException:
				try:await A.message.reply_video(video=E,caption=B,quote=_B)
				except BaseException:
					try:await A.message.reply_video(video=E,quote=_B)
					except BaseException:
						try:await A.message.reply_photo(photo=F,caption=B,reply_markup=G,quote=_B)
						except BaseException:
							try:await A.message.reply_photo(photo=F,caption=B,quote=_B)
							except BaseException:
								try:await A.message.reply_photo(photo=F,quote=_B)
								except BaseException:
									try:await A.message.reply_text(B,reply_markup=G,quote=_B)
									except BaseException:await A.message.reply_text(B,quote=_B)
	else:J=[[InlineKeyboardButton(_L,_M)]];K=InlineKeyboardMarkup(J);await A.message.reply_text(_T,reply_markup=K)
async def stoppost(update,context):
	'add member to bot';A=update;B=A.message.from_user;logger.info('User %s stopped the post.',B.first_name);await A.message.reply_text(nonono)
	if str(A.effective_user.id)==str(owner):
		try:C=context.args[0];DATALIST[C][_P]='false';await A.message.reply_text('stopped')
		except BaseException:await A.message.reply_text('post stopped')
async def postset(update,context):A=update;B=A.message.from_user;logger.info('User %s pressed post setting.',B.first_name);await A.message.reply_text('ENTER THE NUMBER OF POST YOU WANT IN A LOOP\n\nthis will only change for /send command \n press /cancel if you dont want to change it.');return SETPOST
async def postset1(update,context):
	B=update;A=B.message.text;global post_count
	try:A=int(A)
	except:pass
	if isinstance(A,int):post_count=int(A);C=[[_D,_E],[_F,_G]];D=ReplyKeyboardMarkup(C);await B.message.reply_text(f"Post count Changed to : {str(A)}",reply_markup=ReplyKeyboardMarkup(C,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_O));return ConversationHandler.END
	else:await B.message.reply_text('enter digits only')
async def timeset(update,context):A=update;B=A.message.from_user;logger.info('User %s pressed time.',B.first_name);await A.message.reply_text('ENTER THE TIME FORMAT Hours, Minutes, Seconds \n\nthis will only change for /send command \n press /cancel if you dont want to change it.');return SETTIME
async def timeset1(update,context):
	E='enter one of these option\n Hours, Minutes, Seconds only';B=update;C=B.message.text.lower();global waitpost
	if isinstance(C,str):
		if C[0]=='h':waitpost=600;A=[[_D,_E],[_F,_G]];D=ReplyKeyboardMarkup(A);await B.message.reply_text('Time Format Changed TO Hours',reply_markup=ReplyKeyboardMarkup(A,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_O));return ConversationHandler.END
		elif C[0]=='m':waitpost=60;A=[[_D,_E],[_F,_G]];D=ReplyKeyboardMarkup(A);await B.message.reply_text('Time Format Changed TO Minutes',reply_markup=ReplyKeyboardMarkup(A,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_O));return ConversationHandler.END
		elif C[0]=='s':waitpost=1;A=[[_D,_E],[_F,_G]];D=ReplyKeyboardMarkup(A);await B.message.reply_text('Time Format Changed TO SEC',reply_markup=ReplyKeyboardMarkup(A,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_O));return ConversationHandler.END
		else:await B.message.reply_text(E)
	else:await B.message.reply_text(E)
async def taskdone(update,context):await update.message.reply_text('Seting Saved');return ConversationHandler.END
async def setting(update,context):'show two buttons for setting';A=update;C=A.message.from_user;logger.info('User %s pressed setting.',C.first_name);B=[['Post Count','Time Setting']];D=ReplyKeyboardMarkup(B);await A.message.reply_text('Settings for Bot!',reply_markup=ReplyKeyboardMarkup(B,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_O));return RTPT
def main():'Run the bot.';F='^(✅Done)$';E='^(📌 make new post)$';D='cancel';C='done';B='skip';A=Application.builder().token(BOT_TOKEN).build();A.add_handler(CommandHandler('start',start));A.add_handler(CommandHandler('send',send,block=_B));A.add_handler(CommandHandler('stop',stoppost));A.add_handler(CommandHandler('rk',hidekey));A.add_handler(CommandHandler('time',sendonce));A.add_handler(MessageHandler(filters.Regex('^(🤖 Buy bot)$'),buy));G=ConversationHandler(entry_points=[MessageHandler(filters.Regex('^(Setting)$'),setting)],states={RTPT:[MessageHandler(filters.Regex('^(Post Count)$')&~ filters.COMMAND,postset),MessageHandler(filters.Regex('^(Time Setting)$')&~ filters.COMMAND,timeset)],SETPOST:[MessageHandler(filters.TEXT&~ filters.COMMAND,postset1)],SETTIME:[MessageHandler(filters.TEXT&~ filters.COMMAND,timeset1)]},fallbacks=[CommandHandler(D,cancel)]);H=ConversationHandler(entry_points=[MessageHandler(filters.Regex('^(📌 make new post|Post)$'),newpost)],states={PHOTO:[MessageHandler(filters.PHOTO&~ filters.COMMAND,photo),CommandHandler(B,skip_photo),MessageHandler(filters.VIDEO&~ filters.COMMAND,video),MessageHandler(filters.ALL&~ filters.COMMAND,leftinmiddle)],MESS:[MessageHandler(filters.Regex(E)&~ filters.COMMAND,leftinmiddle),MessageHandler(filters.TEXT&~ filters.COMMAND,save_mess),CommandHandler(B,skip_mess)],NAME:[MessageHandler(filters.Regex(E)&~ filters.COMMAND,leftinmiddle),MessageHandler(filters.Regex(F),skip_link),MessageHandler(filters.TEXT&~ filters.COMMAND,link_name),CommandHandler(C,skip_link)],LINK:[MessageHandler(filters.Regex(E)&~ filters.COMMAND,leftinmiddle),MessageHandler(filters.TEXT&~ filters.COMMAND,link),CommandHandler(C,skip_link)]},fallbacks=[CommandHandler(D,cancel)]);I=ConversationHandler(entry_points=[MessageHandler(filters.Regex('^(📝 edit post|edit post)$'),editpost)],states={EDIT:[MessageHandler(filters.TEXT&~ filters.COMMAND,save_post)],PHOTO:[MessageHandler(filters.TEXT&~ filters.COMMAND,edit_photo),MessageHandler(filters.PHOTO&~ filters.COMMAND,edit_photo),MessageHandler(filters.VIDEO&~ filters.COMMAND,edit_video),CommandHandler(B,skip_photo)],MESS:[MessageHandler(filters.TEXT&~ filters.COMMAND,edit_mess),CommandHandler(B,skip_mess)],NAME:[MessageHandler(filters.Regex(F),edit_skip_link),MessageHandler(filters.TEXT&~ filters.COMMAND,link_name),CommandHandler(C,edit_skip_link)],LINK:[MessageHandler(filters.TEXT&~ filters.COMMAND,edit_link),CommandHandler(C,edit_skip_link)]},fallbacks=[CommandHandler(D,cancel)]);A.add_handler(H);A.add_handler(G);A.add_handler(I);A.run_polling()
if __name__=='__main__':main()