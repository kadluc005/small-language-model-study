import torch
from src.create_bigram_dataset import X_encoded, Y

# create the Weight matrices with random values

W = torch.randn((28, 28), requires_grad=True)
X = X_encoded

logits = X @ W

logits_one = logits[0]

counts = torch.exp(logits_one)

probabilities = counts / counts.sum()

print(probabilities)
print(probabilities.sum())

print(probabilities.min())
print(probabilities.max())
print(probabilities.sum())

target = Y[0]

probability_target = probabilities[target]

print("target:", target.item())
print("probability:", probability_target.item())

loss = -torch.log(probability_target)
print('loss', loss.item())

for p in [1.0, 0.5, 0.1, 0.01, 0.001]:
    print(p, -torch.log(torch.tensor(p)).item())