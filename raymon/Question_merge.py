#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#'دمای هوا در زمان اذان صبح امروز تهران چقدر است',#1       
Question_weather=['دمای هوای تهران امروز ',#1
                  'دمای هوای فردای شیراز ساعت ۱۴:۲۵ ',
                  'دمای هوا در زمان اذان صبح امروز تهران',#1
                  'دمای هوای دو روز بعد گرگان چند درجه سانتیگراد است؟',
                  'درجه دمای هوای ۳ روز دیگر رم ساعت ۱۶:۱۰ چند درجه است؟',
                  'گرمی هوای فردای تهران ساعت ۱۹:۱ چقدر است؟ ','درجه حرارت هوای دو روز بعد پکن ساعت ۲۰:۱۰ به چه میزان است؟',#1
                  'میانگین دمای هوای تهران امروز چقدر است؟', 'میانگین اندازه گرمی یا سردی هوای دو روز بعد کاشان چند درجه است؟',#2
                  'امروز حداقل دمای هوای مشهد سردتر است یا تهران؟',#3
                  'اذان صبح تهران سردتر است یا اذان ظهر آن؟']#4        
            #.............................................................#
Question_Re = ['اذان صبح امروز تهران چه ساعتی است؟ ','اذان ظهر فردای تهران چه ساعتی است؟ ', #1
      'اذان ظهر دیروز تهران چه ساعتی بود؟', 'اذان مغرب دیروز قم چه ساعتی بود؟', 
      'اذان ظهر پس فردای تهران چه ساعتی است؟','نیمه شب شرعی تهران چه ساعتی است؟ ',
      'اذان صبح مسکو چه ساعتی است؟ ','طلوع آفتاب مسکو چه ساعتی است؟', 
      'غروب آفتاب مشهد چه ساعتی است؟ ','غروب آفتاب کابل چه ساعتی است؟',
      'اذان ظهر بیروت چه زمانی است؟ ', 'اذان ظهر فردای تورنتو چه زمانی است؟'
      'اذان مغرب پریروز قم چه ساعتی بود؟ ', 'اذان ظهر ۴ روز پیش قم چه ساعتی بود؟',#2 
      'اذان ظهر هفته ی قبل شیراز چه ساعتی بود؟',
      'اذان ظهر هفته ی بعد شیراز چه ساعتی است؟ ', 
      'اذان صبح امروز دوحه چه ساعتی است؟ ','اذان ظهر امروز بغداد چه ساعتی است؟ ', 
      'اذان ظهر امروز تهران چه زمانی است؟',
      'ساعت اذان ظهر بیروت؟ '] #3
      
            #.....................................................................#
Question_Time=['ساعت در تهران چند است؟',      #1
     'ساعت به وقت ابوظبی چند است؟ ',      
     'الان به وقت تهران چه زمانی از روز است؟ ', #2 صبح.... ظهر .... شب
     'الان در سنگاپور چه ساعتی در شبانه روز است؟',      #1
     'الان در استکهلم ساعت دقیقا چند است؟',      
     'در این لحظه ساعت مسکو چند است؟', 
     'ساعت به وقت بیروت چند است؟', 
     'در تاشکند، این لحظه چه زمانی از روز است؟',      #2
     'ساعت به طور دقیق در استانبول چند است؟',      
     'ساعت فعلی در تورنتو؟',      #1
     'در کابل چه زمانی از روز است؟ ', #2
     'ساعت فعلی ونکوور چند است؟',   #1
     'ساعت در شهر زوریخ چند است؟', 
     'ساعت دبی در این لحظه چند است؟', 
     'ساعت در لس آنجلس چند است؟', 
     'اکنون در ریاض چه زمانی از روز است؟',       
     'اکنون در شهر باکو ساعت چند است؟', 
     'ساعت در پایتخت ایران چند است؟',      
     'در پایتخت روسیه چه زمانی از روز است؟',                 
     'الان به وقت پایتخت ازبکستان چه زمانی از روز است؟']
           #.....................................................................................#   
Question_T=['روز حافظ در سال ۹۹ چه روزی است؟',             #1  
    'در سال ۹۷ روز جهانی محیط زیست چه روزی است؟',     
    'کدام روز از سال ۱۴۰۳ روز اصناف است؟',                  #1
    'سالروز زمین لرزه ی بم در سال ۹۹کدام روز است؟',     #1
    'امسال جشن سده در کدام روز است؟',       #1
    'روز جهانی بهداشت در سال ۹۹کدام روز از سال است؟',  #1
    'سالگرد درگذشت پروین اعتصامی در سال ۱۳۹۶ کدام روز است؟',         
    'روز جمهوری اسلامی در سال ۱۴۰۰؟', 
    'کدام روز از سال ۱۴۰۰ روز قلم است؟',   #1
    'سالگرد اعلام پذیرش قطعنامه ۵۹۸ شورای امنیت از سوی ایران در کدام روز ۱۴۰۰ اتفاق افتاده است؟', #1
    'تاریخ روز صنعت و معدن امسال چه روزی است؟ ',    #1
    'در این سال روز عرفه چه روزی بود؟', 
    'تاریخ برگزاری اولین کنکور در ایران؟ ', 
    'روز خبرنگار کدام روز از امسال است؟',     
    'تاریخ ولادت امام موسی کاظم علیه السلام در سال ۹۹؟',      
    'روز بزرگداشت ابوعلی سینا و روز پزشک در کدام روز سال ۹۹است؟',        
    'مناسبت روز ۱۸ اسفند امسال چیست؟ ',                    #2    
    'بهمن امسال به میلادی؟ ۲۲',                 #3        
    'سال شمسی امسال چند روز است؟',        #4
    'تاریخ شمسی امروز؟',                #5
    'تاریخ میلادی امروز؟',     
    'تعداد روزهای اسفند ۱۴۰۰؟']             #6
    
