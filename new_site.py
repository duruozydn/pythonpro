from flask import Flask
import random 

app = Flask(__name__)

@app.route("/")
def gercekler():
    return f' <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle!</a>'

@app.route("/rastgele_gercekler")
def gercekler():
   facts=['Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.','2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50 den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.','Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.','2019 da yapılan bir araştırmaya göre, insanların %60 ından fazlası akıllı telefonlarındaki iş mesajlarına işten ayrıldıktan sonraki 15 dakika içinde yanıt veriyor.','Teknolojik bağımlılıkla mücadele etmenin bir yolu, zevk veren ve ruh halini iyileştiren faaliyetler aramaktır.','Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.','Elon Musk ayrıca sosyal ağların düzenlenmesini ve kullanıcıların kişisel verilerinin korunmasını savunmaktadır. Sosyal ağların hakkımızda büyük miktarda bilgi topladığını ve bu bilgilerin daha sonra düşüncelerimizi ve davranışlarımızı manipüle etmek için kullanılabileceğini iddia ediyor.','Sosyal ağların olumlu ve olumsuz yanları vardır ve bu platformları kullanırken her ikisinin de farkında olmalıyız.']
   return f'<p>{random.choice(facts)}</p>'


karakterler=['akjdhwıuawgdıugawdıagdwıu']

@app.route("/rastgele_gercekler")
def sifre():
    return f'<p>{random.choice(karakterler)}</p>'

