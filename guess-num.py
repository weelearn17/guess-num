# 產生一個隨機整數1-100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了!"
# 猜錯的話 要告訴他 比答案大/小

import random
start = input('請決定隨機數字開始值:')
end = input('請決定隨機數字結束值:')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0 
while True:
	count += 1 # count =count + 1 的快寫法
	num = input('請猜數字：')
	num = int(num)
	if num == r:
		print('恭喜你猜對了！')
		print('這是你猜的', count,'次' ) 
		break
	elif num > r:
		print('比答案大喔')
	elif num < r:
		print('比答案小喔')
	print('這是你猜的', count,'次' ) #13-19行是一個if架構，寫在最底下才不會重複寫


