=====================================================
# 컴퓨터와 가위바위보를 하는 프로그램 입니다.
=====================================================
+-----------+-----------+-----------+
|Contributor| Wonjung   | Heejae    |
+===========+===========+===========+
|   Date    |2016.10.12.|2016.10.12 |
+-----------+-----------+-----------+
| The first project, RSP Game!      |
+-----------+-----------+-----------+


import random

# 컴퓨터와 가위바위보를 하는 프로그램 입니다.

def main():
	
	# 자신이 낼 가위바위보를 선택합니다.
	for i in range(10):
		# 컴퓨터가 낼 가위바위보를 랜덤으로 선택합니다.
		com_finger = random.randrange(3) + 1
		my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
		# 안전코딩
		while not(my_finger == 1 or my_finger == 2 or my_finger ==3):
			my_finger = int(input("가위(1), 바위(2), 보(3)를 입력하세요. "))
		
		# 사용자가 가위를 냈을 경우
		if(com_finger == 1):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은 가위입니다. -> Draw")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은 가위입니다. -> Win!")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은 가위입니다. -> Lose")
		
		# 사용자가 바위를 냈을 경우
		elif(com_finger == 2):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은 바위입니다. -> Lose")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은 가위입니다. -> Draw")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은 가위입니다. -> Win!")
		
		# 사용자가 보를 냈을 경우
		elif(com_finger == 3):
			if(my_finger == 1):
				print("컴퓨터가 낸 것은 바위입니다. -> Win!")
			elif(my_finger == 2):
				print("컴퓨터가 낸 것은 가위입니다. -> Lose")
			elif(my_finger == 3):
				print("컴퓨터가 낸 것은 가위입니다. -> Draw")

main()