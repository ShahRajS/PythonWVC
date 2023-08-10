'''
Raj Shah CIST005B

Create a graph representing a social network.
Add some people (vertices) to the network
then create friendships (edges) among some of them.
Create a graph representing a map between cites.
Add some cities (vertices) to the map like Cupertino, Los Angeles, San Jose, and San Francisco,
then create roads (edges) between them with different weights.
'''

friend_group = {}
friend_group["Adam"] = ["Bob", "Dara", "Francine"]
friend_group["Bob"] = ["Adam", "Evan", "Francine"]
friend_group["Clara"] = ["Dara", "Evan"]
friend_group["Dara"] = ["Adam", "Clara", "Evan"]
friend_group["Evan"] = ["Bob", "Clara", "Dara"]
friend_group["Francine"] = ["Adam", "Bob"]

print(friend_group)

map = {}

map["Cupertino"] = [["San Francisco", 43.5], ["Los Angeles", 347], ["Sacramento", 129]]
map["San Francisco"] = [["Cupertino", 43.5], ["Los Angeles", 383], ["Sacramento", 87.9]]
map["Los Angeles"] = [["Cupertino", 347], ["San Francisco", 383], ["Sacramento", 386]]
map["Sacramento"] = [["Cupertino", 129], ["San Francisco", 87.9], ["Los Angeles", 386]]

print(map)
