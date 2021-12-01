def is_palindrome(l, r, inpt):
	while l >= 0 and r < len(inpt) and inpt[l] == inpt[r]:
		l -= 1
		r += 1
	return len(inpt[l+1:r])

def solution(inpt):
	if len(inpt) < 2:
		return len(inpt)
	
	maxi_ = 0
	for i in range(len(inpt)-1):
		maxi_ = max(is_palindrome(i, i+1, inpt), is_palindrome(i, i+2, inpt), maxi_)
	return maxi_
	
user_input = input()
print(solution(user_input))
