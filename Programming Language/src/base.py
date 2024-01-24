import random
from colorama import Fore

def fill_terminal(version):
    rand_color_num = random.randrange(0, 3)
    if rand_color_num == 0:
        print(Fore.BLUE + f"""

                ;:                
               ,KK:               
    ,NX        :KKl        0N:    
    ,KKXO      ;KKc      xXKK;    
    ,Kd.KN     .KK,     NK'lK;    
    ,Kx 'K0    .KK.    kK; oK;    
    ,Kx  kK'    KK.   .KO  oK;    
    ,Kx  cKl    KK    :Ko  oK;    БАЗА    
    ,Kx  'Kk   .KK.   xK,  oK;    Версія: {version}
    ,Kx   KK   lKKo   0K   oK;    Девіз: Якщо код не
    ,Kx ;NKK. .XKKK. .KKNc oK;    базований, то він не працює
    ,KXWKO    KK'.KX    kKWXK;    
    ,Kd OKd  KK,  'KN  cKK lK;    
    ,Kx   KXXKKN,'WKKXXK   oK;    
    ,Kx    lKc :KKc :Ko    oK;    
    ,KXWWWWXKXWNKKNWNKXWWWWXK;    
           .Kx  KK  oK,           
            cKk KK dKo            
             ,KNKKNK:             
               ,KK;      

                               """)

    elif rand_color_num == 1:
        print(Fore.YELLOW + f"""

                ;:                
               ,KK:               
    ,NX        :KKl        0N:    
    ,KKXO      ;KKc      xXKK;    
    ,Kd.KN     .KK,     NK'lK;    
    ,Kx 'K0    .KK.    kK; oK;    
    ,Kx  kK'    KK.   .KO  oK;    
    ,Kx  cKl    KK    :Ko  oK;    БАЗА    
    ,Kx  'Kk   .KK.   xK,  oK;    Версія: {version}
    ,Kx   KK   lKKo   0K   oK;    Девіз: Без зради не
    ,Kx ;NKK. .XKKK. .KKNc oK;    обходиться жодна перемога
    ,KXWKO    KK'.KX    kKWXK;    
    ,Kd OKd  KK,  'KN  cKK lK;    
    ,Kx   KXXKKN,'WKKXXK   oK;    
    ,Kx    lKc :KKc :Ko    oK;    
    ,KXWWWWXKXWNKKNWNKXWWWWXK;    
           .Kx  KK  oK,           
            cKk KK dKo            
             ,KNKKNK:             
               ,KK;      

                               """)

    elif rand_color_num == 2:
        print(Fore.RED + f"""

                ;:                
               ,KK:               
    ,NX        :KKl        0N:    
    ,KKXO      ;KKc      xXKK;    
    ,Kd.KN     .KK,     NK'lK;    
    ,Kx 'K0    .KK.    kK; oK;    
    ,Kx  kK'    KK.   .KO  oK;    
    ,Kx  cKl    KK    :Ko  oK;    БАЗА    
    ,Kx  'Kk   .KK.   xK,  oK;    Версія: {version}
    ,Kx   KK   lKKo   0K   oK;    Девіз: Коли пишете на Based - думай...те
    ,Kx ;NKK. .XKKK. .KKNc oK;    
    ,KXWKO    KK'.KX    kKWXK;    
    ,Kd OKd  KK,  'KN  cKK lK;    
    ,Kx   KXXKKN,'WKKXXK   oK;    
    ,Kx    lKc :KKc :Ko    oK;    
    ,KXWWWWXKXWNKKNWNKXWWWWXK;    
           .Kx  KK  oK,           
            cKk KK dKo            
             ,KNKKNK:             
               ,KK;      

                               """)

    elif rand_color_num == 3:
        print(Fore.BLACK + f"""

                ;:                
               ,KK:               
    ,NX        :KKl        0N:    
    ,KKXO      ;KKc      xXKK;    
    ,Kd.KN     .KK,     NK'lK;    
    ,Kx 'K0    .KK.    kK; oK;    
    ,Kx  kK'    KK.   .KO  oK;    
    ,Kx  cKl    KK    :Ko  oK;    БАЗА    
    ,Kx  'Kk   .KK.   xK,  oK;    Версія: {version}
    ,Kx   KK   lKKo   0K   oK;    Девіз: Або пиши код,
    ,Kx ;NKK. .XKKK. .KKNc oK;    або вийди звідси, розбійник
    ,KXWKO    KK'.KX    kKWXK;    
    ,Kd OKd  KK,  'KN  cKK lK;    
    ,Kx   KXXKKN,'WKKXXK   oK;    
    ,Kx    lKc :KKc :Ko    oK;    
    ,KXWWWWXKXWNKKNWNKXWWWWXK;    
           .Kx  KK  oK,           
            cKk KK dKo            
             ,KNKKNK:             
               ,KK;      

                               """)

    print(Fore.WHITE)