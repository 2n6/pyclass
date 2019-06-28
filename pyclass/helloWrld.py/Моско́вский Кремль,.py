import random
orders = ["lumber", "grill", "paint", "plumbing", "mulch"]

processing_order = orders[-1]

orders.remove(orders[-1])

print(orders)

orders.insert(0, "shovel")

print(orders)


def shake_ball():
    input("Ask somthing about your future: ")
    responses = ["Yes definitely", "As I see it, yes", "Ask again later", "Cannot predict now", "Don't count on it", "Very doubtful", "Definitely not", "Of course", "I don't think so", "Nope"]
    index = random.randint(0, 9)
    print(responses[index])

shake_ball()