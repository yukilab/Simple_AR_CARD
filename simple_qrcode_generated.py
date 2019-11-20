import qrcode

img = qrcode.make('https://villager-b.github.io/Simple_AR_card/')
img.save('img/simple_qrcode.png')
