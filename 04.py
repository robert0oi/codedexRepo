myFruits = {
  "peach",
  "watermelon",
  "khaki",
  "blackberry",
  "kiwi"
}

friendsFruits = {
  "banana",
  "kiwi",
  "strawberry",
  "peach"
}

# Union of sets
union_result = myFruits.union(friendsFruits)

# Intersection of sets
intersection_result = myFruits.intersection(friendsFruits)

# Difference os sets
difference_result = myFruits.difference(friendsFruits)

print("Union:\n", union_result)
print("\nIntersection:\n", intersection_result)
print("\nDifference(My Fruits - Friends Fruits):\n", difference_result)