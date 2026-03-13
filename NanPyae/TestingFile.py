from collections import deque

def hot_potato(names: list[str], k: int) -> str:
    """
    Simulate the Hot Potato game.

    - names is a list of players in initial order.
    - The potato starts with the first person in the list.
    - Pass the potato exactly k times in a circular manner.
    - After the k-th pass, eliminate the person holding the potato.
    - The person immediately after the eliminated player
      (in circular order) holds the potato next.
    - Continue until one player remains. Return the winner's name.

    Example:
      names = ["A", "B", "C", "D"]
      k = 2
      1st round: 
      - "A"--> "B-->C
      - C is eliminated. 
      - Remaining: ["A", "B", "D"]
      - Next HOlder: "D"
      2nd round:
      - "D" --> "A" --> "B"
      - B is eliminated
      - Remaining: ["D", "A"]
      3rd round: 
      - "D"--> "A" --> "D"
      - D is eliminated. 

     Winner: "A"

    """

    # Convert the list of names into a deque (queue)
    queue = deque(names)

    while len(queue) > 1:  # Keep going until only one player remains
        # Pass the potato k times
        for i in range(k):
            person = queue.popleft()  # Take the person from the front
            queue.append(person)      # Put them at the back

        # Eliminate the person holding the potato (front of queue)
        eliminated = queue.popleft()
        print(f"Eliminated: {eliminated}")

    # The last remaining person is the winner
    winner = queue[0]
    return winner

# Example usage
names = ["A", "B", "C", "D"]
k = 2
winner = hot_potato(names, k)
print("Winner:", winner)