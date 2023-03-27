# thu vien pygame
import pygame
pygame.init()
import time
mucamthanh = 0.5
# am thanh dan
pygame.mixer.init()
amthanh_dan = pygame.mixer.Sound("sound_dan/mixkit-electronic-retro-block-hit-2185.wav")
amthanh_dan.set_volume(mucamthanh)
luachon_nhac_dan = 1
# amthanh nhac nen
luachon_nhacnen_2 = "y2mate.com - Game Show Tension Bed Music  Jon Brooks.mp3"
luachon_nhacnen_1 = "y2mate.com - Nhạc Stream Của Độ Mixi 2 Mixigaming.mp3"
amthanh_nen = pygame.mixer.Sound("sound_nen/"+luachon_nhacnen_1)
amthanh_nen.set_volume(mucamthanh)
amthanh_nen.play()
laplainhacnen = time.time()
laplainhacnen_ = 0
tg_nhacnen = 0
tg_nhacnen_1 = 331
tg_nhacnen_2 = 59
khungchonnhac = False



# random
import random
# font chu
pygame.font.init()
fornt = pygame.font.SysFont(None,30)
# mau
black = (0,0,0)
While = (255,255,255)
black__ = (65,63,63)
black_ = (80,80,80)

# setting nhan vat
    # toa do
tocdo_x = 0
tocdo_y = 0
nhanvat_x = 250
nhanvat_y = 500
nhip = 2
    # do hoa
img_nhanvat = "img_nhanvat/125-1256363_post-anime-girl-icon-transparent-hd-png-download.webp"
img_nhanvat = pygame.image.load(img_nhanvat)
img_nhanvat = pygame.transform.scale(img_nhanvat,(50,50))

# thiet lap man hinh
display = pygame.display.set_mode((800,650))
pygame.display.set_caption("game_gủng")
pygame.display.set_icon(img_nhanvat)

# setting dan
x_dan = [0,0,0,0,0,0,0,0,0,0,0,0]
y_dan = [0,0,0,0,0,0,0,0,0,0,0,0]
tgian_dan = 0
tocdodan = 400
# setting vien dan
img_dan = "img_dan/imgbin-computer-icons-bullet-weapon-weapon-5AkcNgSmsYXRtJw3aQctfhezy.jpg"
img_dan = pygame.image.load(img_dan)
img_dan = pygame.transform.scale(img_dan,(10,20))
# setting quai
x_quai = [0]
y_quai = [0]
img_quai_list = ["img_quai/248Tyranitar.png",
            "img_quai/20130825150619382Kyogre-1.png",
            "img_quai/20140928144641383Groudon.png",
            "img_quai/20190405165040076Golem.png",
            "img_quai/20190720220955644Zekrom.png",
            "img_quai/20191217175504888Zacian-Hero.png",
            "img_quai/20200221165316890Eternatus.png",
            "img_quai/dialga.png",
            "img_quai/giratina.png",
            "img_quai/ho-oh.png",
            "img_quai/kyurem.png",
            "img_quai/OIP.png",
            "img_quai/palkia-good.png",
            "img_quai/screen-shot-2020-12-23-at-12-16-20-pm.png",
            "img_quai/screen-shot-2020-12-23-at-12-18-36-pm.png",
            "img_quai/screen-shot-2020-12-23-at-12-19-55-pm.png",
            "img_quai/screen-shot-2020-12-23-at-12-20-39-pm.png"]
# setting dan quai
tgiandan_quai = 0
tocdodan_quai = 1000
tgian_spoi_dan0_quai = 0.5
tgian_roi_dan_quai = 0.2
x_dan_quai = [0,0,0,0,0]
y_dan_quai = [650,650,650,650,650]
img_dan_quai = "img_dan/imgbin-computer-icons-bullet-weapon-weapon-5AkcNgSmsYXRtJw3aQctfhezy.jpg"
img_dan_quai = pygame.image.load(img_dan_quai)
img_dan_quai = pygame.transform.scale(img_dan_quai,(20,30))
random_quai = [random.randint(0,490)]

# setting game
    # leve game 
leve = 0
tiep_leve = False
chuyen_quai = 0
tg_chuyen_quai = 1000
vitri_leve_text = 100
doimau = True
# menu game
    # dieu kien chay game
chienthang = False
batdau = False
thoat = False
thua = False
choilai = False
menu = True
# spoide quai random
img_quai = pygame.image.load(img_quai_list[0])
img_quai = pygame.transform.scale(img_quai,(50,50))
img_quai_1 = pygame.image.load(img_quai_list[1])
img_quai_1 = pygame.transform.scale(img_quai_1,(50,50))
img_quai_2 = pygame.image.load(img_quai_list[2])
img_quai_2 = pygame.transform.scale(img_quai_2,(50,50))
img_quai_3 = pygame.image.load(img_quai_list[3])
img_quai_3 = pygame.transform.scale(img_quai_3,(50,50))
img_quai_4 = pygame.image.load(img_quai_list[4])
img_quai_4 = pygame.transform.scale(img_quai_4,(50,50))
img_quai_5 = pygame.image.load(img_quai_list[5])
img_quai_5 = pygame.transform.scale(img_quai_5,(50,50))
img_quai_6 = pygame.image.load(img_quai_list[6])
img_quai_6 = pygame.transform.scale(img_quai_6,(50,50))
img_quai_7 = pygame.image.load(img_quai_list[7])
img_quai_7 = pygame.transform.scale(img_quai_7,(50,50))
img_quai_8 = pygame.image.load(img_quai_list[8])
img_quai_8 = pygame.transform.scale(img_quai_8,(50,50))
img_quai_9 = pygame.image.load(img_quai_list[9])
img_quai_9 = pygame.transform.scale(img_quai_9,(50,50))
img_quai_10 = pygame.image.load(img_quai_list[10])
img_quai_10 = pygame.transform.scale(img_quai_10,(50,50))
img_quai_11 = pygame.image.load(img_quai_list[11])
img_quai_11 = pygame.transform.scale(img_quai_11,(50,50))
img_quai_12 = pygame.image.load(img_quai_list[12])
img_quai_12 = pygame.transform.scale(img_quai_12,(50,50))
img_quai_13 = pygame.image.load(img_quai_list[13])
img_quai_13 = pygame.transform.scale(img_quai_13,(50,50))
img_quai_14 = pygame.image.load(img_quai_list[14])
img_quai_14 = pygame.transform.scale(img_quai_14,(50,50))
img_quai_15 = pygame.image.load(img_quai_list[15])
img_quai_15 = pygame.transform.scale(img_quai_15,(50,50))
img_quai_16 = pygame.image.load(img_quai_list[16])
img_quai_16 = pygame.transform.scale(img_quai_16,(50,50))
a = random.randrange(0,1)
b = random.randrange(100,1000)

u = [img_quai,
     img_quai_1,
     img_quai_2,
     img_quai_3,
     img_quai_4,
     img_quai_5,
     img_quai_6,
     img_quai_7,
     img_quai_8,
     img_quai_9,
     img_quai_10,
     img_quai_11,
     img_quai_12,
     img_quai_13,
     img_quai_14,
     img_quai_15,
     img_quai_16]
# vonh lap ve game
while thoat==False:
    if menu==True and batdau==False and chienthang == False and thoat == False and thua == False and khungchonnhac==False:
        display.fill(black)
        a = pygame.draw.rect(display,While,(200,200,120,50))
        c = pygame.draw.rect(display,While,(200,260,120,50))
        b = pygame.draw.rect(display,While,(200,320,120,50))
        win_text = fornt.render("MENU",True,While)
        muc_1 = fornt.render("New game",True,black)
        muc_2 = fornt.render("Sound",True,black)
        muc_3 = fornt.render("Quit",True,black)
        khung_text = win_text.get_rect()
        khung_muc_1 = muc_1.get_rect()
        khung_muc_2 = muc_2.get_rect()
        khung_muc_3 = muc_3.get_rect()
        khung_text.topleft = (200,200)
        khung_muc_1.topleft = (210,210)
        khung_muc_2.topleft = (210,330)
        khung_muc_3.topleft = (210,270)
        display.blit(win_text,khung_text)
        display.blit(muc_1,khung_muc_1)
        display.blit(muc_2,khung_muc_2)
        display.blit(muc_3,khung_muc_3)
        for ev in pygame.event.get():
            if ev.type==pygame.MOUSEBUTTONUP:
                if a.collidepoint(ev.pos):
                    batdau=True
                elif c.collidepoint(ev.pos):
                    thoat=True
                elif b.collidepoint(ev.pos):
                    khungchonnhac = True
            elif ev.type==pygame.QUIT:
                    thoat=True
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_j:
                    mucamthanh-=0.05
                    amthanh_dan.set_volume(mucamthanh)
                    amthanh_nen.set_volume(mucamthanh)
                elif ev.key == pygame.K_k:
                    mucamthanh+=0.05
                    amthanh_dan.set_volume(mucamthanh)
                    amthanh_nen.set_volume(mucamthanh)
    elif menu==True and batdau==False and chienthang == False and thoat == False and thua == False and khungchonnhac == True:
            display.fill(black)
            a = pygame.draw.rect(display,While,(200,260,120,50))
            c = pygame.draw.rect(display,While,(200,320,120,50))
            win_text = fornt.render("Sound setting",True,While)
            muc_1 = fornt.render("Chill",True,black)
            muc_3 = fornt.render("Not chill",True,black)
            khung_text = win_text.get_rect()
            khung_muc_1 = muc_1.get_rect()
            khung_muc_3 = muc_3.get_rect()
            khung_text.topleft = (210,200)
            khung_muc_1.topleft = (210,270)
            khung_muc_3.topleft = (210,330)
            display.blit(win_text,khung_text)
            display.blit(muc_1,khung_muc_1)
            display.blit(muc_3,khung_muc_3)
            for ev in pygame.event.get():
                if ev.type==pygame.MOUSEBUTTONUP:
                    if a.collidepoint(ev.pos):
                        amthanh_nen.stop()
                        amthanh_nen = pygame.mixer.Sound("sound_nen/"+luachon_nhacnen_1)
                        amthanh_nen.set_volume(mucamthanh)
                        amthanh_nen.play()
                        luachon_nhac_dan = 1
                        khungchonnhac = False
                    elif c.collidepoint(ev.pos):
                        amthanh_nen.stop()
                        amthanh_nen = pygame.mixer.Sound("sound_nen/"+luachon_nhacnen_2)
                        amthanh_nen.set_volume(mucamthanh)
                        amthanh_nen.play()
                        luachon_nhac_dan=0
                        khungchonnhac = False
                elif ev.type==pygame.QUIT:
                        thoat=True
                elif ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_j:
                        mucamthanh-=0.05
                        amthanh_dan.set_volume(mucamthanh)
                        amthanh_nen.set_volume(mucamthanh)
                    elif ev.key == pygame.K_k:
                        mucamthanh+=0.05
                        amthanh_dan.set_volume(mucamthanh)
                        amthanh_nen.set_volume(mucamthanh)
    elif menu==True and batdau==True and chienthang == False and thoat == False and thua == False:
    # ve man hinh
        if tiep_leve!=True:
            # tat am thanh tiep leve
            display.fill(black)
            # bat su kien game
            for ev in pygame.event.get():
            # nhan phim di chuyen
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_s:
                        tocdo_y = 1
                    if ev.key == pygame.K_w:
                        tocdo_y = -1
                    if ev.key == pygame.K_d:
                        tocdo_x = 1
                    if ev.key == pygame.K_a:
                        tocdo_x = -1
                    if ev.key == pygame.K_j:
                        mucamthanh-=0.05
                        amthanh_dan.set_volume(mucamthanh)
                        amthanh_nen.set_volume(mucamthanh)
                    if ev.key == pygame.K_k:
                        mucamthanh+=0.05
                        amthanh_dan.set_volume(mucamthanh)
                        amthanh_nen.set_volume(mucamthanh)
                # khong nhan phim di chuyen
                elif ev.type == pygame.KEYUP:
                    tocdo_x = 0
                    tocdo_y = 0
                # thoat game
                elif ev.type == pygame.QUIT:
                    thoat=True
        # thoi gian spoide dan
            tgian_dan+=1
            if tgian_dan ==tocdodan:
                if luachon_nhac_dan == 0:
                    amthanh_dan.play()
                for i in range(12):
                    if y_dan[i]==0:
                        x_dan[i] = nhanvat_x+20
                        y_dan[i] = nhanvat_y-20
                        break
                tgian_dan = 0
        # duong di vien dan
            for i in range(12):
                if y_dan[i] ==0:
                    x_dan[i]=0
                    y_dan[i]=0
                else:
                    y_dan[i]-=1
        # duong di nhan vat
            if nhanvat_x < 1:
                nhanvat_x = 790
            if nhanvat_x > 790:
                nhanvat_x = 1
            if nhanvat_y > 600:
                nhanvat_y=600
            nhanvat_x +=tocdo_x
        # giat giat
            if nhip==-2:
                nhip=2
            elif nhip==2:
                nhip=-2
            y_quai[0] +=nhip
            nhanvat_y +=tocdo_y+nhip
            y_quai[0]+=0.02
        # duong di cua quai va auto tranh dan
            for i in range(12):
                if x_quai[0]>x_dan[i]:
                    if x_quai[0]-300<x_dan[i]:
                        x_quai[0]+=0.3
                        break
                    else:
                        x_quai[0]-=0.3
                        break
                elif x_quai[0]+50<x_dan[i]:
                    if x_quai[0]+50+300>x_dan[i]:
                        x_quai[0]-=0.3
                        break
                    else:
                        x_quai[0]+=0.3
                        break
            # res khi quai cham man hinh
            if x_quai[0]>680:
                x_quai[0]=0
            
            if x_quai[0]<0:
                x_quai[0]=680
            # thoi gian spoide dan cua quai
            tgiandan_quai+=tgian_spoi_dan0_quai
            if tgiandan_quai > tocdodan_quai:
                for i in range(5):
                    if y_dan_quai[i]==650:
                        x_dan_quai[i] = x_quai[0]+10
                        y_dan_quai[i] = y_quai[0]+50
                        break
                tgiandan_quai = 0
            # duong di vien dan cua quai va tu dong nham
            for i in range(5):
                if y_dan_quai[i]>=650:
                    x_dan_quai[i]=650
                    y_dan_quai[i]=650
                else:
                    y_dan_quai[i]+=tgian_roi_dan_quai
            for i in range(5):
                if x_dan_quai[i]<nhanvat_x:
                    x_dan_quai[i]+=leve/20
                elif x_dan_quai[i]>nhanvat_x:
                    x_dan_quai[i]-=leve/20
            # ve quai
            display.blit(u[leve],(x_quai[0],y_quai[0]))
            # ve nhan vat
            display.blit(img_nhanvat,(nhanvat_x,nhanvat_y))
            # dieu kien quai chet
            for i in range(10):
                if x_dan[i]>x_quai[0] and x_dan[i]<=x_quai[0]+50 :
                    if y_dan[i] < y_quai[0]+50 and y_dan[i]>y_quai[0]:
                            x_quai[0] = random.randint(0,780)
                            y_quai[0]=0
                            tocdodan_quai-=100
                            tgian_dan=0
                            tocdodan-=20
                            y_dan = [0,0,0,0,0,0,0,0,0,0,0,0]
                            x_dan = [0,0,0,0,0,0,0,0,0,0,0,0]
                            x_dan_quai = [0,0,0,0,0]
                            y_dan_quai = [650,650,650,650,650]
                            tgian_roi_dan_quai+=0.1
                            tgian_spoi_dan0_quai+=0.1
                            leve+=1
                            pygame.time.delay(500)
                            bienbatnhac_tiepleve = True
                            tiep_leve = True
            #dieu kien chien thang
            if leve==17:
                chienthang=True
            #dieu kien minh chet
            for i in range(5):
                if x_dan_quai[i]>nhanvat_x and x_dan_quai[i]<=nhanvat_x+50 :
                    if y_dan_quai[i]+30 >= nhanvat_y and y_dan_quai[i]+30<nhanvat_y+50:
                            thua= True
                elif x_dan_quai[i]+20>nhanvat_x and x_dan_quai[i]<=nhanvat_x+50:
                    if y_dan_quai[i]+30 >= nhanvat_y and y_dan_quai[i]+30<nhanvat_y+50:
                            thua = True
            if x_quai[0]>nhanvat_x and x_quai[0]<=nhanvat_x+50 :
                    if y_quai[0]+50 >= nhanvat_y and y_quai[0]+50<nhanvat_y+50:
                            thua= True
            elif x_quai[0]+50>nhanvat_x and x_quai[0]<=nhanvat_x+50:
                    if y_quai[0]+50 >= nhanvat_y and y_quai[0]+50<nhanvat_y+50:
                            thua= True
            elif y_quai[0]+50>650:
                 thua=True
            # ve vien dan  
            for i in range(12):
                if y_dan[i]!=0:   
                    display.blit(img_dan,(x_dan[i],y_dan[i]))
                    
            # ve vien dan quai  
            for i in range(5):
                if y_dan_quai[i]!=650:   
                    display.blit(img_dan_quai,(x_dan_quai[i],y_dan_quai[i]))
                    
            
        else :
            if doimau==True:
                display.fill(black)
                win_text = fornt.render("Next leve",True,While)
                leve_text = "Leve - "+str(leve)+" - "+" ==> "+str(leve+1)
                muc_1 = fornt.render(leve_text,True,While)
                khung_text = win_text.get_rect()
                khung_muc_1 = muc_1.get_rect()
                khung_text.topleft = (vitri_leve_text,203)
                khung_muc_1.topleft = (vitri_leve_text,253)
                display.blit(win_text,khung_text)
                display.blit(muc_1,khung_muc_1)
                vitri_leve_text+=0.3
                doimau=False
            else:
                display.fill(black__)
                win_text = fornt.render("Next leve",True,While)
                leve_text = "Leve - "+str(leve)+" - "+" ==> "+str(leve+1)
                muc_1 = fornt.render(leve_text,True,While)
                khung_text = win_text.get_rect()
                khung_muc_1 = muc_1.get_rect()
                khung_text.topleft = (vitri_leve_text,200)
                khung_muc_1.topleft = (vitri_leve_text,250)
                display.blit(win_text,khung_text)
                display.blit(muc_1,khung_muc_1)
                vitri_leve_text+=0.3
                doimau = True
            if chuyen_quai==tg_chuyen_quai:
                 chuyen_quai=0
                 vitri_leve_text=100
                 tiep_leve=False
            else:
                 chuyen_quai+=0.5       
    elif menu==True and batdau==True and chienthang == False and thoat == False and thua == True:
        display.fill(black)
        a = pygame.draw.rect(display,While,(200,200,120,50))
        c = pygame.draw.rect(display,While,(200,260,120,50))
        win_text = fornt.render("MENU",True,While)
        muc_1 = fornt.render("play again",True,black)
        muc_3 = fornt.render("Quit",True,black)
        khung_text = win_text.get_rect()
        khung_muc_1 = muc_1.get_rect()
        khung_muc_3 = muc_3.get_rect()
        khung_text.topleft = (200,200)
        khung_muc_1.topleft = (210,210)
        khung_muc_3.topleft = (210,270)
        display.blit(win_text,khung_text)
        display.blit(muc_1,khung_muc_1)
        display.blit(muc_3,khung_muc_3)
        for ev in pygame.event.get():
            if ev.type==pygame.MOUSEBUTTONUP:
                if a.collidepoint(ev.pos):
                    thua = False
                    leve=0
                    x_quai[0] = random.randint(1,680)
                    y_quai[0] = 0
                    x_dan = [0,0,0,0,0,0,0,0,0,0,0,0]
                    x_dan_quai=[0,0,0,0,0]
                    tgiandan_quai = 0
                    tocdodan_quai = 1000
                    tgian_spoi_dan0_quai = 0.5
                    tgian_roi_dan_quai = 0.2
                    nhanvat_x = random.randint(1,750)
                    nhanvat_y = 600
                    tocdodan = 400
                    tocdo_x = 0
                    tocdo_y = 0
                    y_dan_quai=[650,650,650,650,650]
                    y_dan = [0,0,0,0,0,0,0,0,0,0,0,0]
                    break
                elif c.collidepoint(ev.pos):
                    thoat=True
            elif ev.type==pygame.QUIT:
                    thoat=True
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_j:
                    mucamthanh-=0.05
                    amthanh_dan.set_volume(mucamthanh)
                    amthanh_nen.set_volume(mucamthanh)
                elif ev.key == pygame.K_k:
                    mucamthanh+=0.05
                    amthanh_dan.set_volume(mucamthanh)
                    amthanh_nen.set_volume(mucamthanh)
    elif menu==True and batdau==True and chienthang == True and thoat == False and thua == False:
        display.fill(black__)
        win_text = fornt.render("You won the game",True,While)
        leve_text = "And now press x to exit"
        muc_1 = fornt.render(leve_text,True,While)
        khung_text = win_text.get_rect()
        khung_muc_1 = muc_1.get_rect()
        khung_text.topleft = (350,200)
        khung_muc_1.topleft = (350,250)
        display.blit(win_text,khung_text)
        display.blit(muc_1,khung_muc_1)
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_j:
                        mucamthanh-=0.05
                        amthanh_dan.set_volume(mucamthanh)
                        amthanh_nen.set_volume(mucamthanh)
                    elif ev.key == pygame.K_k:
                        mucamthanh+=0.05
                        amthanh_dan.set_volume(mucamthanh)
                        amthanh_nen.set_volume(mucamthanh)
            elif ev.type == pygame.QUIT:
                thoat=True
    laplainhacnen_ = time.time()
    # lap lai nhac nen
    if luachon_nhac_dan==1:
        if laplainhacnen_ - laplainhacnen > tg_nhacnen_1:
            amthanh_nen.stop()
            amthanh_nen.play()
            laplainhacnen = time.time()
    else:
        if laplainhacnen_ - laplainhacnen > tg_nhacnen_2:
            amthanh_nen.stop()
            amthanh_nen.play()  
            laplainhacnen = time.time()
    time.sleep(0.000001)
    pygame.display.update()