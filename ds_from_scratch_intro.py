from __future__ import division
from collections import defaultdict

print '---------------------------------'
print 'Learning datascience from scratch'
print '---------------------------------'
users = [
{ "id": 0, "name": "Hero" },
{ "id": 1, "name": "Dunn" },
{ "id": 2, "name": "Sue" },
{ "id": 3, "name": "Chi" },
{ "id": 4, "name": "Thor" },
{ "id": 5, "name": "Clive" },
{ "id": 6, "name": "Hicks" },
{ "id": 7, "name": "Devin" },
{ "id": 8, "name": "Kate" },
{ "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
	user["friends"] = []

# Defining relationships among users
for i,j in friendships:
	users[i]["friends"].append(users[j])
	users[j]["friends"].append(users[i])

# Function to find out number of friends a user has
def number_of_friends(user):
	return len(user['friends'])

total_connections = sum(number_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections/num_users
# print 'The average number of connections a user has is %s' %avg_connections

num_friends_by_id = [(user['id'],number_of_friends(user)) for user in users]
# print num_friends_by_id
# print sorted(num_friends_by_id,key=lambda (user_id, num_friends): num_friends,reverse=True)

def friends_of_friends_ids_bad(user):
	return [foaf["id"] for friend in user['friends'] for foaf in friend['friends']]

# print friends_of_friends_ids_bad(users[0])

from collections import Counter

def not_the_same(user,other_user):
	return user['id'] != other_user['id']

def not_friends(user,other_user):
	return all(not_the_same(friend,other_user) for friend in user['friends'])

def friends_of_friend_ids(user):
	return Counter(foaf['id'] for friend in user['friends'] for foaf in friend['friends'] if not_the_same(foaf,user) and not_friends(foaf,user))

# print friends_of_friend_ids(users[3])

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
	return [user_id for user_id,user_interest in interests if user_interest == target_interest]

# print 'Data scientists who like Hadoop are %s' % data_scientists_who_like('Hadoop')

user_ids_by_interest = defaultdict(list)
for user_id,interest in interests:
	user_ids_by_interest[interest].append(user_id)
# print user_ids_by_interest['Java']

interest_by_user_ids = defaultdict(list)
for user_id,interest in interests:
	interest_by_user_ids[user_id].append(interest)
# print interest_by_user_ids[0]

def most_common_interests_with(user):
	return Counter(interested_user for interested_user in user_ids_by_interest[interest] for interest in interest_by_user_ids[user['id']] if interested_user != user['id'])

# print most_common_interests_with(users[0])

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
(48000, 0.7), (76000, 6),
(69000, 6.5), (76000, 7.5),
(60000, 2.5), (83000, 10),
(48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

for salary,tenure in salaries_and_tenures:
	salary_by_tenure[tenure].append(salary)

# print salary_by_tenure
average_salary_by_tenure = {tenure:sum(salaries)/len(salaries) for tenure,salaries in salary_by_tenure.items()}
# print average_salary_by_tenure

def tenure_bucket(tenure):
	if tenure < 2:
		return 'less than two'
	elif tenure <5:
		return 'between two and five'
	else:
		return 'more than five'

salary_by_tenure_bucket = defaultdict(list)

for salary,tenure in salaries_and_tenures:
	bucket = tenure_bucket(tenure)
	salary_by_tenure_bucket[bucket].append(salary)

avg_salary_by_bucket = {bucket:sum(salaries)/len(salaries)for bucket,salaries in salary_by_tenure_bucket.items()}
# print avg_salary_by_bucket

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

words_and_counts = Counter(word for user_id,interest in interests for word in interest.lower().split())
# print words_and_counts

for word,count in words_and_counts.most_common():
	if count > 1:
		print word,count





