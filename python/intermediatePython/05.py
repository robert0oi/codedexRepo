listDictionaries = [
  {
    "name": "Ángel Romero", "team": "Corinthians", "position": "striker", "jerseyNumber": "11", "goals": "77"
  },
  {
    "name": "Guiñazú", "team": "Internacional", "position": "midfielder", "jerseyNumber": "5", "goals": "4"
  },
  {
    "name": "Matheus", "team": "Paysandu", "position": "goalkeeper", "jerseyNumber": "1", "goals": "0"
  },
  {
    "name": "Arrascaeta ", "team": "Flamengo", "position": "striker", "jerseyNumber": "10", "goals": "84"
  }
]

listDictionaries[0]['goals'] = '78' 

positions = [player['position'] for player in listDictionaries]
print("Player positions:", positions)

goals = [int(player['goals']) for player in listDictionaries]
averageGoalsInList = sum(goals) / len(goals)

print("Average goals:", averageGoalsInList)