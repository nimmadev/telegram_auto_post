_b='User %s started the post.'
_a='User %s canceled the conversation.'
_Z='below is the post number for your post\n\nuse below  command to send post to ur group \n\ntime is in seconds'
_Y='skiping link as u entered incorrect link'
_X='Please enter link name for second button\n\n or press /done'
_W='send the photo 📸\n\n/skip the Photo'
_V='User %s seaching post'
_U='but bot👇\u200c\u200c'
_T='Send Link'
_S='linkname'
_R='working'
_Q='✅Done'
_P='setting'
_O='type the text and send! ✍️\n\n/skip the Text'
_N='t.me/r5pro'
_M='Click Here To Buy'
_L='postid'
_K='video_id'
_J='photo_id'
_I='Setting'
_H='Search Old Post'
_G='text'
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
import sys
sys.setrecursionlimit(20000000)
try:from telegram import __version_info__
except ImportError:__version_info__=0,0,0,0,0
if __version_info__<(20,0,0,'alpha',1):raise RuntimeError(f"install python-telegram-bot --pre")
import base64
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove,Update,InlineKeyboardButton,InlineQueryResultArticle,InputTextMessageContent,Bot
from telegram.ext import Application,CommandHandler,ContextTypes,ConversationHandler,MessageHandler,filters,InlineQueryHandler
def random_id(n):range_start=10**(n-1);range_end=10**n-1;return randint(range_start,range_end)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger=logging.getLogger(__name__)
current_path=Path.cwd()
EDIT,PHOTO,MESS,NAME,LINK=range(5)
RTPT,SETPOST,SETTIME=range(3)
SP=range(1)
waitpost=1
post_count=20000000
with open('config.toml','r')as config:
	confd=toml.load(config)
	try:BOT_TOKEN=confd['bot_token'];owner=str(confd['owner'])
	except BaseException:print('fill the config.toml');exit()
DATALIST={}
bytename='dGhpcyBpcyB0aGUgZnJlZSB2ZXJzaW9uIG9mICBib3QgbWFkZSBieSBAcjVwcm8='
bytename=base64.b64decode(bytename)
nonono=str(bytename.decode())
async def start(update,context):
	if str(update.effective_user.id)==str(owner):reply_keyboard=[[_D,_E],[_F,_I],[_H]];await update.message.reply_text('✨! this is free version of bot contact @r5pro',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder='welcome'))
	else:reply_keyboard=[[InlineKeyboardButton(_M,_N)]];mark=InlineKeyboardMarkup(reply_keyboard);await update.message.reply_text('To Buy BOT Contact : @r5pro\u200c\u200c',reply_markup=mark)
async def serachpost(update,context):user=update.message.from_user;logger.info(_V,user.first_name);await update.message.reply_text('enter any sentence or word to serch from posts\n /cancel to stop searching');return SP
async def serachpost2(update,context):
	text=update.message.text;user=update.message.from_user;logger.info(_V,user.first_name);found=_B
	for (key,value) in DATALIST.items():
		if text.lower()in value[_G].lower():await update.message.reply_text(f"found a matching post {key}");found=_A
	if found==_B:await update.message.reply_text(f"no matching post found")
	return ConversationHandler.END
async def buy(update,context):reply_keyboard=[[InlineKeyboardButton(_M,_N)]];mark=InlineKeyboardMarkup(reply_keyboard);await update.message.reply_text('contact @r5pro\u200c\u200c',reply_markup=mark)
async def newpost(update,context):
	if str(update.effective_user.id)==str(owner):context.user_data[_C]=[];reply_keyboard=[[_D,_E],[_F,_Q]];await update.message.reply_text(_W,reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A));return PHOTO
	else:await update.message.reply_text(f"enter coreect user id in config.toml\n your ID is  : {str(update.effective_user.id)}")
async def editpost(update,context):
	if str(update.effective_user.id)==str(owner):await update.message.reply_text('send the post number.\n you want to edit');return EDIT
async def photo(update,context):context.user_data[_J]=update.message.photo[-1].file_id;await update.message.reply_text(_O);return MESS
async def video(update,context):
	mess=f"video file size should be less then 20mb";size=23000000
	if update.message.video.file_size>size:await update.message.reply_text(mess)
	else:context.user_data[_K]=update.message.video.file_id;await update.message.reply_text(_O);return MESS
async def edit_video(update,context):
	mess=f"video file size should be less then 20mb";size=23000000
	if update.message.video.file_size>size:await update.message.reply_text(mess)
	else:DATALIST[context.user_data[_L]][_K]=update.message.video.file_id;await update.message.reply_text(_O);return MESS
async def edit_photo(update,context):
	if update.message.text:await update.message.reply_text('send photo')
	else:DATALIST[context.user_data[_L]][_J]=update.message.photo[-1].file_id;await update.message.reply_text(_O);return MESS
async def save_post(update,context):
	text=update.message.text
	if text in DATALIST:context.user_data[_L]=text;await update.message.reply_text(_W);return PHOTO
	else:await update.message.reply_text('This post ID not avilable.\n Enter correct ID or press /cancel to cancel')
async def skip_photo(update,context):await update.message.reply_text(_O);return MESS
async def save_mess(update,context):
	try:text=update.message.text;context.user_data[_G]=text;await update.message.reply_text(text);await update.message.reply_text('Pease enter the name of link button : \n\n/done')
	except BaseException:await update.message.reply_text('it should be text send again ');return MESS
	return NAME
async def edit_mess(update,context):
	try:text=update.message.text;post=context.user_data[_L];DATALIST[post][_G]=text;await update.message.reply_text(update.message.text);reply_keyboard=[[_D,_E],[_F,_Q]];await update.message.reply_text('Pease enter the name of link button :  \n\n/done',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A))
	except BaseException:await update.message.reply_text('it should be text send again');return MESS
	return NAME
async def skip_mess(update,context):await update.message.reply_text('Pease enter the name of link button : /done');return NAME
async def link_name(update,context):text=update.message.text;context.user_data[_S]=text;await update.message.reply_text('Please enter the link \n\nlink should be valid');return LINK
async def link(update,context):
	text=update.message.text;name=context.user_data[_S]
	try:link=context.user_data[_C];new=InlineKeyboardButton(name,text);link.append(new)
	except BaseException:lin=[];new=InlineKeyboardButton(name,text);lin.append(new);context.user_data[_C]=lin
	reply_keyboard=[[_D,_E],[_F,_Q],[_H]];await update.message.reply_text(_X,reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A));return NAME
async def edit_link(update,context):
	postid=context.user_data[_L];text=update.message.text;name=context.user_data[_S]
	try:link=context.user_data[_C];new=InlineKeyboardButton(name,text);link.append(new)
	except BaseException:lin=[];new=InlineKeyboardButton(name,text);lin.append(new);context.user_data[_C]=lin
	reply_keyboard=[[_D,_E],[_F,_Q]];await update.message.reply_text(_X,reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A));return NAME
async def skip_link(update,context):
	postid=str(random_id(2));keyboard=[];datalink=context.user_data[_C]
	try:
		for data in datalink:key=[];key.append(data);keyboard.append(key)
		reply_markup=InlineKeyboardMarkup(keyboard);reply_markup;context.user_data[_C]=reply_markup
	except BaseException:await update.message.reply_text(_Y)
	DATALIST[postid]=context.user_data.copy();context.user_data.clear()
	try:videoid=DATALIST[postid][_K]
	except BaseException:
		try:photoid=DATALIST[postid][_J]
		except BaseException:pass
	try:text=DATALIST[postid][_G]
	except BaseException:pass
	try:link=DATALIST[postid][_C]
	except BaseException:pass
	try:await update.message.reply_video(video=videoid,caption=text,reply_markup=link)
	except BaseException:
		try:await update.message.reply_video(video=videoid,caption=text)
		except BaseException:
			try:await update.message.reply_video(video=videoid)
			except BaseException:
				try:await update.message.reply_photo(photo=photoid,caption=text,reply_markup=link)
				except BaseException:
					try:await update.message.reply_photo(photo=photoid,caption=text)
					except BaseException:
						try:await update.message.reply_photo(photo=photoid)
						except BaseException:
							try:await update.message.reply_text(text,reply_markup=link)
							except BaseException:await update.message.reply_text(text)
	reply_keyboard=[[_D,_E],[_F,_I],[_H]];await update.message.reply_markdown_v2(_Z,reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_T));await update.message.reply_text(f"/send {postid} (time in seconds)\n/time {postid} (time in minutes) send single post");return ConversationHandler.END
async def hidekey(update,context):await update.message.reply_text('Keyboard Removed',reply_markup=ReplyKeyboardRemove())
async def edit_skip_link(update,context):
	postid=context.user_data[_L];keyboard=[]
	try:
		for data in ontext.user_data[_C]:key=[];key.append(data);keyboard.append(key)
		reply_markup=InlineKeyboardMarkup(keyboard);DATALIST[postid][_C]=reply_markup
	except BaseException:await update.message.reply_text(_Y)
	data=DATALIST[postid]
	try:videoid=DATALIST[postid][_K]
	except BaseException:
		try:photoid=DATALIST[postid][_J]
		except BaseException:pass
	try:text=DATALIST[postid][_G]
	except BaseException:pass
	try:link=DATALIST[postid][_C]
	except BaseException:pass
	try:await update.message.reply_video(video=videoid,caption=text,reply_markup=link)
	except BaseException:
		try:await update.message.reply_video(video=videoid,caption=text)
		except BaseException:
			try:await update.message.reply_video(video=videoid)
			except BaseException:
				try:await update.message.reply_photo(photo=photoid,caption=text,reply_markup=link)
				except BaseException:
					try:await update.message.reply_photo(photo=photoid,caption=text)
					except BaseException:
						try:await update.message.reply_photo(photo=photoid)
						except BaseException:
							try:await update.message.reply_text(text,reply_markup=link)
							except BaseException:await update.message.reply_text(text)
	reply_keyboard=[[_D,_E],[_F,_I],[_H]];await update.message.reply_markdown_v2(_Z,reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_T));await update.message.reply_text(f"/send {postid} (time in seconds)\n/time {postid} (time in minutes) send single post");return ConversationHandler.END
async def cancel(update,context):user=update.message.from_user;reply_keyboard=[[_D,_E],[_F,_I],[_H]];logger.info(_a,user.first_name);await update.message.reply_text('Bye!.',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_T));return ConversationHandler.END
async def leftinmiddle(update,context):user=update.message.from_user;logger.info(_a,user.first_name);await update.message.reply_text('U HAVE LEFT in middle of post press /cancel')
async def send(update,context):
	B='videoid';A='True';user=update.message.from_user;messageid=None;chatid=int(update.message.chat_id);logger.info(_b,user.first_name);await update.message.reply_text(nonono)
	if str(update.effective_user.id)==str(owner):
		postsendid=context.args[0]
		try:wait=float(context.args[1])
		except:await update.message.reply_text('enter command with time');return
		try:text=DATALIST[postsendid][_G];link=DATALIST[postsendid][_C]
		except BaseException:pass
		try:photoid=DATALIST[postsendid][_J]
		except:
			try:videoid=DATALIST[postsendid][_K]
			except BaseException:pass
		DATALIST[postsendid][_R]=A;post_count_copy=post_count;await update.message.reply_text(f"stop by /stop {postsendid}")
		for xx in range(post_count_copy):
			if DATALIST[postsendid][_R]==A:
				if str(update.effective_user.id)==str(owner):
					if B in locals():
						if _G and _C in locals():messag=await update.message.reply_video(video=videoid,caption=text,reply_markup=link,quote=_B)
						elif B and _G in locals():messag=await update.message.reply_video(video=videoid,caption=text,quote=_B)
						else:messag=await update.message.reply_video(video=videoid,quote=_B)
					elif'photoid'in locals():
						if _G and _C in locals():messag=await update.message.reply_photo(photo=photoid,caption=text,reply_markup=link,quote=_B)
						elif _G in locals():messag=await update.message.reply_photo(photo=photoid,caption=text,quote=_B)
						else:messag=await update.message.reply_photo(photo=photoid,quote=_B)
					elif _C in locals():messag=await update.message.reply_text(text,reply_markup=link,quote=_B)
					else:messag=await update.message.reply_text(text,quote=_B)
					post_count_copy-=1;await sleep(wait*waitpost);messageid=messag.message_id
					try:await context.bot.delete_message(chatid,messageid);await sleep(1)
					except:pass
			else:break
		if DATALIST[postsendid][_R]==A:await update.message.reply_text(f"{post_count} : message has been send");reply_keyboard=[[InlineKeyboardButton(_M,_N)]];mark=InlineKeyboardMarkup(reply_keyboard);await update.message.reply_text(_U,reply_markup=mark)
	else:reply_keyboard=[[InlineKeyboardButton(_M,_N)]];mark=InlineKeyboardMarkup(reply_keyboard);await update.message.reply_text(_U,reply_markup=mark)
async def sendonce(update,context):
	user=update.message.from_user;logger.info(_b,user.first_name);await update.message.reply_text(nonono)
	if str(update.effective_user.id)==str(owner):
		postsendid=context.args[0];wait=str(context.args[1])
		try:wait=int(wait)*60
		except BaseException:await update.message.reply_text('enter time un minutes 60 90 120')
		try:videoid=DATALIST[postsendid][_K]
		except BaseException:
			try:photoid=DATALIST[postsendid][_J]
			except BaseException:pass
		try:text=DATALIST[postsendid][_G]
		except BaseException:pass
		try:link=DATALIST[postsendid][_C]
		except BaseException:pass
		await update.message.reply_text(f"post will be send ater {wait/60} minutes");await sleep(wait)
		if str(update.effective_user.id)==str(owner):
			try:await update.message.reply_video(video=videoid,caption=text,reply_markup=link,quote=_B)
			except BaseException:
				try:await update.message.reply_video(video=videoid,caption=text,quote=_B)
				except BaseException:
					try:await update.message.reply_video(video=videoid,quote=_B)
					except BaseException:
						try:await update.message.reply_photo(photo=photoid,caption=text,reply_markup=link,quote=_B)
						except BaseException:
							try:await update.message.reply_photo(photo=photoid,caption=text,quote=_B)
							except BaseException:
								try:await update.message.reply_photo(photo=photoid,quote=_B)
								except BaseException:
									try:await update.message.reply_text(text,reply_markup=link,quote=_B)
									except BaseException:await update.message.reply_text(text,quote=_B)
	else:reply_keyboard=[[InlineKeyboardButton(_M,_N)]];mark=InlineKeyboardMarkup(reply_keyboard);await update.message.reply_text(_U,reply_markup=mark)
async def stoppost(update,context):
	user=update.message.from_user;logger.info('User %s stopped the post.',user.first_name);await update.message.reply_text(nonono)
	if str(update.effective_user.id)==str(owner):
		try:poststopid=context.args[0];DATALIST[poststopid][_R]='false';await update.message.reply_text('stopped')
		except BaseException:await update.message.reply_text('post stopped')
async def postset(update,context):user=update.message.from_user;logger.info('User %s pressed post setting.',user.first_name);await update.message.reply_text('ENTER THE NUMBER OF POST YOU WANT IN A LOOP\n\nthis will only change for /send command \n press /cancel if you dont want to change it.');return SETPOST
async def postset1(update,context):
	text=update.message.text;global post_count
	try:text=int(text)
	except:pass
	if isinstance(text,int):post_count=int(text);reply_keyboard=[[_D,_E],[_F,_I],[_H]];mark=ReplyKeyboardMarkup(reply_keyboard);await update.message.reply_text(f"Post count Changed to : {str(text)}",reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_P));return ConversationHandler.END
	else:await update.message.reply_text('enter digits only')
async def timeset(update,context):user=update.message.from_user;logger.info('User %s pressed time.',user.first_name);await update.message.reply_text('ENTER THE TIME FORMAT Hours, Minutes, Seconds \n\nthis will only change for /send command \n press /cancel if you dont want to change it.');return SETTIME
async def timeset1(update,context):
	A='enter one of these option\n Hours, Minutes, Seconds only';text=update.message.text.lower();global waitpost
	if isinstance(text,str):
		if text[0]=='h':waitpost=3600;reply_keyboard=[[_D,_E],[_F,_I],[_H]];mark=ReplyKeyboardMarkup(reply_keyboard);await update.message.reply_text('Time Format Changed TO Hours',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_P));return ConversationHandler.END
		elif text[0]=='m':waitpost=60;reply_keyboard=[[_D,_E],[_F,_I],[_H]];mark=ReplyKeyboardMarkup(reply_keyboard);await update.message.reply_text('Time Format Changed TO Minutes',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_P));return ConversationHandler.END
		elif text[0]=='s':waitpost=1;reply_keyboard=[[_D,_E],[_F,_I],[_H]];mark=ReplyKeyboardMarkup(reply_keyboard);await update.message.reply_text('Time Format Changed TO SEC',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_P));return ConversationHandler.END
		else:await update.message.reply_text(A)
	else:await update.message.reply_text(A)
async def taskdone(update,context):await update.message.reply_text('Seting Saved');return ConversationHandler.END
async def setting(update,context):user=update.message.from_user;logger.info('User %s pressed setting.',user.first_name);reply_keyboard=[['Post Count','Time Setting']];mark=ReplyKeyboardMarkup(reply_keyboard);await update.message.reply_text('Settings for Bot!',reply_markup=ReplyKeyboardMarkup(reply_keyboard,resize_keyboard=_A,one_time_keyboard=_A,input_field_placeholder=_P));return RTPT
def main():E='^(✅Done)$';D='^(📌 make new post)$';C='done';B='skip';A='cancel';application=Application.builder().token(BOT_TOKEN).build();application.add_handler(CommandHandler('start',start));application.add_handler(CommandHandler('send',send,block=_B));application.add_handler(CommandHandler('stop',stoppost));application.add_handler(CommandHandler('rk',hidekey));application.add_handler(CommandHandler('time',sendonce));application.add_handler(MessageHandler(filters.Regex('^(🤖 Buy bot)$'),buy));post_handler=ConversationHandler(entry_points=[MessageHandler(filters.Regex('^(Setting)$'),setting)],states={RTPT:[MessageHandler(filters.Regex('^(Post Count)$')&~ filters.COMMAND,postset),MessageHandler(filters.Regex('^(Time Setting)$')&~ filters.COMMAND,timeset)],SETPOST:[MessageHandler(filters.TEXT&~ filters.COMMAND,postset1)],SETTIME:[MessageHandler(filters.TEXT&~ filters.COMMAND,timeset1)]},fallbacks=[CommandHandler(A,cancel)]);search_handler=ConversationHandler(entry_points=[MessageHandler(filters.Regex('^(Search Old Post)$'),serachpost)],states={SP:[MessageHandler(filters.TEXT&~ filters.COMMAND,serachpost2)]},fallbacks=[CommandHandler(A,cancel)]);add_handler=ConversationHandler(entry_points=[MessageHandler(filters.Regex('^(📌 make new post|Post)$'),newpost)],states={PHOTO:[MessageHandler(filters.PHOTO&~ filters.COMMAND,photo),CommandHandler(B,skip_photo),MessageHandler(filters.VIDEO&~ filters.COMMAND,video),MessageHandler(filters.ALL&~ filters.COMMAND,leftinmiddle)],MESS:[MessageHandler(filters.Regex(D)&~ filters.COMMAND,leftinmiddle),MessageHandler(filters.TEXT&~ filters.COMMAND,save_mess),CommandHandler(B,skip_mess)],NAME:[MessageHandler(filters.Regex(D)&~ filters.COMMAND,leftinmiddle),MessageHandler(filters.Regex(E),skip_link),MessageHandler(filters.TEXT&~ filters.COMMAND,link_name),CommandHandler(C,skip_link)],LINK:[MessageHandler(filters.Regex(D)&~ filters.COMMAND,leftinmiddle),MessageHandler(filters.TEXT&~ filters.COMMAND,link),CommandHandler(C,skip_link)]},fallbacks=[CommandHandler(A,cancel)]);edit_handler=ConversationHandler(entry_points=[MessageHandler(filters.Regex('^(📝 edit post|edit post)$'),editpost)],states={EDIT:[MessageHandler(filters.TEXT&~ filters.COMMAND,save_post)],PHOTO:[MessageHandler(filters.TEXT&~ filters.COMMAND,edit_photo),MessageHandler(filters.PHOTO&~ filters.COMMAND,edit_photo),MessageHandler(filters.VIDEO&~ filters.COMMAND,edit_video),CommandHandler(B,skip_photo)],MESS:[MessageHandler(filters.TEXT&~ filters.COMMAND,edit_mess),CommandHandler(B,skip_mess)],NAME:[MessageHandler(filters.Regex(E),edit_skip_link),MessageHandler(filters.TEXT&~ filters.COMMAND,link_name),CommandHandler(C,edit_skip_link)],LINK:[MessageHandler(filters.TEXT&~ filters.COMMAND,edit_link),CommandHandler(C,edit_skip_link)]},fallbacks=[CommandHandler(A,cancel)]);application.add_handler(add_handler);application.add_handler(post_handler);application.add_handler(edit_handler);application.add_handler(search_handler);application.run_polling()
if __name__=='__main__':main()