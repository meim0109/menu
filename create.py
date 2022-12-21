import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
  "date":"day1 ",
  "time":"早餐 ",
  "Staple Food":"燻雞起司蛋三明治",
  "Nonstaple Food":"雞蛋一個",
  "beverage":"無糖飲品260ml",
  "fruit":"紅心火龍果四分之一顆",
},
{  
  "date":"day2 ",
  "time":"早餐 ",
  "Staple Food":"燕麥優格(燕麥無糖＋無糖希臘優格)",
  "Nonstaple Food":"雞蛋一個",
  "beverage":"脫脂牛奶200ml",
  "fruit":"紅豆薏米粥200ml",
},
{
  "date":"day3 ",
  "time":"早餐 ",
  "Staple Food":"紫色地瓜一條",
  "Nonstaple Food":"水煮蛋一顆",
  "beverage":"鮮奶250ml",
  "fruit":"半個蘋果",
},
{  
  "date":"day4 ",
  "time":"早餐 ",
  "Staple Food":"饅頭夾蛋+起司（半個拳頭大）",
  "Nonstaple Food":"雞蛋兩個",
  "beverage":"綜合果汁200ml",
  "fruit":"香蕉一根",
},
{  
  "date":"day5 ",
  "time":"早餐 ",
  "Staple Food":"紫色地瓜一條",
  "Nonstaple Food":"雞蛋兩個",
  "beverage":"綜合果汁200ml",
  "fruit":"火龍果三片",
},
{  
  "date":"day6 ",
  "time":"早餐 ",
  "Staple Food":"蔬菜起司貝果",
  "Nonstaple Food":"水煮蛋兩顆",
  "beverage":"美式咖啡350ml",
  "fruit":"番茄10顆",
},
{  
  "date":"day7 ",
  "time":"早餐 ",
  "Staple Food":"半個熱壓吐司",
  "Nonstaple Food":"玉米筍+花椰菜200g",
  "beverage":"綜合果汁200ml",
  "fruit":"芭樂一顆",
},
{  
  "date":"day1 ",
  "time":"午餐 ",
  "Staple Food":"五穀飯半碗",
  "Nonstaple Food":"青菜200g+新鮮的蝦8隻",
  "beverage":"綜合果汁200ml",
  "fruit":"葡萄10幾顆",
},
{  
  "date":"day2 ",
  "time":"午餐 ",
  "Staple Food":"紅豆薏米粥",
  "Nonstaple Food":"烤鮭魚+生菜200g",
  "beverage":"美式咖啡350ml",
  "fruit":"紅心火龍果半個",
},
{  
  "date":"day3 ",
  "time":"午餐 ",
  "Staple Food":"小碗小米粥",
  "Nonstaple Food":"滷牛肉150g+青江菜300g",
  "beverage":"無糖茶200ml",
  "fruit":"紅心火龍果半個",
},
{  
  "date":"day3 ",
  "time":"午餐 ",
  "Staple Food":"白飯100g",
  "Nonstaple Food":"番茄炒蛋+涼拌黃瓜雞胸肉豆芽200g",
  "beverage":"綜合果汁200ml",
  "fruit":"半顆橘子",
},
{  
  "date":"day4 ",
  "time":"午餐 ",
  "Staple Food":"黑米飯100g",
  "Nonstaple Food":"雞胸肉200g+白菜200g",
  "beverage":"果菜汁200ml",
  "fruit":"半顆水梨",
},
{  
  "date":"day5 ",
  "time":"午餐 ",
  "Staple Food":"紫米飯100g",
  "Nonstaple Food":"滷牛肉150g+燙青菜1份＋滷五香豆干1塊",
  "beverage":"芝麻糊100g",
  "fruit":"1/4個蘋果",
},
{ 
  "date":"day1 ",
  "time":"晚餐 ",
  "Staple Food":"糙米飯半碗",
  "Nonstaple Food":"豆豉清蒸魚＋韭菜炒蛋＋燙空心菜",
  "beverage":"雞蛋羹一杯",
  "fruit":"晚餐沒水果!",
},
{  
  "date":"day2 ",
  "time":"晚餐 ",
  "Staple Food":"陽春麵小碗",
  "Nonstaple Food":"香菜炒滷牛肉+滷蛋半顆",
  "beverage":"晚餐沒飲品!",
  "fruit":"番茄半顆",
},
{  
  "date":"day3 ",
  "time":"晚餐 ",
  "Staple Food":"紫薯餅4個",
  "Nonstaple Food":"雞胸肉150g+豌豆夾50g",
  "beverage":"排骨湯",
  "fruit":"晚餐沒水果!",
},
{  
  "date":"day4 ",
  "time":"晚餐 ",
  "Staple Food":"皮蛋瘦肉粥150g",
  "Nonstaple Food":"燙青菜1份＋滷五香豆干1塊",
  "beverage":"晚餐沒飲品!",
  "fruit":"蘋果半顆",
},
{  
  "date":"day5 ",
  "time":"晚餐 ",
  "Staple Food":"五穀飯100g",
  "Nonstaple Food":"牛肉150g+油麥菜200g",
  "beverage":"晚餐沒飲品!",
  "fruit":"火龍果半顆",
},
{  
  "date":"day6 ",
  "time":"晚餐 ",
  "Staple Food":"芋頭粥100g",
  "Nonstaple Food":"大雜燴(花椰菜100g+豆腐半塊+番茄半個+香菇兩個)",
  "beverage":"綜合果汁",
  "fruit":"晚餐沒水果!",
},
]

collection_ref = db.collection("減肥菜單")
for doc in docs:
  collection_ref.add(doc)

