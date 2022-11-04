Ah='User %s started the post.'
Ag='User %s canceled the conversation.'
Af='below is the post number for your post\n\nuse below  command to send post to ur group \n\ntime is in seconds'
Ae='skiping link as u entered incorrect link'
Ad='Please enter link name for second button\n\n or press /done'
Ac='send the photo 📸\n\n/skip the Photo'
Ab='User %s seaching post'
Aa=isinstance
A7='but bot👇\u200c\u200c'
A6='Send Link'
A5='linkname'
A4=range
r='working'
q='✅Done'
j='setting'
i='type the text and send! ✍️\n\n/skip the Text'
h='t.me/r5pro'
g='Click Here To Buy'
f=int
a='postid'
Z='video_id'
Y='photo_id'
W='text'
V='Setting'
S='Search Old Post'
N='🤖 Buy bot'
M='📝 edit post'
L='📌 make new post'
K='link'
H=False
F=str
E=True
A=BaseException
import logging as k,toml
from pathlib import Path
from random import randint
from html import escape
import json
from telegram.constants import ParseMode
from asyncio import sleep as s
from telegram import InlineKeyboardMarkup as T,ReplyKeyboardRemove as t,PassportElementErrorTranslationFile,__version__ as Ai
try:from telegram import __version_info__
except ImportError:__version_info__=0,0,0,0,0
if __version_info__<(20,0,0,'alpha',1):raise RuntimeError(f"install python-telegram-bot --pre")
import base64
from telegram import ReplyKeyboardMarkup as G,ReplyKeyboardRemove as t,Update,InlineKeyboardButton as P,InlineQueryResultArticle,InputTextMessageContent,Bot
from telegram.ext import Application as A8,CommandHandler as I,ContextTypes,ConversationHandler as J,MessageHandler as C,filters as B,InlineQueryHandler
def A9(n):A=10**(n-1);B=10**n-1;return randint(A,B)
k.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=k.INFO)
O=k.getLogger(__name__)
Aj=Path.cwd()
u,b,Q,U,l=A4(5)
v,w,x=A4(3)
y=A4(1)
X=1
c=200000
with open('config.toml','r')as AA:
	z=toml.load(AA)
	try:AB=z['bot_token'];R=F(z['owner'])
	except A:print('fill the config.toml');exit()
D={}
m='dGhpcyBpcyB0aGUgZnJlZSB2ZXJzaW9uIG9mICBib3QgbWFkZSBieSBAcjVwcm8='
m=base64.b64decode(m)
n=F(m.decode())
async def AC(update,context):
	A=update
	if F(A.effective_user.id)==F(R):B=[[L,M],[N,V],[S]];await A.message.reply_text('✨! this is free version of bot contact @r5pro',reply_markup=G(B,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder='welcome'))
	else:B=[[P(g,h)]];C=T(B);await A.message.reply_text('To Buy BOT Contact : @r5pro\u200c\u200c',reply_markup=C)
async def AD(update,context):A=update;B=A.message.from_user;O.info(Ab,B.first_name);await A.message.reply_text('enter any sentence or word to serch from posts\n /cancel to stop searching');return y
async def AE(update,context):
	A=update;C=A.message.text;F=A.message.from_user;O.info(Ab,F.first_name);B=H
	for (G,I) in D.items():
		if C.lower()in I[W].lower():await A.message.reply_text(f"found a matching post {G}");B=E
	if B==H:await A.message.reply_text(f"no matching post found")
	return J.END
async def AF(update,context):A=[[P(g,h)]];B=T(A);await update.message.reply_text('contact @r5pro\u200c\u200c',reply_markup=B)
async def AG(update,context):
	A=update
	if F(A.effective_user.id)==F(R):context.user_data[K]=[];B=[[L,M],[N,q]];await A.message.reply_text(Ac,reply_markup=G(B,resize_keyboard=E,one_time_keyboard=E));return b
	else:await A.message.reply_text(f"enter coreect user id in config.toml\n your ID is  : {F(A.effective_user.id)}")
async def AH(update,context):
	A=update
	if F(A.effective_user.id)==F(R):await A.message.reply_text('send the post number.\n you want to edit');return u
async def AI(update,context):A=update;context.user_data[Y]=A.message.photo[-1].file_id;await A.message.reply_text(i);return Q
async def AJ(update,context):
	A=update;B=f"video file size should be less then 20mb";C=23000000
	if A.message.video.file_size>C:await A.message.reply_text(B)
	else:context.user_data[Z]=A.message.video.file_id;await A.message.reply_text(i);return Q
async def AK(update,context):
	A=update;B=f"video file size should be less then 20mb";C=23000000
	if A.message.video.file_size>C:await A.message.reply_text(B)
	else:D[context.user_data[a]][Z]=A.message.video.file_id;await A.message.reply_text(i);return Q
async def A0(update,context):
	A=update
	if A.message.text:await A.message.reply_text('send photo')
	else:D[context.user_data[a]][Y]=A.message.photo[-1].file_id;await A.message.reply_text(i);return Q
async def AL(update,context):
	A=update;B=A.message.text
	if B in D:context.user_data[a]=B;await A.message.reply_text(Ac);return b
	else:await A.message.reply_text('This post ID not avilable.\n Enter correct ID or press /cancel to cancel')
async def A1(update,context):await update.message.reply_text(i);return Q
async def AM(update,context):
	B=update
	try:C=B.message.text;context.user_data[W]=C;await B.message.reply_text(C);await B.message.reply_text('Pease enter the name of link button : \n\n/done')
	except A:await B.message.reply_text('it should be text send again ');return Q
	return U
async def AN(update,context):
	B=update
	try:C=B.message.text;F=context.user_data[a];D[F][W]=C;await B.message.reply_text(B.message.text);H=[[L,M],[N,q]];await B.message.reply_text('Pease enter the name of link button :  \n\n/done',reply_markup=G(H,resize_keyboard=E,one_time_keyboard=E))
	except A:await B.message.reply_text('it should be text send again');return Q
	return U
async def A2(update,context):await update.message.reply_text('Pease enter the name of link button : /done');return U
async def A3(update,context):A=update;B=A.message.text;context.user_data[A5]=B;await A.message.reply_text('Please enter the link \n\nlink should be valid');return l
async def AO(update,context):
	D=update;B=context;F=D.message.text;H=B.user_data[A5]
	try:J=B.user_data[K];C=P(H,F);J.append(C)
	except A:I=[];C=P(H,F);I.append(C);B.user_data[K]=I
	O=[[L,M],[N,q],[S]];await D.message.reply_text(Ad,reply_markup=G(O,resize_keyboard=E,one_time_keyboard=E));return U
async def AP(update,context):
	D=update;B=context;Q=B.user_data[a];F=D.message.text;H=B.user_data[A5]
	try:J=B.user_data[K];C=P(H,F);J.append(C)
	except A:I=[];C=P(H,F);I.append(C);B.user_data[K]=I
	O=[[L,M],[N,q]];await D.message.reply_text(Ad,reply_markup=G(O,resize_keyboard=E,one_time_keyboard=E));return U
async def o(update,context):
	I=context;B=update;C=F(A9(2));R=[];a=I.user_data[K]
	try:
		for b in a:U=[];U.append(b);R.append(U)
		X=T(R);X;I.user_data[K]=X
	except A:await B.message.reply_text(Ae)
	D[C]=I.user_data.copy();I.user_data.clear()
	try:O=D[C][Z]
	except A:
		try:P=D[C][Y]
		except A:pass
	try:H=D[C][W]
	except A:pass
	try:Q=D[C][K]
	except A:pass
	try:await B.message.reply_video(video=O,caption=H,reply_markup=Q)
	except A:
		try:await B.message.reply_video(video=O,caption=H)
		except A:
			try:await B.message.reply_video(video=O)
			except A:
				try:await B.message.reply_photo(photo=P,caption=H,reply_markup=Q)
				except A:
					try:await B.message.reply_photo(photo=P,caption=H)
					except A:
						try:await B.message.reply_photo(photo=P)
						except A:
							try:await B.message.reply_text(H,reply_markup=Q)
							except A:await B.message.reply_text(H)
	c=[[L,M],[N,V],[S]];await B.message.reply_markdown_v2(Af,reply_markup=G(c,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder=A6));await B.message.reply_text(f"/send {C} (time in seconds)\n/time {C} (time in minutes) send single post");return J.END
async def AQ(update,context):await update.message.reply_text('Keyboard Removed',reply_markup=t())
async def p(update,context):
	B=update;C=context.user_data[a];P=[]
	try:
		for Q in ontext.user_data[K]:R=[];R.append(Q);P.append(R)
		U=T(P);D[C][K]=U
	except A:await B.message.reply_text(Ae)
	Q=D[C]
	try:H=D[C][Z]
	except A:
		try:I=D[C][Y]
		except A:pass
	try:F=D[C][W]
	except A:pass
	try:O=D[C][K]
	except A:pass
	try:await B.message.reply_video(video=H,caption=F,reply_markup=O)
	except A:
		try:await B.message.reply_video(video=H,caption=F)
		except A:
			try:await B.message.reply_video(video=H)
			except A:
				try:await B.message.reply_photo(photo=I,caption=F,reply_markup=O)
				except A:
					try:await B.message.reply_photo(photo=I,caption=F)
					except A:
						try:await B.message.reply_photo(photo=I)
						except A:
							try:await B.message.reply_text(F,reply_markup=O)
							except A:await B.message.reply_text(F)
	X=[[L,M],[N,V],[S]];await B.message.reply_markdown_v2(Af,reply_markup=G(X,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder=A6));await B.message.reply_text(f"/send {C} (time in seconds)\n/time {C} (time in minutes) send single post");return J.END
async def d(update,context):A=update;B=A.message.from_user;C=[[L,M],[N,V],[S]];O.info(Ag,B.first_name);await A.message.reply_text('Bye!.',reply_markup=G(C,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder=A6));return J.END
async def e(update,context):A=update;B=A.message.from_user;O.info(Ag,B.first_name);await A.message.reply_text('U HAVE LEFT in middle of post press /cancel')
async def AR(update,context):
	V='True';I=context;B=update;a=B.message.from_user;S=None;b=f(B.message.chat_id);O.info(Ah,a.first_name);await B.message.reply_text(n)
	if F(B.effective_user.id)==F(R):
		C=I.args[0];d=float(I.args[1])
		try:J=D[C][Z]
		except A:
			try:L=D[C][Y]
			except A:pass
		try:G=D[C][W]
		except A:pass
		try:M=D[C][K]
		except A:pass
		D[C][r]=V;U=c;await B.message.reply_text(f"stop by /stop {C}")
		while D[C][r]==V and U>0:
			if F(B.effective_user.id)==F(R):
				try:E=await B.message.reply_video(video=J,caption=G,reply_markup=M,quote=H)
				except A:
					try:E=await B.message.reply_video(video=J,caption=G,quote=H)
					except A:
						try:E=await B.message.reply_video(video=J,quote=H)
						except A:
							try:E=await B.message.reply_photo(photo=L,caption=G,reply_markup=M,quote=H)
							except A:
								try:E=await B.message.reply_photo(photo=L,caption=G,quote=H)
								except A:
									try:E=await B.message.reply_photo(photo=L,quote=H)
									except A:
										try:E=await B.message.reply_text(G,reply_markup=M,quote=H)
										except A:E=await B.message.reply_text(G,quote=H)
				U-=1;await s(d*X);S=E.message_id
				try:await I.bot.delete_message(b,S)
				except:pass
			else:break
		if D[C][r]==V:await B.message.reply_text(f"{c} : message has been send");N=[[P(g,h)]];Q=T(N);await B.message.reply_text(A7,reply_markup=Q)
	else:N=[[P(g,h)]];Q=T(N);await B.message.reply_text(A7,reply_markup=Q)
async def AS(update,context):
	M=context;B=update;N=B.message.from_user;O.info(Ah,N.first_name);await B.message.reply_text(n)
	if F(B.effective_user.id)==F(R):
		E=M.args[0];G=F(M.args[1])
		try:G=f(G)*60
		except A:await B.message.reply_text('enter time un minutes 60 90 120')
		try:I=D[E][Z]
		except A:
			try:J=D[E][Y]
			except A:pass
		try:C=D[E][W]
		except A:pass
		try:L=D[E][K]
		except A:pass
		await B.message.reply_text(f"post will be send ater {G/60} minutes");await s(G)
		if F(B.effective_user.id)==F(R):
			try:await B.message.reply_video(video=I,caption=C,reply_markup=L,quote=H)
			except A:
				try:await B.message.reply_video(video=I,caption=C,quote=H)
				except A:
					try:await B.message.reply_video(video=I,quote=H)
					except A:
						try:await B.message.reply_photo(photo=J,caption=C,reply_markup=L,quote=H)
						except A:
							try:await B.message.reply_photo(photo=J,caption=C,quote=H)
							except A:
								try:await B.message.reply_photo(photo=J,quote=H)
								except A:
									try:await B.message.reply_text(C,reply_markup=L,quote=H)
									except A:await B.message.reply_text(C,quote=H)
	else:Q=[[P(g,h)]];S=T(Q);await B.message.reply_text(A7,reply_markup=S)
async def AT(update,context):
	B=update;C=B.message.from_user;O.info('User %s stopped the post.',C.first_name);await B.message.reply_text(n)
	if F(B.effective_user.id)==F(R):
		try:E=context.args[0];D[E][r]='false';await B.message.reply_text('stopped')
		except A:await B.message.reply_text('post stopped')
async def AU(update,context):A=update;B=A.message.from_user;O.info('User %s pressed post setting.',B.first_name);await A.message.reply_text('ENTER THE NUMBER OF POST YOU WANT IN A LOOP\n\nthis will only change for /send command \n press /cancel if you dont want to change it.');return w
async def AV(update,context):
	B=update;A=B.message.text;global c
	try:A=f(A)
	except:pass
	if Aa(A,f):c=f(A);C=[[L,M],[N,V],[S]];D=G(C);await B.message.reply_text(f"Post count Changed to : {F(A)}",reply_markup=G(C,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder=j));return J.END
	else:await B.message.reply_text('enter digits only')
async def AW(update,context):A=update;B=A.message.from_user;O.info('User %s pressed time.',B.first_name);await A.message.reply_text('ENTER THE TIME FORMAT Hours, Minutes, Seconds \n\nthis will only change for /send command \n press /cancel if you dont want to change it.');return x
async def AX(update,context):
	H='enter one of these option\n Hours, Minutes, Seconds only';B=update;C=B.message.text.lower();global X
	if Aa(C,F):
		if C[0]=='h':X=3600;A=[[L,M],[N,V],[S]];D=G(A);await B.message.reply_text('Time Format Changed TO Hours',reply_markup=G(A,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder=j));return J.END
		elif C[0]=='m':X=60;A=[[L,M],[N,V],[S]];D=G(A);await B.message.reply_text('Time Format Changed TO Minutes',reply_markup=G(A,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder=j));return J.END
		elif C[0]=='s':X=1;A=[[L,M],[N,V],[S]];D=G(A);await B.message.reply_text('Time Format Changed TO SEC',reply_markup=G(A,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder=j));return J.END
		else:await B.message.reply_text(H)
	else:await B.message.reply_text(H)
async def Ak(update,context):await update.message.reply_text('Seting Saved');return J.END
async def AY(update,context):A=update;C=A.message.from_user;O.info('User %s pressed setting.',C.first_name);B=[['Post Count','Time Setting']];D=G(B);await A.message.reply_text('Settings for Bot!',reply_markup=G(B,resize_keyboard=E,one_time_keyboard=E,input_field_placeholder=j));return v
def AZ():O='^(✅Done)$';G='^(📌 make new post)$';F='done';E='skip';D='cancel';A=A8.builder().token(AB).build();A.add_handler(I('start',AC));A.add_handler(I('send',AR,block=H));A.add_handler(I('stop',AT));A.add_handler(I('rk',AQ));A.add_handler(I('time',AS));A.add_handler(C(B.Regex('^(🤖 Buy bot)$'),AF));K=J(entry_points=[C(B.Regex('^(Setting)$'),AY)],states={v:[C(B.Regex('^(Post Count)$')&~ B.COMMAND,AU),C(B.Regex('^(Time Setting)$')&~ B.COMMAND,AW)],w:[C(B.TEXT&~ B.COMMAND,AV)],x:[C(B.TEXT&~ B.COMMAND,AX)]},fallbacks=[I(D,d)]);L=J(entry_points=[C(B.Regex('^(Search Old Post)$'),AD)],states={y:[C(B.TEXT&~ B.COMMAND,AE)]},fallbacks=[I(D,d)]);M=J(entry_points=[C(B.Regex('^(📌 make new post|Post)$'),AG)],states={b:[C(B.PHOTO&~ B.COMMAND,AI),I(E,A1),C(B.VIDEO&~ B.COMMAND,AJ),C(B.ALL&~ B.COMMAND,e)],Q:[C(B.Regex(G)&~ B.COMMAND,e),C(B.TEXT&~ B.COMMAND,AM),I(E,A2)],U:[C(B.Regex(G)&~ B.COMMAND,e),C(B.Regex(O),o),C(B.TEXT&~ B.COMMAND,A3),I(F,o)],l:[C(B.Regex(G)&~ B.COMMAND,e),C(B.TEXT&~ B.COMMAND,AO),I(F,o)]},fallbacks=[I(D,d)]);N=J(entry_points=[C(B.Regex('^(📝 edit post|edit post)$'),AH)],states={u:[C(B.TEXT&~ B.COMMAND,AL)],b:[C(B.TEXT&~ B.COMMAND,A0),C(B.PHOTO&~ B.COMMAND,A0),C(B.VIDEO&~ B.COMMAND,AK),I(E,A1)],Q:[C(B.TEXT&~ B.COMMAND,AN),I(E,A2)],U:[C(B.Regex(O),p),C(B.TEXT&~ B.COMMAND,A3),I(F,p)],l:[C(B.TEXT&~ B.COMMAND,AP),I(F,p)]},fallbacks=[I(D,d)]);A.add_handler(M);A.add_handler(K);A.add_handler(N);A.add_handler(L);A.run_polling()
if __name__=='__main__':AZ()