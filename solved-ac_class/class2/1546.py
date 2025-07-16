class_cnt = int(input())
current_score = list(map(int, input().split()))

max_score = max(current_score)
avg_score = 0
for c in range(class_cnt):
	new_score = current_score[c]/max_score*100
	avg_score += new_score

new_avg = avg_score/class_cnt
print(new_avg)
