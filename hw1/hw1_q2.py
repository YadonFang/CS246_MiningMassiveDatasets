from collections import defaultdict

with open('./q2/data/browsing.txt') as fi:
	content = fi.readlines()

item_freq = defaultdict(int)
supp = 100
for line in content:
	elements = line.split()
	for item in elements:
		item_freq[item] += 1

freq_item = []
for item in item_freq.keys():
	if item_freq[item] >= supp:
		freq_item.append(item)

print(len(freq_item))
freq_item = sorted(freq_item)
candi_pairs = []
for i in range(len(freq_item)):
	for j in range(i+1,len(freq_item)):
		candi_pairs.append((freq_item[i], freq_item[j]))

print(len(candi_pairs))
pair_support =defaultdict(int)
for line in content:
	elements =line.split()
	elements = sorted(elements)
	for i in range(len(elements)):
		if elements[i] in freq_item:
			for j in range(i+1, len(elements)):
				if elements[j] in freq_item:
					pair_support[(elements[i], elements[j])] += 1


rules = {}
for pair in pair_support.keys():
	if pair_support[pair] >= supp:
		rules[(pair[0], pair[1])] = pair_support[pair]/item_freq[pair[0]]
		rules[(pair[1], pair[0])] = pair_support[pair]/item_freq[pair[1]]
sorted_rules = dict(sorted(rules.items(), key=lambda item: item[1]))
print(sorted_rules)



