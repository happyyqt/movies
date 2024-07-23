def shortestWordEditPath(source, target, words):
	"""
	@param source: str
	@param target: str
	@param words: str[]
	@return: int
	1. find the length of the shortest series of edits
	2. solution: bfs
	3. edge case: target not in words.
	"""
	if target not in words:
		return -1

	if source == target:
		return 0

	visited = set()
	queue = []
	queue.append(source)
	level = 0

	while len(queue):
		size = len(queue)
		level += 1
		for i in range(size):
			new_word = queue.pop(0)
			visited.add(new_word)
			# find all the candidates in words, candidates = []
			for word in words:
				if len(word) != len(target) or word in visited:
					continue
				count = 0
				for i in range(len(word)):
					if word[i] != new_word[i]:
						count += 1
				# print('count', count)
				if count == 1:
					if word == target:
						return level
					queue.append(word)
				
				# print(queue)

	return -1

source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortestWordEditPath(source, target, words))