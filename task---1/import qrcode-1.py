import qrcode

myqr = qrcode.make("https://youtu.be/IUQVO97zcE0?si=oIvJXJCi12U75MOO")
myqr.save("myqr.png",scale=8)


