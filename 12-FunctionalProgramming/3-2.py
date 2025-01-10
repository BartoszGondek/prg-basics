sentence = "I completely agree with you"
result = list(map(lambda sentence : len(sentence), sentence.split()))
print(result)