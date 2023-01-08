Ak='User %s canceled the conversation.'
Aj='below is the post number for your post\n\nuse below  command to send post to ur group \n\ntime is in seconds'
Ai='skiping link as u entered incorrect link'
Ah='Please enter link name for second button\n\n or press /done'
Ag='send the photo 📸\n\n/skip the Photo'
Af='User %s seaching post'
Ae=isinstance
Ad=float
A9='User %s started the post.'
A8='Send Link'
A7='linkname'
A6=range
u='✅Done'
n='setting'
m='but bot👇\u200c\u200c'
l='type the text and send! ✍️\n\n/skip the Text'
g='True'
f='postid'
e=int
d='working'
c='video_id'
b='photo_id'
a='t.me/r5pro'
Z='Click Here To Buy'
Y='Setting'
V='text'
T='Search Old Post'
Q='🤖 Buy bot'
P='📝 edit post'
O='📌 make new post'
K='link'
G=False
F=True
E=str
A=BaseException
import logging as o,toml
from pathlib import Path
from random import randint
from html import escape
import json
from telegram.constants import ParseMode
from asyncio import sleep as p
from telegram import InlineKeyboardMarkup as R,ReplyKeyboardRemove as v,PassportElementErrorTranslationFile,__version__ as Al
try:from telegram import __version_info__
except ImportError:__version_info__=0,0,0,0,0
if __version_info__<(20,0,0,'alpha',1):raise RuntimeError(f"install python-telegram-bot --pre")
import base64
from telegram import ReplyKeyboardMarkup as I,ReplyKeyboardRemove as v,Update,InlineKeyboardButton as L,InlineQueryResultArticle,InputTextMessageContent,Bot
from telegram.ext import Application as AA,CommandHandler as H,ContextTypes,ConversationHandler as J,MessageHandler as D,filters as B,InlineQueryHandler
def AB(n):A=10**(n-1);B=10**n-1;return randint(A,B)
o.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=o.INFO)
M=o.getLogger(__name__)
Am=Path.cwd()
w,h,S,U,q=A6(5)
x,y,z=A6(3)
A0=A6(1)
W=1
X=200000
with open('config.toml','r')as AC:
	A1=toml.load(AC)
	try:AD=A1['bot_token'];N=E(A1['owner'])
	except A:print('fill the config.toml');exit()
C={}
r='dGhpcyBpcyB0aGUgZnJlZSB2ZXJzaW9uIG9mICBib3QgbWFkZSBieSBAcjVwcm8='
r=base64.b64decode(r)
i=E(r.decode())
async def AE(update,context):
	A=update
	if E(A.effective_user.id)==E(N):B=[[O,P],[Q,Y],[T]];await A.message.reply_text('✨! this is free version of bot contact @r5pro',reply_markup=I(B,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder='welcome'))
	else:B=[[L(Z,a)]];C=R(B);await A.message.reply_text('To Buy BOT Contact : @r5pro\u200c\u200c',reply_markup=C)
async def AF(update,context):A=update;B=A.message.from_user;M.info(Af,B.first_name);await A.message.reply_text('enter any sentence or word to serch from posts\n /cancel to stop searching');return A0
async def AG(update,context):
	A=update;D=A.message.text;E=A.message.from_user;M.info(Af,E.first_name);B=G
	for (H,I) in C.items():
		if D.lower()in I[V].lower():await A.message.reply_text(f"found a matching post {H}");B=F
	if B==G:await A.message.reply_text(f"no matching post found")
	return J.END
async def AH(update,context):A=[[L(Z,a)]];B=R(A);await update.message.reply_text('contact @r5pro\u200c\u200c',reply_markup=B)
async def AI(update,context):
	A=update
	if E(A.effective_user.id)==E(N):context.user_data[K]=[];await A.message.reply_text(Ag);return h
	else:await A.message.reply_text(f"enter coreect user id in config.toml\n your ID is  : {E(A.effective_user.id)}")
async def AJ(update,context):
	A=update
	if E(A.effective_user.id)==E(N):await A.message.reply_text('send the post number.\n you want to edit');return w
async def AK(update,context):A=update;context.user_data[b]=A.message.photo[-1].file_id;await A.message.reply_text(l);return S
async def AL(update,context):
	A=update;B=f"video file size should be less then 20mb";C=23000000
	if A.message.video.file_size>C:await A.message.reply_text(B)
	else:context.user_data[c]=A.message.video.file_id;await A.message.reply_text(l);return S
async def AM(update,context):
	A=update;B=f"video file size should be less then 20mb";D=23000000
	if A.message.video.file_size>D:await A.message.reply_text(B)
	else:C[context.user_data[f]][c]=A.message.video.file_id;await A.message.reply_text(l);return S
async def A2(update,context):
	A=update
	if A.message.text:await A.message.reply_text('send photo')
	else:C[context.user_data[f]][b]=A.message.photo[-1].file_id;await A.message.reply_text(l);return S
async def AN(update,context):
	A=update;B=A.message.text
	if B in C:context.user_data[f]=B;await A.message.reply_text(Ag);return h
	else:await A.message.reply_text('This post ID not avilable.\n Enter correct ID or press /cancel to cancel')
async def A3(update,context):await update.message.reply_text(l);return S
async def AO(update,context):
	B=update
	try:C=B.message.text;context.user_data[V]=C;await B.message.reply_text(C);await B.message.reply_text('Pease enter the name of link button : \n\n/done')
	except A:await B.message.reply_text('it should be text send again ');return S
	return U
async def AP(update,context):
	B=update
	try:D=B.message.text;E=context.user_data[f];C[E][V]=D;await B.message.reply_text(B.message.text);G=[[O,P],[Q,u],[T]];await B.message.reply_text('Pease enter the name of link button :  \n\n/done',reply_markup=I(G,resize_keyboard=F,one_time_keyboard=F))
	except A:await B.message.reply_text('it should be text send again');return S
	return U
async def A4(update,context):await update.message.reply_text('Pease enter the name of link button : /done');return U
async def A5(update,context):A=update;B=A.message.text;context.user_data[A7]=B;await A.message.reply_text('Please enter the link \n\nlink should be valid');return q
async def AQ(update,context):
	D=update;B=context;E=D.message.text;G=B.user_data[A7]
	try:J=B.user_data[K];C=L(G,E);J.append(C)
	except A:H=[];C=L(G,E);H.append(C);B.user_data[K]=H
	M=[[O,P],[Q,u],[T]];await D.message.reply_text(Ah,reply_markup=I(M,resize_keyboard=F,one_time_keyboard=F));return U
async def AR(update,context):
	D=update;B=context;N=B.user_data[f];E=D.message.text;G=B.user_data[A7]
	try:J=B.user_data[K];C=L(G,E);J.append(C)
	except A:H=[];C=L(G,E);H.append(C);B.user_data[K]=H
	M=[[O,P],[Q,u],[T]];await D.message.reply_text(Ah,reply_markup=I(M,resize_keyboard=F,one_time_keyboard=F));return U
async def s(update,context):
	H=context;B=update;D=E(AB(2));S=[];X=H.user_data[K]
	try:
		for Y in X:U=[];U.append(Y);S.append(U)
		W=R(S);W;H.user_data[K]=W
	except A:await B.message.reply_text(Ai)
	C[D]=H.user_data.copy();H.user_data.clear()
	try:L=C[D][c]
	except A:
		try:M=C[D][b]
		except A:pass
	try:G=C[D][V]
	except A:pass
	try:N=C[D][K]
	except A:pass
	try:await B.message.reply_video(video=L,caption=G,reply_markup=N)
	except A:
		try:await B.message.reply_video(video=L,caption=G)
		except A:
			try:await B.message.reply_video(video=L)
			except A:
				try:await B.message.reply_photo(photo=M,caption=G,reply_markup=N)
				except A:
					try:await B.message.reply_photo(photo=M,caption=G)
					except A:
						try:await B.message.reply_photo(photo=M)
						except A:
							try:await B.message.reply_text(G,reply_markup=N)
							except A:await B.message.reply_text(G)
	Z=[[O,P],[Q,u],[T]];await B.message.reply_markdown_v2(Aj,reply_markup=I(Z,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder=A8));await B.message.reply_text(f"/send {D} (time in seconds)\n/time {D} (time in minutes) send single post");return J.END
async def AS(update,context):await update.message.reply_text('Keyboard Removed',reply_markup=v())
async def t(update,context):
	B=update;D=context.user_data[f];M=[]
	try:
		for N in ontext.user_data[K]:S=[];S.append(N);M.append(S)
		U=R(M);C[D][K]=U
	except A:await B.message.reply_text(Ai)
	N=C[D]
	try:G=C[D][c]
	except A:
		try:H=C[D][b]
		except A:pass
	try:E=C[D][V]
	except A:pass
	try:L=C[D][K]
	except A:pass
	try:await B.message.reply_video(video=G,caption=E,reply_markup=L)
	except A:
		try:await B.message.reply_video(video=G,caption=E)
		except A:
			try:await B.message.reply_video(video=G)
			except A:
				try:await B.message.reply_photo(photo=H,caption=E,reply_markup=L)
				except A:
					try:await B.message.reply_photo(photo=H,caption=E)
					except A:
						try:await B.message.reply_photo(photo=H)
						except A:
							try:await B.message.reply_text(E,reply_markup=L)
							except A:await B.message.reply_text(E)
	W=[[O,P],[Q,Y],[T]];await B.message.reply_markdown_v2(Aj,reply_markup=I(W,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder=A8));await B.message.reply_text(f"/send {D} (time in seconds)\n/time {D} (time in minutes) send single post \n/sendch {D} (time in seconds) (channelid)\n");return J.END
async def j(update,context):A=update;B=A.message.from_user;C=[[O,P],[Q,Y]];M.info(Ak,B.first_name);await A.message.reply_text('Bye!.',reply_markup=I(C,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder=A8));return J.END
async def k(update,context):A=update;B=A.message.from_user;M.info(Ak,B.first_name);await A.message.reply_text('U HAVE LEFT in middle of post press /cancel')
async def AT(update,context):
	I=context;B=update;Y=B.message.from_user;T=None;f=e(B.message.chat_id);M.info(A9,Y.first_name);await B.message.reply_text(i)
	if E(B.effective_user.id)==E(N):
		D=I.args[0];h=Ad(I.args[1])
		try:J=C[D][c]
		except A:
			try:O=C[D][b]
			except A:pass
		try:H=C[D][V]
		except A:pass
		try:P=C[D][K]
		except A:pass
		C[D][d]=g;U=X;await B.message.reply_text(f"stop by /stop {D}")
		while C[D][d]==g and U>0:
			if E(B.effective_user.id)==E(N):
				try:F=await B.message.reply_video(video=J,caption=H,reply_markup=P,quote=G)
				except A:
					try:F=await B.message.reply_video(video=J,caption=H,quote=G)
					except A:
						try:F=await B.message.reply_video(video=J,quote=G)
						except A:
							try:F=await B.message.reply_photo(photo=O,caption=H,reply_markup=P,quote=G)
							except A:
								try:F=await B.message.reply_photo(photo=O,caption=H,quote=G)
								except A:
									try:F=await B.message.reply_photo(photo=O,quote=G)
									except A:
										try:F=await B.message.reply_text(H,reply_markup=P,quote=G)
										except A:F=await B.message.reply_text(H,quote=G)
				U-=1;await p(h*W);T=F.message_id
				try:await I.bot.delete_message(f,T)
				except:pass
			else:break
		if C[D][d]==g:await B.message.reply_text(f"{X} : message has been send");Q=[[L(Z,a)]];S=R(Q);await B.message.reply_text(m,reply_markup=S)
	else:Q=[[L(Z,a)]];S=R(Q);await B.message.reply_text(m,reply_markup=S)
async def AU(update,context):
	h='-100';H=update;B=context;Y=H.message.from_user;T=None;j=e(H.message.chat_id);M.info(A9,Y.first_name);await H.message.reply_text(i)
	if E(H.effective_user.id)==E(N):
		F=B.args[0]
		if-100 or h in B.args[2]:D=B.args[2]
		else:D=h+E(B.args[2])
		f=Ad(B.args[1])
		try:J=C[F][c]
		except A:
			try:O=C[F][b]
			except A:pass
		try:I=C[F][V]
		except A:pass
		try:P=C[F][K]
		except A:pass
		C[F][d]=g;U=X;await H.message.reply_text(f"stop by /stop {F}")
		while C[F][d]==g and U>0:
			if E(H.effective_user.id)==E(N):
				try:G=await B.bot.send_video(chat_id=D,video=J,caption=I,reply_markup=P)
				except A:
					try:G=await B.bot.send_video(chat_id=D,video=J,caption=I)
					except A:
						try:G=await B.bot.send_video(chat_id=D,video=J)
						except A:
							try:G=await B.bot.send_photo(chat_id=D,photo=O,caption=I,reply_markup=P)
							except A:
								try:G=await B.bot.send_photo(chat_id=D,photo=O,caption=I)
								except A:
									try:G=await B.bot.send_photo(chat_id=D,photo=O)
									except A:
										try:G=await B.bot.send_message(chat_id=D,text=I,reply_markup=P)
										except A:G=await B.bot.send_message(chat_id=D,text=I)
				U-=1;await p(f*W);T=G.message_id
				try:await B.bot.delete_message(D,T)
				except:pass
			else:break
		if C[F][d]==g:await B.bot.send_message(f"{X} : message has been send");Q=[[L(Z,a)]];S=R(Q);await B.bot.send_message(chat_id=D,text=m,reply_markup=S)
	else:Q=[[L(Z,a)]];S=R(Q);await H.message.reply_text(m,reply_markup=S)
async def AV(update,context):
	P=context;B=update;Q=B.message.from_user;M.info(A9,Q.first_name);await B.message.reply_text(i)
	if E(B.effective_user.id)==E(N):
		F=P.args[0];H=E(P.args[1])
		try:H=e(H)*60
		except A:await B.message.reply_text('enter time un minutes 60 90 120')
		try:I=C[F][c]
		except A:
			try:J=C[F][b]
			except A:pass
		try:D=C[F][V]
		except A:pass
		try:O=C[F][K]
		except A:pass
		await B.message.reply_text(f"post will be send ater {H/60} minutes");await p(H)
		if E(B.effective_user.id)==E(N):
			try:await B.message.reply_video(video=I,caption=D,reply_markup=O,quote=G)
			except A:
				try:await B.message.reply_video(video=I,caption=D,quote=G)
				except A:
					try:await B.message.reply_video(video=I,quote=G)
					except A:
						try:await B.message.reply_photo(photo=J,caption=D,reply_markup=O,quote=G)
						except A:
							try:await B.message.reply_photo(photo=J,caption=D,quote=G)
							except A:
								try:await B.message.reply_photo(photo=J,quote=G)
								except A:
									try:await B.message.reply_text(D,reply_markup=O,quote=G)
									except A:await B.message.reply_text(D,quote=G)
	else:S=[[L(Z,a)]];T=R(S);await B.message.reply_text(m,reply_markup=T)
async def AW(update,context):
	B=update;D=B.message.from_user;M.info('User %s stopped the post.',D.first_name);await B.message.reply_text(i)
	if E(B.effective_user.id)==E(N):
		try:F=context.args[0];C[F][d]='false';await B.message.reply_text('stopped')
		except A:await B.message.reply_text('post stopped')
async def AX(update,context):A=update;B=A.message.from_user;M.info('User %s pressed post setting.',B.first_name);await A.message.reply_text('ENTER THE NUMBER OF POST YOU WANT IN A LOOP\n\nthis will only change for /send command \n press /cancel if you dont want to change it.');return y
async def AY(update,context):
	B=update;A=B.message.text;global X
	try:A=e(A)
	except:pass
	if Ae(A,e):X=e(A);C=[[O,P],[Q,Y],[T]];D=I(C);await B.message.reply_text(f"Post count Changed to : {E(A)}",reply_markup=I(C,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder=n));return J.END
	else:await B.message.reply_text('enter digits only')
async def AZ(update,context):A=update;B=A.message.from_user;M.info('User %s pressed time.',B.first_name);await A.message.reply_text('ENTER THE TIME FORMAT Hours, Minutes, Seconds \n\nthis will only change for /send command \n press /cancel if you dont want to change it.');return z
async def Aa(update,context):
	G='enter one of these option\n Hours, Minutes, Seconds only';B=update;C=B.message.text.lower();global W
	if Ae(C,E):
		if C[0]=='h':W=3600;A=[[O,P],[Q,Y],[T]];D=I(A);await B.message.reply_text('Time Format Changed TO Hours',reply_markup=I(A,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder=n));return J.END
		elif C[0]=='m':W=60;A=[[O,P],[Q,Y],[T]];D=I(A);await B.message.reply_text('Time Format Changed TO Minutes',reply_markup=I(A,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder=n));return J.END
		elif C[0]=='s':W=1;A=[[O,P],[Q,Y],[T]];D=I(A);await B.message.reply_text('Time Format Changed TO SEC',reply_markup=I(A,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder=n));return J.END
		else:await B.message.reply_text(G)
	else:await B.message.reply_text(G)
async def An(update,context):await update.message.reply_text('Seting Saved');return J.END
async def Ab(update,context):A=update;C=A.message.from_user;M.info('User %s pressed setting.',C.first_name);B=[['Post Count','Time Setting']];D=I(B);await A.message.reply_text('Settings for Bot!',reply_markup=I(B,resize_keyboard=F,one_time_keyboard=F,input_field_placeholder=n));return x
def Ac():O='^(✅Done)$';I='^(📌 make new post)$';F='done';E='skip';C='cancel';A=AA.builder().token(AD).build();A.add_handler(H('start',AE));A.add_handler(H('send',AT,block=G));A.add_handler(H('sendch',AU,block=G));A.add_handler(H('stop',AW));A.add_handler(H('rk',AS));A.add_handler(H('time',AV));A.add_handler(D(B.Regex('^(🤖 Buy bot)$'),AH));K=J(entry_points=[D(B.Regex('^(Setting)$'),Ab)],states={x:[D(B.Regex('^(Post Count)$')&~ B.COMMAND,AX),D(B.Regex('^(Time Setting)$')&~ B.COMMAND,AZ)],y:[D(B.TEXT&~ B.COMMAND,AY)],z:[D(B.TEXT&~ B.COMMAND,Aa)]},fallbacks=[H(C,j)]);L=J(entry_points=[D(B.Regex('^(Search Old Post)$'),AF)],states={A0:[D(B.TEXT&~ B.COMMAND,AG)]},fallbacks=[H(C,j)]);M=J(entry_points=[D(B.Regex('^(📌 make new post|Post)$'),AI)],states={h:[D(B.PHOTO&~ B.COMMAND,AK),H(E,A3),D(B.VIDEO&~ B.COMMAND,AL),D(B.ALL&~ B.COMMAND,k)],S:[D(B.Regex(I)&~ B.COMMAND,k),D(B.TEXT&~ B.COMMAND,AO),H(E,A4)],U:[D(B.Regex(I)&~ B.COMMAND,k),D(B.Regex(O),s),D(B.TEXT&~ B.COMMAND,A5),H(F,s)],q:[D(B.Regex(I)&~ B.COMMAND,k),D(B.TEXT&~ B.COMMAND,AQ),H(F,s)]},fallbacks=[H(C,j)]);N=J(entry_points=[D(B.Regex('^(📝 edit post|edit post)$'),AJ)],states={w:[D(B.TEXT&~ B.COMMAND,AN)],h:[D(B.TEXT&~ B.COMMAND,A2),D(B.PHOTO&~ B.COMMAND,A2),D(B.VIDEO&~ B.COMMAND,AM),H(E,A3)],S:[D(B.TEXT&~ B.COMMAND,AP),H(E,A4)],U:[D(B.Regex(O),t),D(B.TEXT&~ B.COMMAND,A5),H(F,t)],q:[D(B.TEXT&~ B.COMMAND,AR),H(F,t)]},fallbacks=[H(C,j)]);A.add_handler(M);A.add_handler(K);A.add_handler(N);A.add_handler(L);A.run_polling()
if __name__=='__main__':Ac()
